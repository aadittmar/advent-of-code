from pathlib import Path
from typing import List


class Lock:
    def __init__(self) -> None:
        self.dial_position: int = 50
        self.total_times_at_zero: int = 0
        self.total_landed_on_zero: int = 0

    def spin_and_count_zeroes(self) -> None:
        for rotation in self.get_rotation_sequence_from_input_file():
            self.rotate(rotation)

        print(f"Part 1: {self.total_landed_on_zero}")
        print(f"Part 2: {self.total_times_at_zero}")

    def rotate(self, rotation: str) -> None:
        if "R" in rotation:
            self.rotate_right(self.get_num_of_clicks(rotation, "R"))
        elif "L" in rotation:
            self.rotate_left(self.get_num_of_clicks(rotation, "L"))

        self.dial_position = self.dial_position % 100

        self.update_landed_on_zero()

    def rotate_right(self, clicks: int) -> None:
        dial_to: int = self.dial_position + clicks

        while self.dial_position != dial_to:
            self.click_right()

    def rotate_left(self, clicks: int) -> None:
        dial_to: int = self.dial_position - clicks

        while self.dial_position != dial_to:
            self.click_left()

    def click_left(self) -> None:
        self.dial_position -= 1
        self.check_for_zero()

    def click_right(self) -> None:
        self.dial_position += 1
        self.check_for_zero()

    def check_for_zero(self) -> None:
        if self.dial_position % 100 == 0:
            self.total_times_at_zero += 1

    def update_landed_on_zero(self) -> None:
        if self.dial_position == 0:
            self.total_landed_on_zero += 1

    @staticmethod
    def get_num_of_clicks(rotation: str, direction: str) -> int:
        return int(rotation.replace(direction, "").strip())

    @staticmethod
    def get_rotation_sequence_from_input_file() -> List[str]:
        # Use path relative to this source file so the file is found even if
        # the script is run from a different working directory.




if __name__ == "__main__":
    lock = Lock()
    lock.spin_and_count_zeroes()
