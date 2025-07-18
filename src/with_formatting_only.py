from typing import List
import math
from random import seed, sample
import statistics


from itertools import *
from random import *


def pick_random_elements(
    list: List[int] = [],
    how_many_elements: int = 1,
    seed_for_deterministic_output=0,
    a_forgotten_flag: bool = False,
) -> List[int]:
    seed(seed_for_deterministic_output)
    return sample(list, how_many_elements)


if __name__ == "__main__":
    print(f"Hello!")
    print(pick_random_elements([2025, 7, 24, 16, 0], 10, True))
