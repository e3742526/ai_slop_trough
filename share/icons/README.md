# Icon Share

Reusable AI-generated PNG icons organized into descriptive buckets for
low-friction reuse.

## Summary

- `225` unique icons
- `900` exported PNG assets across `64`, `128`, `256`, and `512` sizes
- `6` public buckets
- `1` machine-readable catalog: [`catalog.json`](catalog.json)
- `1` catalog schema: [`catalog.schema.json`](catalog.schema.json)
- Source pack provenance under [`_meta/source-packs/`](_meta/source-packs/)

## Buckets

| Bucket | Count | Use |
| --- | --- | --- |
| `aquatic-life` | `89` | Fish, turtles, crustaceans, mollusks, and other aquatic animals |
| `aquatic-habitats` | `19` | Aquarium tanks, aquatic plants, coral, shells, and other habitat elements |
| `aquarium-care` | `16` | Aquarium tools, health, water handling, and maintenance equipment |
| `nautical-items` | `11` | Boats, navigation, safety gear, and sea-adjacent objects |
| `maker-lab` | `40` | Workshop, field-science, instrumentation, and other oddball utility icons |
| `office-items` | `50` | Office supplies, workplace gear, and desk objects |

The public buckets are descriptive rather than source-pack based. The aquarium
packs were folded into the aquatic buckets, the earlier marine object bucket was
split between aquatic habitats and nautical items, and the original “random
other things” pack remains normalized to `maker-lab` so it stays discoverable
instead of becoming a junk drawer.

## Layout

```text
share/icons/
  catalog.json
  aquatic-life/<size>/*.png
  aquatic-habitats/<size>/*.png
  aquarium-care/<size>/*.png
  nautical-items/<size>/*.png
  maker-lab/<size>/*.png
  office-items/<size>/*.png
  _meta/source-packs/<pack>/
```

Each bucket uses the same four-size layout, so consumers can swap sizes without
changing IDs.

## Metadata

[`catalog.json`](catalog.json) includes one record per icon with:

- `id` and `label`
- `bucket`
- short `description`
- search `tags`
- `sourcePack`
- `files` for each exported size
- source sheet row and column metadata from the original pack manifests

That file is the intended search/index surface if you want to build a picker,
website, or import script later.

[`catalog.schema.json`](catalog.schema.json) documents the current catalog
shape for tooling that wants to validate or consume it.

## Gallery

[`index.html`](index.html) is a static browser for the catalog. It supports
search, bucket filtering, preview-size switching, and one-click copy actions
for:

- direct file paths
- Markdown image snippets
- HTML `<img>` snippets

If you want to validate the machine-readable metadata locally, run:

```bash
npx --yes -p ajv-cli@5.0.0 -p ajv-formats@2.1.1 \
  ajv validate --spec=draft2020 -c ajv-formats \
  -s share/icons/catalog.schema.json \
  -d share/icons/catalog.json
```

## Provenance

The assets were generated with ChatGPT 5.5 High. Many were originally generated
for personal applications, prototypes, or experiments rather than as a public
asset product. They are shared here because the generic icons are still useful
outside those original contexts.

The earlier ocean and office packs were generated for
"https://github.com/repo-makeover/jinn", which is a fork of "hristo2612/jinn".
The aquarium packs were generated later as Jinn-compatible aquarium and
aquarium-care assets.

The original upstream `README.md`, `manifest.json`, and preview images are
preserved under [`_meta/source-packs/`](_meta/source-packs/) for reference.

## License and Use

These icons are available under the repo’s `CC0-1.0` license. Use, remix, and
redistribute them freely. They are provided as-is, and third-party rights are
not granted.
