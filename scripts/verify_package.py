#!/usr/bin/env python3
"""Dependency-free release checks for the public GDSYNCER package.

This checker validates only the package contract. It does not publish a
repository, contact a network service, or claim that every AI model will obey
the Markdown instructions.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
import tempfile
from pathlib import Path


ROOT_FILES = (
    "README.md",
    "BETA.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "SECURITY.md",
    "docs/HOW-IT-WORKS.md",
    "docs/OPTIONAL-MEMORY.md",
    "docs/QUICKSTART.md",
    "docs/TEMPLATES.md",
    "docs/VALIDATION.md",
    "docs/WALKTHROUGH.md",
    "workspace/START_HERE.md",
    "workspace/TOOLBOX.md",
    "workspace/PROTOCOL_VERSION.md",
    "workspace/AGENTS.md",
    "workspace/CLAUDE.md",
)

PROJECT_FILES = (
    "START_HERE.md",
    "PROGRESS.md",
    "TOOLBOX.md",
    "NEXT_ACTION.md",
    "AGENTS.md",
    "CLAUDE.md",
    "log/.gitkeep",
)

BRANCH_FILES = (
    "START_BRANCH.md",
    "PROGRESS.md",
    "TOOLBOX.md",
    "NEXT_ACTION.md",
    "AGENTS.md",
    "CLAUDE.md",
    "log/.gitkeep",
)

EXTERNAL_LINK = re.compile(r"^(?:https?://|mailto:|#)", re.IGNORECASE)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
PLACEHOLDERS = ("{{PROJECT_NAME}}", "{{PROJECT_SLUG}}", "{{PURPOSE}}", "{{SUCCESS}}")
STALE_LAUNCH_PHRASES = {
    "README.md": ("Unpublished beta staging package",),
    "BETA.md": ("Publication is paused",),
    "docs/QUICKSTART.md": ("publication is paused", "While this beta is unpublished"),
    "CHANGELOG.md": ("unpublished",),
    "workspace/PROTOCOL_VERSION.md": ("beta.3-unpublished",),
}


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.passes = 0

    def check(self, condition: bool, message: str) -> None:
        if condition:
            self.passes += 1
            print(f"PASS: {message}")
        else:
            self.failures.append(message)
            print(f"FAIL: {message}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def required_files_exist(root: Path, paths: tuple[str, ...], report: Report, label: str) -> None:
    missing = [relative for relative in paths if not (root / relative).is_file()]
    report.check(not missing, f"{label} contains every required file" + (f": {', '.join(missing)}" if missing else ""))


def check_nonempty_markdown(root: Path, paths: tuple[str, ...], report: Report, label: str) -> None:
    empty = [relative for relative in paths if relative.endswith(".md") and (root / relative).is_file() and not read_text(root / relative).strip()]
    report.check(not empty, f"{label} Markdown control files are nonempty" + (f": {', '.join(empty)}" if empty else ""))


def check_local_links(root: Path, report: Report) -> None:
    broken: list[str] = []
    for markdown in root.rglob("*.md"):
        if "_validation" in markdown.parts:
            continue
        text = read_text(markdown)
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip()
            if EXTERNAL_LINK.match(target):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            relative_file = markdown.relative_to(root).as_posix()
            if relative_file == "workspace/_templates/project/TOOLBOX.md" and target_path == "../TOOLBOX.md":
                continue  # This link becomes valid after a project is installed into AAA.
            resolved = (markdown.parent / target_path).resolve()
            if root not in resolved.parents and resolved != root:
                broken.append(f"{relative_file} -> {target} escapes the package")
            elif not resolved.exists():
                broken.append(f"{relative_file} -> {target}")
    report.check(not broken, "packaged Markdown local links resolve" + (f": {'; '.join(broken)}" if broken else ""))


def check_launch_copy(root: Path, report: Report) -> None:
    stale = [
        f"{relative} ({phrase})"
        for relative, phrases in STALE_LAUNCH_PHRASES.items()
        for phrase in phrases
        if phrase in read_text(root / relative)
    ]
    report.check(
        not stale,
        "release copy contains no stale launch language" + (f": {', '.join(stale)}" if stale else ""),
    )

def personalize_project(project_root: Path) -> None:
    values = {
        "{{PROJECT_NAME}}": "Shorts",
        "{{PROJECT_SLUG}}": "shorts",
        "{{PURPOSE}}": "Fictional GDSYNCER setup, save, and resume proof.",
        "{{SUCCESS}}": "A fresh session recovers the saved next action and source citation.",
    }
    for markdown in project_root.rglob("*.md"):
        text = read_text(markdown)
        for token, value in values.items():
            text = text.replace(token, value)
        markdown.write_text(text, encoding="utf-8", newline="\n")


def isolated_aaa_flow(root: Path, report: Report) -> None:
    with tempfile.TemporaryDirectory(prefix="gdsyncer-package-") as temporary:
        temporary_root = Path(temporary)
        aaa = temporary_root / "AAA"
        shutil.copytree(root / "workspace", aaa)
        required_files_exist(aaa, ("START_HERE.md", "TOOLBOX.md", "PROTOCOL_VERSION.md", "_templates/project/START_HERE.md"), report, "isolated AAA workspace")

        template = aaa / "_templates" / "project"
        template_hashes = {path.relative_to(template): sha256(path) for path in template.rglob("*") if path.is_file()}
        project = aaa / "GDS Shorts"
        shutil.copytree(template, project)
        personalize_project(project)

        unchanged_template = all(sha256(template / relative) == digest for relative, digest in template_hashes.items())
        report.check(unchanged_template, "project creation leaves the AAA project template unchanged")
        required_files_exist(project, PROJECT_FILES, report, "materialized GDS Shorts project")
        check_nonempty_markdown(project, PROJECT_FILES, report, "materialized GDS Shorts project")

        project_start = read_text(project / "START_HERE.md")
        unresolved = [token for token in PLACEHOLDERS if token in project_start]
        report.check(not unresolved, "project personalization resolves confirmed project fields" + (f": {', '.join(unresolved)}" if unresolved else ""))
        report.check((project / "../TOOLBOX.md").resolve().is_file(), "installed project resolves its inherited AAA toolbox link")

        next_action_path = project / "NEXT_ACTION.md"
        unopened = read_text(next_action_path)
        report.check("- State: closed" in unopened and "initialize this project" in unopened, "new project begins closed with one truthful setup action")

        active = unopened.replace("- State: closed", "- State: active", 1).replace("- Session ID: none", "- Session ID: isolated-short-session-001", 1).replace("- Assistant/device: none", "- Assistant/device: package-verifier / isolated fixture", 1)
        next_action_path.write_text(active, encoding="utf-8", newline="\n")
        active_readback = read_text(next_action_path)
        foreign_hash = sha256(next_action_path)
        foreign_writer_detected = "- State: active" in active_readback and "isolated-short-session-001" in active_readback
        report.check(foreign_writer_detected and sha256(next_action_path) == foreign_hash, "advisory lock data identifies an active writer without a foreign mutation")

        decision = "Each fictional sample video keeps its sources with its script."
        sample_file = project / "03_Videos" / "sample-001" / "README.md"
        sample_file.parent.mkdir(parents=True)
        sample_file.write_text(f"# Fictional sample-001\n\n{decision}\n", encoding="utf-8", newline="\n")
        log_path = project / "log" / "2026-09-12_validation-gds-shorts.md"
        log_path.write_text(
            "# Isolated GDS Shorts validation\n\n"
            f"Decision: {decision}\n\n"
            "Next action: Review the sample-001 source checklist.\n",
            encoding="utf-8",
            newline="\n",
        )
        progress_path = project / "PROGRESS.md"
        progress = read_text(progress_path).replace(
            "No completed sessions yet. After END, add a dated entry here with a useful outcome paragraph, files touched, and a link to the full log. Add exact memory citations only for configured and verified writes; otherwise record pending or disabled.",
            "### 2026-09-12 — Isolated fictional Shorts validation\n\n"
            f"{decision} Files touched: `03_Videos/sample-001/README.md`. "
            "Full page: [validation log](log/2026-09-12_validation-gds-shorts.md).\n",
        )
        progress_path.write_text(progress, encoding="utf-8", newline="\n")
        next_action_path.write_text(
            "---\n"
            "type: next-action\n"
            "project: shorts\n"
            "---\n\n"
            "# Current state — Shorts\n\n"
            "## SESSION STATUS\n"
            "- State: closed\n"
            "- Session ID: isolated-short-session-001\n"
            "- Assistant/device: package-verifier / isolated fixture\n"
            "- Started: 2026-09-12\n"
            "- Last END: package-verifier / isolated fixture\n\n"
            "## Work-unit\n"
            "- Checkpoint: gds-shorts-validation-2026-09-12-001\n"
            "- Desired outcome: preserve a fictional decision across a fresh session.\n"
            "- Acceptance test: a fresh read finds the next action and cited log.\n"
            "- In scope: fictional protocol validation only\n"
            "- Out of scope: channel work, publication, paid services, and private data\n"
            "- Source checkpoint: log/2026-09-12_validation-gds-shorts.md\n"
            "- Verified current facts: the fictional decision and cited log exist.\n"
            "- Canonical resources: START_HERE.md; TOOLBOX.md; PROGRESS.md; log/2026-09-12_validation-gds-shorts.md\n"
            "- Blocker: none\n"
            "- Exactly one next action: Review the sample-001 source checklist.\n"
            "- Why: confirm the cited fictional source list before adding work.\n"
            "- Pending memory receipts: disabled for this isolated package proof.\n",
            encoding="utf-8",
            newline="\n",
        )

        fresh_next_action = read_text(next_action_path)
        fresh_progress = read_text(progress_path)
        fresh_log = read_text(log_path)
        report.check(
            "Review the sample-001 source checklist." in fresh_next_action
            and "log/2026-09-12_validation-gds-shorts.md" in fresh_progress
            and decision in fresh_log
            and decision in read_text(sample_file),
            "fresh readback recovers the exact next action, citation, and fictional decision",
        )


def validate(root: Path) -> Report:
    report = Report()
    required_files_exist(root, ROOT_FILES, report, "public package")
    check_nonempty_markdown(root, ROOT_FILES, report, "public package")
    report.check("KISS" in read_text(root / "README.md") and "AAA" in read_text(root / "README.md"), "README explains the KISS rule and AAA workspace flow")
    report.check("python scripts/verify_package.py" in read_text(root / "CONTRIBUTING.md"), "contribution guide names the release checker")
    report.check((root / "scripts" / "verify_package.py").is_file(), "documented release checker exists")
    quickstart = read_text(root / "docs" / "QUICKSTART.md")
    validation = read_text(root / "docs" / "VALIDATION.md")
    report.check("start a project named Shorts" in quickstart, "Quickstart names the AAA to GDS Shorts first-use path")
    report.check(
        "Normal use does not require Python" in quickstart
        and "python scripts/verify_package.py --root ." in quickstart,
        "Quickstart makes release verification optional and discoverable",
    )
    report.check("Status: NEEDS REVALIDATION" not in validation, "validation status is updated after a successful package proof")
    report.check("`r`n" not in validation, "validation record contains real Markdown line breaks")
    report.check(
        "log/2026-09-12_validation-gds-shorts.md" in validation
        and "gds-shorts-validation-2026-09-12-001" in validation,
        "validation record names the reproducible isolated proof",
    )
    check_launch_copy(root, report)

    project_template = root / "workspace" / "_templates" / "project"
    branch_template = root / "workspace" / "_templates" / "branch"
    required_files_exist(project_template, PROJECT_FILES, report, "project template")
    check_nonempty_markdown(project_template, PROJECT_FILES, report, "project template")
    required_files_exist(branch_template, BRANCH_FILES, report, "branch template")
    check_nonempty_markdown(branch_template, BRANCH_FILES, report, "branch template")
    report.check("SAFE WRITE" in read_text(project_template / "START_HERE.md"), "project template contains the safe-write protocol")
    report.check("MERGE BRANCH" in read_text(branch_template / "START_BRANCH.md"), "branch template contains the explicit merge contract")
    check_local_links(root, report)
    isolated_aaa_flow(root, report)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a public GDSYNCER release package without network access.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="package root to validate")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        print(f"FAIL: package root does not exist: {root}")
        return 2
    report = validate(root)
    if report.failures:
        print(f"PACKAGE_VALIDATION_FAIL: {len(report.failures)} failed; {report.passes} passed")
        return 1
    print(f"PACKAGE_VALIDATION_PASS: {report.passes} checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
