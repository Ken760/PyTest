import pytest


@pytest.mark.parametrize("set_, expected_result", [
                                                    [type({1, 1, 2, 2, 3, 4, 5, 6}), set],
                                                    [type({1, 1, 2, 2, 3, 4, 5, 6}), set],
                                                    [type({1, 1, 2, 2, 3, 4, 5, 6}), set],
                                                    ])
def test_passing(set_, expected_result):
    """Проверка на тип данных"""

    assert set_ == expected_result




