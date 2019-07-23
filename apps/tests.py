"""
Top-level test module for all apps.
"""

from __future__ import absolute_import
import unittest


def apps_test_suite():
    """
    Build test suite for apps package.
    """
    from apps.circularity.tests import circularity_test_suite
    from apps.scale.tests import scale_test_suite

    # load test suites from child packages
    apps_test_suites = [
                circularity_test_suite(),
                scale_test_suite(),
            ]

    # load test cases in this pacakge
    apps_tests = [
            ]

    # build test suite and add test cases
    apps_test_suite = unittest.TestSuite(apps_test_suites)
    [ apps_test_suite.addTest(apps_test) for apps_test in apps_tests ]

    return apps_test_suite


if __name__ == '__main__':
    # run apps tests
    runner = unittest.TextTestRunner()
    runner.run(apps_test_suite())

