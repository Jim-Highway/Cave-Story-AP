# this should be good?
import typing
from Options import Choice, Option, Toggle, Range, OptionSet


class StartLocation(Choice):
    """Choose where to start the game.
	Start Point: Start in the First Cave (Vanilla start)
	Arthur's House: Start in Arthur's House (No access to Mimiga Village until Key found or Core fight/waterway complete
	Camp: Start in the Physician's camp in the Labyrinth"""
    display_name = "Start Location"
    option_Start_Point = 1
    option_Arthurs_House = 2
    option_Camp = 3
    default = 1


class VictoryCondition(Choice):
    """Choose which ending will be the goal
	Bad Ending: Escape with Kazuma
	Good Ending: Defeat the Doctor
	True Ending: Defeat Balos"""
    display_name = "Goal"
    option_Bad_End = 1
    option_Good_End = 2
    option_True_End = 3
    default = 2


class Puppysanity(Toggle):
    """Choose whether puppies can't be found
	anywhere or only in the Sand Zone"""
    display_name = "Puppysanity"


class Glitches(OptionSet):
    """Select which glitches you want to include
	in the randomizer logic"""
    display_name = "Glitches"
	valid_keys = {
		"Cthulhu's Abode (requires 3HP)",
		"Chaco Skip (requires 5HP)",
		"Chaco Skip without a weapon (requires 10HP)",
		"Flightless Grasstown Hut (requires 3HP)",
		"Flightless Camp Chest (requires 9HP)",
		"Sisters Skip (requires flight)",
		"Flightless Plantation Chest (requires 15HP)",
		"Rocket Skip (requires 3HP, Machine Gun, and Booster 2.0)",
	}

class Deathlink(Toggle):
    """When you die, everyone dies. Of course the reverse is true too."""
    display_name = "Deathlink"


cave_story_options: typing.Dict[str, type(Option)] = {
    "starting_location": StartLocation,
    "goal": VictoryCondition,
    "puppysanity": Puppysanity,
    "glitches": Glitches,
    "death_link": Deathlink,
}
