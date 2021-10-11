import java.util.Scanner;
public class palindrome
{
    public static void main(String args[])
    {
        String x, y = "";
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the string you want to check:");
        x = scan.nextLine();
        int len = x.length();
       for(int t = len - 1; t >= 0; t--)
     {
          y = y + x.charAt(t);
      }
      if(x.equalsIgnoreCase(y))
        {
            System.out.println("The string is a palindrome.");
        }
        else
        {
            System.out.println("The string is not a palindrome.");
        }
        scan.close();
    }
}
