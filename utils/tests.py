from __future__ import absolute_import
import unittest


def utils_test_suite():
    """
    Build test suite for utils suite.
    """
    import utils.lazy_property

    utils_tests = [
                unittest.TestLoader().loadTestsFromModule(utils.lazy_property),
            ]

    utils_test_suite = unittest.TestSuite()
    [ utils_test_suite.addTests(test) for test in utils_tests ]

    return utils_test_suite

if __name__ == '__main__':
    # run utils tests
    runner = unittest.TextTestRunner()
    runner.run(utils_test_suite())

