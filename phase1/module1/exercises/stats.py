def stats(nums: list[int]) -> list[dict]:
    return [
        {
            "min": min(nums),
            "max": max(nums),
            "mean": sum(nums) / len(nums),
            "median": sorted(nums)[len(nums) // 2],
        }
    ]


nums = list(map(int, input("Numbers = ").split(" ")))

res = stats(nums)
print(res)
