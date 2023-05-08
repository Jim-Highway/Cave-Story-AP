from typing import Dict, Set
from BaseClasses import Region, Entrance, LocationProgressType, MultiWorld
from . import Locations


# Creates a new Region with the locations found in `location_region_mapping`
# and adds them to the world

# A lot of this was copied from Noita and very slightly modified.
def create_region(world: MultiWorld, player: int, region_name: str) -> Region:
    new_region = Region(region_name, player, world)

    for location_name, location_data in Locations.location_region_mapping.get(region_name, {}).items():
        location = Locations.CaveStoryLocation(player, location_name, location_data.id, new_region)
        opt_bosses = world.bosses_as_checks[player].value
        ltype = location_data.ltype
        flag = location_data.flag

        if flag == 0 or ltype == "boss" and flag <= opt_bosses:
            new_region.locations.append(location)

    return new_region


def create_connections(player: int, regions: Dict[str, Region]) -> None:
    for source, destinations in cave_story_connections.items():
        new_entrances = []

        for destination in destinations:
            entrance = Entrance(player, f"From {source} To {destination}", regions[source])
            entrance.connect(regions[destination])
            new_entrances.append(entrance)

        regions[source].exits = new_entrances


def create_regions(world: Multiworld, player: int) -> Dict[str, Region]:
    regions = {name: create_region(world, player, name) for name in cave_story_regions}
    return regions


def create_all_regions_and_connections(world: MultiWorld, player: int) -> None:
    created_regions = create_regions(world, player)
    create_connections(player, created_regions)

    world.regions += created_regions.values()


cave_story_connections: Dict[str, Set[str]] = {
    "Menu": {"Start Point", "Arthur's House", "Camp"},
    "Start Point": {"First Cave"},
    "First Cave": {"Hermit Gunsmith", "Mimiga Village", "Start Point"},
    "Hermit Gunsmith": {"First Cave"},

    "Mimiga Village": {"Resevoir", "Mimiga Village Save Point", "Yamashita Farm", "Shack", "Assembly Hall",
                       "Graveyard", "Arthur's House"},
    "Resevoir": {"Mimiga Village", "Dark Place"},
    "Mimiga Village Save Point": {"Mimiga Village"},
    "Yamashita Farm": {"Mimiga Village"},
    "Shack": {"Mimiga Village"},
    "Assembly Hall": {"Mimiga Village"},
    "Graveyard": {"Mimiga Village", "Storage"},
    "Arthur's House": {"Mimiga Village", "Egg Corridor", "Grasstown", "Sand Zone", "Egg Corridor?", "Labyrinth B",
                       "Teleporter"},
    "Storage": {"Graveyard"},

    "Egg Corridor": {"Arthur's House", "Cthulhu's Abode", "Egg No. 06", "Egg Observation Room", "Egg No. 01",
                     "Egg No. 00", "Side Room"},
    "Cthulhu's Abode": {"Egg Corridor"},
    "Egg No. 06": {"Egg Corridor"},
    "Egg Observation Room": {"Egg Corridor"},
    "Egg No. 01": {"Egg Corridor"},
    "Egg No. 00": {"Egg Corridor"},
    "Side Room": {"Egg Corridor"},

    "Grasstown": {"Arthur's House", "Santa's House", "Chaco's House", "Power Room", "Grasstown Save Point",
                  "Grasstown Hut", "Shelter", "Execution Chamber", "Gum"},
    "Santa's House": {"Grasstown"},
    "Chaco's Hosue": {"Grasstown"},
    "Power Room": {"Grasstown"},
    "Grasstown Save Point": {"Grasstown"},
    "Grasstown Hut": {"Grasstown"},
    "Shelter": {"Grasstown", "Jail No. 02"},
    "Execution Chamber": {"Grasstown"},
    "Gum": {"Grasstown"},

    "Sand Zone": {"Arthur's House", "Sand Zone Residence", "Jenka's House", "Deserted House", "Sand Zone Storehouse",
                  "Labyrinth I"},
    "Sand Zone Residence": {"Sand Zone", "Small Room"},
    "Small Room": {"Sand Zone Residence"},
    "Jenka's House": {"Sand Zone"},
    "Deserted House": {"Sand Zone"},
    "Sand Zone Storehouse": {"Sand Zone"},
    "Labyrinth I": {"Sand Zone", "Labyrinth H"},

    "Labyrinth H": {"Labyrinth W", "Labyrinth I"},
    "Labyrinth W": {"Labyrinth B", "Labyrinth Shop", "Labyrinth H", "Clinic Ruins", "Camp"},
    "Clinic Ruins": {"Labyrinth W"},
    "Camp": {"Labyrinth W"},
    "Labyrinth B": {"Labyrinth W", "Boulder Room", "Arthur's House"},
    "Labyrinth Shop": {"Labyrinth W", "Labyrinth M"},
    "Labyrinth M": {"Labyrinth B", "Labyrinth Shop", "Dark Place"},
    "Boulder Room": {"Labyrinth B", "Labyrinth M"},
    "Dark Place": {"Labyrinth M", "Core", "Waterway"},
    "Core": {"Dark Place"},
    "Waterway": {"Dark Place", "Waterway Cabin"},
    "Waterway Cabin": {"Waterway", "Dark Place"},
    # Not sure about the connection to a dark place for the waterway cabin as it's not always there

    "Egg Corridor?": {"Arthur's House", "Cthulhu's Abode?", "Egg Observation Room?", "Egg No. 00?", "Side Room?"},
    "Cthulhu's Abode?": {"Egg Corridor?"},
    "Egg Observation Room?": {"Egg Corridor?"},
    "Egg No. 00?": {"Egg Corridor?", "Outer Wall"},
    "Side Room?": {"Egg Corridor?"},

    "Teleporter": {"Plantation", "Arthur's House"},
    "Plantation": {"Teleporter", "Jail No. 01", "Hideout", "Rest Area", "Jail No. 02", "Storehouse", "Last Cave",
                   "Last Cave (Hidden)", "Passage"},
    "Jail No. 01": {"Plantation"},
    "Hideout": {"Plantation"},
    "Rest Area": {"Plantation"},
    "Jail No. 02": {"Plantation", "Shelter"},
    "Storehouse": {"Plantation", "Outer Wall"},
    "Passage": {"Plantation", "Statue Chamber"},
    "Statue Chamber": {"Passage"},
    "Last Cave": {"Plantation", "Balcony"},
    "Last Cave (Hidden)": {"Plantation", "Balcony"},

    "Balcony": {"Last Cave", "Last Cave (Hidden)", "Prefab Building", "Throne Room", "Prefab House"},
    "Prefab Building": {"Balcony"},
    "Throne Room": {"Balcony", "The King's Table"},
    "The King's Table": {"Throne Room", "Black Space"},
    "Black Space": {"The King's Table"},
    "Prefab House": {"Sacred Ground B1"},

    "Sacred Ground B1": {"Sacred Ground B2"},
    "Sacred Ground B2": {"Sacred Ground B3"},
    "Sacred Ground B3": {"Passage?"},
    "Passage?": {"Corridor", "Statue Chamber?"},
    "Statue Chamber?": {"Passage?"},
    "Corridor": {"Seal Chamber"},

    "Outer Wall": {"Storehouse", "Clock Room", "Egg No. 00", "Little House"},
    "Clock Room": {"Outer Wall"},
    "Little House": {"Outer Wall"}
}

cave_story_regions: Set[str] = set(cave_story_connections.keys()).union(*cave_story_connections.values())
