from typing import List

from grayscale.clang import dll


def std(nums: List[float]) -> float:
    return dll.gs_std(nums)
