import random,os
aq=os.system("cls")
while True:
    print('1 Ai, 2 User')
    vorodi= input("Open windows One or Tow. (1, 2) , Exit Non_Alphanumeric and Integers ")
    if vorodi.isalnum():
        list_vorodi=["1", "2"]
        if vorodi in list_vorodi:
            if vorodi=="1":
                
                    def get_input():#انتخاب صحیح کاربر از لیست
                        while True:
                            user_input=input('Enter your guess: ')
                            if user_input.isalnum():
                                return user_input.lower()
                            print('Your input was not correct. please enter again. ')
                            print('All words:',list_of_words )
                            print('_'*10)
                    def get_input_list():#ساخت لیست
                        list_of_words1=set()#ورودی تکراری ممنوع
                        while True:
                            user=input('Name list ')
                            if user.isalnum():
                                break
                        while True:
                            while user != 'ex':
                                if user.isalnum():
                                    list_of_words1.add(user.lower()) 
                                    user=input('Name lists next and output ex ')#برای خروج شدن از ساخت لیست
                                    list_of_words=list(list_of_words1)#تبدیل ب لیست
                                else:
                                    user=input('Name lists next and output ex ')
                            print('_'*10)       
                            return list_of_words
                    def get_input_form_list(words):#ورودی اشتباه
                        user_input=get_input()
                        while user_input not in words:
                            print('_'*10)
                            print('You should guess a word form the given words list! ')
                            print('please enter a correct word.')
                            print('All words:',list_of_words )
                            print('_'*10)
                            user_input=get_input()
                        return user_input
                    def print_game_intro():#خوش امد گویی
                        print('_'*10)
                        print('Hi, welcome was not correct. ')
                        print('please enter again.')
                        print('All words:',list_of_words )
                        print('please strat gussing. ')
                        print('_'*10)
                    def run_game(tedad_entkhab, words):
                        print('_'*10)
                        print_game_intro()
                        print(f'Number of guesses {tedad_entkhab}')
                        print('_'*10)
                        correct_word= random.choice(words)
                        guessed_words=set()
                        attempst=0
                        while attempst < tedad_entkhab:
                            user_input= get_input_form_list(words)
                            if user_input in guessed_words:
                                continue
                            attempst+=1
                            if user_input== correct_word:
                                print('YOU WON! ')
                                print('_'*10)
                                return
                            else:
                                print('_'*10)
                                print('You gurddrf wrong! ')
                                print(f'please try again! number of rounds left: {(tedad_entkhab)-attempst}')
                                print('_'*10)  
                                guessed_words.add(user_input)
                            print(guessed_words)
                        print(f'select Ai {correct_word}')
                        print('You lost! ')
                        print('_'*10)
                    def tedad_entkhab():#تعداد انتخاب ها
                        while True:
                            tedad_entkhab=random.randint(1,len(list_of_words))
                            print(tedad_entkhab)
                            if (tedad_entkhab) <= (len(list_of_words)):
                                run_game((tedad_entkhab),list_of_words)
                                break
                    list_of_words= get_input_list()
                    tedad_entkhab()
                    
            else:
                def get_input():#انتخاب صحیح کاربر از لیست
                    while True:
                        user_input=input('Enter your guess: ')
                        if user_input.isalnum():
                            return user_input.lower()
                        print('Your input was not correct. please enter again. ')
                        print('All words:',list_of_words )
                        print('_'*10)
                def get_input_list():#ساخت لیست
                    list_of_words1=set()#ورودی تکراری ممنوع
                    while True:
                        user=input('Name list ')
                        if user.isalnum():
                            break
                    while True:    
                        while user != 'ex':
                            if user.isalnum():
                                list_of_words1.add(user.lower()) 
                                user=input('Name lists next and output ex ')#برای خروج شدن از ساخت لیست
                                list_of_words=list(list_of_words1)#تبدیل ب لیست
                            else:
                                user=input('Name lists next and output ex ')
                        print('_'*10)       
                        return list_of_words
                def get_input_form_list(words):#ورودی اشتباه
                    user_input=get_input()
                    while user_input not in words:
                        print('_'*10)
                        print('You should guess a word form the given words list! ')
                        print('please enter a correct word.')
                        print('All words:',list_of_words )
                        print('_'*10)
                        user_input=get_input()
                    return user_input
                def print_game_intro():#خوش امد گویی
                    print('_'*10)
                    print('Hi, welcome was not correct. ')
                    print('please enter again.')
                    print('All words:',list_of_words )
                    print('please strat gussing. ')
                    print('_'*10)
                def run_game(tedad_entkhab, words):
                    print('_'*10)
                    print_game_intro()
                    print(f'Number of guesses {tedad_entkhab}')
                    print('_'*10)
                    correct_word= random.choice(words)
                    guessed_words=set()
                    attempst=0
                    while attempst < tedad_entkhab:
                        user_input= get_input_form_list(words)
                        if user_input in guessed_words:
                            continue
                        attempst+=1
                        if user_input== correct_word:
                            print('YOU WON! ')
                            print('_'*10)
                            return
                        else:
                            print('_'*10)
                            print('You gurddrf wrong! ')
                            print(f'please try again! number of rounds left: {(tedad_entkhab)-attempst}')
                            print('_'*10)  
                            guessed_words.add(user_input)
                        print(guessed_words)
                    print(f'select Ai {correct_word}')
                    print('You lost! ')
                    print('_'*10)
                def tedad_entkhab():#تعداد انتخاب ها
                    while True:
                        tedad_entkhab=(input('just the number '))
                        if tedad_entkhab.isdigit():
                            if int(tedad_entkhab) <= (len(list_of_words)):
                                run_game(int(tedad_entkhab),list_of_words)
                                break
                list_of_words= get_input_list()
                print('len list',len(list_of_words))#راهنما
                tedad_entkhab()
        else:
            print("_"*10)
            print("N0 , Just Choose 1 or 2 ")
            print("_"*10)
    else:
        print("Exit")
        break