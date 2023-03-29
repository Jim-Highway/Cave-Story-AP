from BaseClasses import Item
import typing


class CaveStoryItem(Item):
    game: str = "Cave Story"


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool


# 997001 - 997055
# ItemData(ID, Used for progress) maybe change this? (Noita for reference)
item_table = {
    # weapons
    "Polar Star": ItemData(997001, True),
    "Spur": ItemData(997002, True),
    "Missile Launcher": ItemData(997003, False),
    "Super Missile Launcher": ItemData(997004, False),
    "Fireball": ItemData(997005, True),
    "Snake": ItemData(997006, False),
    "Bubbler": ItemData(997007, False),
    "Machine Gun": ItemData(997008, True),
    "Blade": ItemData(997009, True),
    "Nemesis": ItemData(997010, False),
    # inventory
    "Map System": ItemData(997011, False),
    "Locket": ItemData(997012, True),
    "Arthur Key": ItemData(997013, True),
    "id Card": ItemData(997014, True),
    "Santa Key": ItemData(997015, True),
    "Lipstick": ItemData(997016, False),
    "Juice": ItemData(997017, True),
    "Charcoal": ItemData(997018, True),
    "Rusty Key": ItemData(997019, True),
    "Gum Key": ItemData(997020, True),
    "Gum Base": ItemData(997021, True),
    "Explosive": ItemData(997022, True),
    "Panties": ItemData(997023, False),
    "Hajime": ItemData(997024, True),
    "Mick": ItemData(997025, True),
    "Kakeru": ItemData(997026, True),
    "Nene": ItemData(997027, True),
    "Shinobu": ItemData(997028, True),
    "Lifepot": ItemData(997029, False),
    "Turbocharge": ItemData(997030, False),
    "Clinic Key": ItemData(997031, True),
    "Arms Barrier": ItemData(997032, False),
    "Cure-All": ItemData(997033, True),
    "Booster 0.8": ItemData(997034, True),
    "Booster 2.0": ItemData(997035, True),
    "Tow Rope": ItemData(997036, True),
    "Air Tank": ItemData(997037, True),
    "Alien Medal": ItemData(997038, False),
    "Whimsical Star": ItemData(997039, False),
    "Nikumaru": ItemData(997040, False),
    "Teleport Room Key": ItemData(997041, True),
    "Letter": ItemData(997042, True),
    "Mimiga Mask": ItemData(997043, True),
    "Broken Sprinkler": ItemData(997044, True),
    "Sprinkler": ItemData(997045, True),
    "Controller": ItemData(997046, True),
    "Mushroom Badge": ItemData(997047, True),
    "Ma Pignon": ItemData(997048, True),
    "Mr Little": ItemData(997049, True),
    "Iron Bond": ItemData(997050, True),
    "Clay Medal": ItemData(997051, False),
    "Life Capsule (3HP)": ItemData(997052, False),
    "Life Capsule (4HP)": ItemData(997053, False),
    "life Capsule (5HP)": ItemData(997054, False),
    "Missile Expansion": ItemData(997055, False)
}

item_frequencies = {
    "Life Capsule (3HP)": 3,
    "Life Capsule (4HP)": 2,
    "life Capsule (5HP)": 7,
    "Missile Expansion": 5,
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
