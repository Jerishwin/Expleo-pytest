import pytest
from pytest import assume

@pytest.mark.smoke
def test_sample1():
    print("hi")

@pytest.mark.reg
def test_sample_2():
    print("Hello")
    x=5
    y=5
    assume(x>y)

@pytest.mark.smoke
def test_sample_3():
    x=10
    y=5
    assume(x=y)

@pytest.mark.xfail
def test_sample_4():
    x="arun"
    y="aruns"
    assume(x.__eq__(y))
