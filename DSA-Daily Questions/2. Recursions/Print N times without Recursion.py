from typing import *

ans = []


def printNtimes(n: int) -> List[str]:
    if n < 1:
        return ans
    ans.append("Coding Ninjas")
    return printNtimes(n - 1)
