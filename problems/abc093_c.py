def main():
    nums = list(map(int, input().split()))

    M = max(nums)
    diff = 3 * M - sum(nums)

    print((diff) // 2) if diff%2 == 0 else print((3*M+3-sum(nums))//2)

# def main():
#     nums = list(map(int, input().split()))

#     res = 0

#     while len(set(nums)) != 1:
#         maxIdx = nums.index(max(nums))
#         minIdx = nums.index(min(nums))

#         if nums[maxIdx] - nums[minIdx] >= 2:
#             nums[minIdx] += 2
#             res += 1
#         else:
#             nums[minIdx] += 1
#             nums[nums.index(min(nums))] += 1

#             res += 1
    
#     print(res)

if __name__ == '__main__':
    main()