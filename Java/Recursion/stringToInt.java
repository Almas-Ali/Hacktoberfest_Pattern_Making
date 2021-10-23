public class Main
{
    static int stringToInt(String str)
    {
        if(str.length()<=0) return 0;
    
        int sum=Integer.parseInt(str.substring(0,1));
        sum=sum*(int)Math.pow(10,str.length()-1)+stringToInt(str.substring(1));
        return sum;
        
    }
	public static void main(String[] args) {
        String str = "1235";
        System.out.print(stringToInt(str));	
  }
}
