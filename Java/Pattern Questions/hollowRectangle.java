import java.util.Scanner;
class hollowRectangle{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        //int row = in.nextInt();
        //int col=in.nextInt();
        int row=5;
        int col=5;
        for(int i=1;i<=row;i++){
            for(int j=1;j<=col;j++){
                if(i==1 || i==row){
                     System.out.print("*");
                }
                else if(j==1 || j==col){
                    System.out.print("*");
                }
                else{
                    System.out.print(" ");
                }
          
            }
            System.out.println();
        }
       
    }
}