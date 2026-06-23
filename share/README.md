# Shared Collections

`share/` is the controlled public surface for reusable generated artifacts in this repository.

## Current Collections

| Path | Summary | Status |
| --- | --- | --- |
| [`icons/`](icons/) | PNG icon library with tags, descriptions, and provenance metadata | Active |
| [`apps/`](apps/) | Placeholder for future reusable generated app artifacts | Reserved |
| [`links/`](links/) | “Other People's Slop,” a curated index of external icon packs and generation tools | Active |

## Contributing

- [`CONTRIBUTING.md`](CONTRIBUTING.md) defines the import contract for future collections.
- New collections should be added under `share/<collection>/`, not at the repo root.

## Collection Rules

- Each collection should be self-contained and linkable.
- Each collection should have its own `README.md`.
- Machine-readable indexes should live next to the assets they describe.
- If a collection needs terms different from the repo default, it should carry its own license notice.
- Provenance or import metadata should stay under a local `_meta/` directory rather than leaking into the repo root.

## Planned Growth

This directory is intended to support future additions such as `share/apps/`, `share/images/`, or “Other People's Slop” style indexes of external asset dumps.
