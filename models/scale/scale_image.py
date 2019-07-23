from __future__ import absolute_import

from utils.meta_singleton_mixin import MetaSingletonMixin
from models.element_image import ElementImage
from models.model_mixins.scale_image_mixin import ScaleImageMixin
from models.scale.scale_element import ScaleElement


class ScaleImage(ElementImage,
                 metaclass=MetaSingletonMixin, mixins=(ScaleImageMixin, )):
    # set the element class for mixin method
    _ELEMENT = ScaleElement

