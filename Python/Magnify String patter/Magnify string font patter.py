'''
Guys if you can please add more character patter as much you can like,
-> Add small letter
-> Add number
-> Symbol like !@#$%^&*()_+-=~`{}[]|\:;"'<,>.?/

  *   *  *****  *      *       ***          *   *   ***   ****   *      **** 
  *   *  *      *      *      *   *         *   *  *   *  *   *  *      *   *
  *****  ****   *      *      *   *         * * *  *   *  ****   *      *   *
  *   *  *      *      *      *   *         ** **  *   *  *  *   *      *   *
  *   *  *****  *****  *****   ***          *   *   ***   *   *  *****  ****
'''
class Magnify_string:
    def __init__(self,data):
        if type(data)==str:
            self.data=data.lower()
        else:
            raise "Enter string data"
    def display(self):
        lst=["","","","",""]

        for i in self.data:
            lst[0]+="  "
            lst[1]+="  "
            lst[2]+="  "
            lst[3]+="  "
            lst[4]+="  "
            if i=="a":
                lst[0]+=" ***  "
                lst[1]+="*    *"
                lst[2]+="******"
                lst[3]+="*    *"
                lst[4]+="*    *"
            elif i=="b":
                lst[0]+="**** "
                lst[1]+="*   *"
                lst[2]+="**** "
                lst[3]+="*   *"
                lst[4]+="**** "
            elif i=="c":
                lst[0]+=" ****"
                lst[1]+="*    "
                lst[2]+="*    "
                lst[3]+="*    "
                lst[4]+=" ****"
            elif i=="d":
                lst[0]+="**** "
                lst[1]+="*   *"
                lst[2]+="*   *"
                lst[3]+="*   *"
                lst[4]+="**** "
            elif i=="e":
                lst[0]+="*****"
                lst[1]+="*    "
                lst[2]+="**** "
                lst[3]+="*    "
                lst[4]+="*****"
            elif i=="f":
                lst[0]+="*****"
                lst[1]+="*    "
                lst[2]+="**** "
                lst[3]+="*    "
                lst[4]+="*    "
            elif i=="g":
                lst[0]+=" ****"
                lst[1]+="*    "
                lst[2]+="* ***"
                lst[3]+="*   *"
                lst[4]+=" ****"
            elif i=="h":
                lst[0]+="*   *"
                lst[1]+="*   *"
                lst[2]+="*****"
                lst[3]+="*   *"
                lst[4]+="*   *"
            elif i=="i":
                lst[0]+="*****"
                lst[1]+="  *  "
                lst[2]+="  *  "
                lst[3]+="  *  "
                lst[4]+="*****"
            elif i=="j":
                lst[0]+="*****"
                lst[1]+="    *"
                lst[2]+="    *"
                lst[3]+="    *"
                lst[4]+="**** "
            elif i=="k":
                lst[0]+="*   *"
                lst[1]+="*  * "
                lst[2]+="**   "
                lst[3]+="*  * "
                lst[4]+="*   *"
            elif i=="l":
                lst[0]+="*    "
                lst[1]+="*    "
                lst[2]+="*    "
                lst[3]+="*    "
                lst[4]+="*****"
            elif i=="m":
                lst[0]+="*   *"
                lst[1]+="** **"
                lst[2]+="* * *"
                lst[3]+="*   *"
                lst[4]+="*   *"
            elif i=="n":
                lst[0]+="*   *"
                lst[1]+="**  *"
                lst[2]+="* * *"
                lst[3]+="*  **"
                lst[4]+="*   *"
            elif i=="o":
                lst[0]+=" *** "
                lst[1]+="*   *"
                lst[2]+="*   *"
                lst[3]+="*   *"
                lst[4]+=" *** "
            elif i=="p":
                lst[0]+="**** "
                lst[1]+="*   *"
                lst[2]+="**** "
                lst[3]+="*    "
                lst[4]+="*    "
            elif i=="q":
                lst[0]+=" **  "
                lst[1]+="*  * "
                lst[2]+="** * "
                lst[3]+="* ** "
                lst[4]+=" ****"
            elif i=="r":
                lst[0]+="**** "
                lst[1]+="*   *"
                lst[2]+="**** "
                lst[3]+="*  * "
                lst[4]+="*   *"
            elif i=="s":
                lst[0]+="*****"
                lst[1]+="*    "
                lst[2]+="*****"
                lst[3]+="    *"
                lst[4]+="*****"
            elif i=="t":
                lst[0]+="*****"
                lst[1]+="  *  "
                lst[2]+="  *  "
                lst[3]+="  *  "
                lst[4]+="  *  "
            elif i=="u":
                lst[0]+="*   *"
                lst[1]+="*   *"
                lst[2]+="*   *"
                lst[3]+="*   *"
                lst[4]+=" *** "
            elif i=="v":
                lst[0]+="*   *"
                lst[1]+="*   *"
                lst[2]+="*   *"
                lst[3]+=" * * "
                lst[4]+="  *  "
            elif i=="w":
                lst[0]+="*   *"
                lst[1]+="*   *"
                lst[2]+="* * *"
                lst[3]+="** **"
                lst[4]+="*   *"
            elif i=="x":
                lst[0]+="*   *"
                lst[1]+=" * * "
                lst[2]+="  *  "
                lst[3]+=" * * "
                lst[4]+="*   *"
            elif i=="y":
                lst[0]+="*   *"
                lst[1]+=" * * "
                lst[2]+="  *  "
                lst[3]+=" *   "
                lst[4]+="*    "
            elif i=="z":
                lst[0]+="*****"
                lst[1]+="   * "
                lst[2]+="  *  "
                lst[3]+="*    "
                lst[4]+="*****"
            elif i==" ":
                lst[0]+="     "
                lst[1]+="     "
                lst[2]+="     "
                lst[3]+="     "
                lst[4]+="     "
        for i in lst:
            print(i)
MyObj = Magnify_string(input("Enter string you want to magnify--> "))
MyObj.display()