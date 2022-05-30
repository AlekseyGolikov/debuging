
import splitter
import unittest
import time

def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        func(*args)
        runtime = time.perf_counter() - start
        print("Время работы тестового API: %4.2f" % runtime)
    return wrapper

@timer
class TestSplitFunction(unittest.TestCase):
    def setUp(self):
        pass # Выполнить настройку тестов при необходимости
    def tearDown(self) -> None:
        pass # Выполнить завершающие действия при необходимости
    def testSimpleString(self):
        r = splitter.split('erger 100 rfg 23.4')
        self.assertEqual(r, ['erger','100','rfg','23.4'])
    def testTypeConvert(self):
        r = splitter.split('erger 100 rfg 23.4', [str,int,str,float])
        self.assertEqual(r, ['erger',100,'rfg',23.4])
    def testDelimiter(self):
        r = splitter.split('erger,100,rfg,23.4', delimiter=',')
        self.assertEqual(r, ['erger','100','rfg','23.4'])

if __name__ == "__main__":
    unittest.main()
