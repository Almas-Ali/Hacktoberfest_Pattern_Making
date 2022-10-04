using System;

class Program
{
    public static void Main()
    {
        Console.Write("Enter width: ");
        int n;

        try
        {
            n = Convert.ToInt32(Console.ReadLine());
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input.");
            return;
        }
        
        int space = n - 1;

        for (int i = 0; i < n; i++)
        {

            for (int j = 0; j < space; j++)
                Console.Write(" ");

            for (int j = 0; j <= i; j++)
                Console.Write("* ");

            Console.Write("\n");
            space--;
        }

        space = 0;

        for (int i = n; i > 0; i--)
        {
            for (int j = 0; j < space; j++)
                Console.Write(" ");

            for (int j = 0; j < i; j++)
                Console.Write("* ");

            Console.Write("\n");
            space++;
        }
    }
}