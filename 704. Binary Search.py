def search(nums, target: int) -> int:
    left = 0
    right = len(nums) - 1
    mid = -1

    while left <= right:
        # We get the average to found the mid and split the array in 2
        mid = (left + right) //2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        # Mid == Target, we found it
        else:
            return mid
    return -1

def main():
    search([-1,0,3,5,9,12], 2)

main()