# AGENTS.md

## Scope and source of truth
- This repo is an auto-synced NeetCode submissions archive (see `README.md`); optimize for preserving submission history, not for building an app/package.
- Trust repository structure and existing files over generic NeetCode assumptions.

## Repository shape
- Main content lives under `Data Structures & Algorithms/<problem-slug>/`.
- Per problem, files are typically:
  - `submission-<n>.py` (multiple attempts kept as separate files)
  - `problem.md` (problem statement)
  - optional `notes.md` (personal notes, not executable spec)
- Keep existing folder/file names exactly as-is (including existing typos like `products-of-array-discluding-self` and `is-anagram/probelm.md`) unless explicitly asked to rename.

## Editing conventions for this repo
- Default behavior: preserve historical attempts; add a new `submission-<next>.py` instead of rewriting older submissions unless the user asks to modify a specific file.
- Keep NeetCode-style solution shape: `class Solution:` with the expected method signature for that problem.
- When using shell commands, always quote paths with spaces, e.g. `"Data Structures & Algorithms/..."`.

## Execution and verification reality
- There is no repo-level build/test/lint/typecheck config (`package.json`, `pyproject.toml`, CI workflows, and pre-commit config are absent).
- Many submissions rely on NeetCode runtime-provided names (e.g., `List`, `collections`) without local imports; running files directly may fail unless imports are added temporarily.
- Prefer targeted sanity checks on edited files over invented repo-wide commands.
