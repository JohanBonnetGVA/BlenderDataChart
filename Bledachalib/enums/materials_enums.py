"""
Material-related enumerations for Blender.

This module contains enums for material types and world background types
used in Blender.
"""

from .base_enum import DescriptiveEnum


class MaterialType(DescriptiveEnum):
    """Material types."""
    SURFACE = ("SURFACE", "Standard surface material for solid objects")
    WIRE = ("WIRE", "Wireframe material that only renders the edges")
    VOLUME = ("VOLUME", "Volumetric material for smoke, fire, and other volume effects")
    HALO = ("HALO", "Halo material for particles and glowing effects")


class WorldType(DescriptiveEnum):
    """World background types."""
    PAPER_SKY = ("PAPER_SKY", "Simple paper-like backdrop with no horizon or gradient")
    BLEND_SKY = ("BLEND_SKY", "Gradient blend between horizon and zenith colors")
    REAL_SKY = ("REAL_SKY", "Simulated atmospheric sky with realistic lighting")


if __name__ == "__main__":
    # Example usage
    from .base_enum import print_enum_values
    
    print(f"Material type: {MaterialType.VOLUME.value}")
    print(f"Description: {MaterialType.VOLUME.description}")
    
    # Print all available material types with descriptions
    print_enum_values(MaterialType)
    print_enum_values(WorldType)