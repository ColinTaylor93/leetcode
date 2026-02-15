function maxDifference(s: string): number {
    // Create a frequency map to store the count of each character in the input string.
    const characterFrequencyMap = s.split('').reduce(
        (accumulatorMap, character) => {
            // Increment the count for the current character. If the character is not yet in the map, initialize its count to 0.
            return accumulatorMap.set(character, (accumulatorMap.get(character) || 0) + 1);
        },
        new Map<string, number>()
    );

    // Determine the maximum frequency among characters with odd frequencies
    // and the minimum frequency among characters with even frequencies.
    const [maxOddFrequency, minEvenFrequency] = Array.from(characterFrequencyMap.values()).reduce(
        (accumulator, frequency) => {
            const currentMaxOddFrequency = accumulator[0];
            const currentMinEvenFrequency = accumulator[1];

            // If the current frequency is odd, update maxOddFrequency if it's greater.
            const newMaxOddFrequency = frequency % 2
                ? Math.max(frequency, currentMaxOddFrequency)
                : currentMaxOddFrequency;

            // If the current frequency is even, update minEvenFrequency if it's smaller.
            // We use Infinity as an initial value so any even frequency will be smaller.
            const newMinEvenFrequency = frequency % 2 === 0
                ? Math.min(frequency, currentMinEvenFrequency)
                : currentMinEvenFrequency;

            return [newMaxOddFrequency, newMinEvenFrequency];
        },
        [0, Infinity] // Initialize maxOddFrequency to 0 and minEvenFrequency to Infinity.
    );

    // The result is the difference between the maximum odd frequency and the minimum even frequency.
    return maxOddFrequency - minEvenFrequency;
};