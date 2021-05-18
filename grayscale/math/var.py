from grayscale.math import mean


def var(nums):
    mean_ = mean(nums)
    vsum = 0
    for n in nums:
        vsum += (n - mean_) ** 2
    return vsum / len(nums)
