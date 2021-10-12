public class SumandProduct
{
 public static void main(final String[] args)
 {
  int sum = 0;
  int prod = 1;
  int[] arg = {1,2,3,4,5};
  for (int i : arg){
   sum += i;
   prod *=i;
  }
  System.out.printf("Your sum of arrayvalues is: %d \n and product of arrayvalues: %d ",sum,prod);

 }
}
