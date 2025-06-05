/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    /**
     * Helper function to get the sum of digits squared
     */
    const happyTotal = (num) => {
        const digits = num.toString().split('').map(Number);
        let total = 0;
        digits.forEach((digit) => {
            total += digit * digit;
        })
        return total;
    }

    // use a hash set to keep the previously found total, this will be used to find a loop
    const visit = new Set();
    // if we encountered the value before, we have to be in a loop and its false
    while (!visit.has(n)) {
        visit.add(n);
        n = happyTotal(n);
        if (n === 1) {
            return true;
        }
    }
    return false;
};