from typing import List

from grayscale.math.sqrt import sqrt
from grayscale.math.var import var


def std(nums: List[float]) -> float:
    return sqrt(var(nums))
