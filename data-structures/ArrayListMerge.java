import java.util.*;

public class ArrayListMerge {

    private static ArrayList<String> merge(String[] words, String[] more) {
        ArrayList<String> sentence = new ArrayList<>();
        for (String word : words) {
            sentence.add(word);
        }
        for (String word : more) {
            sentence.add(word);
        }
        return sentence;
    }

    public static void main(String [] args) {
        String[] first = {"what", "an", "exciting"};
        String[] second = {"time", "to", "be", "alive!"};
        
        ArrayList<String> mergedArray = merge(first, second);
        System.out.println(String.join(" ", mergedArray));
    }
}
