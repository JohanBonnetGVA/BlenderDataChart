"""
Render-related enumerations for Blender.

This module contains enums for render engines, file formats, and other
rendering-related constants used in Blender.
"""

from .base_enum import DescriptiveEnum


class RenderEngine(DescriptiveEnum):
    """Render engines available in Blender."""
    CYCLES = ("CYCLES", "Path tracing renderer with advanced features")
    BLENDER_EEVEE = ("BLENDER_EEVEE", "Real-time PBR renderer with good visual quality and fast performance")
    BLENDER_WORKBENCH = ("BLENDER_WORKBENCH", "Fast renderer for preview and modeling work")


class FileFormat(DescriptiveEnum):
    """File formats for rendering and export."""
    BMP = ("BMP", "Windows Bitmap - uncompressed image format")
    IRIS = ("IRIS", "Silicon Graphics IRIS format")
    PNG = ("PNG", "Portable Network Graphics - lossless compression with alpha")
    JPEG = ("JPEG", "Joint Photographic Experts Group - lossy compression format")
    JPEG2000 = ("JPEG2000", "JPEG 2000 format - improved compression algorithm")
    TARGA = ("TARGA", "Truevision TGA - supports alpha and compression")
    TARGA_RAW = ("TARGA_RAW", "Truevision TGA - uncompressed variant")
    CINEON = ("CINEON", "Kodak Cineon format - used in film industry")
    DPX = ("DPX", "Digital Picture Exchange - commonly used in film production")
    OPEN_EXR = ("OPEN_EXR", "OpenEXR HDR format - high dynamic range with compression")
    OPEN_EXR_MULTILAYER = ("OPEN_EXR_MULTILAYER", "OpenEXR with multiple layers/passes")
    HDR = ("HDR", "High Dynamic Range - Radiance RGBE format")
    TIFF = ("TIFF", "Tagged Image File Format - flexible format with various compression options")
    FFMPEG = ("FFMPEG", "Video format encoding using the FFMPEG library")


if __name__ == "__main__":
    # Example usage
    from .base_enum import print_enum_values
    
    print(f"Using {RenderEngine.CYCLES.value} engine")
    print(f"Engine description: {RenderEngine.CYCLES.description}")
    
    # Print all available render engines with descriptions
    print_enum_values(RenderEngine)
    print_enum_values(FileFormat)