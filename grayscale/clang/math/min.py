from typing import List

from grayscale.clang import dll


def min(nums: List[float]) -> float:
    return dll.gs_min(nums)
