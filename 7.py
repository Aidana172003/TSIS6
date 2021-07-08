def letter(str):
    count_upper=0
    count_lower=0
    for i in str:
        if i.isupper():
            count_upper+=1
        elif i.islower():
            count_lower+=1
    print("Upper case ", count_upper)
    print("Lower case ", count_lower)
str=input()
letter(str)