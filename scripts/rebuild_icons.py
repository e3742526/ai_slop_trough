#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
ICONS_ROOT = REPO_ROOT / "share" / "icons"
CATALOG_PATH = ICONS_ROOT / "catalog.json"
SCHEMA_PATH = ICONS_ROOT / "catalog.schema.json"
README_PATH = ICONS_ROOT / "README.md"
GALLERY_PATH = ICONS_ROOT / "index.html"
META_PACKS_DIR = ICONS_ROOT / "_meta" / "source-packs"
SOURCE_ROOT = Path("/home/ericl/Downloads") / "s\n"
SIZES = ("64", "128", "256", "512")
TODAY = datetime.now(timezone.utc).date().isoformat()

EXCLUDED_PACKS = {
    "cuttlefish_aquarium_pack_2_transparent",
}

NAUTICAL_IDS = {
    "anchor",
    "buoy",
    "captains_wheel",
    "life_ring",
    "lighthouse",
    "message_bottle",
    "sailboat",
    "ship_wheel",
    "submarine",
    "treasure_chest",
    "trident",
}

HABITAT_IDS = {
    "aquarium_standard_tank",
    "aquarium_rimless_planted_tank",
    "aquarium_nano_cube_tank",
    "aquarium_bowfront_tank",
    "aquarium_turtle_tank",
    "aquatic_plant_vallisneria",
    "aquatic_plant_anubias",
    "aquatic_plant_red_stem",
    "aquatic_plant_java_fern",
    "aquatic_plant_floating_cluster",
    "clam_shell",
    "coral",
    "oyster_pearl",
    "seaweed",
}

BUCKETS = {
    "aquatic-life": {
        "label": "Aquatic Life",
        "description": "Fish, crustaceans, turtles, marine mammals, and other aquatic animals.",
    },
    "aquatic-habitats": {
        "label": "Aquatic Habitats",
        "description": "Aquariums, plants, coral, shells, and other aquatic environment elements.",
    },
    "nautical-items": {
        "label": "Nautical Items",
        "description": "Boats, navigation gear, safety objects, and other sea-adjacent items.",
    },
    "maker-workshop": {
        "label": "Maker Workshop",
        "description": "Fabrication, electronics, welding, sewing, and mixed maker-space equipment.",
    },
    "workshop-tools": {
        "label": "Workshop Tools",
        "description": "Garage, woodshop, and handheld or powered workshop tools and fixtures.",
    },
}


@dataclass(frozen=True)
class SourcePack:
    dir_name: str
    has_manifest: bool = True


SOURCE_PACKS = (
    SourcePack("aquarium_25_transparent_icon_pack"),
    SourcePack("cuttlefish_ocean_avatar_pack"),
    SourcePack("fishlore_cartoon_fish_icons", has_manifest=False),
    SourcePack("garage_workshop_avatar_icon_pack"),
    SourcePack("maker_workshop_avatar_icon_pack"),
    SourcePack("woodshop_avatar_icon_pack_final"),
    SourcePack("woodworking_power_tool_icon_pack"),
)


def ensure_source_root() -> Path:
    if not SOURCE_ROOT.is_dir():
        raise FileNotFoundError(f"Source root not found: {SOURCE_ROOT!r}")
    return SOURCE_ROOT


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def snake_to_label(value: str) -> str:
    return " ".join(part.capitalize() for part in value.replace("-", "_").split("_"))


def stable_unique(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        out.append(value)
    return out


def path_from_served(pack_root: Path, asset_root: str, served_root: str, served_path: str) -> Path:
    suffix = served_path.removeprefix(served_root).lstrip("/")
    return pack_root / asset_root / suffix


def infer_bucket(pack_name: str, icon: dict, icon_id: str) -> str:
    if pack_name == "aquarium_25_transparent_icon_pack":
        return "aquatic-habitats" if icon_id in HABITAT_IDS else "aquatic-life"
    if pack_name == "cuttlefish_ocean_avatar_pack":
        if icon_id in NAUTICAL_IDS:
            return "nautical-items"
        if icon_id in HABITAT_IDS:
            return "aquatic-habitats"
        return "aquatic-life"
    if pack_name == "fishlore_cartoon_fish_icons":
        return "aquatic-life"
    if pack_name == "maker_workshop_avatar_icon_pack":
        return "maker-workshop"
    return "workshop-tools"


def derive_grid(icon: dict, index: int) -> dict[str, int]:
    row = icon.get("row")
    column = icon.get("column")
    if isinstance(row, int) and isinstance(column, int):
        return {"row": row, "column": column}
    source_index = icon.get("sourceIndex")
    if isinstance(source_index, int):
        return {"row": source_index // 10 + 1, "column": source_index % 10 + 1}
    return {"row": 1, "column": index + 1}


def source_files_for_manifest_icon(pack_root: Path, manifest: dict, icon: dict) -> dict[str, Path]:
    files: dict[str, Path] = {}
    if "files" in icon:
        for size in SIZES:
            files[size] = pack_root / icon["files"][size]
        return files
    asset_root = manifest["assetRoot"]
    served_root = manifest["servedRoot"]
    for size in SIZES:
        served_path = icon.get(f"path{size}") or icon.get("path")
        candidate = path_from_served(pack_root, asset_root, served_root, served_path)
        if not candidate.exists():
            top_level_candidate = pack_root / size / f"{icon['id']}.png"
            if top_level_candidate.exists():
                candidate = top_level_candidate
        files[size] = candidate
    return files


def copy_pack_provenance(pack_root: Path, pack_dir_name: str, manifest: dict | None, icon_count: int) -> dict:
    target_dir = META_PACKS_DIR / pack_dir_name
    target_dir.mkdir(parents=True, exist_ok=True)

    readme_src = pack_root / "README.md"
    manifest_src = pack_root / "manifest.json"
    readme_dst = target_dir / "README.md"
    manifest_dst = target_dir / "manifest.json"

    if readme_src.exists():
        shutil.copy2(readme_src, readme_dst)
    else:
        readme_dst.write_text(
            f"# {pack_dir_name}\n\nImported from `{pack_root}` during curated icon-share rebuild.\n"
        )

    if manifest_src.exists():
        shutil.copy2(manifest_src, manifest_dst)
        created = manifest.get("created") or TODAY
        display_name = manifest.get("name", pack_dir_name.replace("_", "-"))
    else:
        inferred = {
            "name": pack_dir_name.replace("_", "-"),
            "created": TODAY,
            "count": icon_count,
            "sizes": [int(size) for size in SIZES],
            "notes": "Manifest inferred during import because the source pack did not provide one.",
        }
        manifest_dst.write_text(json.dumps(inferred, indent=2) + "\n")
        created = TODAY
        display_name = inferred["name"]

    return {
        "id": pack_dir_name,
        "name": display_name,
        "created": created,
        "iconCount": icon_count,
        "sizes": [int(size) for size in SIZES],
        "sourceReadme": str(readme_dst.relative_to(ICONS_ROOT)).replace("\\", "/"),
        "sourceManifest": str(manifest_dst.relative_to(ICONS_ROOT)).replace("\\", "/"),
        "previewFiles": [],
    }


def build_manifest_pack_items(pack_root: Path, pack_dir_name: str) -> tuple[list[dict], dict]:
    manifest = load_json(pack_root / "manifest.json")
    items: list[dict] = []

    for index, icon in enumerate(manifest["icons"]):
        icon_id = icon["id"]
        files = source_files_for_manifest_icon(pack_root, manifest, icon)
        bucket = infer_bucket(pack_dir_name, icon, icon_id)

        repo_files: dict[str, str] = {}
        for size, source_path in files.items():
            if not source_path.exists():
                raise FileNotFoundError(f"Missing source file for {icon_id} size {size}: {source_path}")
            target_path = ICONS_ROOT / bucket / size / f"{icon_id}.png"
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, target_path)
            repo_files[size] = str(target_path.relative_to(ICONS_ROOT)).replace("\\", "/")

        tags = stable_unique(
            [
                *icon_id.split("_"),
                bucket.replace("-", " "),
                str(icon.get("category", "")).replace("_", " "),
                str(icon.get("toolType", "")),
                str(icon.get("colorway", "")),
                pack_dir_name.replace("_", " "),
            ]
        )

        items.append(
            {
                "id": icon_id,
                "label": icon.get("label") or snake_to_label(icon_id),
                "bucket": bucket,
                "description": icon.get("description")
                or f"Glossy AI-generated {bucket} icon featuring {snake_to_label(icon_id)}.",
                "tags": tags,
                "sourcePack": pack_dir_name,
                "sourceSheet": icon.get("sourceSheet", ""),
                "sourceGrid": derive_grid(icon, index),
                "sizes": [int(size) for size in SIZES],
                "files": repo_files,
                "preview": repo_files["128"],
            }
        )

    source_pack = copy_pack_provenance(pack_root, pack_dir_name, manifest, len(items))
    return items, source_pack


def build_fishlore_pack_items(pack_root: Path, pack_dir_name: str) -> tuple[list[dict], dict]:
    items: list[dict] = []
    stems = sorted(path.stem.removesuffix("_128") for path in (pack_root / "128").glob("*.png"))

    for index, stem in enumerate(stems):
        icon_id = stem.replace("-", "_")
        repo_files: dict[str, str] = {}
        for size in SIZES:
            source_path = pack_root / size / f"{stem}_{size}.png"
            if not source_path.exists():
                raise FileNotFoundError(f"Missing fishlore size {size} for {stem}: {source_path}")
            target_path = ICONS_ROOT / "aquatic-life" / size / f"{icon_id}.png"
            target_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, target_path)
            repo_files[size] = str(target_path.relative_to(ICONS_ROOT)).replace("\\", "/")

        label = snake_to_label(icon_id)
        items.append(
            {
                "id": icon_id,
                "label": label,
                "bucket": "aquatic-life",
                "description": f"Cartoon aquatic-life icon featuring {label}.",
                "tags": stable_unique([*icon_id.split("_"), "fishlore", "cartoon", "fish"]),
                "sourcePack": pack_dir_name,
                "sourceSheet": "",
                "sourceGrid": {"row": 1, "column": index + 1},
                "sizes": [int(size) for size in SIZES],
                "files": repo_files,
                "preview": repo_files["128"],
            }
        )

    source_pack = copy_pack_provenance(pack_root, pack_dir_name, None, len(items))
    return items, source_pack


def reset_icons_surface() -> None:
    for child in ICONS_ROOT.iterdir():
        if child.name in {SCHEMA_PATH.name, GALLERY_PATH.name, README_PATH.name, CATALOG_PATH.name}:
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def build_catalog(items: list[dict], source_packs: list[dict]) -> dict:
    bucket_counts = {bucket_id: 0 for bucket_id in BUCKETS}
    for item in items:
        bucket_counts[item["bucket"]] += 1

    buckets = [
        {
            "id": bucket_id,
            "label": meta["label"],
            "description": meta["description"],
            "count": bucket_counts[bucket_id],
        }
        for bucket_id, meta in BUCKETS.items()
        if bucket_counts[bucket_id] > 0
    ]

    return {
        "title": "AI Slop Trough Icon Catalog",
        "generatedOn": TODAY,
        "license": "CC0-1.0",
        "totalIcons": len(items),
        "sizes": [int(size) for size in SIZES],
        "buckets": buckets,
        "sourcePacks": source_packs,
        "items": items,
    }


def main() -> None:
    source_root = ensure_source_root()
    reset_icons_surface()

    all_items: list[dict] = []
    source_packs: list[dict] = []

    for pack in SOURCE_PACKS:
        if pack.dir_name in EXCLUDED_PACKS:
            continue
        pack_root = source_root / pack.dir_name
        if not pack_root.is_dir():
            raise FileNotFoundError(f"Missing source pack: {pack_root}")
        if pack.has_manifest:
            items, source_pack = build_manifest_pack_items(pack_root, pack.dir_name)
        else:
            items, source_pack = build_fishlore_pack_items(pack_root, pack.dir_name)
        all_items.extend(items)
        source_packs.append(source_pack)

    all_items.sort(key=lambda item: (item["bucket"], item["label"], item["id"]))
    source_packs.sort(key=lambda pack: pack["name"])

    catalog = build_catalog(all_items, source_packs)
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2) + "\n")

    print(f"Imported {len(all_items)} icons from {len(source_packs)} clean source packs.")
    for bucket in catalog["buckets"]:
        print(f"{bucket['id']}: {bucket['count']}")


if __name__ == "__main__":
    main()
