import java.util.Scanner;
class floydTriangle{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        //int n=in.nextInt();
        int n =5;
        int count=1;
        for(int i=1;i<=n;i++){
            for(int j=1;j<=i;j++){
           System.out.print(count);
           count++;
            }
            System.out.println();
        }
       
    }
}