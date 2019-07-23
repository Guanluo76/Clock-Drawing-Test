"""
Top-level test module for models.
"""

from __future__ import absolute_import
import unittest


def models_test_suite():
    """
    Build test suite for models package.
    """
    from models.model_mixins.tests import model_mixins_test_suite

    # load test suites from child packages
    models_test_suites = [
                model_mixins_test_suite(),
            ]

    import models.clock_face
    import models.circle
    import models.element
    import models.element_image

    # load test cases in this pacakge
    models_tests = [
                unittest.TestLoader().loadTestsFromModule(models.clock_face),
                unittest.TestLoader().loadTestsFromModule(models.circle),
                unittest.TestLoader().loadTestsFromModule(models.element),
                unittest.TestLoader().loadTestsFromModule(
                                                    models.element_image),
            ]

    # build test suite and add test cases
    models_test_suite = unittest.TestSuite(models_test_suites)
    [ models_test_suite.addTest(test) for test in models_tests ]

    return models_test_suite


if __name__ == '__main__':
    # run models tests
    runner = unittest.TextTestRunner()
    runner.run(models_test_suite())

