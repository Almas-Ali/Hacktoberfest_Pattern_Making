def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6:
        print('Invalid Password: length should be at least 6')
        val = False
        return val

    if len(passwd) > 20:
        print('Invalid Password: length should be not be greater than 8')
        val = False
        return val
        
    if not any(char.isdigit() for char in passwd):
        print('Invalid Password: Password should have at least one numeral')
        val = False
        return val

    if not any(char.isupper() for char in passwd):
        print('Invalid Password: Password should have at least one uppercase letter')
        val = False
        return val

    if not any(char.islower() for char in passwd):
        print('Invalid Password: Password should have at least one lowercase letter')
        val = False
        return val

    if not any(char in SpecialSym for char in passwd):
        print('Invalid Password: Password should have at least one of the symbols $@#')
        val = False
        return val

    if val:
        print("valid Password !!")

          
if __name__ == '__main__':
    passwd = input("Enter your Password: ")
    password_check(passwd)

      
    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
