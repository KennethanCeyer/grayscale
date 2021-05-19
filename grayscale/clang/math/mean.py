from typing import List

from grayscale.clang import dll


def mean(nums: List[float]) -> float:
    return dll.gs_mean(nums)
