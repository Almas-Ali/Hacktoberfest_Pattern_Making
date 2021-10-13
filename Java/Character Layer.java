import java.util.*;
class Character_Layer
{
    public static void main(String args[])
    {
        Scanner I=new Scanner (System.in);
        int i,j,l,r=0,d,k;
        String s;
        System.out.println("ENTER A STRING");
        s=I.nextLine();
        l = s.length();
        d = 2*l - 1;
        String a[][]= new String[d][d];
        for(i=l-1;i>=0;i--)
        {
            for(j=r;j<d-r;j++)
            {
                for(k=r;k<d-r;k++)
                {
                    if(j==r||j==d-r-1||k==r||k==d-r-1)
                    {
                        a[j][k]=s.substring(i,l-r);
                    }
                }
            }
            r++;
        }
        for(j=0;j<d;j++)
            {
                for(k=0;k<d;k++)
                {
                    System.out.print(a[j][k]+ " ");
                }
                System.out.println();
            }
        }
    }
