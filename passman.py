import string

Alpha = string.ascii_uppercase
Alpha_list = list(Alpha)

Alpha_slist = []

for i in range(len(Alpha_list)):
    if i <= 4:
        char = Alpha_list[(i+21)]
        Alpha_slist.append(char)
    elif i > 4:        
        char = Alpha_list[((i+21)-26)]
        Alpha_slist.append(char)

