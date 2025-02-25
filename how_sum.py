from typing import List
def how_sum(target_sum: int, numbers: int, current = []) -> List[int]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for number in numbers:
        pass

def main() -> None:
    numbers: List[int] = [5, 3, 4, 7]
    target_sum: int = 7
    print(f"Numbers that can achieve target sum of {target_sum} are: {how_sum(target_sum, numbers)}")

if __name__ == "__main__":
    main()