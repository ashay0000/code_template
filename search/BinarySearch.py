def search(nums: list, target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left != right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
            continue
        if nums[mid] > target:
            right = mid  # 由于使用了整数除法,mid会向下取整,所以此处不能令right=mid-1,否则在right-left=1时会出错
            continue
    if nums[left] == target:
        return left
    return -1


if __name__ == "__main__":
    print(search([-1, 0, 3, 5, 9, 12], 9))  # 4
    print(search([-1, 0, 3, 5, 9, 12], 2))  # -1
