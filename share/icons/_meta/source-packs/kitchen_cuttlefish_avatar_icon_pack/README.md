# Kitchen_Cuttlefish_Avatar_Icon_Pack

Production-ready kitchen-themed avatar/icon pack for the Cuttlefish/Jinn app.

## Summary

- Pack slug: `kitchen_cuttlefish`
- Version: `1.0.0`
- Icon count: `50`
- Sizes included: `64x64`, `512x512`
- Format: `PNG`, `8-bit RGBA`
- Background: true alpha transparency
- Master size: `512x512`
- Downsampled size: `64x64`
- Target repo: `repo-makeover/jinn`

## Style

The icons use a glossy, semi-realistic 3D-rendered mobile-game asset style:
rounded friendly forms, soft gradients, subtle highlights, ambient shadows, and darker rim outlines where useful.

Each shipped icon is a single centered subject on a transparent canvas. The preview sheet may contain labels and a checkerboard background; the individual icon PNGs do not.

## App paths

The app-facing paths are:

```text
/avatars/kitchen_cuttlefish/64/<id>.png
/avatars/kitchen_cuttlefish/512/<id>.png
```

## Folder structure

```text
Kitchen_Cuttlefish_Avatar_Icon_Pack/
  README.md
  manifest.json
  icon_descriptions.json
  alpha_audit.json
  docs/
    kitchen_cuttlefish-preview.png
  icons/
    64/
      <id>.png
    512/
      <id>.png
  packages/
    web/
      public/
        avatars/
          kitchen_cuttlefish/
            64/
              <id>.png
            512/
              <id>.png
      src/
        lib/
          kitchen_cuttlefish-avatar-pool.ts
```

## Validation

Validation passed for every shipped PNG. Checks include:

- exact dimensions
- RGBA mode
- alpha channel present
- transparent pixels present
- non-empty visible subject
- subject centered within tolerance
- subject not touching canvas edges
- no detected opaque corner contamination
- generated icons contain no embedded text or labels

See `alpha_audit.json` for per-icon validation results.
