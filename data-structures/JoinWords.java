public class JoinWords {

    // GOOD - O(n)
    private static String goodJoinWords(String[] words) {
        StringBuilder sentence = new StringBuilder();
        for (String word : words) {
            sentence.append(word);
            sentence.append(" ");
        }
        return sentence.toString().trim();
    }

    // BAD - O(n^2) due to moving copying an increasing number of characters to a new array
    // BUT! The compiler optimises this later, so it might be fine.
    private static String badJoinWords(String[] words) {
        String sentence = "";
        for (String word : words) {
            sentence += word + " ";
        }
        return sentence.trim();
    }

    public static void main(String [] args) {
        String[] words = {"what", "an", "exciting", "time", "to", "be", "alive!"};
        
        String goodJoinedWords = goodJoinWords(words);
        System.out.println(goodJoinedWords);

        String badJoinedWords = badJoinWords(words);
        System.out.println(badJoinedWords);
    }
}