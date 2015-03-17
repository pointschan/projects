from control.main_control import  *
from nose.tools import *
import unittest


st_control_list = ['GET,http://offers-st.lxc.points.com:1300/offers/',
                   'GET,http://offers-st.lxc.points.com:1300/offers/offer123',
                   'POST,http://offers-st.lxc.points.com:1300/offers/']

ft_control_list = ['GET,http://offers-ft.lxc.points.com:1300/offers/',
                   'GET,http://offers-ft.lxc.points.com:1300/offers/offer123',
                   'POST,http://offers-ft.lxc.points.com:1300/offers/']

class main_controlTestCase(unittest.TestCase):

    def testBuildStagingList(self):
        urlList = getUrlfile("staging_url.txt")
        print urlList
        self.assertEqual(urlList, st_control_list)

    def testBuildFtList(self):
        urlList = getUrlfile("ft_url.txt")
        print urlList
        self.assertEqual(urlList, ft_control_list)


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"


if __name__ == '__main__':
    unittest.main()
