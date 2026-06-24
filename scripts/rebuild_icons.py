#!/usr/bin/env python3

from __future__ import annotations

import json
import shutil
from copy import deepcopy
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "share" / "icons" / "catalog.json"
SOURCE_PACKS_DIR = REPO_ROOT / "share" / "icons" / "_meta" / "source-packs"
DEFAULT_DOWNLOADS_DIR = Path("/home/ericl/Downloads")
SIZES = ("64", "128", "256", "512")


OFFICE_OVERRIDES = {
    "pencil": "marker",
    "pen": "pencil",
    "crayon": "highlighter",
    "highlighter": "pen",
    "marker": "crayon",
    "eraser": "scissors",
    "whiteout": "whiteout",
    "ruler": "glue_bottle",
    "scissors": "ruler",
    "glue_bottle": "eraser",
    "calendar": "sticky_notes",
    "notebook": "clipboard_checklist",
    "clipboard_checklist": "notebook",
    "sticky_notes": "calendar",
    "envelope": "envelope",
    "paperclip": "paperclip",
    "binder_clip": "binder_clip",
    "push_pin": "push_pin",
    "stapler": "hole_punch",
    "hole_punch": "stapler",
    "filing_cabinet": "copier",
    "paper_cutter": "paper_cutter",
    "printer": "filing_cabinet",
    "copier": "calculator",
    "calculator": "printer",
    "tape_dispenser": "in_tray",
    "file_folder": "out_tray",
    "document_stack": "file_folder",
    "in_tray": "document_stack",
    "out_tray": "tape_dispenser",
    "corded_phone": "corded_phone",
    "whiteboard": "projector",
    "blackboard": "whiteboard",
    "projector": "computer_monitor",
    "computer_monitor": "blackboard",
    "keyboard": "keyboard",
    "desk_lamp": "office_chair",
    "office_chair": "wall_clock",
    "wall_clock": "desk_lamp",
    "desk_clock": "desk_clock",
    "lunchbox": "lunchbox",
    "lunch_bag": "water_bottle",
    "coffee_mug": "office_desk",
    "water_bottle": "lunch_bag",
    "office_desk": "coffee_mug",
    "backpack": "backpack",
    "name_badge": "office_plant",
    "thumb_drive": "name_badge",
    "paper_shredder": "paper_shredder",
    "office_plant": "thumb_drive",
}

MAKER_OVERRIDES = {
    "benchy_boat": "printer_3d_cartesian",
    "printer_3d_cartesian": "geppetto",
    "printer_3d_enclosed": "pinocchio",
    "geppetto": "benchy_boat",
    "pinocchio": "printer_3d_enclosed",
    "archaeology_brush": "archaeology_shovel",
    "archaeology_trowel": "archaeology_brush",
    "archaeology_hand_pick": "archaeology_trowel",
    "archaeology_shovel": "archaeology_hand_pick",
    "archaeology_sieve": "archaeology_sieve",
    "cnc_machine": "microscope_binocular",
    "magnifying_glass": "cnc_machine",
    "microscope_classic": "microscope_classic",
    "microscope_digital": "magnifying_glass",
    "microscope_binocular": "microscope_digital",
    "microscope_field": "microscope_field",
    "microscope_pocket": "microscope_pocket",
    "binoculars": "astrolabe",
    "telescope": "telescope",
    "astrolabe": "binoculars",
    "pirate_flag": "compass_antique",
    "compass_antique": "compass_modern",
    "compass_modern": "pirate_flag",
    "satellite": "satellite",
    "laptop": "laptop",
    "smartphone": "flip_phone",
    "flip_phone": "walkie_talkie",
    "rugged_phone": "rugged_phone",
    "candybar_phone": "smartphone",
    "walkie_talkie": "candybar_phone",
    "woodworking_hammer": "woodworking_hammer",
    "woodworking_hand_saw": "woodworking_mallet",
    "woodworking_chisel": "woodworking_hand_saw",
    "woodworking_mallet": "woodworking_chisel",
    "woodworking_hand_plane": "woodworking_hand_plane",
    "woodworking_clamp": "woodworking_router",
    "woodworking_router": "woodworking_table_saw",
    "woodworking_circular_saw": "woodworking_drill_press",
    "woodworking_table_saw": "woodworking_clamp",
    "woodworking_drill_press": "woodworking_circular_saw",
}

AQUARIUM_ADVANCED_OVERRIDES = {
    "discus_blue": "sick_fish_thermometer",
    "discus_red": "school_of_fish",
    "discus_turquoise": "aquarium_medication",
    "discus_pigeon_blood": "quarantine_tank",
    "discus_golden": "sponge_filter",
    "hypancistrus_zebra": "air_stone_bubbler",
    "hypancistrus_king_tiger": "breeder_box",
    "hypancistrus_snowball": "algae_scraper",
    "hypancistrus_inspector": "aquarium_net",
    "hypancistrus_spotted": "siphon_hose",
    "ancistrus_longfin": "ancistrus_longfin",
    "ancistrus_albino": "ancistrus_albino",
    "ancistrus_bristlenose": "ancistrus_bristlenose",
    "ancistrus_calico": "ancistrus_calico",
    "snail_mystery": "snail_mystery",
    "snail_nerite": "snail_nerite",
    "snail_ramshorn": "snail_ramshorn",
    "hillstream_loach": "hillstream_loach",
    "catfish_corydoras": "catfish_corydoras",
    "catfish_pictus": "catfish_pictus",
    "catfish_whiskered": "catfish_whiskered",
    "plant_banana": "plant_banana",
    "plant_anubias_nana": "plant_anubias_nana",
    "plant_amazon_sword": "plant_amazon_sword",
    "plant_java_fern": "plant_java_fern",
    "plant_anacharis": "plant_anacharis",
    "crayfish_orange": "crayfish_orange",
    "crayfish_blue": "crayfish_blue",
    "crayfish_natural": "crayfish_natural",
    "goldfish_fancy": "goldfish_fancy",
    "goldfish_comet": "goldfish_comet",
    "koi": "koi",
    "convict_cichlid": "convict_cichlid",
    "brine_shrimp": "brine_shrimp",
    "glass_shrimp": "glass_shrimp",
    "minnows": "minnows",
    "bloodworms": "bloodworms",
    "blackworms": "blackworms",
    "daphnia": "daphnia",
    "earthworm_red_wiggler": "earthworm_red_wiggler",
    "thermometer_clip_on": "discus_blue",
    "thermometer_strip": "discus_red",
    "thermometer_floating": "discus_turquoise",
    "sea_salt_container": "discus_pigeon_blood",
    "water_aging_barrel": "discus_golden",
    "mop_spill": "hypancistrus_zebra",
    "aquarium_cracked_leaking": "hypancistrus_king_tiger",
    "aquarium_cracked_empty": "hypancistrus_snowball",
    "sick_goldfish": "hypancistrus_inspector",
    "sick_fish_ich": "hypancistrus_spotted",
    "sick_fish_thermometer": "thermometer_clip_on",
    "school_of_fish": "thermometer_strip",
    "aquarium_medication": "thermometer_floating",
    "quarantine_tank": "sea_salt_container",
    "sponge_filter": "water_aging_barrel",
    "air_stone_bubbler": "mop_spill",
    "breeder_box": "aquarium_cracked_leaking",
    "algae_scraper": "aquarium_cracked_empty",
    "aquarium_net": "sick_goldfish",
    "siphon_hose": "sick_fish_ich",
}


@dataclass(frozen=True)
class PackConfig:
    avatar_dir: str
    overrides: dict[str, str]


PACKS: dict[str, PackConfig] = {
    "aquarium_25_icon_pack": PackConfig("aquarium-25", {}),
    "cuttlefish_aquarium_advanced_avatar_pack": PackConfig(
        "aquarium-advanced",
        AQUARIUM_ADVANCED_OVERRIDES,
    ),
    "cuttlefish_ocean_avatar_pack": PackConfig("ocean", {}),
    "cuttlefish_ocean_maker_avatar_pack": PackConfig("ocean-maker", MAKER_OVERRIDES),
    "cuttlefish_office_avatar_pack": PackConfig("office", OFFICE_OVERRIDES),
}


def detect_source_root() -> Path:
    required = set(PACKS)
    for child in sorted(DEFAULT_DOWNLOADS_DIR.iterdir()):
        if not child.is_dir():
            continue
        present = {entry.name for entry in child.iterdir() if entry.is_dir()}
        if required.issubset(present):
            return child
    raise FileNotFoundError(
        f"Could not find source pack directory under {DEFAULT_DOWNLOADS_DIR}"
    )


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def build_corrected_items(source_root: Path) -> tuple[list[dict], list[str]]:
    current_catalog = load_json(CATALOG_PATH)
    current_items = current_catalog["items"]
    item_templates = {item["id"]: item for item in current_items}
    corrected_by_id: dict[str, dict] = {}

    for pack_name, config in PACKS.items():
        manifest_path = SOURCE_PACKS_DIR / pack_name / "manifest.json"
        manifest = load_json(manifest_path)
        source_avatar_root = (
            source_root
            / pack_name
            / "packages"
            / "web"
            / "public"
            / "avatars"
            / config.avatar_dir
        )

        for icon in manifest["icons"]:
            source_id = icon["id"]
            actual_id = config.overrides.get(source_id, source_id)
            if actual_id in corrected_by_id:
                raise ValueError(f"Duplicate corrected id detected: {actual_id}")
            if actual_id not in item_templates:
                raise KeyError(f"Missing catalog template for id: {actual_id}")

            item = deepcopy(item_templates[actual_id])
            item["sourcePack"] = pack_name
            item["sourceSheet"] = icon["sourceSheet"]
            item["sourceGrid"] = {
                "row": icon["row"],
                "column": icon["column"],
            }
            item["preview"] = item["files"]["128"]
            corrected_by_id[actual_id] = item

            for size in SIZES:
                source_file = source_avatar_root / size / f"{source_id}.png"
                dest_file = REPO_ROOT / "share" / "icons" / item["files"][size]
                if not source_file.exists():
                    raise FileNotFoundError(source_file)
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source_file, dest_file)

    missing = sorted(set(item_templates) - set(corrected_by_id))
    if missing:
        raise ValueError(f"Missing corrected items: {missing}")

    corrected_items = [corrected_by_id[item["id"]] for item in current_items]
    return corrected_items, [item["id"] for item in corrected_items]


def write_catalog(corrected_items: list[dict]) -> None:
    catalog = load_json(CATALOG_PATH)
    catalog["generatedOn"] = datetime.now(timezone.utc).date().isoformat()
    catalog["items"] = corrected_items
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2) + "\n")


def main() -> None:
    source_root = detect_source_root()
    corrected_items, corrected_ids = build_corrected_items(source_root)
    write_catalog(corrected_items)
    print(f"Rebuilt {len(corrected_ids)} icons from {source_root!s}")


if __name__ == "__main__":
    main()
