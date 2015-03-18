from control.main_control import *
from nose.tools import *
import unittest


st_control_list = ['GET,http://offers-st.lxc.points.com:1300/offers/',
                   'GET,http://offers-st.lxc.points.com:1300/offers/offer123',
                   'POST,http://offers-st.lxc.points.com:1300/offers/']

ft_control_list = ['GET,http://offers-ft.lxc.points.com:1300/offers/',
                   'GET,http://offers-ft.lxc.points.com:1300/offers/offer123',
                   'POST,http://offers-ft.lxc.points.com:1300/offers/']

class main_controlTestCase(unittest.TestCase):

    def setup(self):
        print "SETUP!"

    def teardown(self):
        print "TEAR DOWN!"

    def test_basic(self):
        print "I RAN!"

    def testBuildStagingList(self):
        urlList = getUrlfile("staging_url.txt")
        self.assertEqual(urlList, st_control_list)

    def testBuildFtList(self):
        urlList = getUrlfile("ft_url.txt")
        self.assertEqual(urlList, ft_control_list)


if __name__ == '__main__':
    unittest.main()
