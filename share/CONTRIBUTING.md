# Share Contribution Guide

This repository treats `share/` as a controlled public surface for reusable generated artifacts.

## What Belongs Here

- commodity assets that are useful enough to keep and generic enough to share
- generated app artifacts that work as examples, starters, or throwaway utilities
- curated indexes pointing to external slop collections, branded here as “Other People's Slop,” with clear notes

Do not put one-off scratch files, half-imported zips, unclear licensing surfaces, or empty collection scaffolding directly under `share/`.

## Collection Contract

Every collection under `share/<name>/` should include:

- a `README.md` that explains what the collection is
- a stable directory layout
- machine-readable metadata when the collection has more than a handful of items
- a local `_meta/` directory for provenance, previews, import notes, or upstream manifests
- a collection-local license note only when it differs from the repo default

## Import Rules

When importing a new asset pack:

1. Normalize it into a controlled subdirectory such as `share/icons/` or `share/images/`.
2. Keep public-facing buckets small and legible. Avoid junk-drawer categories when a better name exists.
3. Preserve provenance under `_meta/` rather than keeping upstream app glue in the public asset path.
4. Generate a machine-readable catalog if search, tagging, or previews will matter later.
5. Update the root [README.md](../README.md) and the collection index [README.md](README.md) when a new collection is added.

## App Shares

Future app artifacts should live under `share/apps/<slug>/`.

Do not create `share/apps/` as a public placeholder. Create it only when the first app artifact is ready to document.

Recommended layout:

```text
share/apps/<slug>/
  README.md
  _meta/
  src-or-export/
```

The app README should document:

- what the artifact is
- how complete it is
- whether it is code, a static export, or a design artifact
- how to run or inspect it
- any non-CC0 license exceptions for code or bundled dependencies

## External Link Indexes

Curated external slop links should live under `share/links/`.

Public-facing name:

- “Other People's Slop”

Use a compact table with at least:

- name
- URL
- type
- stated license
- brief note on why it is worth indexing

Do not imply endorsement or ownership of external assets. Link rows should be descriptive, not promotional.

## Naming

- Use lowercase kebab-case for collection directories.
- Prefer descriptive bucket names over source-pack names when the public grouping is clearer.
- Preserve original upstream names inside `_meta/` and machine-readable catalogs.

## Validation

Before closing a share import:

- verify file counts
- verify catalog paths
- verify README links
- call out residual ambiguity, especially around category boundaries or licensing posture
