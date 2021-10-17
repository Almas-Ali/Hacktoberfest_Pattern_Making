import java.util.Scanner;
public class DownArrowPattern {
    public static void main(String[] args) {
        System.out.println("Enter Number ");
        Scanner scan=new Scanner(System.in);
        int num=scan.nextInt();
        int t=num+1;
        int i=0;
        scan.close();
       if(num>=2 && num<=20){
       for(int r=0;r<(num*num);r++){
        //Square
                if(r<num-1){
                      System.out.print("  ");
                for(int sqc=0;sqc<(num-1);sqc++){
                  
                    System.out.print("* ");
                    
                }
                System.out.println("");
                }
        //head  
                if(r>=num-1){
                for(int j=0;j<i;j++){
                    System.out.print(" ");
                }
                for(int tr=t;tr>0;tr--){
                    System.out.print("*");
                    System.out.print(" ");
                }
                System.out.println("");
                t--;
                i++;
                }
       }
           
   
    }
}
}
// IF Number : 5

//  * * * * 
//  * * * * 
//  * * * * 
//  * * * * 
//* * * * * * 
// * * * * * 
//  * * * * 
//   * * * 
//    * * 
//     * 
