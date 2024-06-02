# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50

class Charactersanity(Toggle):
    """Adds all characters to the item pool as well as a location check for each."""
    display_name = "Charactersanity"
    default = True

class IncludeOperationGunsDLC(Toggle):
    """Whether or not the Operation Guns DLC is included."""
    display_name = "Include Operation Guns DLC"
    default = True

class IncludeMoonspellDLC(Toggle):
    """Whether or not the Legacy of the Moonspell DLC is included."""
    display_name = "Include Legacy of the Moonspell DLC"
    default = True

class IncludeEmergencyMeetingDLC(Toggle):
    """Whether or not the Emergency Meeting DLC is included."""
    display_name = "Include Emergency Meeting DLC"
    default = True

class IncludeFoscariDLC(Toggle):
    """Whether or not the Tides of the Foscari DLC is included."""
    display_name = "Include Tides of the Foscari DLC"
    default = True


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["charactersanity"] = Charactersanity
    options["include_moonspell_dlc"] = IncludeMoonspellDLC
    options["include_foscari_dlc"] = IncludeFoscariDLC
    options["include_emergency_meeting_dlc"] = IncludeEmergencyMeetingDLC
    options["include_operation_guns_dlc"] = IncludeOperationGunsDLC
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options