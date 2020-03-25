import random

import pytest

from python.calc import Calc


def get_calc_params() -> list:
    rand_int_list = [random.randint(1, 100) for _ in range(2)]
    rand_float_list = [random.uniform(1, 100) for _ in range(2)]

    return rand_float_list + rand_int_list + [0]


@pytest.mark.parametrize('a', get_calc_params())
@pytest.mark.parametrize('b', get_calc_params())
def test_calc1(a, b):
    calc = Calc()
    assert calc.add(a, b) == a + b

    # 捕获异常 ZeroDivisionError
    if b != 0:
        assert calc.div(a, b) == a / b
    else:
        with pytest.raises(ZeroDivisionError) as e:
            calc.div(a, b)
        if isinstance(a, int):
            assert e.value.args[0] == 'division by zero'
        elif isinstance(a, float):
            assert e.value.args[0] == 'float division by zero'
