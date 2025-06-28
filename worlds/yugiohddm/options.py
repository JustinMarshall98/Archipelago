import typing
import dataclasses

from Options import Range, Choice, PerGameCommonOptions, Toggle
from dataclasses import dataclass

class DuelistRematches(Choice):
    """
    No matter what choice is made here, Yami Yugi will be unlocked after defeating every duelist
    at least once.

    "No Rematches" means each duelist you unlock can be beaten only once to yield a check.

    "One Rematch" means each duelist you unlock can be beaten twice to yield two different checks.

    "Two Rematches" means each duelist you unlock can be beaten thrice to yield three different checks.
    Note, the Two Rematches option is currently under development and is not present in the yaml

    The more rematches you add, the more game time you can expect to have.
    Extra check locations are randomized dice rewards that get added to your dice pool.
    """
    display_name = "Duelist Rematches"
    option_no_rematches = 0
    option_one_rematch = 1
    #option_two_rematches = 2
    default = 1

#class StartingDuelists(Range):
#    """
#    The number of Duelists to start with unlocked.
#    There are 92 duelists in total, Yami Yugi is reserved for the game's goal and there must be
#    at least as many duelists to unlock as you start with, so the max you can start with is 45.
#    """
#    display_name = "Starting Duelists"
#    range_start = 1
#    range_end = 45
#    default = 1

class RandomizeStartingDice(Toggle):
    """
    In the base game your starting pool is lightly randomized to begin with,
    but this setting takes off the guardrails and generates you with any
    15 dice from the game (no duplicates).

    It is impossible to generate a starting pool with only items and no creatures to summon.

    With this option active you have to select all of your new dice from your collection
    before the first duel begins.
    """
    display_name = "Randomize Starting Dice"

class ShopProgressInPool(Toggle):
    """
    Adds 91 checks to the multiworld, 18 shop progression levels and
    73 money rewards of varying sizes. These checks locations are
    added as additional rewards for beating a duelist in Free Duel
    for the first time.

    Normally playing Free Duel doesn't award either of these things,
    so turning this option on makes Grandpa's Shop functional
    during your playthrough.
    """
    display_name = "Money and Shop Progress in Pool"

@dataclass
class YGODDMOptions(PerGameCommonOptions):
    duelist_rematches: DuelistRematches
    #starting_duelists: StartingDuelists
    randomize_starting_dice: RandomizeStartingDice
    shop_progress_in_pool: ShopProgressInPool

    def serialize(self) -> typing.Dict[str, int]:
        return {field.name: getattr(self, field.name).value for field in dataclasses.fields(self)}