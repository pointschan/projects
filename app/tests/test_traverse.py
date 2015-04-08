__author__ = 'pointschan'


from control.traverse import *
import unittest
import os

sub_dir = '/home/vagrant/workspaces/projects/app/tests/'

class test_traverse(unittest.TestCase):

    def setUp(self):
        self.test_case_1 = []
        self.test_case_2 = ['-d']
        self.test_case_3 = ['-h']
        self.test_case_4 = ['-d', '.']
        self.test_case_5 = ['-d', 'xxx']
        self.test_case_6 = ['-d', '/home/vagrant/workspaces/projects/app/docs/']
        self.test_case_7 = ['-d', '/home/vagrant/workspaces/docs/']
        self.test_case_8 = ['anything', 'anything']

    def test_traverse_case_1(self):
        result = main(self.test_case_1)
        print result
        self.assertEqual(result, 'usage: traverse.py -d <directory>')

    def test_traverse_case_2(self):
        result = main(self.test_case_2)
        print result
        self.assertEqual(result, 'usage: traverse.py -d <directory>')

    def test_traverse_case_3(self):
        result = main(self.test_case_3)
        print result
        self.assertEqual(result, 'usage: traverse.py -d <directory>')

    def test_traverse_case_4(self):
        os.chdir('/home/vagrant/workspaces/docs')
        f = open(os.path.join(sub_dir, 'expected_test_result_4.txt'), 'r')
        expected_result=f.read()
        # print expected_result
        result = main(self.test_case_4)
        # print result
        self.assertEqual(result, expected_result)

    def test_traverse_case_5(self):
        test_result = main(self.test_case_5)
        # print test_result
        self.assertEqual(test_result, 'Directory is xxx\nThere are no files to scan\n')

    def test_traverse_case_6(self):
        f = open(os.path.join(sub_dir, 'expected_test_result_6.txt'), 'r')
        expected_result=f.read()
        # print expected_result
        result = main(self.test_case_6)
        # print result
        self.assertEqual(result, expected_result)

    def test_traverse_case_7(self):
        f = open(os.path.join(sub_dir, 'expected_test_result_7.txt'), 'r')
        expected_result=f.read()
        # print expected_result
        result = main(self.test_case_7)
        # print result
        self.assertEqual(result, expected_result)

    def test_traverse_case_8(self):
        result = main(self.test_case_8)
        print result
        self.assertEqual(result, 'usage: traverse.py -d <directory>')


if __name__ == '__main__':
    unittest.main()

