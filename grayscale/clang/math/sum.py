from typing import List

from grayscale.clang import dll


def sum(nums: List[float]) -> float:
    return dll.gs_sum(nums)
