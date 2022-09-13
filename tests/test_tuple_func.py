import pytest


@pytest.mark.parametrize("tuples, expected_result", [
                                                    [type(("apple", "banana", "cherry")), tuple],
                                                    [type(("test", 1, {(1, 1, 1) : 1}, 2, 3)), tuple],
                                                    [type((1, {('banana'): 1})), tuple]
                                                    ])
def test_for_type(tuples, expected_result):
    """Проверка на тип данных"""

    assert tuples == expected_result


