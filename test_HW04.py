#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import unittest
from HW04 import get_repo


class TestResults(unittest.TestCase):

    def testOutputList(self):
        self.assertEqual(get_repo("chinmliu"),
                         [['CS_546', 9], ['git_fall_2019', 2], ['HW02TriangleTest', 9], ['HW04a', 11], ['HW09', 2], ['SSW-567', 2], ['SSW-810', 2]])


if __name__ == '__main__':
    unittest.main()
