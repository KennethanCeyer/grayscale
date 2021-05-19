from typing import List

from grayscale.clang import dll


def var(nums: List[float]) -> float:
    return dll.gs_var(nums)
