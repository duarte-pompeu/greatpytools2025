from src.before import pick_random_elements


def test_before():
    assert pick_random_elements([1,2,3], 1, seed_for_deterministic_output=3) == [1]
