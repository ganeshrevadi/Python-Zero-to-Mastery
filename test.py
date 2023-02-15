import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')
    def test_do_stuff(self):
        num = 10
        result = main.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'hslelg'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)
    def tearDown(self):
        print('Cleaning Up')

if __name__ == '__main__':
    unittest.main()