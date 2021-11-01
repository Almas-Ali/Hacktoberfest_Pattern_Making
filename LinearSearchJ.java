public class LinearSearch
{    
  public static int linearSearch(int[] arr, int key)
  {    
      for(int i=0;i<arr.length;i++)
      {    
          if(arr[i] == key)
          {    
              return i;    
          }    
      }    
      return -1;    
  }    
  public static void main(String a[])
  {    
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter the size:");
    int n=sc.nextInt();
    System.out.println("Enter the elements of the array:");
    int a[]=new int[n];
    for(int i=0;i<n;i++)
    {
      a[i]=sc.nextInt();
    }
    System.out.println("Enter the element to be searched:");
    int key=sc.nextInt();
    int ans=linearSearch(a1, key);
    if(ans==-1)
    {
      System.out.println(key+" is not found");
    }
    else
    {
      System.out.println(key+" is found at index: "+ans);
    }
  }
}    
