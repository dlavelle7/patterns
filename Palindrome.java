
public class Palindrome {

	public static boolean isPalindrome(String word){
		word = word.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
		for (int i = word.length() -1, count = 0; i > count; i--, count++){
			if (word.charAt(count) != word.charAt(i))
				return false;
		}
		return true;
	}

}
