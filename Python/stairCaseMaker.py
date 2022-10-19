class Error(Exception):
    pass
class IntegerOutOfRangeException(Error):
    pass
class NoStaircaseSizeException(Error):
    pass


def getUserInput():
    x = input("Please input your staircase size:\n")
    if x == "DONE":
        return "DONE"
    elif str(x).isdigit() == False: 
        if str(x)[0] != "-":
            raise ValueError
        else:
            return x
    else:
        return x


def printSteps(stepCount):
        if stepCount == "DONE":
            return "DONE"
        elif 0 < int(stepCount) < 1000:
            stepCount = int(stepCount)
            spaces = " " * ((stepCount-1)*2)
            holder = [spaces + "+-+"]
            lines = stepCount*2
            while lines != 1:
                if lines%2 == 0:
                    y = spaces + "| |"
                    holder.append(y)
                    spaces = spaces[2:]
                    lines = lines - 1
                else:
                    stepCount =- 1
                    x = spaces + "+-+-+"
                    holder.append(x)
                    lines = lines - 1
            holder.append("+-+")
            joinedString = "\n".join(holder)
            return joinedString
        elif int(stepCount) == 0:
            raise NoStaircaseSizeException
        elif int(stepCount) >= 1000 or int(stepCount) < 0:
            raise IntegerOutOfRangeException


def runProgram():
    while True:
        try:
            abb = getUserInput()
            if abb == "DONE":
                    return "Done Executing"
                    break
            elif abb != "DONE":
                    final = printSteps(abb)
                    print(final)
        except NoStaircaseSizeException:
            print("I cannot draw a staircase with no steps.")
        except IntegerOutOfRangeException:
            print("That staircase size is out of range.")
        except ValueError:
            print("Invalid staircase value entered.")
    
runProgram()