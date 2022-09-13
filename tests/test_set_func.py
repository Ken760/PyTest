import pytest


@pytest.mark.parametrize("set_, expected_result", [
                                                    [type({1, 1, 2, 2, 3, 4, 5, 6}), set],
                                                    [type({'apple', 'apple', 'cherry'}), set],
                                                    [type({1, 6}), set],
                                                    ])
def test_for_type(set_, expected_result):
    """Проверка на тип данных"""

    assert set_ == expected_result


@pytest.mark.parametrize("set_, expected_result",  [
                                    [{1, 1, 1, 4, 4}, {1, 1, 1, 4}],
                                    [{'apple', 'apple', 'cherry'}, {'apple', 'cherry'}],
                                    [{'test', 'test', 1, 1, 1}, {'test', 1}]
                                    ])
def test_for_comparison(set_, expected_result):
    """Проверка на равенсто множеств"""

    assert set_ == expected_result


@pytest.mark.parametrize("set_, expected_result",  [
                                    [{1, 1, 1, 4, 4}, {1, 3, 1, 4}],
                                    [{'apple', 'apple', 'cherry'}, {'banan', 'cherry'}],
                                    [{'test', 'test', 1, 1, 1}, {2, 4, 'test', 1}]
                                    ])
def test_for_inequality(set_, expected_result):
    """Проверка на не равенсто множеств"""

    assert set_ != expected_result

