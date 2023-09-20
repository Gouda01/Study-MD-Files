class Game :
    
    def __init__(self):
        while True:
            print('''Welcome to our Game Please enter game number :
        1 : Sentence No duplicate
        2 : Diveded by number
        3 : Exit the game''')

            while True :        
                choice_number = int(input('Please enter game number : '))
                if choice_number == 1 :
                    sentence = input('Enter your sentence : ')
                    self.sentence_no_duplicate(sentence)
                elif choice_number == 2 :
                    x = int(input('Enter First Number : '))
                    y = int(input('Enter Second Number : '))
                    self.devided_by(x,y)
                elif choice_number == 3 :
                    print('Good Bye')
                    return
                if choice_number in range (1,4):
                    break
                else :
                    print('Please choose correct Number')
                

            play_again = input('Enter any key to Play Again or n to exit ')
            if play_again == 'n' :
                break

    def sentence_no_duplicate (self,sentence):
        words = sentence.split()
        new_words = []
        for w in words :
            if w not in new_words :
                new_words.append(w)
        print(' '.join(new_words))

    def devided_by(self,x,y):
        for n in range(1,100):
            if n%x ==0 and n%y ==0 :
                print(n)
            
        

g = Game()
