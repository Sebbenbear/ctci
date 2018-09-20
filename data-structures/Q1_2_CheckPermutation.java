
import java.util.*;

class Q1_2_CheckPermutation {

    /*
     * O(n log n) run, O(n) space
     */
    private static boolean checkPermutation(String one, String two) {
        if (one.length() != two.length()) { // O(1) run, O(1) space
            return false;
        }

        String [] one_arr = one.split(""); // O(n) run, O(n) space
        String [] two_arr = two.split(""); // O(n), O(n) space

        Arrays.sort(one_arr); // O(n log n) run, O(1) space
        Arrays.sort(two_arr); // O(n log n) run, O(1) space

        for (int i = 0; i < one_arr.length; i++) { // O(n) run, O(1) space
            if (!one_arr[i].equals(two_arr[i])) { // O(n) run, O(1) space
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {

        if (checkPermutation("rar", "rar") != true) {
            throw new AssertionError("rar was not a permutation of rar");
        }

        if (checkPermutation("rraa", "rara") != true) {
            throw new AssertionError("rara was not a permutation of rraa");
        }

        if (checkPermutation("", "rara") != false) {
            throw new AssertionError("empty string was not a permutation of rara");
        }

        if (checkPermutation("", "") != true) {
            throw new AssertionError("empty string was not a permutation of empty string");
        }
    }
}
