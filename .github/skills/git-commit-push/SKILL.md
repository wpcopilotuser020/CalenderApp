---
name: git-commit-push
description: 'Create clean git commits and push safely. Use when you need to stage changes, write a clear commit message, validate branch/remote, and push without disrupting other work.'
argument-hint: 'What changed and where should it be pushed?'
user-invocable: true
disable-model-invocation: false
---

# Git Commit And Push

## Outcome
Produce one or more clean commits on the intended branch and push them to the intended remote.

## When To Use
- You finished a coding task and need to publish changes.
- You need a reliable checklist before pushing.
- You want to avoid pushing unrelated files.

## Inputs
- Summary of what changed.
- Target branch name.
- Target remote name, usually origin.
- Optional commit message style preference.
- Push confirmation from the user before any push command.

## Procedure
1. Confirm repository context.
- Run status and branch checks.
- Ensure you are in the intended repository and branch.

2. Review change scope.
- Inspect changed files before staging.
- If unrelated changes exist, do not revert them unless explicitly asked.
- Stage only task-relevant files.

3. Validate before commit.
- Run fast checks relevant to the changed area, such as tests or lint.
- If checks fail, fix or report clearly before committing.

4. Create commit.
- Write an imperative, specific commit message.
- Prefer one focused commit unless the work naturally splits.

5. Verify commit state.
- Confirm clean working tree after commit.
- Review latest commit summary to ensure message and file scope are correct.

6. Push safely.
- Ask for explicit user confirmation immediately before pushing.
- Push to the intended remote and branch only after confirmation.
- If remote has new commits, rebase or merge according to project policy, then push again.

## Decision Points
- If no files changed: stop and report no commit needed.
- If branch is wrong: switch to correct branch before staging.
- If sensitive or generated files are staged accidentally: unstage and add ignore rules when appropriate.
- If push is rejected due to non-fast-forward: pull with rebase (or team-preferred strategy), resolve conflicts, rerun checks, and push.
- If user does not confirm push: stop after commit and report next command to run.

## Quality Checks
- Commit includes only intended files.
- Commit message reflects the actual change.
- Working tree is clean after commit.
- Push was explicitly approved by the user.
- Remote branch contains the new commit(s).

## Completion Criteria
- Commit hash is available.
- Push command succeeds.
- Final status is clean or intentionally includes unrelated untouched user changes.
