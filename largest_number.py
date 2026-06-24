def largest_number(nums):
    if len(nums) == 1:
        return nums[0];

    if nums[0] > nums[len(nums) - 1]:
        nums.pop(len(nums) - 1);
        return largest_number(nums);
    else:
        nums.pop(0);
        return largest_number(nums);

print(largest_number([3,1,6,8,2,4,5]));