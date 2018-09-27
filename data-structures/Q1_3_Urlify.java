
import java.util.*;

/* 
 * URLify: Write a method to replace all spaces in a string with '%20: You may assume that 
 * the string has sufficient space at the end to hold the additional characters, and that 
 * you are given the "true" length of the string. (Note: If implementing in Java, please 
 * use a character array so that you can perform this operation in place.)
 */
public class Q1_3_Urlify {

    /*
     * Urls replace spaces with %20.
     * Since we know there's extra spaces at the back, we should just start from the back of the string and move everything.
     * When we get to a space, we shuffle and make room.
     */
    private static void urlify(char[] charArray, int trueLength) {
        int spaceCount = 0;
        int index = 0;
        int i = 0;

        for (i = 0; i < trueLength; i++) {
            if (charArray[i] == ' ') {
                spaceCount++;
            }
        }

        index = trueLength + spaceCount * 2; // adjust for the actual number of spaces
        if (trueLength < charArray.length) {
            charArray[trueLength] = '\0'; // so we don't get into a loop, we need a termination character
        }

        for (i = trueLength - 1; i >= 0; i--) {
            if (charArray[i] == ' ') {
                charArray[index - 1] = '0';
                charArray[index - 2] = '2';
                charArray[index - 3] = '%';
                index = index - 3;
            } else {
                // move things backwards: no need to swap them since moving from the back where there's space
                charArray[index - 1] = charArray[i];
                index--;
            }
        }
    }

    public static void main(String[] args) {
        char[] string =   {'m', 'r', ' ', 'j', 'o', 'h', 'n', ' ', 's', 'm', 'i', 't', 'h', ' ', ' ', ' ', ' '};
        char[] expected = {'m', 'r', '%', '2', '0', 'j', 'o', 'h', 'n', '%', '2', '0', 's','m', 'i', 't', 'h', '\0'};

        urlify(string, 13);

        for (char character : string) {
            System.out.print(character);
        }
        System.out.println();

        for (char character : expected) {
            System.out.print(character);
        }
        System.out.println();

        if (!string.equals(expected)) {
            throw new AssertionError("Spaces were not correctly set to %20");
        }
    }
}
