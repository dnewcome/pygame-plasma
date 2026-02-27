"""
Base class for animations.
"""


class AnimationBase:
    """Base class for animations."""

    def __init__(self, num_pixels):
        """
        Initialize the animation base.
        Args:
            num_pixels (int): The number of pixels in the animation.
        """
        self.num_pixels = num_pixels
        self.current_frame = 0
        self.frame = bytearray(self.num_pixels * 3)  # RGB format

    def reset(self):
        """Reset the animation to its initial state."""
        self.current_frame = 0
        self.frame = bytearray(self.num_pixels * 3)  # new empty frame

    def get_next(self) -> bytearray:
        """Advance the animation to the next frame/state."""
        raise NotImplementedError("next() must be implemented by subclasses.")
