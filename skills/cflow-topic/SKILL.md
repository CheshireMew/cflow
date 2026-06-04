---
name: cflow-topic
description: Content topic discovery and evaluation workflow for finding specific topics from business context, audience pain, personal experience, notes, transcripts, diagnosis outputs, research, or creator goals. Use when Codex needs to generate topic options, evaluate whether a topic is worth making, build topic pools, map content lanes, turn vague directions into concrete topics, or choose the next content idea before angle, draft, edit, packaging, or review work.
---

# CFlow Topic

## Boundary

Own topic discovery. Stop before writing the final angle, outline, or draft unless the user explicitly asks to continue.

A topic is a concrete subject the creator can make content about. It is not yet the claim, hook, title, or structure.

## Workflow

1. Identify the creator's domain, audience, and publishing goal.
2. Extract topic raw material from the user's context: problems, questions, decisions, failures, examples, objections, and repeated explanations.
3. Group topics by content lane.
4. Score candidates by reader pain, author credibility, specificity, freshness, and production cost.
5. Select the strongest topics and explain why each is worth making.
6. Hand off the chosen topic to `$cflow-angle` when the user needs a sharper point of view.

## Output

For topic generation, return:

- Content lane
- Topic
- Target reader
- Reader problem
- Why now
- Source material needed
- Risk or weakness
- Best next step

For topic evaluation, return:

- Verdict
- Strongest use case
- Weakness
- Fix
- Recommended angle direction

## Reference

Read `references/topic-system.md` when building a topic pool, scoring candidates, or diagnosing why a topic feels generic.
