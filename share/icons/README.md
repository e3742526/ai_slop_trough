# Icon Share

The public icon-share payload has been cleared. This surface is intentionally
empty pending a fresh recreation pass.

## Summary

- `0` unique icons
- `0` exported PNG assets
- `0` public buckets
- `1` machine-readable catalog scaffold: [`catalog.json`](catalog.json)
- `1` catalog schema: [`catalog.schema.json`](catalog.schema.json)
- `1` static gallery scaffold: [`index.html`](index.html)

## Layout

```text
share/icons/
  catalog.json
  catalog.schema.json
  index.html
```

## Metadata

[`catalog.json`](catalog.json) is intentionally empty right now. It remains in
place as the machine-readable surface that the next import pass should refill.

[`catalog.schema.json`](catalog.schema.json) documents the current catalog
shape for tooling that wants to validate or consume it.

The current catalog lists no icons, no buckets, and no source packs.

## Gallery

[`index.html`](index.html) is still the static browser for the catalog. With an
empty catalog it serves as an empty-state viewer until new assets are imported.

If you want to validate the machine-readable metadata locally, run:

```bash
npx --yes -p ajv-cli@5.0.0 -p ajv-formats@2.1.1 \
  ajv validate --spec=draft2020 -c ajv-formats \
  -s share/icons/catalog.schema.json \
  -d share/icons/catalog.json
```

To rebuild the public icon share from downloaded source material, run:

```bash
python3 scripts/rebuild_icons.py
```

The rebuild script is retained as a local helper, but the public repo surface
has been fully cleared so the next import can start from zero.

## License and Use

These icons are available under the repo’s `CC0-1.0` license. Use, remix, and
redistribute them freely. They are provided as-is, and third-party rights are
not granted.
