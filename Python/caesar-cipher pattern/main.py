import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

response = "yes"

def caesar(response):

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if shift > 25:
    shift %= 26    
  en_message = ""

  for char in text:
    if char.lower() not in alphabet:
      new_letter = char
      en_message += new_letter
      continue
    index = alphabet.index(char)
    if direction.lower() == "encode":
      new_index = index + shift
      if new_index > 25:
        new_index = shift - (26 - index)
    else:
      new_index = index - shift
      if new_index < 0:
        new_index = (26 - shift ) + index    
    new_letter = alphabet[new_index]
    en_message += new_letter 
  print(f"The {direction}d text is: {en_message}")    
    

while response == "yes":
  caesar(response)

  response = input("Type 'yes' if you wish to go back, else type 'no'.\n")
