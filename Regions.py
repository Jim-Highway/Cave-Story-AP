from typing import Dict, Set
from BaseClasses import Region, Entrance, LocationProgressType, MultiWorld
from . import Locations

# Creates a new Region with the locations found in `location_region_mapping`
# and adds them to the world

def create_region(world: MultiWorld, player: int, region_name: str) -> \
        Region: new_region = Region(region_name, player, world)

    # Here we create and assign locations to the region
   # for location_name, location_data in Locations.location_region_mapping.get(region_name, {}).items():
       # location = Locations.CaveStoryLocation(player, location_name,location_data.id, new_region)

cave_story_connections: Dict[str, Set[str]] = {
    "Menu": {"Start Point", "Arthur's House", "Camp"},
    "Start Point": {"First Cave"},
    "First Cave": {"Hermit Gunsmith", "Mimiga Village", "Start Point"},
    "Hermit Gunsmith": {"First Cave"},

    "Mimiga Village": {"Resevoir", "Mimiga Village Save Point", "Yamashita Farm", "Shack", "Assembly Hall",
                       "Graveyard", "Arthur's House"},
    "Resevoir": {"Mimiga Village", "Waterway"},
    "Mimiga Village Save Point": {"Mimiga Village"},
    "Yamashita Farm": {"Mimiga Village"},
    "Shack": {"Mimiga Village"},
    "Assembly Hall": {"Mimiga Village"},
    "Graveyard": {"Mimiga Village", "shroom boss"},
    "Arthur's House": {"Mimiga Village", "Egg Corridor", "Grasstown", "Sand Zone", "Egg Corridor?", "Labyrinth B",
                       "Teleporter"},

    "Egg Corridor": {"Cthulhu's Abode", "Egg No. 06", "Egg Observation Room", ""},

    "Grasstown": {"Santa's House", "Chaco's House", "Power Room", "Grasstown Save Point", "Grasstown Hut",
                  "kazuma room","Execution Chamber", "gum room"},
    "Santa's House": {"Grasstown"},
    "Chaco's Hosue": {"Grasstown"},
    "Power Room": {"Grasstown"},
    "Grasstown Save Point": {"Grasstown"},
    "Grasstown Hut": {"Grasstown"},
    "kazuma room": {"Grasstown", "mimiga jail"},
    "Execution Chamber": {"Grasstown"},
    "gum room": {"Grasstown"},

    "Sand Zone": {"Sand Zone Residence", "Jenka's House", "Deserted House", "toroko boss", "labyrinth"}
    "Sand Zone Residence": {"Sand Zone", "Small Room"},
    "Small Room": {"Sand Zone Residence"},
    "Jenka's House": {"Sand Zone"},
    "Deserted House": {"Sand Zone"},
    "toroko boss": {"Sand Zone"},
    "labyrinth": {"Sand Zone", "labyrinth"},
}