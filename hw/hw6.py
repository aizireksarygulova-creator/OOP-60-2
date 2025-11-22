from typing import List, Tuple

def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return (seen[need], i)
        seen[num] = i
    raise ValueError("Нет решения")

if __name__ == "__main__":
    examples = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]

    for nums, target in examples:
        i, j = two_sum(nums, target)
        print(f"nums = {nums}, target = {target} -> indices: {i}, {j}")
