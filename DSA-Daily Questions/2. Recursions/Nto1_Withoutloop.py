from typing import List

# def printNos(x: int) -> List[int]:
#     ans = []
#     if x < 1:
#         return ans
#     ans.append(x)
#     ans=ans + printNos(x - 1)  # Concatenate the result of the recursive call
#     return ans


def printNos(x: int) -> List[int]:
    if x < 1:
        return []
    return [x] + printNos(x - 1)
