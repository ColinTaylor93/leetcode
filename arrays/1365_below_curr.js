/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    let returnArray = [];

    // sort the nums array
    const sorted = [...nums].sort((a, b) => a - b);

    // find the index of each number in sorted, that is also how many are lower
    for (let i=0;i<nums.length;i++) {
        index = sorted.indexOf(nums[i]);
        returnArray.push(index);
        debugger;
    }

    return returnArray;
};