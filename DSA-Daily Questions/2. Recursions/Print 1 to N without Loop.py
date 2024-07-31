from typing import List


def printNos(x: int) -> List[int]:
    if x == 0:
        return []
    return printNos(x - 1) + [x]
