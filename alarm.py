import datetime
from playsound import playsound
import random
import pygame
import time

alarmH=int(input("Enter Hour :"))
alarmM=int(input("Enter Minutes :"))
alarmam=input("AM/PM :")



if alarmH == 12 and alarmam.lower() == "pm":
    alarmH=12
elif alarmH == 12 and alarmam.lower() == "am":
    alarmH=0
elif alarmH != 12 and alarmam.lower() == "pm":
    alarmH = alarmH + 12
elif alarmH !=12 and alarmam.lower() == "am":
    alarmH =alarmH + 0


while True:
    now=datetime.datetime.now()
    if alarmH == now.hour and alarmM == now.minute:
        start_time=datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=5)
        random_numbers=random.sample(range(1,50),2)
        number1=random_numbers[0]
        number2=random_numbers[1]
        operators=["+","-"]
        random_operator=random.choice(operators)
        
        if random_operator == "-":
            correct_answer=number1 - number2
        elif random_operator == "+":
            correct_answer=number1 + number2
            
        print(f"what is answer for this calculation {number1} {random_operator} {number2} = ?")
        
        pygame.mixer.init()
        pygame.mixer.music.load('static/audio/ringtone.mp3')
        pygame.mixer.music.play(-1)
        
        while datetime.datetime.now() < end_time:
            user_input = input("Enter your answer :")
            
            if user_input !=0:
                user_answer = int(user_input)
                if user_answer == correct_answer:
                    pygame.mixer.music.stop()
                    break
                else:
                    print("Incorrect Answer try again")
                    print(f"what is answer for this calculation {number1} {random_operator} {number2} = ?")
            else:
                print("Invalid Input")
                
            time.sleep(1)
        pygame.mixer.music.stop()
        break            
            
        

            
            
    
        
        
    

