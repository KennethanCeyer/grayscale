from typing import List

from grayscale.math import mean


def var(nums: List[float]) -> float:
    mean_ = mean(nums)
    vsum = 0
    for n in nums:
        vsum += (n - mean_) ** 2
    return vsum / len(nums)
