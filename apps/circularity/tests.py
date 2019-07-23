"""
Test module for circularity package.
"""

import unittest


def circularity_test_suite():
    """
    Build test suite for circularity package.
    """
    import apps.circularity.circularity

    # load test cases in this pacakge
    circularity_tests = [
                unittest.TestLoader().loadTestsFromModule(
                                            apps.circularity.circularity),
            ]

    # build test suite and add test cases
    circularity_test_suite = unittest.TestSuite()
    [ circularity_test_suite.addTests(test) for test in circularity_tests ]

    return circularity_test_suite


if __name__ == '__main__':
    # run circularity tests
    runner = unittest.TextTestRunner()
    runner.run(circularity_test_suite())

