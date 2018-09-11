import java.util.*;

public class IsUnique {

    /**
     * Returns whether a string has all unique characters, 
     * Complexity: O(n log n + n) time, O(1) space
     * @param words The array of words to be checked
     * @return true if the array contains unique words, otherwise false
     */
    private static boolean uniqueChars(String[] words) {
        if (words.length > 2) {
            Arrays.sort(words);
            for (int i = 0; i < words.length - 1; i++) {
                //System.out.println(words[i] + " " + words[i+1] + " : " + words[i].equals(words[i+1]));
                if (words[i].equals(words[i+1])) {
                    return false;
                }
            }
        }
        return true;
    }

    /**
     * Returns whether a string has all unique characters, 
     * Complexity: O(2n) time, O(n) space
     * @param words The array of words to be checked
     * @return true if the array contains unique words, otherwise false
     */
    private static boolean uniqueChars2(String[] words) {
        Set<String> wordSet = new HashSet<>(Arrays.asList(words));
        return wordSet.size() == words.length;
    }

    public static void main(String [] args) {
        String[] words = {"exciting", "what", "an", "exciting", "exciting"};
        System.out.println(String.format("Array contains unique words: %b", uniqueChars(words)));

        String[] words2 = {"what", "an", "exciting"};
        System.out.println(String.format("Array contains unique words: %b", uniqueChars(words2)));

        String[] words3 = {"what"};
        System.out.println(String.format("Array contains unique words: %b", uniqueChars(words3)));

        String[] words4 = {"exciting", "what", "an", "exciting", "exciting"};
        System.out.println(String.format("Array contains unique words: %b", uniqueChars2(words)));

        String[] words5 = {"what", "an", "exciting"};
        System.out.println(String.format("Array contains unique words: %b", uniqueChars2(words2)));

        String[] words6 = {"what"};
        System.out.println(String.format("Array contains unique words: %b", uniqueChars2(words3)));
    }
}