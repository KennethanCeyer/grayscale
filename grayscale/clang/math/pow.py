from grayscale.clang import dll


def pow(x: float, y: float) -> float:
    return dll.gs_pow(x, y)
