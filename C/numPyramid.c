#include <stdio.h>
void main(){

	for(int rows=1; rows<=4; rows++){
		int x=1;
		for(int space=3; space>=rows; space--){

			printf("  ");
		}
		for(int cols=1; cols<=2*rows-1; cols++){

			printf("%d ",x);
			
			if(cols<rows){
				
				x++;	
			}
			else{

				x--;
			}
		}
	printf("\n");	
	}
}
