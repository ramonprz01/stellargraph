"""
Stellar Machine Learning Library

"""

__all__ = [
    "data",
    "layer",
    "mapper",
    "utils",
    "StellarDiGraph",
    "StellarGraph",
    "__version__",
]

# Version
from .version import __version__

# Import modules
from stellargraph import mapper, layer, utils

# Top-level imports
from stellargraph.core.graph import StellarGraph, StellarDiGraph
from stellargraph.core.schema import GraphSchema
from stellargraph.utils.calibration import TemperatureCalibration, IsotonicCalibration
from stellargraph.utils.calibration import (
    plot_reliability_diagram,
    expected_calibration_error,
)
from stellargraph.utils.ensemble import Ensemble

# Custom layers for keras deserialization:
custom_keras_layers = {
    "GraphConvolution": layer.GraphConvolution,
    "GraphAttention": layer.GraphAttention,
    "GraphAttentionSparse": layer.GraphAttentionSparse,
    "SqueezedSparseConversion": layer.SqueezedSparseConversion,
}