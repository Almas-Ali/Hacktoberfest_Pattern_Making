import java.util.*;

public class patterns {
    public static void main(String argc[]) {

        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        for (int i = 1; i <=a; i++) {
            for (int j = 1; j <=2*a; j++) {
                if(j==1||j==2*a||i==j||i+j==2*a+1){
                    System.out.print("* ");
                }
                else{
                    System.out.print("  ");
                }
            }
                 System.out.println("");
          }
          for (int i = 1; i <=a; i++) {
            for (int j = 1; j <=2*a; j++) {
                if(j==1||j==2*a||i+j==a+1||j-i==a){
                    System.out.print("* ");
                }
                else{
                    System.out.print("  ");
                }
            }
                 System.out.println("");
          }

    }
}
