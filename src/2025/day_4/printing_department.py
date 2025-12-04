import dataclasses

from src.utils.utils import get_input_file


@dataclasses.dataclass
class Location:
    line: int
    column: int


class Rolls:

    def __init__(self) -> None:
        self.roll_locations: list[list[str]] = self.get_roll_locations()

        print(
            "Part 1 (initial accessible rolls): ",
            len(self.find_how_many_rolls_can_be_removed()),
        )

        print(
            "Part 2 (total removed rolls): ",
            len(self.remove_all_possible_rolls()),
        )

    def remove_all_possible_rolls(self) -> list[Location]:
        removed_rolls: list[Location] = []

        while True:
            removable_rolls: list[Location] = self.find_how_many_rolls_can_be_removed()

            if not removable_rolls:
                break

            removed_rolls = [*removed_rolls, *removable_rolls]

            for location in removable_rolls:
                self.roll_locations[location.line][location.column] = "x"

        return removed_rolls

    def find_how_many_rolls_can_be_removed(self) -> list[Location]:
        removable_rolls: list[Location] = []

        for line in range(len(self.roll_locations)):
            for column in range(len(self.roll_locations[line])):

                location = Location(line, column)

                if self.roll_can_be_removed(location):
                    removable_rolls.append(location)

        return removable_rolls

    def roll_can_be_removed(self, location: Location) -> bool:
        rolls_around: int = 0

        if not self.there_is_a_roll_here(location):
            return False

        if self.there_is_a_roll_here(location):
            for neighbor in self.get_locations_around(location):
                if self.there_is_a_roll_here(neighbor):
                    rolls_around += 1

        return rolls_around < 4

    @staticmethod
    def get_locations_around(location: Location) -> list[Location]:
        return [
            Location(location.line - 1, location.column),  # Up
            Location(location.line + 1, location.column),  # Down
            Location(location.line, location.column - 1),  # Left
            Location(location.line, location.column + 1),  # Right
            Location(location.line - 1, location.column - 1),  # Up-Left
            Location(location.line - 1, location.column + 1),  # Up-Right
            Location(location.line + 1, location.column - 1),  # Down-Left
            Location(location.line + 1, location.column + 1),  # Down-Right
        ]

    def there_is_a_roll_here(self, location: Location) -> bool:
        if location.line < 0 or location.column < 0:
            return False

        try:
            return self.roll_locations[location.line][location.column] == "@"
        except:
            return False

    @staticmethod
    def get_roll_locations() -> list[list[str]]:
        return [list(line) for line in get_input_file(__file__).splitlines()]


if __name__ == "__main__":
    rolls = Rolls()
