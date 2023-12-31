import tkinter as tk
import tkinter.font as font
from PIL import ImageTk
from PIL import Image
from PIL import ImageOps
from border import border_effects, arrows, options, key, keys
from handle_selector import *
import random
import time
import sys
from handle_mode_2 import handle_keypress, keypress, temp_char
import keyboard

count = 0         #to count how many you have attempted
correct = 0       #to count how many you have pressed correct
temp_start = 0    #temporary star and temporary end to calculate reaction time
temp_end = 0
_sum = 0          #it is a sum of all reaction times to calculate average

overall_time = 0.3 #this is the reaction time required of this mode

def destroy_window(win):  #function to destroy the window 
    time.sleep(0.01)    
    window.destroy()

def get_keypress():
    temp = keyboard.read_key()   #function to read the key the user has pressed
    if temp in keys:
        return temp
def ask_question(value):
    global correct
    key_from_user = get_keypress()
    
    #get word value for character through key dictionary
    try:
        if value == key[key_from_user]:
            correct += 1                                                  #if value matches the user imput key, increase correct number
            button7.config(text=f"Total: {correct} / {count + 1}")
            window.update()                                             #updates percentage correct button
            return None
        else:
            button7.config(text=f"Total: {correct} / {count + 1}")
            window.update()
    except KeyError:
        
        button7.config(text=f"Total: {correct} / {count + 1}")
        window.update()
        return None
   
    # use timeout and while loop to integrate function in handle_mode_two to set bool to true if keypress given (prompt until valid option, have exit button avalible as well)

def start_time():
    start_time = time.time()
    return start_time
def end_time():                #calculates user reaction times
    end_time = time.time()
    return end_time

def start():
    global overall_time
    frame_a.place_forget()        #forgets the start buttons that display instruction
    frame_b.place_forget()
    window.update()
    temp_val = random.choice(options)        #gets a value between 0 and 2 inclusive
    # print(temp_val)
    button3.config(text=f"{arrows[temp_val]}")  #prints out the arrow on the button. The arrow it prints out corresponds to each of the temp_val
    window.update()
    time.sleep(random.randint(3,5))        #choses random waiting time
    temp_start = start_time()
    frame_c.place(x=round(scalerx * random.randint(0,1500)), y=round(scalery * random.randint(0,475)))
    window.update()
    
    time.sleep(overall_time)
    window.update()
    
    frame_c.place_forget()    #forges the click me button
    window.update()
    frame_f.place(x=round(scalerx*600), y=round(scalery*50))
    window.update()                #displays intructions
    ask_question(temp_val)
    frame_f.place_forget()       #removes instructions
    rapid_click()
    
def rapid_click():
    global temp_start
    global temp_end
    global count
    global _sum
    
    temp_end = end_time()
    total = temp_end - temp_start        #calculates the time taken to press the button
    
    if count != 0:
        # print(total)
        _sum += total
        # print(_sum, "sum")    #just for trouble shooting purposes
   
    if count < 9: 
        count+=1         #increase the number of attempted
        # print(count)
        
        if count != 1:
            if (total * 1000) < 1000:
                button5.config(text=f"Count: {count}\nCurrent:\n{round((total * 1000) , 2)} ms")
            else:
                button5.config(text=f"Count: {count}\nCurrent:\n{round(total, 2)} s")      #displays the current time with unit milisecond
        else:
            button5.config(text=f"Count: {count}")      #displays
        
        window.update()
        
        #spawns button
        xval = random.randint(0,1500)   #spawns button
        yval = random.randint(0,475)
        
        temp_val = random.choice(options)
        # print(temp_val)
        button3.config(text=f"{arrows[temp_val]}")  
        
        #randomly choses which arrow to display

        window.update()
        time.sleep(random.randint(1,5))
        window.update()
        temp_start = start_time()
        frame_c.place(x=round(scalerx*xval), y=round(scalery*yval))
        window.update()
        #picks random time to spawn the button in randome position

        time.sleep(overall_time)
        window.update()
        
        frame_c.place_forget()     #forgets the click me button
        window.update()
        frame_f.place(x=round(scalerx*600), y=round(scalery*50))
        window.update()
        ask_question(temp_val)
        frame_f.place_forget() #removes the instructions
        rapid_click()

    else:
        count+=1
        button5.config(text=f"Count: {count}\nCurrent:\n{round((total * 1000) , 2)} ms")
        frame_g.place_forget()       
        button4.config(text=f"Your average reaction time is {round(((_sum/9) * 1000), 3)} ms. \n Your total correct is {correct} / {count} \nClick to Close.")
        window.update()
        frame_d.place(x=round(scalerx*350),y=round(scalery*160))
        frame_c.place_forget()

        #display end result

def mode_two_v3():
    global window
    window = tk.Tk()
    
    #RH = 1920 x 1080p
    #SW = 1280 x 800p
    #SW = 1920 x 1200
    #lz =1280 x 720
    
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    
    # print(width)
    # print(height)

    global scalerx
    scalerx = width/1920
    global scalery
    scalery = height/1080
    
    #variables to adjust the ratios due to people having different screen resolution and size 

    buttonFont = font.Font(size=round(15*scalerx), family="Cambria")
    arrowFont = font.Font(size=round(19*scalerx), family="Cambria", weight="bold")
    endFont = font.Font(size=round(20*scalerx), family="Cambria")
    titleFont = font.Font(size = round(18*scalerx), family="Cambria")

    #initiate all the fonts
    
    window.title("Mode 2 (300 ms Test)")
    
    window.state('zoomed')
    
    car = Image.open("car.png")
    wth, hgt = car.size
    car = car.resize((round(wth * scalerx), round(hgt * scalery)))
    
    test = ImageTk.PhotoImage(car)

    backgroundimg = tk.Label(image=test)
    backgroundimg.image = test

    #sets the background pic

    # Position image
    backgroundimg.place(x=0, y=0)
    global frame_a
    frame_a = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=5)
    
    global frame_b
    frame_b = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=7)
    
    global frame_c
    frame_c = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=7)
    
    global frame_d
    frame_d = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=7)
    
    global frame_e
    frame_e = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=7)
    
    global frame_f
    frame_f = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=7)
    
    global frame_g
    frame_g = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=7)
    
    frame_h = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=7)

    #sets various frames for various buttons for later use
    
    # greeting.place(x=0, y=0)
    frame_a.place(x=round(scalerx*800), y=round(scalery*400))

    global button3
    button3 = tk.Button(
        master=frame_c,
        width=round(35*scalerx),
        height=round(7*scalery),
        bg="red",
        fg="white",
        text="Click Me!",
        font=arrowFont,
        
    )
    button3.pack()

    button1 = tk.Button(
        master=frame_a,
        text="Click me to start!",
        width=round(scalerx*25),
        height=round(scalery*5),
        bg="#2F5D8C",
        fg="white",
        font=buttonFont,
        command=lambda: start()
    )
    button1.pack()
    
    button2=tk.Button(
        master=frame_b,
        width=round(85),
        height=round(scalery*8),
        bg="#2F5D8C",
        fg="white",
        font=titleFont,
        text="Directions:\nThis module tests your peripheral vision and your reaction speed from stilmuli at your peripheral \n vision. For the test to be accurate, please keep your eyes at center of the screen. \n\nClick to continue. (300 ms Test)",
        justify='center',
        command=lambda: frame_b.place_forget()
    )  
       
    frame_b.place(x=round(20*scalerx), y=round(10*scalery))
    button2.pack()

    global button4
    button4 = tk.Button(
        master=frame_d,
        width=round(75),
        height=round(scalery * 8),
        bg="#2F5D8C",
        fg="white",
        font=endFont,
        text=f"Your average reaction time is {round((_sum/9) * 1000, 4)} ms. Click to Close.",
        command=lambda: destroy_window(window)
    )  
    button4.pack()
    
    global button5
    button5 = tk.Label(
        master=frame_e,
        width=round(15 * scalerx),
        height=round(5 * scalery),
        bg="#2F5D8C",
        fg="white",
        font=endFont,
        text=f"Count: {count}"
    )
    frame_e.place(x=round(scalerx*50), y=round(scalery*720))
    #sets the other values and aspects of buttons
    
    button5.pack()
    
    global button6
    button6 = tk.Label(
        master=frame_f,
        width=round(90 * scalerx),
        height=round(8* scalery),
        bg="#2F5D8C",
        fg="white",
        font=titleFont,
        text=f"Enter the key on your keyboard that corresponds with the arrow shown \n 'A' = Left 'D' = Right 'W' = Up \n(if you do not know, just guess)"
    )
    button6.pack()
    #sets the values of buttons
    
    window.bind("<Key>", handle_keypress)
    #connects keypress to a function
    
    button5.pack()
    
    global button7
    button7 = tk.Label(
        master=frame_g,
        width=round(14 * scalerx),
        height=round(5* scalery),
        bg="#2F5D8C",
        fg="white",
        font=titleFont,
        text=f"Total: {correct} / {count}"
    )
    frame_g.place(x=round(scalerx*1700), y=round(scalery*750))

    button7.pack()
    
    global button8
    button8 = tk.Button(
        master=frame_h,
        width=round(7 * scalerx),
        height=round(3* scalery),
        bg="#2F5D8C",
        fg="white",
        font=buttonFont,
        text="Exit",
        command = lambda : destroy_window(window)
    )
    button8.pack()
    frame_h.place(x=round(1450*scalerx),y=round(710*scalery))
    
    #set various buttons
    
    window.mainloop()