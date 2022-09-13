import pytest


@pytest.mark.parametrize("tuples, expected_result", [
                                                    [type(("apple", "banana", "cherry")), tuple],
                                                    [type(("test", 1, {(1, 1, 1) : 1}, 2, 3)), tuple],
                                                    [type((1, {('banana'): 1})), tuple]
                                                    ])
def test_for_type(tuples, expected_result):
    """Проверка на тип данных"""

    assert tuples == expected_result


@pytest.mark.parametrize("tuples, expected_result",  [
                                    [(1, 2, 3, 4), 1],
                                    [("apple", "banana", "cherry"), 'apple'],
                                    [("test", 1, {(1, 1, 1) : 1}, 2, 3), 'test']
                                    ])
def test_for_elements(tuples, expected_result):
    """Проверка нулевого элементов кортежа"""

    assert tuples[0] == expected_result


@pytest.mark.parametrize("tuples, expected_result",  [
                                    [(1, 2, 3, 4), (4, 3, 2, 1)],
                                    [("apple", "banana", "cherry"), ("chery", "apple", "banana")],
                                    [("test", 1, {(1, 1, 1) : 1}, 2, 3), (3, 2, {(1, 1, 1): 1}, "test")]
                                    ])
def test_for_inequality(tuples, expected_result):
    """Проверка на не равенсто кортежей"""

    assert tuples != expected_result

