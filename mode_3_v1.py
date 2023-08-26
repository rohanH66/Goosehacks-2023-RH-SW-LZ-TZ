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

end = False
car_xpos = 240
ypos = 0

car_thread = ''
overallxpos = 0

car1_x=0  #why we adding x position? Road is going horizontal no? -Larry
car2_x=0
car3_x=0

importedscalerx = 0
importedscalery = 0

car_y_pos = {
    100, 200, 300, 400
}

def move(event):
    global importedscalerx
    global importedscalery
    importedscalerx = float(importedscalerx)
    importedscalery = float(importedscalery)
    frame_b.place_forget()
    global car_xpos
    temp = event.char
    # print(temp)
       
    if car_xpos == 75:
        if (temp=='d' or temp == 'D'):
            car_xpos += 165
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
        else:
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
    
    elif car_xpos == 240:
        if (temp=='d' or temp == 'D'):
            car_xpos = 388
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
        elif (temp=='a' or temp == 'A'):
            car_xpos = 75
            frame_b.place(x=car_xpos, y=round(importedscalery*650))
            window.update()
        else:
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
    
    elif car_xpos == 388:
        if (temp=='d' or temp == 'D'):
            car_xpos = 533
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
        elif (temp=='a' or temp == 'A'):
            car_xpos = 240
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
        else:
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
    
    elif car_xpos == 533:
        if (temp=='d' or temp == 'D'):
            car_xpos = 686
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
        elif (temp=='a' or temp == 'A'):
            car_xpos = 388
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
        else:
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
    elif car_xpos == 686:
        
        if (temp=='a' or temp == 'A'):
            car_xpos = 533
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
        else:
            frame_b.place(x=round(importedscalerx*car_xpos), y=round(importedscalery*650))
            window.update()
    else:
        frame_b.place(x=car_xpos, y=650)
        window.update()
    # print(car_xpos)
    

def car_down(car_frame, xpos, xscaler, yscaler):
    global end
    global ypos
    global overallxpos
    overallxpos = xpos
    if end != True:
        for x in range(round(yscaler*68)):
            window.update()
            time.sleep(.1)
            car_frame.place(x=round(xpos*xscaler), y=round(ypos*yscaler))
            window.update()
            ypos += round(yscaler*10)
            
            # print (x)
            
            # following lines r for hit registration
            if(650 - round(yscaler * 5) < ypos < 650 + round(yscaler * 5) and (car_xpos - round(xscaler*15)) < xpos < (car_xpos + round(xscaler*15))):
                frame_b.place_forget()
                frame_c.place_forget()
                frame_d.place_forget()
                frame_e.place_forget()
                car_frame.place_forget()
                
                end = True
                
                end_frame.place(x=250, y=250)
                break
    else:
        pass
            
            
            
            
            
    ypos = 0
    car_frame.place_forget()

def get_scalers():
    with open ("window.txt", "r") as windows:
        temp = windows.readline()
        return temp.split(",")

def mode_3():

    global car1_x
    global car2_x
    global car3_x
    
    global importedscalerx
    global importedscalery
    global window
    window = tk.Tk()
    
    importedscalerx, importedscalery = get_scalers()
    
    print(importedscalerx, importedscalery)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    print(width, height)
    
    print(width)
    print(height)
    
    scalerx = width/1920
    scalery = height/1080
    
    car1_x = 75 * scalerx  #why we adding x position? Road is going horizontal no? -Larry
    car2_x = 240 * scalerx
    car3_x = 392 * scalerx

    #RH = 1920 x 1080p
    #SW = 1280 x 800p
    #SW = 1920 x 1200
    
    buttonFont = font.Font(size=round(15*scalerx), family="Cambria")
    endFont = font.Font(size=round(20*scalerx), family="Cambria")
    titleFont = font.Font(size = round(18*scalerx), family="Cambria")
    
    endButtonFont = font.Font(size=round(15* scalerx), family="Cambria")
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
    global end_frame
    end_frame = tk.Frame(master=window, relief=border_effects["groove"], borderwidth=5)
            
            
    end_button=tk.Button (
        master=end_frame,
        text = "Oops, you have colided",
        width=round(scalerx*30),
        height=round(scalery*5),
        bg="#ff0000",
        fg="white",
        font=buttonFont,
        command = lambda : window.destroy(),
    )
    
    end_button.pack()       
   

    player_car=tk.Button(
        master=frame_b,
        text="main car",
        width=round(scalerx*10),
        height=round(scalery*3),
        bg="#266867",
        fg="white",
        font=buttonFont,
        
    )

    player_car.pack()
    frame_b.place(x=round(car_xpos * scalerx), y=round(650*scalery))
    window.bind("<Key>", move)

    

    car1=tk.Button(
        master=frame_c,
        text="Car 1!",
        width=round(scalerx*10),
        height=round(scalery*3),
        bg="#266867",
        fg="white",
        font=buttonFont,
    )
    
    car1.pack()
    
    
    car_down(frame_c,car1_x, scalerx, scalery)
    


    car2=tk.Button(
        master=frame_d,
        text="Car 2!",
        width=round(scalerx*10),
        height=round(scalery*3),
        bg="#266867",
        fg="white",
        font=buttonFont,
        
    )

    car2.pack()
    # frame_c.place(x=car1, y=0)
    car_down(frame_d,car2_x, scalerx, scalery)

    car3=tk.Button(
        master=frame_e,
        text="Car 3!",
        width=round(scalerx*9),
        height=round(scalery*3),
        bg="#266867",
        fg="white",
        font=buttonFont,
    )

    car3.pack()
    # frame_c.place(x=car1, y=0)
    car_down(frame_e,car3_x, scalerx, scalery)
    
    

    
    
    window.mainloop()