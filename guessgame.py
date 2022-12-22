print("                              WELCOME     TO   THE    ( GUESS   THE   WORD )  GAME")
print("                                                                                             -- developed by Mr. AKASH YADAV ")
game=input("                       Do you want to play as a single player or multiplayer ? \n")


if game=='single':
    list1=["c_ _ f o _ t a _ l e","h _ l _ o"," n _ m _ "," g _ e _ s"," l _ v _ "," s _ m _ "," f _ i _ n _","m _ e _"," f _ s _ i _ n","t _ a _ e _","v _ c _ o _ y","i _ t e _ n_ _ i _ _ _ l" ]
    list2=["comfortable","hello","name","guess","love","some","friend","meet","fashion","travel","victory","international"]
    list3=["relax","greeting","common","guess","pyar","few","dost","gathering","trend","ghumna","jeet","videsh"]
    print("                         ***** YOU HAVE ENTERED INTO THE SINGLE PLAYER MODE*****\n")
    u=input("press any key to enter into the game :: ")
    str1=input("                                          ENTER YOUR NAME  :: ")
    print("                                    ",str1," -------WELCOME TO THE GAME------- ")
    print("\n\n  RULES OF THE GAME :: \n1. You will be given the words with some blanks .\n2. With each correct guess you will be awarded with 20 points .\n3. With each wrong guess 5 points will be deducted from your score.\n4. You will be asked to use hint after every wrong answer .\n5. If your answer is correct after hint you will be given 10 point.\n6. If your answer (after hint) remains wrong you will be penalised with 10 points.")
    print("\n                                     ****LET'S BEGIN THE GAME****")
    score=0
    i=0
    k=0
    e=input("\n                                 ****ENTER ANY KEY TO BEGIN****")
    for j in list1:
        print("\n",str1," , your word number ",i+1," is :: ",        j)
        str2=input("Enter your answer :: ")
        if str2==list2[i]:
            print("HURRAY! , YOU HAVE GUESSED CORRECT ANSWER")
            score=score+20
            i=i+1
            k=k+1
            choice=int(input("\nDo you want to continue the game :: press 1 to continue and press any key to exit :: "))
            if choice==1:
                continue
            else:
                break

        else:
            print("OOPS, YOU HAVE GUESSED WRONG ANSWER")
            n=int(input("\nFor hint press 1 otherwise press 2 for next question :: "))
            if n==1:
                for z in list3[k]:
                    print(z)
                    str2=input("enter your answer again :: ")
                    if str2==list2[i]:
                        print("yes you guessed correctly this time")
                        score=score+10
                        k=k+1
                        i=i+1
                        break
                    else :
                        print("you guessed wrong answer again")
                        score=score-10
                        i=i+1
                        k=k+1
                        break
            else:
                print("")
                score=score-5
                i=i+1
                k=k+1
    print("\n*****YOUR FINAL SCORE IS ",score,"*****")
    print(" I hope you enjoyed the game ",str1,". See you soon.")
    print(" THANK YOU")




elif game=='multiplayer':
    list1=["c_ _ f o _ t a _ l e","h _ l _ o"," n _ m _ "," g _ e _ s"," l _ v _ "," s _ m _ "," f _ i _ n _","i _ _ e _ _ a t _ _ _ _ l"]
    list2=["comfortable","hello","name","guess","love","some","friend","international"]
    list4=["b _ o _"," c _ l _ u _ a _ _ r"," m _ b _ l _","d _ o _","f _ i _ n _","c _ m _ t _ r ","r _ d _","f _ s _ i o _"]
    list5=["book","calculator","mobile","door","friend","computer","ride","fashion"]
    print("                             ***** YOU HAVE ENTERED INTO THE MULTIPLAYER MODE *****\n")
    print("\n                                                 HOPE YOU WILL ENJOY")
    R=input("Press any key to enter into the game  :: ")
    str1=input("\n                           ENTER THE NAME OF PLAYER 1 :: ")
    str3=input("\n                           ENTER THE NAME OF PLAYER 2 :: ")
    print(str1 ,"and ", str3 ," -------WELCOME TO THE GAME------- ")
    print("\n\nRULES OF THE GAME :: \n1. You will be given the words with some blank .\n2. With each correct guess you will be awarded with 20 points .\n3.With each wrong guess 5 points will be deducted from your score")
    print("\n                               ****LET'S BEGIN THE GAME****")
    score=0
    score1=0
    i=0
    z=0
    e=input("\n                         ****ENTER ANY KEY TO BEGIN****")
    for start in range(0,50):
        if start%2==0:
            for j in list1:
                print("\n",str1," , it is your turn and your word number ",i+1," is :: ",j)
                str2=input("Enter your answer :: ")
                if str2==list2[i]:
                    print("HURRAY! , YOU HAVE GUESSED CORRECT ANSWER")
                    score=score+20
                    list1.pop(0)
                    i=i+1
                    break

                else:
                    print("OOPS, YOU HAVE GUESSED WRONG ANSWER")
                    score=score-5
                    list1.pop(0)
                    i=i+1
                    break
    
    
        else:
            for j in list4:
                print("\n",str3," , it is your turn and your word number ",z+1," is :: ",j)
                str2=input("Enter your answer :: ")
                if str2==list5[z]:
                    print("HURRAY! , YOU HAVE GUESSED CORRECT ANSWER")
                    score1=score1+20
                    list4.pop(0)
                    z=z+1
                    break

                else:
                    print("OOPS, YOU HAVE GUESSED WRONG ANSWER")
                    score1=score1-5
                    list4.pop(0)
                    z=z+1
                    break

        choice=int(input("\nif you want to continue :: press 1 \nif you want to exit :: press 2 :: "))
        if choice==1:
            continue
        else:
            break
    if score>score1:
        print("\nThe final score of ",str1," is ",score)
        print("\nThe final score of ",str3,"is ",score1)
        print("\n\n                                    *****HURRAY",str1," is winner *****")
    

    elif score1>score:
        print("\nThe final score of ",str1," is ",score)
        print("\nThe final score of ",str3,"is ",score1)
        print("\n\n                                    *****HURRAY",str3," is winner *****")
    elif score1==score:
        print("\nThe final score of ",str1," is ",score)
        print("\nThe final score of ",str3,"is ",score1)
        print("\n\n                       *****HURRAY",str1," and ",str3," both have equal score *****") 


else:
    print("gadhe padhna nhi ata kya single ya multiplayer likhna tha")
    




