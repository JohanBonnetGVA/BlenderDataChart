"""
View-related enumerations for Blender.

This module contains enums for 3D viewport modes, space types, 
shading modes, and coordinate systems used in Blender.
"""

from .base_enum import DescriptiveEnum


class ViewType(DescriptiveEnum):
    """View types for 3D viewport."""
    PERSP = ("PERSP", "Perspective view with depth perception")
    ORTHO = ("ORTHO", "Orthographic view without perspective distortion")
    CAMERA = ("CAMERA", "View through the active camera")


class Space(DescriptiveEnum):
    """Blender space types."""
    VIEW_3D = ("VIEW_3D", "3D Viewport for manipulating objects in 3D space")
    IMAGE_EDITOR = ("IMAGE_EDITOR", "Editor for UV mapping and texture painting")
    NODE_EDITOR = ("NODE_EDITOR", "Editor for creating node-based materials, compositing, and textures")
    SEQUENCE_EDITOR = ("SEQUENCE_EDITOR", "Video Sequence Editor for editing video")
    CLIP_EDITOR = ("CLIP_EDITOR", "Movie Clip Editor for motion tracking")
    DOPESHEET_EDITOR = ("DOPESHEET_EDITOR", "Dope Sheet for keyframe animation overview")
    GRAPH_EDITOR = ("GRAPH_EDITOR", "Graph Editor for editing animation curves")
    NLA_EDITOR = ("NLA_EDITOR", "Nonlinear Animation Editor for animation clips and blending")
    TEXT_EDITOR = ("TEXT_EDITOR", "Text Editor for creating and editing Python scripts")
    CONSOLE = ("CONSOLE", "Python Console for interactive Python commands")
    INFO = ("INFO", "Info panel showing logs and operations")
    OUTLINER = ("OUTLINER", "Outliner showing scene hierarchy and collections")
    PROPERTIES = ("PROPERTIES", "Properties panel for editing object and scene parameters")
    FILE_BROWSER = ("FILE_BROWSER", "File Browser for loading and saving files")
    PREFERENCES = ("PREFERENCES", "User Preferences editor")


class ShadeMode(DescriptiveEnum):
    """Shading modes for 3D viewport."""
    WIREFRAME = ("WIREFRAME", "Display the object as wireframe showing only edges")
    SOLID = ("SOLID", "Display objects with basic lighting and material colors")
    MATERIAL = ("MATERIAL", "Display objects with material preview mode")
    RENDERED = ("RENDERED", "Display objects with full rendering and lighting")


class CoordinateSystem(DescriptiveEnum):
    """Coordinate systems."""
    GLOBAL = ("GLOBAL", "World space coordinates independent of object orientation")
    LOCAL = ("LOCAL", "Object space coordinates relative to the object's orientation")
    NORMAL = ("NORMAL", "Coordinate system aligned with the selected element's normal")
    GIMBAL = ("GIMBAL", "Gimbal coordinate system for dealing with gimbal lock")
    VIEW = ("VIEW", "Coordinates relative to the current view orientation")
    CURSOR = ("CURSOR", "Coordinates relative to the 3D cursor position and orientation")


if __name__ == "__main__":
    # Example usage
    from .base_enum import print_enum_values
    
    print(f"View mode: {ViewType.ORTHO.value}")
    print(f"View description: {ViewType.ORTHO.description}")
    
    # Print all available view types with descriptions
    print_enum_values(ViewType)
    print_enum_values(ShadeMode)