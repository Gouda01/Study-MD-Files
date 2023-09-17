#### <u>OOP Examples :</u>

##### Game Example :

```python
class Game :
    def __init__(self) :
        while True :
            print ('''Welcome in our game, please enter game number :
        1 : Sentence no duplicate
        2 : Devides by numbers
        3 : Exit game''')
            while True :
                user_choice = int(input('Enter Game Number : '))
                if user_choice in range (1,4):
                    break
                else :
                    print ('Please Enter number between 1 to 3')

            if user_choice == 1 :
                sentence = input('Enter sentence : ')
                self.sentence_no_duplicate(sentence)

            elif user_choice == 2 :
                x = int(input('Enter first number : '))
                y = int(input('Enter second number : '))
                self.devidi_by(x,y)

            elif user_choice == 3 :
                print('Good Bye')
                return

            play_again = input('Press any key to play again or n to Exit : ')

            if play_again == 'n' :
                break

    def sentence_no_duplicate(self,sentence):
        words = sentence.split(' ')
        new_words = []
        for w in words :
            if w not in new_words :
                new_words.append(w)
        print (' '.join(new_words))

    def devidi_by (self,x , y):
        for n in range(1,100) :
            if n%x == 0 and n%y ==0 :
                print(n)

g = Game()
```

