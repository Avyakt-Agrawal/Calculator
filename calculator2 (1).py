import time
import math
import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()

def SpeakText(command):
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
def speak(MyText):
    
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2,duration=0.2)
            SpeakText(MyText)
    except sr.RequestError as s:
        print("an error occur")
def res():
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2,duration=0.2)
            audio2=r.listen(source2)
            MyText=r.recognize_google(audio2)
            MyText=MyText.lower()
            
            SpeakText(MyText)
            return MyText
    except sr.RequestError as s:
        print("an error occur")


mytext = 'Welcome'
speak(mytext)
mytxt = 'I am your personal calculator, I am a creation of Saksham & Avyacht. I am a product of their Genius Hour.'
speak(mytxt)
mytext2 = 'Press 1 if you want to solve a math operation or press 2 to check a equation'
speak(mytext2)
b = res()
while True:
    
    if b == "1"or "Number 1":
        print('1) Basic math operations-x')
        print('    addition')
        print('    subtraction')
        print('    multiplication')
        print('    division')
        print('    exponents')
        print('    quetoinent')
        print('    remainder')
        print('    square root')
        print('    bodmass')
            
        print('2) Root')
        print('3) Percentage')
        print('4) Rounding decimals')
        print('5) Adding tax')
        print('6) Type of triangle')
        print('7) What quadrent coodernates are in')
        print('8) Percentage to decimals')
        print('9) Decimals to percentage')
        print('10) Factorials')
        print('11) Prime number or not')
        print('12) Pallindrome number or not')
        print('13) Single step algebric equations')
        print('14) Average')
        print('15) Exponential growth')
    
        mytext3 = 'What operation do you want to do'
        speak(mytext3)
        oof = res()
        
        
        
        if oof == 'Number 1'or "1":
            print('+ to do addition')
            print('- to do subtraction')
            print('* to do multiplication')
            print('/ to do division')
            print('** to do exponents')
            print('// to get only the quetoinent')
            print('% to get only remainder')
            print('do ** 1/2 to do square root')
            print('Brackets if you waant to solve something first')
            
            a = input('Enter a math expression:')
            final = eval(a)
            print(final)
       
        elif oof == '2':
            iff = input('enter first number')
            what = input('enter second number')
            final = pow(float(iff),1/float(what))
            print(final)
        elif oof  == '3'or oof== "Number 3":
            iff = input('enter first number')
            what = input('enter second number')
            p = float(what) / 100
            final = float(iff) * p
            print(final)
        elif oof == 'number four':
            iff = input('enter first number')
            what = input('enter second number')
            final = round(float(iff))

        elif oof == 'number five':
            iff = input('enter first number')
            what = input('enter second number')
            c = float(what) / 100
            f = float(iff) * c
            final = f+float(iff)
            print(final)
        elif oof == 'number six':
            n = int(input('Tell me the lenght of the first side of triangles'))
            p = int(input('Tell me the lenght of the second side of triangles'))
            c = int(input('Tell me the lenght of the third side of triangles'))
            if((n<c+p)and(c<n+p)and(p<n+c)):
                if(n == p and p == c):
                    final = 'This is an equilateral triangle'

                elif((n == p)or(n == c )or(c == p)):
                    final = 'This is a isoceles triangle'

                else:
                      final = 'This is a scalene triangle'

            else:
                final = 'The inputs you have given do not form a triangle'
            print(final)
        elif oof == 'number seven':
                 x = int(input('What is the x axis'))
                 y = int(input('What is the y axis'))
                 if(x>-1 and y>-1):
                         final = 'This lies in the first quadrent'
                 if(x>-1 and y<0): 
                         final = 'This lies in the second quaderent'
                 if(x<0 and y<0):
                         final = 'This lies in the third quadrent'
                 if(x>-1 and y<0):
                         final = 'This lies in the fourth quadrent'

                 print(final)

        elif oof == 'number eight':
            iff = float(input('What percentage do you want to convert'))
            final = iff/100

        elif oof == 'number nine':
            iff = float(input('What decimal do you want to convert'))
            final = iff*100
            print(final,'%')

        elif oof == 'number ten':
            iff = float(input('What numbers factorial do you want'))
            a =  math.factorial(iff)
            print(a)

        elif oof == 'number eleven':
            n = int(input('Number to check if prime or not'))
            c = 0
            for i in range(n+1):
                if n%i == 0:
                    c = c+1
            if c == 2:
                print('This is a prime number')
            else:
                print('This is a composite number')
        elif oof == 'number twelve':
            n = int(input('number please'))
            n1 = 0
            a = n
            while n>0:
                    
                x = n%10
                n1 = (n1 * 10) + x
                n = n//10
            
            if n1 == a:
                print('Pallindrome')
            else:
                print('Not pallindrome')
        elif oof == 'number thirteen':
            x = -100
            i = int(input('What is the number on the variable side'))
            n = int(input("What does the equation equal to"))
            e = input('what is the operation')
            if e == "+":
                while True:
                    if i+x == n:
                        print('x=',x)
                        break
                    
                    x = x+1
            if e == "-":
                while True:
                    if i-x == n:
                        print('x =',x)
                        break
                    
                    x = x+1
            if e == "*":
                while True:
                    if i*x == n:
                        print('x =',x)
                        break
                    
                    x = x+1
            if e == "/":
                while True:
                    if i/x == n:
                        print('x =',x)
                        break
                    
                    x = x+1

        elif oof == 'number fourtenn':
            j = int(input('How many inputs do you want'))
            f = 0
                
            for i in range(j):
                n = int(input('Enter input:'))
                f = f+n
            print(f/j)
        elif oof == 'number fifteen':
            a = int(input('Inital amount'))
            r = int(input('Rate of increase'))
            t = int(input('Time in weeks'))
            for i in range(1,t+1):
                b = a*r+a
                print('week', i,'=',b)
                a = b
    if b == 'number two':
        check = 'What is the equation that you want to check'
        speak(check)
        c = input('')
        c = eval(c)
        j = 'what is your awnser'
        speak(j)
        a = int(input(''))
        if c == a:
            s = 'your awnser is correct'
            speak(s)
        else:
            d = 'Wrong awnser, try again'
            speak(d)
        


     

                    
                
                
                
                
                
        
    
            

   
            
        
            
    
    

    
    
       
        


    
    time.sleep(2)
    my = 'Do you want use the calculator again y/n'
    speak(my)
    f = input('')
    if f == 'y':
        print('ok')

    else:
        print('Bye Bye')
        time.sleep(2)
        break
    
    
    

            
