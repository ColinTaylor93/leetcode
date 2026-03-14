/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(numbers, windowSize) {
    const n = numbers.length;

    // Arrays to store max values from the left and right within each block
    const maxFromLeft = new Array(n);
    const maxFromRight = new Array(n);

    maxFromLeft[0] = numbers[0];
    maxFromRight[n - 1] = numbers[n - 1];

    // Preprocessing step: fill in maxFromLeft and maxFromRight arrays
    for (let i = 1; i < n; i++) {
        // From left to right: restart max every windowSize steps
        if (i % windowSize === 0) {
            maxFromLeft[i] = numbers[i]; // Start of a new block
        } else {
            maxFromLeft[i] = Math.max(maxFromLeft[i - 1], numbers[i]);
        }

        // From right to left: restart max every windowSize steps
        const j = n - 1 - i;
        if ((j + 1) % windowSize === 0) {
            maxFromRight[j] = numbers[j]; // Start of a new block (from right)
        } else {
            maxFromRight[j] = Math.max(maxFromRight[j + 1], numbers[j]);
        }
    }

    // Result array to store the maximums for each window
    const slidingMaxes = new Array(n - windowSize + 1);

    // Compute maximums for each sliding window
    for (let i = 0; i <= n - windowSize; i++) {
        slidingMaxes[i] = Math.max(maxFromRight[i], maxFromLeft[i + windowSize - 1]);
    }

    return slidingMaxes;
};