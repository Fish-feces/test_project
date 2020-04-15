import time

from pytest import fixture


@fixture(scope='function', autouse=True)
def timer_fixture():
    start = time.time()
    yield
    print(f' ->Time cost: {time.time() - start}s.')
