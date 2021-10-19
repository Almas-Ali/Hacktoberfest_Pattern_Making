public class QuickSort{

    public static int[] quickSort(int arr[], int start, int end)
{
      int pi=partition(arr, start, end);
       if(start<pi-1)
       {
             quickSort(arr,start,pi-1);
       }
       if(pi<end)
       {
             quickSort(arr,pi,end); 
       }

      return arr;      
}
public static int partition(int[]arr, int start, int end)
{
      int pivote=arr[(start+end)/2];
      while(start<=end)
      {
            while(arr[start]<pivote)
            {
                  start++;
            }
            while(arr[end]>pivote){
                  end--;
            }
            if(start<=end)
            {
                  int temp = arr[start];
                  arr[start]=arr[end];
                  arr[end] = temp;
                  start++;
                  end--;
            }
      }
      return start;
}
}