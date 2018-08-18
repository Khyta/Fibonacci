import time
number1 = 1
number2 = 1

while True:
    time.sleep(0.005)
    number3 = number1 + number2
    number1 = number2
    number2 = number3
    print(number3) 
