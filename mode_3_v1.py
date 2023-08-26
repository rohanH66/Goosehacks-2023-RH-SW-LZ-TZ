import tkinter as tk
import tkinter.font as font
from PIL import ImageTk
from PIL import Image
from PIL import ImageOps
from border import border_effects
from handle_selector import *
import random
import time
import threading
car_xpos = 257
ypos=0

global t



car1_x=157   #why we adding x position? Road is going horizontal no? -Larry
car2_x=257
car3_x=357

car_y_pos = {
    100, 200, 300, 400
}



def move(event):
    frame_b.place_forget()
    global car_xpos
    temp = event.char
    print(temp)
    if car_xpos == 57:
        if (temp=='d' or temp == 'D'):
            car_xpos += 100
            frame_b.place(x=car_xpos, y=400)
            window.update()
        else:
            frame_b.place(x=car_xpos, y=400)
            window.update()
    elif car_xpos == 457:
        if (temp=='a' or temp == 'A'):
            car_xpos -= 100
            frame_b.place(x=car_xpos, y=400)
            window.update()
        else:
            frame_b.place(x=car_xpos, y=400)
            window.update()
    else:
        if (temp=='a' or temp == 'A'):
            car_xpos -= 100
            frame_b.place(x=car_xpos, y=400)
            window.update()
        elif (temp=='d' or temp == 'D'):
            car_xpos += 100
            frame_b.place(x=car_xpos, y=400)
            window.update()
        else:
            frame_b.place(x=car_xpos, y=400)
            window.update()
    

def car_down(car_frame, xpos):
    
    global ypos
    for x in range(45):
        
        window.update()
        time.sleep(.1)
        car_frame.place(x=xpos, y=ypos)
        window.update()
        ypos+=10
        # print (x)
    ypos = 0

def background_car_crash():
    while ypos != car_y_pos:
        if ypos == car_y_pos:
            
            window.destory()
            break
            print("DONE")
            
        else:
            print("not the same")

t = threading.Thread(target=background_car_crash)

def start():
    t.start()
    frame_a.place_forget()
    
def background_thread():
    global t
    t = threading.Thread(target=background_car_crash)
    t.start()

def mode_3():
    global window
    window = tk.Tk()
    
    #RH = 1920 x 1080p
    #SW = 1280 x 800p
    #SW = 1920 x 1200
    
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    print(width, height)
    
    print(width)
    print(height)
    
    global scalerx
    scalerx = width/1920
    global scalery
    scalery = height/1080
    
    buttonFont = font.Font(size=round(15*scalerx), family="Cambria")
    endFont = font.Font(size=round(20*scalerx), family="Cambria")
    titleFont = font.Font(size = round(18*scalerx), family="Cambria")
    window.title("Mode 3")
    window.state('zoomed')
    
    road = Image.open("four_lane.png")
    wth, hgt = road.size
    road = road.resize((round(wth * scalerx), round(hgt * scalery)))
    
    test = ImageTk.PhotoImage(road)

    backgroundimg = tk.Label(image=test)
    backgroundimg.image = test

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

    

    

    

    button1 = tk.Button(
        master=frame_a,
        text="Click me to start!",
        width=round(scalerx*25),
        height=round(scalery*5),
        bg="#266867",
        fg="white",
        font=titleFont,
        command=lambda: t.start()
    )
    button1.pack()
    frame_a.place(x=0,y=0)
   

    player_car=tk.Button(
        master=frame_b,
        text="main car",
        width=round(scalerx*15),
        height=round(scalery*5),
        bg="#266867",
        fg="white",
        font=buttonFont,
        
    )

    player_car.pack()
    frame_b.place(x=car_xpos, y=400)
    window.bind("<Key>", move)

    if ypos == car_xpos:
            window.destory()
    else:
        print("okay")
        window.update()

    car1=tk.Button(
        master=frame_c,
        text="car 1",
        width=round(scalerx*15),
        height=round(scalery*5),
        bg="#266867",
        fg="white",
        font=buttonFont,
    )
    
    car1.pack()
    
    frame_c.place(x=500, y=500)
    car_down(frame_c,car1_x)
    


    car2=tk.Button(
        master=frame_d,
        text="car 2",
        width=round(scalerx*15),
        height=round(scalery*5),
        bg="#266867",
        fg="white",
        font=buttonFont,
        
    )

    car2.pack()
    # frame_c.place(x=car1, y=0)
    car_down(frame_d,car2_x)

    car3=tk.Button(
        master=frame_e,
        text="car 3",
        width=round(scalerx*15),
        height=round(scalery*5),
        bg="#266867",
        fg="white",
        font=buttonFont,
    )

    car3.pack()
    # frame_c.place(x=car1, y=0)
    car_down(frame_e,car3_x)

    t.stop()
    
    window.mainloop()