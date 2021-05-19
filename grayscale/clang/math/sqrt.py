from grayscale.clang import dll


def sqrt(x: float) -> float:
    return dll.gs_sqrt(x)
