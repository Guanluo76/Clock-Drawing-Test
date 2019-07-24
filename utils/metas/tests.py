"""
Test module for all util metas.
"""

import unittest


def metas_test_suite():
    """
    Build test sutie for metas package.
    """
    import utils.metas.meta_mixin
    import utils.metas.meta_singleton
    import utils.metas.meta_singleton_mixin

    # load test cases in this pacakge
    metas_tests = [
                unittest.TestLoader().loadTestsFromModule(
                                    utils.metas.meta_mixin),
                unittest.TestLoader().loadTestsFromModule(
                                    utils.metas.meta_singleton),
                unittest.TestLoader().loadTestsFromModule(
                                    utils.metas.meta_singleton_mixin),
            ]

    # build test suite and add test cases
    metas_test_suite = unittest.TestSuite()
    [ metas_test_suite.addTest(test) for test in metas_tests ]

    return metas_test_suite


if __name__ == '__main__':
    # run metas tests
    runner = unittest.TextTestRunner()
    runner.run(metas_test_suite())

