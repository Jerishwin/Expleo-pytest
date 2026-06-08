import pytest

@pytest.mark.smoke
def test_sample1():
    print("hi")

@pytest.mark.reg
def test_sample_2():
    print("Hello")
    x=5
    y=5
    assert x>=y

@pytest.mark.smoke
def test_sample_3():
    x=10
    y=5
    assert x>y

@pytest.mark.xfail
def test_sample_4():
    x="arun"
    y="aruns"
    assert x.__eq__(y)
