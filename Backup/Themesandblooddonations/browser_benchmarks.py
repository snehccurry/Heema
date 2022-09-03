import webbrowser
import time
url=input("Enter the URL: ")
no_of_tabs=int(input("Enter the number of tabs you want to open [Enter 0 for auto benchmarking]"))
delay=int(input("Enter the delay for opening a new tab"))
if(no_of_tabs==0):
    for i in range(10000000000000000000000000000000000000000):
        webbrowser.open_new_tab(url)
        time.sleep(delay)
        print(f"{i} tabs opened")
        if(i==5):
            print("passed the OLD END PC benchmarks")
        if(i==50):
            print("passed the LOW  END PC benchmarks")
        if(i==150):
            print("passed the MID  END PC benchmarks")
        if(i==500):
            print("passed the HIGH END PC bechmarks")
        if(i==1500):
            print("passed the HIGHER END PC benchmarks")
        if(i==5000):
            print("passed the EXTREME END PC benchmarks")
        if(i==10000):
            print("passed the ABOVE EXTREME END PC benchmarks")
        if(i==100000000000000):
            print("passed the Quantum Computer benchmarks")
        if(i==10000000000000000000000000000000):
            print("****************   QUANTUM SUPERYMACY REACHED **************** ")
            print("Story doesn't end here")
        if(i==10000000000000000000000000000000000000000):
            print("****************   ENOUGH PERFORMANCE TO BLOW UP THE WORLD  **************** ")
            print("****************   CONGRATUALTIONS YOU HAVE REACHED THE END **************** ")
            print("****************   WITH GREAT POWER COMES GREAT RESPONSIBILITIES **************** ")
            print("****************   MAKE THIS WORLD A BETTER PLACE AND I HAND YOU MY POWERS **************** ")
            print("****************   TASK: CREATE NEW BENCHMARKING APP ICEFIRE **************** ")
elif(no_of_tabs<=10000000000000000000000000000000000000000):
    for i in range(1,no_of_tabs+1,1):
        webbrowser.open_new_tab(url)
        time.sleep(delay)

webbrowser.open_new_tab(url)


