function maxAdjacentDistance(nums: number[]): number {
    // edge case for 2 numbers

    // get the overlapping diffrence
    let max_diff: number = Math.abs(nums[nums.length - 1] - nums[0]);

    // brute force through each number in the array checking the difference and if its the new max
    for (let i=1;i<nums.length;i++) {
        if (Math.abs(nums[i] - nums[i - 1]) > max_diff) {
            max_diff = Math.abs(nums[i] - nums[i - 1])
        }
    }

    return max_diff
};