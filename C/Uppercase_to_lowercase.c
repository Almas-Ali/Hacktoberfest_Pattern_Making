#include<stdio.h>
#include<conio.h>
int main()
{
    char upperChar, lowerChar;
    int ascii;
    printf("Enter an uppercase Character: ");
    scanf("%c", &upperChar);
    ascii = upperChar;
    lowerChar = ascii+32;
    printf("\nIts Lowercase = %c", lowerChar);
    getch();
    return 0;
}
