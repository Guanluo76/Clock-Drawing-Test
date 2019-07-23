"""
Test module for all model mixins.
"""

import unittest


def model_mixins_test_suite():
    """
    Build test sutie for model_mixins package.
    """
    import models.model_mixins.image_mixin
    import models.model_mixins.scale_element_mixin
    import models.model_mixins.scale_image_mixin

    # load test cases in this pacakge
    model_mixins_tests = [
                unittest.TestLoader().loadTestsFromModule(
                                    models.model_mixins.image_mixin),
                unittest.TestLoader().loadTestsFromModule(
                                    models.model_mixins.scale_element_mixin),
                unittest.TestLoader().loadTestsFromModule(
                                    models.model_mixins.scale_image_mixin),
            ]

    # build test suite and add test cases
    model_mixins_test_suite = unittest.TestSuite()
    [ model_mixins_test_suite.addTest(test) for test in model_mixins_tests ]

    return model_mixins_test_suite


if __name__ == '__main__':
    # run model_mixins test
    runner = unittest.TextTestRunner()
    runner.run(model_mixins_test_suite())

