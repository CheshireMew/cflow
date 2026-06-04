---
name: cflow-maintain
description: CFlow skill-suite maintenance workflow for updating, refactoring, merging, deleting, or reorganizing CFlow skills based on new writing rules, workflow defects, user feedback, observed failures, or process improvements. Use when Codex needs to inspect the CFlow skill projects, decide which skill should receive new guidance, detect duplicate or conflicting rules, propose removals or merges, generate an update plan, request explicit user approval before editing, apply approved changes, validate skills, and commit the maintenance work.
---

# CFlow Maintain

## Boundary

Own changes to the CFlow skill suite itself. Do not use this skill to write, edit, package, or review ordinary content unless that work is needed to diagnose a skill defect.

The source of truth is the CFlow monorepo at `D:\Code\cflow\skills`. Inspect source files there before proposing changes. Treat `C:\Users\Lenovo\.codex\skills\cflow-*` as discovery links only, not as editable source.

## Hard Gate

Do not edit any CFlow skill file until the user explicitly approves a concrete update plan.

Allowed before approval:

- Read CFlow skill files
- Classify new guidance
- Detect duplicates, conflicts, obsolete rules, and missing workflows
- Propose a patch plan
- Explain expected files and sections to change

Not allowed before approval:

- Modify `SKILL.md`
- Modify `references/`
- Delete or merge files
- Commit changes
- Regenerate metadata

## Workflow

1. **Inventory**: List all relevant CFlow skills and read their `SKILL.md` plus only the needed reference files.
2. **Classify Input**: Decide whether the user's new material is a rule, workflow step, decision criterion, platform note, voice guideline, defect report, test case, or deletion request.
3. **Locate Boundary**: Assign each item to exactly one primary skill. Use cross-references only when a second skill needs to route to it.
4. **Check Existing Coverage**: Determine whether the guidance already exists, partially exists, conflicts with existing rules, or creates a new need.
5. **Plan Refactor**: Prefer one clean migration over compatibility layers. If a rule belongs elsewhere, move it rather than duplicate it.
6. **Request Approval**: Present a concrete change plan and wait for user approval before editing.
7. **Apply Changes**: Edit only approved files. Remove obsolete or duplicate rules when the approved plan requires it.
8. **Validate**: Run `quick_validate.py` for every changed skill, and for all CFlow skills when routing or shared boundaries changed.
9. **Commit**: Commit each affected repository with a clear message if the user approved implementation and validation passes.

## Routing Rules

Use these ownership boundaries:

- `cflow-content`: Suite coordinator, end-to-end routing, source-of-truth preservation.
- `cflow-topic`: Topic discovery, topic scoring, content lanes, topic pools.
- `cflow-angle`: Reader tension, core claim, angle selection, premise sharpening.
- `cflow-draft`: First complete draft from brief, notes, transcripts, or source material.
- `cflow-edit`: Existing draft diagnosis, rewrite depth, voice preservation, anti-AI cleanup.
- `cflow-package`: Titles, hooks, CTAs, cover text, publishing variants, platform packaging.
- `cflow-review`: Post-publication learning, metrics interpretation, feedback loop.
- `cflow-maintain`: CFlow skill architecture, rule placement, refactor, validation, commits.

## Approval Plan Format

Before editing, return:

```text
Proposed update:
Input classification:
Affected skills:
Existing coverage:
Conflicts or duplicates:
Files to change:
Rules to add:
Rules to move:
Rules to delete:
Validation plan:
Commit plan:
Approval needed:
```

Ask for explicit approval after the plan. Do not proceed on vague agreement; wait for a clear approval to apply the listed changes.

## Reference

Read `references/maintenance-protocol.md` when classifying a rule, planning a refactor, deciding whether to merge/delete guidance, or preparing the approval plan.
