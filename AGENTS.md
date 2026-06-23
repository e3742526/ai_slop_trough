# AI Slop Trough Agent Instructions

This file defines how future agents should organize and extend this repository.

## Purpose

This repo is a controlled public share for reusable AI-generated artifacts.

The organizing principle is practical rather than precious:

- keep generic assets that are worth reusing
- make them easy to browse, search, and link
- avoid turning the repo root into a junk drawer

Treat this repo as a curated commons for low-friction reuse, not as a scratchpad.

## Primary Rule

Public artifacts belong under `share/`, not at the repo root.

Do not add new asset dumps directly to the root directory unless the user explicitly asks for a different structure.

## Current Structure

At the time of writing:

- `share/icons/` is the active local asset collection
- `share/links/` is active as “Other People's Slop,” the curated external asset index

Agents should preserve this pattern and extend it rather than inventing parallel top-level directories. Do not add empty public collection scaffolding; create a collection directory only when there is real content to document.

## Root README Expectations

When the repo changes in a user-visible way, keep `README.md` aligned with reality.

The root README should:

- read like the repo front door, not a raw file listing
- describe what the repo is for
- clearly distinguish active collections from reserved ones
- include a table of contents
- include a current-state summary of what is actually in the repo now
- link directly to the active collection README files
- link directly to any gallery or machine-readable catalog that matters
- explain how future collection growth should happen without pretending those collections already exist

Do not overstate repo completeness. Avoid public reserved-collection placeholders unless the user explicitly asks for them.

## Share Organization Rules

Each collection under `share/<name>/` should be self-contained.

Expected minimum:

- `README.md`
- stable directory layout
- `_meta/` for provenance, import notes, previews, or upstream manifests when relevant

Add machine-readable metadata when the collection is large enough that users or future tooling will need search, filtering, tagging, or indexing.

## Collection Types

### Asset collections

Examples: icons, images, sprites, pattern packs, sticker packs.

Requirements:

- normalize imported material into a clean public-facing structure
- prefer descriptive public categories over opaque source-pack names
- preserve provenance under `_meta/`
- keep category counts legible
- if nominal bucketing is used, prefer no more than 5 public buckets unless the user asks otherwise

### App collections

App artifacts should live under `share/apps/<slug>/`.

Do not create an empty `share/apps/` lane just to reserve the name. Add it when an actual app share lands.

Each app share should document:

- what it is
- whether it is source code, export, mockup, or prototype
- how to run or inspect it
- how complete it is
- any license exception from the repo default

### External link collections

Curated external resources should live under `share/links/`.

Public-facing label:

- “Other People's Slop”

Link indexes should be structured and minimally opinionated. Include at least:

- name
- URL
- type
- stated license if known
- short reason it is included

Do not imply ownership of external assets.

## Naming and Categorization

- Use lowercase kebab-case for collection directories.
- Prefer user-facing descriptive names over internal or upstream naming.
- Preserve upstream naming in manifests and `_meta/` when it matters for provenance.
- Avoid catch-all category names like `misc` or `random` when a better public label exists.

## README Additions For New Collections

When adding a new populated collection:

1. Add or update that collection’s `README.md`.
2. Update `share/README.md` to list the new collection and its status.
3. Update the root `README.md` so the current-state table and start-here links remain accurate.
4. If the collection includes a gallery, catalog, or preview surface, link it from the root README and the collection README.

## License Posture

The repo currently uses `CC0-1.0`, which is the default posture for shared generated assets here.

Interpretation for future organization:

- default to low-friction reuse
- avoid attribution-heavy or restrictive terms unless the user explicitly wants them
- if a future collection needs different terms, declare that inside the collection rather than silently changing the meaning of the whole repo

Do not claim rights that the repo may not have over AI-generated output. Keep disclaimers practical and accurate.

## Aesthetic and Presentation Standard

Documentation should be clean, spare, and useful.

Prefer:

- concise explanations
- strong navigation
- tables when they improve scanability
- clear separation between active content and future scaffolding
- language that sounds curated rather than hype-driven

Avoid:

- breathless marketing tone
- pretending placeholders are finished collections
- giant undifferentiated README sections
- dumping raw import notes into public-facing READMEs

## Import Workflow

When importing new material:

1. Inspect the source pack structure before reorganizing it.
2. Normalize the public asset surface under the correct `share/<collection>/` path.
3. Preserve provenance and upstream manifests under `_meta/` when useful.
4. Generate descriptions, tags, or catalog metadata when that materially improves reuse.
5. Update READMEs so a user landing on the repo can find the new material quickly.
6. Validate the resulting paths, counts, and links.

## Validation Expectations

Before closing work that changes collection structure or docs:

- verify referenced files exist
- verify generated catalog paths resolve
- verify README links still point to real paths
- call out category ambiguity or license caveats when relevant

If a gallery or static browser is added or changed, prefer a simple runtime verification over assuming it works from inspection alone.
