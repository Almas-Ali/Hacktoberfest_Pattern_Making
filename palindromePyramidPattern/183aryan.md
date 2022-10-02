# Palindromic pyramid pattern

- The palindromic number are the number whose reverse is equal to the original number. For example - 12321 is a original number whose reverse is same as the original number, that is 12321.


### Pattern Looks Like
- ![image](https://user-images.githubusercontent.com/76700307/193434225-a55aca9c-5e00-48b9-bd4c-e4b8d76bf16a.png)

### Working
- Step 1- Initialize the there variable for the loop

- Step 2- the first loop is for the the row, in how many row you want to print data.

- Step 3- the second loop is for the spaces, the space print in the row from i to row-1.

- Step 4- the third loop is for the the print element from i to row.

- Step 5- print j.

- Step 6. the forth loop is for print reverse number.

- Step 7- print j.

- Step 8. Stop.

### Code for pattern in JAVA :
```
import java.util.Scanner;

public class Main
{
    public static void main(String[] args) 
    {
        int i,j;
        //Scanner class declaration
        Scanner sc = new Scanner(System.in);
        //input from user
        System.out.print("Enter the row");
        int row = sc.nextInt();
        //declare for loop for every new row
        for(i=1;i<=row;i++)
        {
            //this lopp is for the space
            for(j=i;j<=row;j++)
                System.out.print(" ");
            //this loop is for print number 1 to i
            for(j=1;j<=i;j++)
                System.out.print(j+"");
            //this loop is for the number in reverse order
            for(j=i-1;j>=1;j--)
                System.out.print(j+"");
            System.out.println();
         }
    }
}
```

### Output :
- ![image](https://user-images.githubusercontent.com/76700307/193434060-bc2633cf-91aa-4d20-92a9-4a2a910d5e5b.png)

- That's all from my side. Thanks for reading.
