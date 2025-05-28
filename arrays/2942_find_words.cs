public class Solution {
    public IList<int> FindWordsContaining(string[] words, char x) {
        // Create an array for indexes to go
        List<int> indexList = new List<int>();
        
        // loop through each word and add if it has the letter in it
        for (int i=0;i<words.Length;i++) {
            if (words[i].Contains(x)) {
                indexList.Add(i);
            }
        }

        return indexList;
    }
}