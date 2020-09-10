from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=10)


class MyThreadPoolExecutor:

    def __init__(self):
        pass

    @staticmethod
    def add(fn):
        return pool.submit(fn)
