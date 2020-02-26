#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from unittest import mock
import unittest
from unittest.mock import Mock

import HW04


class TestResults(unittest.TestCase):

    @mock.patch("HW04.requests.get")
    def testGetRepo(self, mock_get_repo):
        r_results = [{'name': 'CS-546'}, {'name': 'HW02TriangleTest'}, {'name': 'HW04a'}, {'name': 'HW09'},
                     {'name': 'SSW-567'}]
        mock_get_repo.return_value.json.return_value = r_results
        self.assertEqual(r_results, HW04.get_repo('chinmliu'))

    @mock.patch("HW04.requests.get")
    @mock.patch("HW04.get_repo")
    def testGetCommits(self, mock_get_repo, mock_get_commits):
        mock_get_repo.return_value = [{'name': 'CS-546'}, {'name': 'HW02TriangleTest'}, {'name': 'HW04a'}, {'name': 'HW09'},
                     {'name': 'SSW-567'}]
        raw_list = [['CS-546', 1], ['HW02TriangleTest', 1], ['HW04a', 1], ['HW09', 1], ['SSW-567', 1]]
        mock_get_commits.return_value.json.return_value = {1, 1, 1, 1, 1}
        self.assertEqual(raw_list, HW04.get_commits('chinmliu'))


if __name__ == '__main__':
    unittest.main()
