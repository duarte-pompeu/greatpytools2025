from random import sample
from random import seed


def pick_random_elements(
    list: list[int] | None = None,
    how_many_elements: int = 1,
    seed_for_deterministic_output=0,
    a_forgotten_flag: bool = False,
) -> list[int]:
    if list is None:
        list = []

    seed(seed_for_deterministic_output)
    return sample(list, how_many_elements)


if __name__ == "__main__":
    print("Hello!")
    print(pick_random_elements([2025, 7, 24, 16, 0], 10, True))
