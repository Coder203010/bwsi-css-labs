import pytest

from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([1,2,3],3) == [0,1]
    assert two_sum([-1,-2,-3],-4) == [0,2]
    assert two_sum([1,2], 10) == []