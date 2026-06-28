# Icon Share

Curated clean PNG icon library rebuilt from vetted individual source files.

## Summary

- `532` unique icons
- `1924` exported PNG assets (`64`/`128`/`256`/`512` for most packs; `64`/`512`
  only for `ocean-nautical-avatar-icon-pack` and `kitchen-cuttlefish-avatar-icon-pack`)
- `6` public buckets
- `9` included source packs
- `1` excluded contaminated pack: `cuttlefish_aquarium_pack_2_transparent`
- `1` machine-readable catalog: [`catalog.json`](catalog.json)
- `1` catalog schema: [`catalog.schema.json`](catalog.schema.json)
- `1` static gallery: [`index.html`](index.html)
- Source pack provenance under [`_meta/source-packs/`](_meta/source-packs/)

## Buckets

| Bucket | Count | Use |
| --- | --- | --- |
| `aquatic-life` | `208` | Fish, crustaceans, turtles, marine mammals, sea legends, and other aquatic animals |
| `aquatic-habitats` | `23` | Aquariums, aquatic plants, coral, shells, seascape features, and other habitat elements |
| `nautical-items` | `51` | Boats, navigation gear, safety gear, and sea-adjacent objects |
| `maker-workshop` | `50` | 3D printing, electronics, safety gear, sewing, welding, and maker-space tools |
| `workshop-tools` | `150` | Garage, woodshop, hand-tool, and power-tool icons |
| `kitchen-items` | `50` | Kitchen appliances, cookware, tableware, tools, furniture, and other kitchen and dining items |

This import used only provided individual PNG files. It did not cut sheets into
public assets. The contaminated `cuttlefish_aquarium_pack_2_transparent` pack
was excluded from the repo surface.

The `ocean-nautical-avatar-icon-pack` and `kitchen-cuttlefish-avatar-icon-pack`
ship only `64` and `512` assets, so their catalog entries carry
`sizes: [64, 512]`. The `ocean-nautical-avatar-icon-pack`'s `life_ring` and
`coral` collided with existing ids and were imported as `life_ring_safe` and
`coral_reef`; the originals were left untouched. See
[`_meta/source-packs/ocean_nautical_avatar_icon_pack/`](_meta/source-packs/ocean_nautical_avatar_icon_pack/)
for those import notes.

## Layout

```text
share/icons/
  catalog.json
  catalog.schema.json
  index.html
  aquatic-life/<size>/*.png
  aquatic-habitats/<size>/*.png
  nautical-items/<size>/*.png
  maker-workshop/<size>/*.png
  workshop-tools/<size>/*.png
  kitchen-items/<size>/*.png
  _meta/source-packs/<pack>/
```

## Metadata

[`catalog.json`](catalog.json) includes one record per icon with:

- `id` and `label`
- `bucket`
- `description`
- search `tags`
- `sourcePack`
- `sourceSheet` and `sourceGrid`
- `sizes`, `files`, and `preview`

[`catalog.schema.json`](catalog.schema.json) documents the current catalog
shape for tooling that wants to validate or consume it.

The current catalog lists only the clean imported icons and the included source
packs.

## Gallery

[`index.html`](index.html) is a static browser for the catalog. It supports
search, bucket filtering, preview-size switching, and one-click copy actions
for direct file paths, Markdown snippets, and HTML `<img>` snippets.

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

The rebuild script is retained as a local helper. It is wired to the vetted
`Downloads/s\n` source folder, imports only individual PNG files, and keeps the
contaminated aquarium pack excluded.

## License and Use

These icons are available under the repo’s `CC0-1.0` license. Use, remix, and
redistribute them freely. They are provided as-is, and third-party rights are
not granted.
