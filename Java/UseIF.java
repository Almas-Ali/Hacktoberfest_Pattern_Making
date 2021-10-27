import java.util.Scanner;
public class UseIF
{
    public UseIF()
    {
        Scanner input=new Scanner(System.in);
        int age=0;
        System.out.println("Enter your age please: ");
        age=input.nextInt();
        if (age>=18)
        {
            System.out.println("You are eligible to vote!");
        }
        else
        {
            System.out.println("Not eligible to vote");
        }
    }
}
       