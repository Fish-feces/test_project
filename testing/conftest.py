import time

from pytest import fixture

from python.calc import Calc


# scope fixture的作用范围:session(多个文件) > module(单个py文件) > class > function
@fixture(scope='function', autouse=True)
def timer_fixture():
    start = time.time()
    yield
    print(f' ->Time cost: {time.time() - start}s.')


@fixture(scope='function', autouse=False)
def calc():
    # yield Calc()
    # 可以用return, 效果只有setup没有teardown
    return Calc()
