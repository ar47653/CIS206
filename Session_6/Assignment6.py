#USER INPUTS STRINGS TO EITHER ENCODE OR DECODE
def user_string_input():
    print("RUN-LENGTH-ENCODING")
    print("Enter a string of alphabetic characters to encode.")
    print("Or Enter a string of alphanumeric (RLE) characters to decode. Numbers up to 2 digits.")
    user_string = input("Enter string of alphabet or alphanumeric characters: ")
    while user_string.isalnum() == False or user_string.isnumeric():
        print("Error: Need to be either alphabetic sequence to encode or RLE characters to decode")
        user_string = input("Enter string of alphabet or alphanumeric characters: ")
    while user_string[0].isnumeric():
        print("Error: Cannot start with a number")
        user_string = input("Enter string of alphabet or alphanumeric characters: ")
        
    return user_string

#CHECKS IF USER INPUT 3 DIGIT NUMBERS IN THEIR RLE CHARACTERS
def string_digits_check(string):
    if string.isalpha():
        return
    elif string.isalnum():
        n = len(string)
        for i in range(n):
            if i < n-2 and string[i].isnumeric() and string[i+1].isnumeric() and string[i+2].isnumeric():
                return "redo"

#ENCODES OR DECODES THE CHARACTERS
def convert_rle(string):
    rle = ""
    n = len(string)
    counter = 1
    if string.isalpha():
        print("ENCODING:")
        for i in range(n):
            if i < n - 1 and string[i] == string[i + 1]:
                counter += 1
                i += 1
     
            elif i < n - 1 and string[i] != string[i + 1]:
                rle += string[i]
                if counter > 1:
                    rle += str(counter)
                counter = 1

            elif i == n - 1:
                if string[i] == string[i-1]:
                    rle += string[i]
                    rle += str(counter)
                elif string[i] != string[i-1]:
                    rle += string[i]

    elif not string.isalpha() and string.isalnum():
        string += "x"
        n = len(string)
        print("DECODING")
        for i in range(n):
            if string[i].isalpha() and i != n-1:
                rle += string[i]
            elif i < n-1 and string[i].isnumeric() and not string[i+1].isnumeric() and not string[i-1].isnumeric():
                for j in range(int(string[i])-1):
                    rle += string[i-1]
            elif i < n-1 and string[i].isnumeric() and string[i+1].isnumeric():
                m = (int(string[i]) * 10) + int(string[i+1])
                for j in range(m-1):
                    rle += string[i-1]
            elif string[i].isnumeric() and string[i-1].isnumeric():
                continue
            elif i == n-1:
                continue
            
    return rle
            

def main():

    user_string = user_string_input()
    while string_digits_check(user_string) == "redo":
        print("Error: keep numbers up to 2 digits.")
        user_string = user_string_input()
    rle = convert_rle(user_string)
    print(rle)




main()


