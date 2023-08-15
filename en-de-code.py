# Using list comprehension to create a list of alphabets
alphabet_list = [chr(ord('a') + i) for i in range(26)]*10000
# print(alphabet_list)

print("Welcone in code encode decode  ")

def both_code(user_input,shift):
    encode = "" 
    if user_choose == "d":
        shift = -(shift)
    for char_is in user_input:
        if char_is in alphabet_list:
          possion = alphabet_list.index(char_is)
          new_possion = possion+shift
        #   print(char_is)
        #   print(f"possion {possion}")
        #   print(f"new possion {new_possion}")
          if new_possion > 25:
                new_possion -= 26
          if new_possion < 0:
                new_possion += 26
          
          encode += alphabet_list[new_possion]
        else :
            encode += char_is
    print(encode)
    
    
    
    


def encode(user_input,shift):
    encode = ""
    
    for char_is in user_input:
        if char_is in alphabet_list:
          possion = alphabet_list.index(char_is)
          new_possion = possion+shift
          if new_possion > 25:
                new_possion -= 26
          encode += alphabet_list[new_possion]
        else :
            encode += char_is
    print(encode)

def decode(user_input,shift):
    encode = ""
    for char_is in user_input:
        if char_is in alphabet_list:
            possion = alphabet_list.index(char_is)
            new_possion = possion-shift
            if new_possion < 0:
                new_possion += 26
                # print(f"new poss <0 {new_possion}")
            encode += alphabet_list[new_possion]
        else :
            encode += char_is   
    print(encode)

is_code = True
while is_code:
    user_choose = input("For encode : e\nFor decode : d\n").lower()
    user_code = input("Enter code :").lower()
    shift = int(input("Enter shift number : "))
   
    both_code(user_code,shift)
    # if user_choose == "e":
    #     encode(user_code, shift)
    # elif user_choose == "d":
    #     decode(user_code , shift)

    retry = input("More code encode , decode ? \nType'y' or 'n' : ").lower()
    if retry == "n":
        is_code = False

