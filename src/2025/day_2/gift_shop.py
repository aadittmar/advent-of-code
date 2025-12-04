import math
import time
from typing import List

from src.utils.utils import get_input_file


class ProductIdScrubber:

    def __init__(self) -> None:
        print("Finding Invalid Product IDs...")

        self.product_ids: List[int] = []
        self.get_product_ids()

        self.find_invalid_product_ids_for_sequence_repeated_twice()
        self.find_product_ids_with_repeating_sequence()

    def find_invalid_product_ids_for_sequence_repeated_twice(self) -> None:
        start = time.perf_counter()

        invalid_product_ids = [
            product_id
            for product_id in self.product_ids
            if self.does_product_id_contain_sequence_repeated_twice(product_id)
        ]

        print("First part: ", sum(invalid_product_ids))
        elapsed = time.perf_counter() - start
        print(f"First part time: {elapsed:.6f}s")

    def find_product_ids_with_repeating_sequence(self) -> None:
        start = time.perf_counter()

        invalid_product_ids = [
            product_id
            for product_id in self.product_ids
            if self.product_id_has_repeating_sequence(product_id)
        ]

        print("\nSecond part: ", sum(invalid_product_ids))
        elapsed = time.perf_counter() - start
        print(f"Second part time: {elapsed:.6f}s")

    def get_product_ids(self) -> None:
        for product_id_range in get_input_file(__file__).split(","):
            self.product_ids = [
                *self.product_ids,
                *self.get_ids_from_range(product_id_range),
            ]

    def product_id_has_repeating_sequence(self, product_id: int) -> bool:
        product_id_repeats: bool = True

        for sequence in self.get_all_possibles_sequences_for_product_id(product_id):
            sections = math.ceil(len(str(product_id)) / len(sequence))

            if sections == 1:
                product_id_repeats = False
                break

            section_repeats: bool = True

            for section_index in range(sections):
                current_section: str = str(product_id)[
                    section_index * len(sequence) : (section_index + 1) * len(sequence)
                ]

                if current_section != sequence:
                    section_repeats = False
                    break

            if section_repeats:
                return True

        return product_id_repeats

    @staticmethod
    def get_all_possibles_sequences_for_product_id(product_id: int) -> List[str]:
        sequences: List[str] = []

        for character in str(product_id):
            if len(sequences) == 0:
                sequences.append(character)
            else:
                sequences.append(sequences[-1] + character)

        return sequences

    @staticmethod
    def does_product_id_contain_sequence_repeated_twice(product_id: int) -> bool:
        first_half: str = str(product_id)[: len(str(product_id)) // 2]
        second_half: str = str(product_id)[len(str(product_id)) // 2 :]

        if first_half == second_half:
            return True

        return False

    @staticmethod
    def get_ids_from_range(product_id_range: str) -> List[int]:
        product_id_list: list = []

        current_product_id: int = int(product_id_range.split("-")[0])
        end: int = int(product_id_range.split("-")[1])

        while current_product_id <= end:
            product_id_list.append(current_product_id)
            current_product_id += 1

        return product_id_list


if __name__ == "__main__":
    scrubber = ProductIdScrubber()
