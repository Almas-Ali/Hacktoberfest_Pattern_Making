public class Palindrome_Check {
    static  boolean isPalindrome(String s, int start, int end){
        if(start>=end){
            return true;
        }
        return ((s.charAt(start)==s.charAt(end)) && isPalindrome(s,start+1, end-1));

    }
    public static void main(String[] args) {
        String s="racecar";
        int start=0, end= s.length()-1;
        System.out.println("is racecar palindrome => "+ isPalindrome(s, start, end)); //Returns true 

        String s1="hacktoberFest";
        int start_s1=0, end_s1=s1.length()-1;
        System.out.println("is hacktoberFest a palindrome => "+ isPalindrome(s1, start_s1, end_s1));
    }
}
