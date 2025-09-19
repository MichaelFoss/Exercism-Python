def get_nums(max_num: int) -> set[int]:
    nums: set[int] = set()
    for i in range(2, max_num + 1):
        nums.add(i)
    return nums

def primes(limit):
    primes: list[int] = []
    if limit < 2:
        return primes

    unmarked_nums: set[int] = get_nums(limit)
    num: int = 1
    while True:
        num += 1
        if num in unmarked_nums:
            primes.append(num)
            num_to_mark: int = num
            while num_to_mark <= limit:
                if num_to_mark in unmarked_nums:
                    unmarked_nums.remove(num_to_mark)
                num_to_mark += num
            if len(unmarked_nums) == 0:
                return primes
