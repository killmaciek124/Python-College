

from main import random_yx, print_hint, random_yx
import pytest

def test_random_yx():
    x=random_yx()
    assert  len(x)==2


#def test_print_hint():
 #   x=print_hint(['1','a'], ['2','b'])
  #  assert x == 'Prawiej i niżej'


def test_random_yx():
    y=random_yx()
    assert y[0].isnumeric()
    assert y[1].isnumeric() == False