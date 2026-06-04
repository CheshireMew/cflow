---
name: cflow-content
description: Complete content creation workflow for turning rough ideas, notes, transcripts, diagnosis outputs, or source material into publishable content. Use when Codex needs to help with topic selection, angle finding, content briefs, outlines, drafts, rewrites, editing, platform adaptation, content series planning, repurposing, publishing packages, or post-publication review for articles, social posts, newsletters, scripts, short videos, Xiaohongshu/RED, LinkedIn, Twitter/X, blogs, or other creator workflows.
---

# CFlow Content

## Core Rule

Diagnose the content task type before writing. Do not start by polishing surface language if the real problem is unclear intent, weak audience, wrong platform, missing evidence, or an unfocused angle.

Work from one source of truth:

1. User goal
2. Target audience
3. Platform and format
4. Raw material
5. Author voice
6. Publishing constraint

If one is missing, infer conservatively from context and state the assumption. Ask only when the missing item would materially change the output.

## Workflow

Use the smallest workflow that solves the request.

1. **Classify**: Identify whether the request is strategy, topic selection, angle, outline, draft, rewrite, edit, packaging, repurposing, or review.
2. **Clarify Boundary**: Define the deliverable: post, thread, article, script, series plan, content calendar, rewrite, or critique.
3. **Extract Material**: Pull useful facts, claims, scenes, tensions, examples, and audience pain points from the user's material.
4. **Select Angle**: Choose the argument, contradiction, question, or practical transformation that makes the piece worth reading.
5. **Build Structure**: Create only the structure needed for the target format.
6. **Produce**: Draft or edit in the author's likely voice, preserving useful roughness instead of over-smoothing.
7. **Package**: Add title, opening, CTA, platform-specific framing, or variants only when useful.
8. **Review**: Check whether the output matches goal, audience, platform, evidence, and voice.

## CFlow Suite Routing

Use `cflow-content` as the coordinator when the user asks for a complete content workflow or the task type is ambiguous. For narrow requests, route mentally to the matching CFlow boundary:

- `$cflow-topic`: find and evaluate content topics.
- `$cflow-angle`: turn a topic into a readable angle.
- `$cflow-draft`: write a publishable draft from a brief or source material.
- `$cflow-edit`: diagnose and improve an existing draft.
- `$cflow-package`: create titles, hooks, CTAs, and platform variants.
- `$cflow-review`: analyze published results and extract reusable lessons.
- `$cflow-maintain`: update, refactor, merge, delete, and validate CFlow skill guidance with approval before edits.

Do not duplicate the specialized skill's full workflow inside `cflow-content`. Use this skill to coordinate, compose, and preserve the end-to-end source of truth.

## Operating Modes

### From Scratch

Use when the user has only a vague topic or intention. Convert it into a production brief before drafting.

Output a compact brief with:

- Target reader
- Reader problem
- Core claim
- Angle
- Evidence or examples needed
- Format
- Draft plan

### From Raw Material

Use when the user provides notes, transcript, screenshots, previous diagnosis, or rough bullets. Preserve the strongest original material and reorder it around the chosen angle.

Do not treat all input as equal. Separate:

- Usable facts
- Personal voice
- Examples and stories
- Claims needing support
- Noise to ignore

### Editing Existing Drafts

Use when the user provides a draft. Diagnose first, then edit at the minimum depth needed:

- Structure surgery for wrong order or unclear argument
- Paragraph surgery for weak flow
- Sentence surgery for style, rhythm, and clarity
- Packaging for title, opening, ending, or platform fit

Do not rewrite everything unless the draft's structure cannot carry the goal.

### Platform Adaptation

Use when the same idea must become different formats. Keep the source claim stable, then change only structure, pacing, surface conventions, and CTA.

## References

Read `references/cflow-framework.md` when building a multi-step content plan, diagnosing a weak content idea, designing a repeatable workflow, or turning scattered material into a publishable piece.
