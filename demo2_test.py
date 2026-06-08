import pytest

@pytest.mark.smoke
def test_sample1():
    print("hi")


@pytest.mark.reg
def test_sample_2():
    print("Hello")


@pytest.mark.smoke
def test_sample_3():
    print("hi")

@pytest.mark.parametrize("test_input,expected",[(1,3),(3,6),(5,7)])
def test_para(test_input,expected):
    assert test_input+2==expected


