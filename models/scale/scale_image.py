"""
The scale_image module. Defines the element image for scale-like elements.
"""

from __future__ import absolute_import

from models.element_image import ElementImage
from utils.metas.meta_singleton_mixin import MetaSingletonMixin
from models.model_mixins.scale_image_mixin import ScaleImageMixin
from models.scale.scale_element import ScaleElement


class ScaleImage(ElementImage,
                 metaclass=MetaSingletonMixin, mixins=(ScaleImageMixin, )):
    """
    The ScaleImage class.
    """
    # set the element class for mixin method
    _ELEMENT = ScaleElement

