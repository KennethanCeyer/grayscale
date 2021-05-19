from typing import List

from grayscale.clang import dll


def max(nums: List[float]) -> float:
    return dll.gs_max(nums)
