from typing import List
def how_sum(target_sum: int, numbers: int) -> List[int]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for number in numbers:
        remainder = target_sum - number
        result = how_sum(remainder, numbers)
        if result != None:
            return result + [number]
        how_sum(remainder ,numbers)



def main() -> None:
    numbers: List[int] = [3, 5, 7]
    target_sum: int = 11
    result = how_sum(target_sum, numbers)
    print(f"Numbers in {numbers} that can achieve target sum of {target_sum} are: {result}")

if __name__ == "__main__":
    main()