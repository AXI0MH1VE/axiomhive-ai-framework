"""
AxiomHive AI Strategic Framework - Core Package

This package contains the core intelligence, prediction, and automation
systems that power the AxiomHive strategic framework.

Copyright (c) 2025 AxiomHive. All rights reserved.
"""

__version__ = '1.0.0'
__author__ = 'AxiomHive'
__license__ = 'Proprietary'

from .intelligence import StrategicEngine
from .prediction import ForecastEngine
from .automation import DecisionAgent

__all__ = [
    'StrategicEngine',
    'ForecastEngine',
    'DecisionAgent',
]
