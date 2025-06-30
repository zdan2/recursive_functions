# 009.py
from typing import Sequence, Any, Optional

def binary_search(arr: Sequence[Any], target: Any,
                  left: int = 0, right: Optional[int] = None) -> int:
    """再帰版二分探索。見つからなければ -1 を返す"""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)

if __name__=='__main__':
    print(binary_search([1,2,3,4,5,6],5))