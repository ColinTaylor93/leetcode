/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    // edge cases for when target is higher or lower then array
    if (target <= nums[0]) {
        return 0
    }
    const arraylength = nums.length - 1
    if (target > nums[arraylength]) {
        return arraylength + 1
    }

    // use binary search to find the number and return the target
    let left = 0
    let right = arraylength

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] > target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }

    // return the search postion if not found
    return left
};