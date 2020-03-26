import time

from pytest import fixture


# scope fixture的作用范围:session(多个文件) > module(单个py文件) > class > function
@fixture(scope='function', autouse=False)
def timer_fixture():
    start = time.time()
    yield
    print(f' ->Time cost: {time.time() - start}s.')
