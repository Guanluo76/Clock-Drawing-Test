"""
The app module. Defines template parent class for all apps.
"""

from functools import reduce


class App():
    """
    The parent class for all apps. All apps should have a methods method
    decorated by @subscribe_app_methods, and add other app methods with
    decorator @methods.add_method.
    """
    def __call__(self, img):
        """
        Run the app.

        @param ClockFace / ElementImageMixin img: image to be processed
        @return True if passed
        """
        return reduce(lambda res, mtd: res and mtd(self, img),
                      [ True ] + self.methods)

