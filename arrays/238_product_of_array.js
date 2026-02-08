/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    // init vars
    let prefix = [];
    let postfix = [];
    let preMultiplyer = 1;
    let postMultiplyer = 1;
    let returnArr = [];

    // fill the prefix array
    for (let i=0;i<nums.length;i++) {
        // get the inverted index
        let j = nums.length - 1 - i;

        // add the prefix value
        prefix[i] = preMultiplyer;
        preMultiplyer *= nums[i];

        // add the postfix value
        postfix[j] = postMultiplyer;
        postMultiplyer *= nums[j];
    }

    // multiply the 2 at each position
    for (let i=0;i<nums.length;i++) {
        returnArr[i] = postfix[i] * prefix[i];
    }

    return returnArr
};