from src.with_formatting_plus_linting import pick_random_elements


def test_example():
    result = pick_random_elements([1, 2, 3], 1, seed_for_deterministic_output=3)
    print(result)
    assert result == [1]
