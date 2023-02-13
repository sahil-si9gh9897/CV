########  ENCRYPTION PROGRAM
print("\t\t\t\tSECRET CODE ENCRYPTION & DECRYPTION PROGRAM")
ask=input("Do you want to code(y) or decode(n):")
if(ask=="y"):
    ask2=input("Enter what do want to code:")
    if(ask2[0]== "a"):
        ask2+="rsk"
        lst=list(ask2)
        lst[0]="o"
        str=''.join(lst)
        print(str[::-1])

    elif(ask2[0]== "c"):
        ask2+="rsk"
        lst = list(ask2)
        lst[0] = "m"
        str = ''.join(lst)
        print(str[::-1])

    elif (ask2[0] == "e"):
        ask2 += "rsk"
        lst = list(ask2)
        lst[0] = "l"
        str = ''.join(lst)
        print(str[::-1])

    elif(ask2[0]== "g"):
        ask2+="rsk"
        lst = list(ask2)
        lst[0] = "i"
        str = ''.join(lst)
        print(str[::-1])

    elif(ask2[0]== "i"):
        ask2+="rsk"
        lst = list(ask2)
        lst[0] = "g"
        str = ''.join(lst)
        print(str[::-1])

    elif(ask2[0]== "l"):
        ask2+="rsk"
        lst = list(ask2)
        lst[0] = "e"
        str = ''.join(lst)
        print(str[::-1])

    elif(ask2[0]== "m"):
        ask2+="rsk"
        lst = list(ask2)
        lst[0] = "c"
        str = ''.join(lst)
        print(str[::-1])

    elif(ask2[0]== "o"):
        ask2+="rsk"
        lst = list(ask2)
        lst[0] = "a"
        str = ''.join(lst)
        print(str[::-1])

    else:
        ask2+="xkv"
        lst = list(ask2)
        str = ''.join(lst)
        print(str[::-1])



elif(ask=="n"):
    ask3 = input("enter what do want to decode:")
    if(ask3[0]=="k"):
        rep=ask3.replace("ksr","")
        rev=rep[::-1]
        if(rev[0]=="m"):
            rel = list(rev)
            rel[0] = "c"
            str1 = ''.join(rel)
            print(str1)

        elif(rev[0]=="l"):
            rel = list(rev)
            rel[0] = "e"
            str1 = ''.join(rel)
            print(str1)

        elif (rev[0] == "i"):
            rel = list(rev)
            rel[0] = "g"
            str1 = ''.join(rel)
            print(str1)

        elif (rev[0] == "g"):
            rel = list(rev)
            rel[0] = "i"
            str1 = ''.join(rel)
            print(str1)

        elif (rev[0] == "e"):
            rel =list(rev)
            rel[0]="l"
            str1=''.join(rel)
            print(str1)

        elif (rev[0] == "c"):
            rel = list(rev)
            rel[0] = "m"
            str1 = ''.join(rel)
            print(str1)

        elif (rev[0] == "a"):
            rel = list(rev)
            rel[0] = "o"
            str1 = ''.join(rel)
            print(str1)
        elif (rev[0] == "o"):
            rel = list(rev)
            rel[0] = "a"
            str1 = ''.join(rel)
            print(str1)

    elif(ask3[0]=="v"):
        rem=ask3.replace("vkx","")
        print(rem[::-1])





