import pytest
from unittest import TestCase, skip


def amazing_math(a, b):
    return a + b


class TestOldWay(TestCase):
    def test_with_method(self):
        for a, b, out in [
            (1, 2, 3),
            (2, 4, 6)]:

            self.assertEqual(amazing_math(a, b), out)

    @skip
    def test_list_equality(self):
        self.assertListEqual([1, 2, 3], [2, 2, 3])


def test_old_way():
    for a, b, out in [
        (1, 2, 3),
        (2, 4, 6)]:
        assert amazing_math(a, b) == out


@pytest.mark.parametrize(('a', 'b', 'out'), [
    (1, 2, 3),
    (2, 4, 6),
])
def test_new_way(a, b, out):
    assert amazing_math(a, b) == out


@pytest.mark.skip
def test_new_list_equality():
    assert [1, 2, 3] == [2, 2, 3]
