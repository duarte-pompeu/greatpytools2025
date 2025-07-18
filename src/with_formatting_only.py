import math
import statistics
from itertools import *
from random import *
from random import sample
from random import seed
from typing import List


def pick_random_elements(
    list: List[int] = [],
    how_many_elements: int = 1,
    allow_repetition: bool = True,
    seed_for_deterministic_output=0,
    a_forgotten_flag: bool = False,
) -> List[int]:
    seed(seed_for_deterministic_output)

    if allow_repetition:
        return list(permutations(list, how_many_elements))
    else:
        elements = sample(list, how_many_elements)

    return elements


if __name__ == "__main__":
    print(f"Hello!")
    print(pick_random_elements([2025, 7, 24, 16, 0], 10, True))
