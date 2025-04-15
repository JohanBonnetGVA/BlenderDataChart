"""
Base enum class for Blender constants.

This module provides the base enum implementation with description support.
"""

from enum import Enum


class DescriptiveEnum(Enum):
    """Base class for Blender enums with description support."""
    
    def __init__(self, value, description):
        self._value_ = value
        self.description = description


def print_enum_values(enum_class):
    """Helper function to print all values of an enum with descriptions."""
    print(f"\nAvailable {enum_class.__name__} values:")
    for item in enum_class:
        print(f"  {item.value}: {item.description}")