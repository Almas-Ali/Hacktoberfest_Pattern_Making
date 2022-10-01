import java.util.Scanner;
public class AlphabeticSquarePattern {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in=new Scanner(System.in);
		int num=in.nextInt();
		int i,j,k;
		char ch='e',ch1='b';
		int x=1;
		int num1=num;
		num=(num/2)+1;
		for(i=0;i<num;i++){
			System.out.print(ch);
			--ch;
		}
		++ch;
		for(i=0;i<num-1;i++){
			++ch;
			System.out.print(ch);
		}
		System.out.println("");
		for(i=0;i<num-1;i++)
		{
			
			for(j=num-1;j>i;j--){
				System.out.print(ch);
				--ch;				
			}
			for(k=i;k<=x-1;k++){
				System.out.print(" ");
			}
			ch1=ch++;
			x+=3;
			for(j=num-1;j>i;j--){
				++ch1;
				System.out.print(ch1);
			}
			ch='e';
			System.out.println("");
		}
		x=num1-4;
		ch='e';
		for(i=0;i<num-2;i++)
		{
			ch='e';
			for(j=0;j<=i+1;j++){
				System.out.print(ch);
				ch-=1;
			}
			for(k=0;k<x;k++){
				System.out.print(" ");
			}
			x-=2;
			ch1=ch;
			for(j=0;j<=i+1;j++){
				++ch1;
				System.out.print(ch1);
			}
			ch='e';
			System.out.println("");
		}
		for(i=0;i<num;i++){
			System.out.print(ch);
			--ch;
		}
		++ch;
		for(i=0;i<num-1;i++){
			++ch;
			System.out.print(ch);
		}
		in.close();
	}
			
}
