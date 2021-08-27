
import time 

start_time = time.time()

print("enter the seconds : ")
seconds = input()

while True:

    current_time = time.time()

    elapsed_time = current_time - start_time


    if elapsed_time > seconds:

        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")

        break