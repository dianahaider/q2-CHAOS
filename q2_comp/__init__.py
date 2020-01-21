from . import _alpha
from . import _denoise
from . import _taxonomy

from ._alpha import (alpha_frequency, alpha_diversity)
from ._denoise import (denoise_stats)
from ._taxonomy import (taxo_variability)


__all__ = ['alpha_frequency', 'alpha_diversity', 'denoise_stats', 'taxo_variability']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
