#Imports the time library. 
import time
#The amount of seconds it takes. this will be divided by the divide variable.
clock = 10
#The amount the clock variable will be divided every time the loop loops.
divide = 2
#The initial number that will be printed.
counter = 1
#The amount the counter variable will be incremented every loop.
increment = 1
#If you want an infinite loop, set this to False, otherwise True. Remember The F and T in False/True is capitalized.
ifLimit = True
#This variable is useless if ifLimit is False. If ifLimit is True it sets how many times the loop will loop. The last number that gets printed will always be: Limit * increment + counter - 1.
limit = 1531
#If limit is set to True it will run a ""for loop"" limit amounts of times.
if ifLimit:
    for i in range(limit):
        #It prints counter.
        print ('*',+counter)
        #Waits the amount of seconds = clock.
        time.sleep(clock)
        #clock gets divided by whatever divide is set to.
        clock /= divide
        #And counter gets incremented by increment.
        counter += increment
    #Prints a nice little done message. \n is a line break.
    print('\n\t*Done.')

    #input stops the program from closing, until you press enter.
    input()
#If ifLimit is false it will run a while loop witch will run for as long as the thing after while = True. In this case it will always be True, so it will never stop.

else:
   while True:
        #Prints counter

        print(counter)
        #Waits the amount of seconds = clock.

        time.sleep(clock)
        #clock gets divided by whatever divide is set to.

        clock /= divide
        #And counter gets incremented by increment.

        counter += increment
        #There is no done message here, or input to stop the program from closing, cause this will never be "done"
