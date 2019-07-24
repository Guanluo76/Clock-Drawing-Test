"""
Test module for all utils.
"""

from __future__ import absolute_import
import unittest


def utils_test_suite():
    """
    Build test sutie for utils package.
    """
    from utils.metas.tests import metas_test_suite

    # load test suites from child packages
    utils_test_suites = [
                metas_test_suite(),
            ]

    import utils.lazy_property
    import utils.subscribe_methods

    # load test cases in this pacakge
    utils_tests = [
                unittest.TestLoader().loadTestsFromModule(
                                    utils.lazy_property),
                unittest.TestLoader().loadTestsFromModule(
                                    utils.subscribe_methods),
            ]

    # build test suite and add test cases
    utils_test_suite = unittest.TestSuite(utils_test_suites)
    [ utils_test_suite.addTest(test) for test in utils_tests ]

    return utils_test_suite


if __name__ == '__main__':
    # run utils tests
    runner = unittest.TextTestRunner()
    runner.run(utils_test_suite())

