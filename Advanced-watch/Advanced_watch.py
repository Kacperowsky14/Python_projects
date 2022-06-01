import sys
import time
import datetime
import date_now_file 

# imports the necessary modules, and a second file written in python

lap = 0
chose = 4

#assigns values ​​to variables that the program could then use

def start():
    time = datetime.datetime.now()  # The program gets date
    print(time.strftime("%H:%M"))   # displays the current time
    day = time.strftime("%d")
    month = date_now_file.date_now()
    year = time.strftime("%Y")          # assigns the current date to the variables, in the next line displays the date, 
    print(day +" "+  month +" "+ year)  #retrieving the  month from the module that assigns the name of the month to 
                                        #the number corresponding to it    


def stopwatch():
    start = input(("Press enter to turn on stopwatch"))
    timer = time.time() # assigns the current time to a variable
    while True:
        try:
            timing = time.time() - timer
            print("Time: %4.2f" % timing,  end = "\r",) # this is a function that causes time to appear on one line 
                                                        #(element end = "\ r"). Element "% 4.2f" Is responsible for 
                                                        #displaying a maximum four-digit number, rounded to 2 places after the trim
        except KeyboardInterrupt:  # ctrl + c turns off the loop above
            time_stop = time.time()
            chose = input("\n") # after pressing ctrl + c we have to choose what we want to do
            if chose == 'r':
                time_start = time.time()        
                new_time = time_start-time_stop 
                timer += new_time
                continue        # the three lines above are used to display the correct time after the pause
            if chose == 'l':
                lap =+ 1
                timing = time.time() - timer
                print("Lap " , lap, ", time : ",timing)
                continue
            if chose == 's':
                timing = time.time() - timer
                print('Time:  %4.2f' % timing)
                break
    


def countdown_timer():
    try:
        time_cd = float(input("Enter the time in minutes for which you want to set the time\n"))
        timer = time.time() + time_cd * 60 # in the line above there is a number of seconds, so the 
                                           #program must multiply this by 60 for the result to be minutes
    except:
        print("You have entered an invalid value")  # exception handling
    while True:
        try:
            remaining_time = timer - time.time()
            print("Time is left: %4.2f" %remaining_time,  end = "\r",)
            if remaining_time <= 0:
                stop = 1
                print("\nTime is up!")
                while stop <= 10:
                    print('\a', end = "\r") 
                    time.sleep(0.5)
                    stop += 1 #loop which causes the system bell ('\a') to repeat 10 time
                break
        except KeyboardInterrupt:
            print("Timer off")
            break


def date():
    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y") 
    # assigns values ​​to variables corresponding to the current date

    selected_day = int(input("Enter the day\n"))
    selected_month = int(input("Enter the month\n"))
    selected_year = int(input("Enter the year\n"))  
    # the user enters the date by which he wants to calculate the difference


    date_today = datetime.date(int(year), int(month), int(day))  # converts str values ​​to int
    selected_date = datetime.date(selected_year, selected_month,selected_day)  

    if date_today > selected_date: 
        print("It has passed from the given date: ",(date_today - selected_date).days," days")
    if selected_date > date_today:
        print("Until the given date it has remained ",(selected_date - date_today).days," days")

    # the conditional statements above check to see if the user 
    #has entered a date back or a date yet to come. Then it prints the result


#main

start()
while chose == 4:
    chose = input("1 - Stopwatch \n2 - Timer \n3 - How many days left to / how many days have passed from \n0 - Exit\n")
    if chose == '0':
       exit(0)
    elif chose == '1':
        print("Type Ctr + c to stop, and next 'r' to continue")
        print("Press Ctrl + c and next 'l' to complete the lap. In this place time won't stop")
        print("Press Ctrl + c and next 's' to stop stopwatch")
        chose = chose.lower()
        stopwatch()
        chose = 4
    elif chose == '2':
        countdown_timer()
        chose = 4
    elif chose == '2':
        date()
        chose = 4

