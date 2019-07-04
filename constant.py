import numpy as np
"""
Common colors triplets (BGR space) to use in OpenCV
"""
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
YELLOW = (0, 255, 255)
MAGENTA = (255, 0, 255)
CYAN = (255, 255, 0)
DARK_GRAY = (50, 50, 50)
RAND = np.random.randint(0, high=256, size=(3,)).tolist()
LIGHT_GRAY = (220, 220, 220)