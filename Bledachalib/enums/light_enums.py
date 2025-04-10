"""
Light-related enumerations for Blender.

This module contains enums for light types used in Blender.
"""

from .base_enum import DescriptiveEnum


class LightType(DescriptiveEnum):
    """Types of lights in Blender."""
    POINT = ("POINT", "Omnidirectional light source that emits from a single point")
    SUN = ("SUN", "Directional light with parallel rays, simulating distant light source like the sun")
    SPOT = ("SPOT", "Conical light with directionality and falloff")
    AREA = ("AREA", "Light emitted from a surface, creating soft shadows")


if __name__ == "__main__":
    # Example usage
    from .base_enum import print_enum_values
    
    print(f"Light type: {LightType.SPOT.value}")
    print(f"Description: {LightType.SPOT.description}")
    
    # Print all available light types with descriptions
    print_enum_values(LightType)