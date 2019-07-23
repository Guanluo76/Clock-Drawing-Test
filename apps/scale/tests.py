"""
Test module for scale package.
"""

import unittest


def scale_test_suite():
    """
    Build test suite for scale package.
    """
    import apps.scale.scale

    # load test cases in this pacakge
    scale_tests = [
                unittest.TestLoader().loadTestsFromModule(apps.scale.scale),
            ]

    # build test suite and add test cases
    scale_test_suite = unittest.TestSuite()
    [ scale_test_suite.addTests(test) for test in scale_tests ]

    return scale_test_suite


if __name__ == '__main__':
    # run scale tests
    runner = unittest.TextTestRunner()
    runner.run(scale_test_suite())

