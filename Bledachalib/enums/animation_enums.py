"""
Animation-related enumerations for Blender.

This module contains enums for animation interpolation types
used in Blender.
"""

from .base_enum import DescriptiveEnum


class InterpolationType(DescriptiveEnum):
    """Interpolation types for animation."""
    CONSTANT = ("CONSTANT", "No interpolation, value jumps from one keyframe to next")
    LINEAR = ("LINEAR", "Straight line interpolation between keyframes")
    BEZIER = ("BEZIER", "Smooth curve interpolation with control handles")
    SINE = ("SINE", "Sinusoidal interpolation with gentle ease in/out")
    QUAD = ("QUAD", "Quadratic interpolation with stronger ease in/out than sine")
    CUBIC = ("CUBIC", "Cubic interpolation with even stronger ease in/out")
    QUART = ("QUART", "Quartic interpolation with very strong ease in/out")
    QUINT = ("QUINT", "Quintic interpolation with extremely strong ease in/out")
    EXPO = ("EXPO", "Exponential interpolation with dramatic ease in/out")
    CIRC = ("CIRC", "Circular interpolation with smooth arc-like motion")
    BACK = ("BACK", "Overshooting interpolation with slight backward motion")
    BOUNCE = ("BOUNCE", "Bouncing effect at the end of the interpolation")
    ELASTIC = ("ELASTIC", "Elastic/springy effect at the end of the interpolation")


if __name__ == "__main__":
    # Example usage
    from .base_enum import print_enum_values
    
    print(f"Interpolation type: {InterpolationType.BEZIER.value}")
    print(f"Description: {InterpolationType.BEZIER.description}")
    
    # Print all available interpolation types with descriptions
    print_enum_values(InterpolationType)