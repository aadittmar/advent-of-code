from pathlib import Path
from typing import List


class BatteryBank:

    def __init__(self) -> None:
        self.banks: List[str] = self.get_battery_banks()

        self.find_total_joltage_part_1()
        self.find_total_joltage_part_2()

    def find_total_joltage_part_1(self) -> None:
        total_joltage: int = 0

        for bank in self.banks:
            total_joltage += self.find_biggest_sum(bank, iterations=2)

        print("Part 1 (total joltage): ", total_joltage)

    def find_total_joltage_part_2(self) -> None:
        total_joltage: int = 0

        for bank in self.banks:
            total_joltage += self.find_biggest_sum(bank, iterations=12)

        print("Part 2 (total joltage): ", total_joltage)

    def find_biggest_sum(self, bank: str, iterations: int) -> int:
        biggest_sum: List[str] = []

        first_iteration = True
        last_index = 0
        start_index = 0

        for i in range(iterations):

            if not first_iteration:
                start_index = last_index + 1

            amount_from_end = -(iterations - i - 1)

            biggest_number, last_index = self.find_next_biggest_number(
                bank=bank,
                start_index=start_index,
                first_iteration=first_iteration,
                amount_from_end=amount_from_end,
            )

            biggest_sum.append(biggest_number)

            first_iteration = False

        return int("".join(biggest_sum))

    @staticmethod
    def find_next_biggest_number(
        bank: str, start_index: int, first_iteration: bool, amount_from_end: int
    ) -> tuple[str, int]:
        end = None if amount_from_end == 0 else amount_from_end

        slice_start = 0 if first_iteration else start_index
        bank_slice = bank[slice_start:end]

        next_biggest_number = max(bank_slice, key=int)

        index_in_slice = bank_slice.index(next_biggest_number)
        next_biggest_number_index = slice_start + index_in_slice

        return next_biggest_number, next_biggest_number_index

    @staticmethod
    def get_battery_banks() -> List[str]:
        src_dir: Path = Path(__file__).parent
        input_path: Path = src_dir / "banks.txt"

        text: str = input_path.read_text(encoding="utf-8").strip()

        return [line.strip() for line in text.splitlines() if line.strip() != ""]


if __name__ == "__main__":
    batteryBank = BatteryBank()
