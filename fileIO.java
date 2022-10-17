package userinput;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
public class fileIO {

   public static void main(String args[]) throws IOException {  
      FileInputStream in = null;
      FileOutputStream out = null;
      try {
         out = new FileOutputStream("input.txt");
         in = new FileInputStream("File.txt");
         List<Integer> list = new ArrayList<Integer>();
         int c;
         while ((c = in.read()) != -1) {
            System.out.println((int) c);
            list.add(c);
         }
      } catch(Exception o) {
    	  o.printStackTrace();
      }finally {
         if (in != null) {
            in.close();
         }
         if (out != null) {
            out.close();
         }
      }
   }
}