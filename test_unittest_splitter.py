# Вывод:
#   ...
#   ----------------------------------------------------------------------
#   Ran 3 tests in 0.000s
#
#   OK
#   Время работы теста testDelimiter: 0.01730 мс
#   Время работы теста testSimpleString: 0.01020 мс
#   Время работы теста testTypeConvert: 0.01900 мс

import splitter
import unittest
import time

def timer(func):
    def wrapper(*args):
        start = time.perf_counter_ns()
        func(*args)
        runtime = (time.perf_counter_ns() - start) / 1000000
        print("Время работы теста %s: %1.5f мс" % (func.__name__, runtime))
    return wrapper


class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        pass # Выполнить настройку тестов при необходимости
    def tearDown(self) -> None:
        pass # Выполнить завершающие действия при необходимости

    @timer
    def testSimpleString(self):
        r = splitter.split('erger 100 rfg 23.4')
        self.assertEqual(r, ['erger','100','rfg','23.4'])

    @timer
    def testTypeConvert(self):
        r = splitter.split('erger 100 rfg 23.4', [str,int,str,float])
        self.assertEqual(r, ['erger',100,'rfg',23.4])

    @timer
    def testDelimiter(self):
        r = splitter.split('erger,100,rfg,23.4', delimiter=',')
        self.assertEqual(r, ['erger','100','rfg','23.4'])

if __name__ == "__main__":
    unittest.main()
