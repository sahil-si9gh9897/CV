questions=[
    ["QUE1.WHAT IS THE CAPITAL OF INDIA?","A.DELHI" ,"B.MUMBAI" ,"C.PATNA" ,"D.BENGLURU ","a"],
    ["QUE2.WHO IS THE FATHER OF LORD RAMA?","A.BHARATH" ,"B.SHATRUGHAN" ,"C.BRAHMA" ,"D.DASHRATH ","d"],
    ["QUE3.WHO IS KNOWN AS THE FATHER OF COMPUTER ","A.RAMESH" ,"B.ALEX" ,"C.CHARLES BABBAGE" ,"D.JOHN ","c"],
    ["QUE4.WHICH CITY IS KNOWN AS THE SILICON VALLEY OF INDIA?","A.DELHI" ,"B.MUMBAI" ,"C.PATNA ","D.BENGLURU","d"],
    ["QUE5.PYTHON IS A_______LANGUAGE?","A.HINDI" ,"B.OBJECT ORIENTED" ,"C.TAMIL" ,"D.ENGLISH ","b"],
]
print("\t\t\tKAUN BANEGA LAKHPATI")
levels=[1000,5000,25000,100000,500000]
i=0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"question for {levels[i]} rs is :")
    print(question[0])
    print(question[1],"\t",              question[2])
    print(question[3],"\t",               question[4])
    reply=input("CHOOSE A VALID ANSWER:")
    if(reply== question[-1]):
        print(f"CORRECT ANSWER ",{reply}, "YOU HAVE WON {levels[i]} RS\n")
    else:
        print(f"wrong answer you have lost {levels[i]}rs")
        break
print("thanks for playing this game!!!")



