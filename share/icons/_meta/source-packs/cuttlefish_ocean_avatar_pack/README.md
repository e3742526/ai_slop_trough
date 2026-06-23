# Cuttlefish Ocean Avatar Pack

Generated replacement agent avatars for a Jinn/Cuttlefish ocean theme.

## Contents

- `50` individual avatar PNGs
- Sizes: `64`, `128`, `256`, `512`
- Repo-ready asset path: `packages/web/public/avatars/ocean/<size>/<id>.png`
- Vite-served URL path: `/avatars/ocean/<size>/<id>.png`
- `manifest.json`
- `packages/web/src/lib/ocean-avatar-pool.ts`
- Optional image-avatar support replacement: `packages/web/src/components/ui/employee-avatar.tsx`

## Repo integration

Copy the `packages/` directory from this zip into the repo root.

Current Jinn avatar rendering is emoji-first. The included `employee-avatar.tsx`
keeps that behavior but adds `profileImage` support using the existing
`employeeOverrides[employeeId].profileImage` setting.

Example:

```json
{
  "employeeOverrides": {
    "giles-watcher": {
      "profileImage": "/avatars/ocean/128/shark.png"
    },
    "incident-commander": {
      "profileImage": "/avatars/ocean/128/octopus.png"
    }
  }
}
```

## Icon IDs

clownfish, blue_tang, pufferfish, seahorse, octopus, crab, dolphin, shark, whale, anchor, jellyfish, starfish, sea_turtle, lobster, squid, anglerfish, manta_ray, swordfish, sailboat, seaweed, hermit_crab, stingray, orca, narwhal, hammerhead_shark, beluga_whale, moray_eel, nautilus, buoy, ship_wheel, manatee, sea_lion, cuttlefish, sea_urchin, clam_shell, oyster_pearl, shrimp, coral, flying_fish, life_ring, penguin, pelican, sea_otter, albatross, trident, treasure_chest, lighthouse, submarine, message_bottle, captains_wheel
