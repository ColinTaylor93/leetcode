/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const romanMap = new Map();
    romanMap.set("M", 1000);
    romanMap.set("D", 500);
    romanMap.set("C", 100);
    romanMap.set("L", 50);
    romanMap.set("X", 10);
    romanMap.set("V", 5);
    romanMap.set("I", 1);
    let total = 0;

    for (let x=0;x<s.length;x++) {
        if (x == s.length - 1) {
            total += romanMap.get(s[x]);
        } else {
            if (romanMap.get(s[x]) < romanMap.get(s[x+1])) {
                total -= romanMap.get(s[x]);
            } else {
                total += romanMap.get(s[x]);
            }
        }
    }
    return total;
};