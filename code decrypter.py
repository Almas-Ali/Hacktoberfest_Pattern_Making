from tkinter import *

from tkinter import messagebox


root = Tk()
variable1 = StringVar(root)
variable2 = StringVar(root)

variable1.set("lang-code")
variable2.set("lang-code")

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ', ':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

def clearAll() :
	
	language1_field.delete(1.0, END)
	language2_field.delete(1.0, END)


def convert() :

	message = language1_field.get("1.0", "end")[:-1]

	if variable1.get() == variable2.get() :
		
		messagebox.showerror("Can't Be same Language")
		return

	elif variable1.get() == "Eng" and variable2.get() == "Morse" :

		
		rslt = encrypt(message)

	elif variable1.get() == "Morse" and variable2.get() == "Eng" :

	    
		rslt = decrypt(message)

	else :
		
		
		messagebox.showerror("please choose valid language code..")
		return
	
	language2_field.insert('end -1 chars', rslt)
	
		
def encrypt(message):
	cipher = ''
	for letter in message:
		if letter != ' ':

			cipher += MORSE_CODE_DICT[letter] + ' '
		else:
			cipher += ' '

	return cipher

def decrypt(message):
	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		if (letter != ' '):

			i = 0
			citext += letter
		else:
			i += 1
			if i == 2 :

			    
				decipher += ' '
			else:
				decipher += list(MORSE_CODE_DICT.keys())[
							list(MORSE_CODE_DICT .values()).index(citext)]
				citext = ''

	return decipher


if __name__ == "__main__" :
	
    
	root.configure(background = 'light green')
	root.geometry("400x350")
	root.title("Translator")
	headlabel = Label(root, text = 'Welcome to Morse Code Translator',
							fg = 'black', bg = "red")

	label1 = Label(root, text = "One Language ",
				fg = 'black', bg = 'dark green')
	
	label2 = Label(root, text = "From Language",
				fg = 'black', bg = 'dark green')
	
	label3 = Label(root, text = "To Language ",
				fg = 'black', bg = 'dark green')

	label4 = Label(root, text = "Converted Language ",
				fg = 'black', bg = 'dark green')
	
	headlabel.grid(row = 0, column = 1)
	label1.grid(row = 1, column = 0)
	label2.grid(row = 2, column = 0)
	label3.grid(row = 3, column = 0)
	label4.grid(row = 5, column = 0)
	
	language1_field = Text(root, height = 5, width = 25,
									font = "lucida 13")
	language2_field = Text(root, height = 5, width = 25,
									font = "lucida 13")
		
	language1_field.grid(row = 1, column = 1, padx = 10)
	language2_field.grid(row = 5, column = 1, padx = 10)


	languageCode_list = ["Eng", "Morse"]

	FromLanguage_option = OptionMenu(root, variable1, *languageCode_list)
	ToLanguage_option = OptionMenu(root, variable2, *languageCode_list)
	
	FromLanguage_option.grid(row = 2, column = 1, ipadx = 10)
	ToLanguage_option.grid(row = 3, column = 1, ipadx = 10)
	
	button1 = Button(root, text = "Convert", bg = "red", fg = "black",
								command = convert)
	
	button1.grid(row = 4, column = 1)

	button2 = Button(root, text = "Clear", bg = "red",
					fg = "black", command = clearAll)
	
	button2.grid(row = 6, column = 1)
	
	root.mainloop()
