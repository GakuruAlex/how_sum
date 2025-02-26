from typing import List, Dict
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

def how_sum_memo(target_sum: int, numbers: List[int], memo: Dict[int, List[int]] = {0: []}):
    if target_sum in memo:
        return memo[target_sum]
    if target_sum < 0:
        return None
    for number in numbers:
        remainder = target_sum - number

        result = how_sum_memo(remainder, numbers, memo)
        memo[remainder] = result
        if result != None:
            return [number] + result
    return None



def main() -> None:
    numbers: List[int] = [7, 14]
    target_sum: int = 300
    result = how_sum_memo(target_sum, numbers)
    print(f"Possible combination of number(s) in {numbers} that can achieve target sum of {target_sum} are: {result}")

if __name__ == "__main__":
    main()