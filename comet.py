"""
Comet Animation Module
"""

from animation_base import AnimationBase


class Comet(AnimationBase):
    """Comet Animation Class"""

    def __init__(
        self,
        num_pixels,
        tail_length=5,
        color=(255, 255, 255),
    ):
        """Initialize the Comet animation.
        Args:
            num_pixels (int): The number of pixels in the animation.
            tail_length (int): Length of the comet's tail.
            color (tuple): RGB color of the comet. Specify the color at max brightness.
        """
        super().__init__(num_pixels)
        self.tail_length = tail_length
        self.color = color

        self.comet = bytearray(self.tail_length * 3)

        self.frame = bytearray(self.num_pixels * 3)
        self.tail_index = 0

    def reset(self):
        """Reset the animation to its initial state."""
        self.comet = bytearray(self.tail_length * 3)
        self.frame = bytearray(self.num_pixels * 3)
        self.tail_index = 0
        for i in range(self.tail_length):
            r, g, b = self.color
            # Linear scaling of brightness
            self.comet[i * 3] = min(r, 255 * (i + 1) // self.tail_length)
            self.comet[i * 3 + 1] = min(g, 255 * (i + 1) // self.tail_length)
            self.comet[i * 3 + 2] = min(b, 255 * (i + 1) // self.tail_length)

    def get_next(self):
        """Advance the animation to the next frame."""
        # Clear the current tail pixel
        for i in range(3):
            index = self.tail_index + i
            if index < len(self.frame):
                self.frame[index] = 0

        # Move the tail index forward
        self.tail_index += 3
        if self.tail_index == self.num_pixels * 3:
            self.tail_index = 0

        # Copy the comet into the new positions of the frame
        for i in range(self.tail_length * 3):
            index = self.tail_index + i
            if index < len(self.frame):
                self.frame[index] = self.comet[i]

        return self.frame
