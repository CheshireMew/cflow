# Maintenance Protocol

## Input Classification

Classify each user-provided item as one of:

- **Rule**: A durable instruction that should constrain future behavior.
- **Workflow step**: A repeatable sequence action.
- **Decision criterion**: A test for choosing between options.
- **Platform note**: Guidance specific to RED, short video, LinkedIn, Twitter/X, blog, newsletter, or another platform.
- **Voice guideline**: Instruction about preserving or shaping author voice.
- **Defect report**: A failure observed during use of a CFlow skill.
- **Test case**: A realistic example that should be used to validate behavior.
- **Deletion request**: A rule or resource that should be removed.
- **Architecture request**: A change to boundaries, routing, naming, or repository structure.

## Placement Decision

Place each item at the narrowest durable boundary.

- Put orchestration and suite routing in `cflow-content`.
- Put discovery and scoring in `cflow-topic`.
- Put claim and reader tension in `cflow-angle`.
- Put structure-to-draft guidance in `cflow-draft`.
- Put revision diagnosis and voice preservation in `cflow-edit`.
- Put titles, hooks, CTAs, and platform package variants in `cflow-package`.
- Put performance learning and next experiments in `cflow-review`.
- Put maintenance procedures in `cflow-maintain`.

## Source Layout

Use the monorepo as the only editable source:

```text
D:\Code\cflow
└── skills
    ├── cflow-content
    ├── cflow-topic
    ├── cflow-angle
    ├── cflow-draft
    ├── cflow-edit
    ├── cflow-package
    ├── cflow-review
    └── cflow-maintain
```

Codex discovery links may exist under `C:\Users\Lenovo\.codex\skills`, but do not edit through those links unless the user explicitly asks. Edit the monorepo source, then validate and commit from `D:\Code\cflow`.

If the item seems to fit multiple skills, identify the root behavior. Add one primary rule and only a short routing note elsewhere if needed.

## Coverage States

Use these labels:

- **Already covered**: No edit needed.
- **Partially covered**: Existing rule should be tightened or extended.
- **Duplicate**: Merge into the best existing location and delete repetition.
- **Conflict**: Choose the rule that preserves the CFlow boundary; ask the user if business intent is unclear.
- **New rule**: Add it to the narrowest skill or reference file.
- **Obsolete**: Remove it if it no longer matches the architecture.

## Refactor Rules

- Keep one source of truth for each rule.
- Do not preserve old helper language, deprecated flows, or compatibility explanations after a migration.
- Prefer moving a rule over copying it.
- Keep `SKILL.md` concise and put detailed patterns in `references/`.
- Update `cflow-content` routing only when suite boundaries change.
- Regenerate or edit `agents/openai.yaml` only when display metadata becomes stale.

## Approval Standard

The user must approve:

- Affected repositories
- Files to edit
- Rules to add, move, merge, or delete
- Validation plan
- Commit plan

If the user changes the plan, revise the plan and ask again before editing.

## Validation

Run:

```powershell
$env:PYTHONPATH='D:\Code\.codex-python-libs'
python 'C:\Users\Lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '<skill-path>'
```

Validate every changed skill. Validate all CFlow skills when suite routing, ownership boundaries, or shared conventions changed.

## Commit Guidance

Commit only after validation passes. Use focused messages:

- `Update <skill> <rule-area>`
- `Move <rule> into <skill>`
- `Refine CFlow routing`
- `Remove duplicate <rule-area> guidance`

When multiple repositories change, commit each repository separately unless the user explicitly wants a different release workflow.
