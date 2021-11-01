import qrcode       #this module is used to convert any text or link to a qrcode image

n = input("Enter the msg or link you want to make the qrcode of :\n")       #taking input from the user

img = qrcode.make(n)                                                        #make keyword is used to create a qr code


img.save("QR_code_img.jpg")                                                      #this step is to save qrcode in jpg format 
                                                                            #you can save it in other formats too see more on 
                                        
#you can use another module called cv2 (Opencv) to read qrcodes in python


import cv2

d = cv2.QRCodeDetector()

val,points,qr = d.detectAndDecode(cv2.imread("QR_code_img.jpg"))

print("The value hide inside qrcode is printed below using opencv:   ")
print(val)

#just like thaty we decoded the value in the qrcode 
#to know more about the attributes present before detectAndDecode function refer the documentation
