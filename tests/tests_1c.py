import pytest

from labs.lab_1.lab_1c import max_subarray_sum

def test_subarray_sum():
    assert max_subarray_sum([1,2,3]) == 6
    assert max_subarray_sum([0,0,0]) == 0
    assert max_subarray_sum([-1,-2,-3]) == -1

def test_undefined_sum():
    with pytest.raises(ValueError, match="Undefined array."):
        max_subarray_sum([1,2,"hello"]) 

if __name__ == "__main__":
    pytest.main()