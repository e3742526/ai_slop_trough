# Ocean / Nautical Avatar Icon Pack

Upstream provenance for the `ocean-nautical-avatar-icon-pack` source pack
(transparent-fixed rebuild).

## Contents

- `52` individual avatar PNGs (transparent RGBA, verified checkerboard-free)
- Sizes: `64` shipping icons and `512` masters only
- `manifest.json` (upstream, verbatim)

## Import notes

- Imported additively into the existing public buckets; no new buckets were
  created.
- The provided `64` and `512` PNGs were copied verbatim. This pack ships only
  those two sizes, so the catalog entries carry `sizes: [64, 512]` and no
  synthetic `128`/`256` variants were generated.
- The catalog schema treats `128`/`256` as optional, and the gallery falls back
  to the nearest available size when a requested preview size is missing, so the
  partial-size icons render and copy cleanly.
- Bucket split: `40` nautical items, `9` aquatic habitats, `3` aquatic life.
- `sourceGrid` values were reconstructed from each icon's upstream
  `sourceCropBox` position on `source-sheets/nautical_generated_source_sheet.png`.

## Collision handling

Two upstream ids already existed in the catalog (both from
`cuttlefish_ocean_avatar_pack`). The existing entries were left untouched and
the incoming versions were imported under distinct ids so there are no file or
catalog id conflicts:

| Upstream id | Imported as | Label |
| --- | --- | --- |
| `life_ring` | `life_ring_safe` | Life Ring (Safe Margin) |
| `coral` | `coral_reef` | Coral Reef |

The upstream `life_ring` is a circular-avatar-safe replacement with extra
margin; it is retained alongside the original rather than overwriting it.

## Source

Generated programmatically as a Cuttlefish/Jinn-compatible nautical avatar set.
The large upstream source sheet and preview image were not copied into the repo
surface, consistent with the other source packs here.
