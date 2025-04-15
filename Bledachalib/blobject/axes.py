from typing import List, Tuple, Optional


class Axis:
    def __init__(
        self,
        position: Tuple[float, float, float] = (0, 0, 0),
        rotation: Tuple[float, float, float] = (0, 90, 0),
        length: Tuple[float, float, float] = (5, 5, 5),
    ):

        # position: (x, y, z) coordinates of the axis
        self.position: Tuple[float, float, float] = position
        # rotation: (x, y, z) rotation angles in degrees
        self.rotation: Tuple[float, float, float] = rotation
        # length: (x, y, z) length of the axis in blender value
        self.length: Tuple[float, float, float] = (length, length, length)

        self.axes: Tuple[AxisFormatOption, AxisFormatOption, AxisFormatOption]


class AxisFormatOption:
    def __init__(
        self,
        show_ticks: bool = True,
        tick_count: int = 5,
        tick_labels: Optional[List[str]] = None,
        axis_label: str = "",
        color: Tuple[float, float, float] = (0.8, 0.8, 0.8),
    ):
        self.show_ticks = show_ticks
        self.tick_count = tick_count
        self.tick_labels = tick_labels
        self.axis_label = axis_label
        self.color = color
