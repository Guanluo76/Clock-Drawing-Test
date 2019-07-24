"""
Top-level test module for the whole program.
"""

from __future__ import absolute_import
import unittest


def cdt_test_suite():
    """
    Build test suite for CDT package.
    """
    from apps.tests import apps_test_suite
    from utils.tests import utils_test_suite
    from models.tests import models_test_suite

    # load test suites from child packages
    cdt_test_suites = [
                apps_test_suite(),
                utils_test_suite(),
                models_test_suite(),
            ]

    import settings
    import image_generator
    import image_loader
    import experiment

    # load test cases in this pacakge
    cdt_tests = [
                unittest.TestLoader().loadTestsFromModule(settings),
                unittest.TestLoader().loadTestsFromModule(image_generator),
                unittest.TestLoader().loadTestsFromModule(image_loader),
                unittest.TestLoader().loadTestsFromModule(experiment),
            ]


    # build test suite and add test cases
    cdt_test_suite = unittest.TestSuite(cdt_test_suites)
    [ cdt_test_suite.addTest(cdt_test) for cdt_test in cdt_tests ]

    return cdt_test_suite


if __name__ == '__main__':
    # run cdt tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(cdt_test_suite())

