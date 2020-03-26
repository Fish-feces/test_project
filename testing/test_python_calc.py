import random
from math import isnan

import pytest

from python.calc import Calc


def get_calc_params() -> list:
    rand_int_list = [random.randint(1, 100) if i % 2 == 0 else -random.randint(1, 100) for i in range(2)]
    rand_float_list = [random.uniform(1, 100) if i % 2 == 0 else -random.randint(1, 100) for i in range(2)]
    raise_err_list = [
        0,
        True,
        False,
        float('Nan'),
        'rand_str?',
        ['list', ],
        {'key': 'val'},
        {'set', },
        ('tuple', ),
        # 123j 突然想起来还有复数
    ]

    return rand_float_list + rand_int_list + raise_err_list


@pytest.mark.parametrize('a', get_calc_params())
@pytest.mark.parametrize('b', get_calc_params())
def test_calc(a, b, timer_fixture):
    calc = Calc()
    if isinstance(a, (int, float, bool)) and isinstance(b, (int, float, bool)):
        if b == 0:
            if isnan(a):
                assert isnan(calc.add(a, b))
            else:
                assert calc.add(a, b) == a + b
                with pytest.raises(ZeroDivisionError) as e:
                    calc.div(a, b)
                if isinstance(a, (int, bool)):
                    assert e.value.args[0] == 'division by zero'
                else:
                    assert e.value.args[0] == 'float division by zero'
        else:
            if isnan(a) or isnan(b):
                assert isnan(calc.add(a, b))
                assert isnan(calc.div(a, b))
            else:
                assert calc.add(a, b) == a + b
                assert calc.div(a, b) == a / b
    else:
        type_a_name = type(a).__name__
        type_b_name = type(b).__name__
        with pytest.raises(TypeError) as e:
            calc.div(a, b)
        assert e.value.args[0] == f"unsupported operand type(s) for /: '{type_a_name}' and '{type_b_name}'"

        # str, list, dict, set, tuple
        if type_a_name == type_b_name:
            if type_a_name in ['set', 'dict']:
                with pytest.raises(TypeError) as e:
                    calc.add(a, b)
                assert e.value.args[0] == f"unsupported operand type(s) for +: '{type_a_name}' and '{type_b_name}'"
            else:
                assert calc.add(a, b) == a + b
        else:
            with pytest.raises(TypeError):
                calc.add(a, b)
