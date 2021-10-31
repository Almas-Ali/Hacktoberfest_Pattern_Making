import java.util.Scanner;

class BinaryPyramid{
public static void main(String args[]){
int i,j,k,count=1,num=1,space;
    Scanner scan=new Scanner(System.in);
System.out.print("Enter the number of rows: ");
int rows=scan.nextInt();
System.out.print("\nYour pattern here\n\n");
    space=rows-1;
  
    for(i=1; i<=rows; i++){ //parent for loop- outer for loop
        for(j=1; j<=space; j++){//fo display space
        System.out.print(" ");
    }
         for(k=1; k<=num; k++){
        System.out.print(count%2);
        count++;
    }
    space--;
    num+=2;
    System.out.print("\n");
      
    }
}
}
