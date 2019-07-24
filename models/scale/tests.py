"""
Test module for all scale models.
"""

import unittest


def scale_model_test_suite():
    """
    Build test sutie for scale package.
    """
    import models.scale.scale_element

    # load test cases in this pacakge
    scale_model_tests = [
                unittest.TestLoader().loadTestsFromModule(
                                                models.scale.scale_element),
            ]

    # build test suite and add test cases
    scale_model_test_suite = unittest.TestSuite()
    [ scale_model_test_suite.addTest(test) for test in scale_model_tests ]

    return scale_model_test_suite


if __name__ == '__main__':
    # run scale test
    runner = unittest.TextTestRunner()
    runner.run(scale_model_test_suite())

