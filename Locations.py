from typing import Dict, Optional, NamedTuple
from BaseClasses import Location


class CaveStoryLocation(Location):
    game: str = "Cave Story"

    def __init__(self, player: int, name="", code=None, parent=None):
        super(CaveStoryLocation, self).__init__(player, name, code, parent)
        self.event = code is None


class LocationData(NamedTuple):
    id: int
    ltype: Optional[str] = ""
    flag: int = 0


# 998000 - 998067
# mapping of items in each region
location_region_mapping: Dict[str, Dict[str, LocationData]] = {
    "First Cave": {
        "Capsule 1 (3 hp)": LocationData(998000),
    },
    "Gunsmith": {
        "Polar Star": LocationData(998001),
        "Spur": LocationData(998002),
    },
    "Mimiga Village": {
        "map system": LocationData(998003),
    },
    "Assembly Hall": {
        "Bubbler": LocationData(998004),
    },
    "Resevoir": {
        "Silver Locket": LocationData(998005),
    },
    "Graveyard": {
        "Arthur's Key": LocationData(998006),
        "Mr Little": LocationData(998007),
    },
    "Ma Pignon Room": {
        "Mushroom Badge": LocationData(998008),
        "Ma Pignon": LocationData(998009),
    },
    "Yamashita Farm": {
        "Capsule 2 (3 hp)": LocationData(998010),
    },
    "Arthur's House": {
        "Booster 2.0": LocationData(998011),
    },
    "Egg Corridor": {
        "Capsule 3 (3hp)": LocationData(998012),
        "Capsule 4 (4hp)": LocationData(998013),
    },
    "Egg 6": {
        "ID Card": LocationData(998014),
    },
    "Egg Observation Room": {
        "Missile Launcher": LocationData(998015),
    },
    "Egg Corridor?": {
        "Missile Expansion": LocationData(998016),
    },
    "Sister Boss Room": {
        "Missile Expansion": LocationData(998017),
    },
    "Grasstown": {
        "Santa's key": LocationData(998018),
        "Jelly Juice": LocationData(998019),
        "Capsule 5 (5hp)": LocationData(998020),
        "Rusted Key": LocationData(998021),
        "Gum Key": LocationData(998022),
        "Missile Expansion": LocationData(998023),
    },
    "Santa's House": {
        "Fireball": LocationData(998024),
        "Charcoal": LocationData(998025),
    },
    "Chaco's House": {
        "Chaco's Lipstick": LocationData(998026),
    },
    "Power Room": {
        "Explosive": LocationData(998027),
    },
    "Grasstown Hut": {
        "Missile Expansion": LocationData(998028),
    },
    "Execution Chamber": {
        "Capsule 6 (5hp)": LocationData(998029),
    },
    "Gum Room": {
        "Gum Base": LocationData(998030),
    },
    "Sand Zone": {
        "Capsule 7 (5hp)": LocationData(998031),
        "Mick (Chest Dog)": LocationData(998032),
        "Capsule 8 (5hp)": LocationData(998033),
        "Kakeru (Running Dog)": LocationData(998034),
        "Nene (Sleeping Dog)": LocationData(998035),
    },
    "Sand Zone Residence": {
        "Machine Gun": LocationData(998036),
    },
    "Small Room": {
        "Hajime": LocationData(998037),
        "Curly's Panties": LocationData(998038),
    },
    "Jenka's House": {
        "Life Pot": LocationData(998039),
    },
    "Deserted House": {
        "Shinobu": LocationData(998040),
    },
    "Storage Room": {
        "Blade": LocationData(998041),
    },
    "Labyrinth I": {
        "Capsule 9 (5hp)": LocationData(998042),
    },
    "Labyrinth Shop": {
        "Turbocharge": LocationData(998043),
        "Whimsical Star": LocationData(998044),
        "Snake": LocationData(998045),
    },
    "Labyrinth Clinic": {
        "Cure-all": LocationData(998046),
    },
    "Camp": {
        "Clinic Key": LocationData(998047),
        "Arms Barrier": LocationData(998048),
    },
    "Labyrinth B": {
        "Booster 0.8": LocationData(998049),
    },
    "Boulder Chamber": {
        "Super Missile Launcher": LocationData(998050),
    },
    "Core Boss Room": {
        "Tow Rope": LocationData(998051),
        "Curly's Air Tank": LocationData(998052),
    },
    "Ironhead Boss": {
        "Alien Medal": LocationData(998053),
    },
    "Plantation": {
        "Teleporter Room Key": LocationData(998054),
        "Broken Sprinkler": LocationData(998055),
        "Capsule 10 (4hp)": LocationData(998056),
        "Iron Bond": LocationData(998057),
        "Puppy Capsule (5hp)": LocationData(998058),
    },
    "Plantation Jail": {
        "Sue's Letter": LocationData(998059),
    },
    "Plantation Hideout": {
        "Mimiga Mask": LocationData(998060),
    },
    "Itoh's Hideout": {
        "Controller": LocationData(998061),
    },
    "Mimiga Room": {
        "Sprinkler": LocationData(998062),
    },
    "Clock Room": {
        "Nikumaru Counter": LocationData(998063),
    },
    "Little house": {
        "Nemesis": LocationData(998064),
    },
    "Last Cave": {
        "Clay Medal": LocationData(998065),
    },
    "Hell B1": {
        "Capsule 11 (5hp)": LocationData(998066),
    },
    "Hell B3": {
        "Missile Expansion": LocationData(998067),
    }
}
