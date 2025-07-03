function kthCharacter(k: number): string {
    let currentWord = "a";

    // Expand the word until it reaches at least k characters
    while (currentWord.length < k) {
        let nextCharacters = "";

        for (let i = 0; i < currentWord.length; i++) {
            const currentChar = currentWord[i];

            // Compute the next character in the alphabet (wrapping from 'z' to 'a')
            const nextCharCode = ((currentChar.charCodeAt(0) - 97 + 1) % 26) + 97;
            nextCharacters += String.fromCharCode(nextCharCode);
        }

        currentWord += nextCharacters;
    }

    return currentWord[k - 1];
};