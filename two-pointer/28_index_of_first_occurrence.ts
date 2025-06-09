function strStr(haystack: string, needle: string): number {
    // get the length of the needle
    const needleLength: number = needle.length;

    // if the needle is nothing then it appears immediately
    if (needleLength === 0) return 0;

    // go through each char in the haystack
    for (let i:number = 0; i <= haystack.length - needleLength; i++) {
        // if the letter matches the first letter in the needle, check if it's the needle
        if (haystack[i] === needle[0]) {
            if (haystack.slice(i, i + needleLength) === needle) {
                return i;
            }
        }
    }

    // if we got here the needle wasn't found
    return -1;
};