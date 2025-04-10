"""
Object-related enumerations for Blender.

This module contains enums for object types and selection modes
used in Blender.
"""

from .base_enum import DescriptiveEnum


class ObjectType(DescriptiveEnum):
    """Type of objects in Blender."""
    MESH = ("MESH", "Polygon mesh object composed of vertices, edges, and faces")
    CURVE = ("CURVE", "Curve object defined by control points and handles")
    SURFACE = ("SURFACE", "NURBS surface object")
    META = ("META", "Metaball object for organic blob-like shapes")
    FONT = ("FONT", "Text object that can be extruded and manipulated")
    ARMATURE = ("ARMATURE", "Skeletal structure for rigging and animation")
    LATTICE = ("LATTICE", "Lattice for non-destructive deformation")
    EMPTY = ("EMPTY", "Null object for parenting, constraints, and transforms")
    GPENCIL = ("GPENCIL", "Grease Pencil object for 2D animation in 3D space")
    CAMERA = ("CAMERA", "Camera object for scene rendering")
    LIGHT = ("LIGHT", "Light source object")
    SPEAKER = ("SPEAKER", "Speaker object for positional audio")
    LIGHT_PROBE = ("LIGHT_PROBE", "Light probe for environment reflection and lighting")


class SelectionMode(DescriptiveEnum):
    """Selection modes for mesh objects."""
    VERTEX = ("VERTEX", "Select individual vertices")
    EDGE = ("EDGE", "Select edges between vertices")
    FACE = ("FACE", "Select polygonal faces")


if __name__ == "__main__":
    # Example usage
    from .base_enum import print_enum_values
    
    print(f"Object type: {ObjectType.MESH.value}")
    print(f"Description: {ObjectType.MESH.description}")
    
    # Print all available object types with descriptions
    print_enum_values(ObjectType)
    print_enum_values(SelectionMode)