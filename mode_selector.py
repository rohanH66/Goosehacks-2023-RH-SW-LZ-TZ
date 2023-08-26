import tkinter as tk
import tkinter.font as font
from PIL import ImageTk
from PIL import Image
from PIL import ImageOps
from border import border_effects
from handle_selector import handle_click1, handle_click2, handle_click3, handle_click4, handle_keypress
import time

window = tk.Tk()

def select_mode():
    
    window.title("Using Python 3.11 to Help Improve Reaction Times")
    window.configure(bg='#457373')
    
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    
    window.state('zoomed')
    
    global scalerx
    scalerx = width/1920
    global scalery
    scalery = height/1080
      


    # car = Image.open("car.png")
    # test = ImageTk.PhotoImage(car)

    # backgroundimg = tk.Label(image=test)
    # backgroundimg.image = test

    # # Position image
    # backgroundimg.place(x=0, y=0)

    buttonFont = font.Font(size=round(15), family="Cambria")
    titleFont = font.Font(size = round(25*scalerx), family="Times New Roman")
    frame_z = tk.Frame(master=window, relief=border_effects["raised"], borderwidth=7)
    frame_y= tk.Frame(master=window, relief=border_effects["raised"], borderwidth=7)
    frame_x = tk.Frame(master=window, relief=border_effects["raised"], borderwidth=7)
    frame_w = tk.Frame(master=window, relief=border_effects["raised"], borderwidth=7)

    frame_a = tk.Frame(master=window, relief=border_effects["raised"], borderwidth=7)
    frame_b = tk.Frame(master=window, relief=border_effects["raised"], borderwidth=7)
    frame_c = tk.Frame(master=window, relief=border_effects["raised"], borderwidth=7)
    frame_d = tk.Frame(master=window, relief=border_effects["raised"], borderwidth=7)
    frame_title = tk.Frame(master=window, borderwidth=7)

    title = tk.Label(
        master=frame_title,
        text="Using Python 3.11 to Help Improve Reaction Times",
        fg="white",  # Set the text color to white
        bg="#7C4935",  # Set the background color to black
        width=round(45),
        height=round(2),
        font=titleFont
    )
    title.pack()
    
    button1 = tk.Button(
        master=frame_a,
        text="Mode 1: \nReaction Speed (click)",
        width=round(37*scalerx),
        height=round(5*scalery),
        bg="#355C7D",
        fg="white",
        font=buttonFont,
        command = lambda : destroy_window(frame_a, frame_b, frame_c, frame_d, frame_z, frame_y, frame_x, frame_w,window)
    )
    
    button2 = tk.Button(
        master=frame_b,
        text="Mode 2:\nAim Trainer \n(Short-Term Memory): 200ms",
        width=round(37*scalerx),
        height=round(5*scalery),
        bg="#355C7D",
        fg="white",
        font=buttonFont,
        command = lambda : destroy_window(frame_a, frame_b, frame_c, frame_d, frame_z, frame_y, frame_x, frame_w, window)
    )
    
    button3 = tk.Button(
        master=frame_c,
        text="Mode 3: \nDirection Based (Keyboard) \n(Short-Term Memory)",
        width=round(37*scalerx),
        height=round(5*scalery),
        bg="#355C7D",
        fg="white",
        font=buttonFont,
        command = lambda : destroy_window(frame_a, frame_b, frame_c, frame_d, frame_z, frame_y, frame_x, frame_w, window)
    )
    
    button4 = tk.Button(
        master=frame_d,
        text="Mode 4: tbd",
        width=round(37*scalerx),
        height=round(5*scalery),
        bg="#355C7D",
        fg="white",
        font=buttonFont,
        command = lambda : destroy_window(frame_a, frame_b, frame_c, frame_d, frame_z, frame_y, frame_x, frame_w, window)
    )

    button5 = tk.Button(
        master=frame_z,
        text="Mode 2: (200ms)",
        width=round(37*scalerx),
        height=round(5*scalery),
        bg="#355C7D",
        fg="white",
        font=buttonFont,
        command = lambda : destroy_window(frame_a, frame_b, frame_c, frame_d, frame_z, frame_y, frame_x, frame_w, window)
    )
    button6 = tk.Button(
        master=frame_y,
        text="Mode 2: (250ms)",
        width=round(37*scalerx),
        height=round(5*scalery),
        bg="#355C7D",
        fg="white",
        font=buttonFont,
        command = lambda : destroy_window(frame_a, frame_b, frame_c, frame_d, frame_z, frame_y, frame_x, frame_w, window)
    )
    button7 = tk.Button(
        master=frame_x,
        text="Mode 2: (300ms)",
        width=round(37*scalerx),
        height=round(5*scalery),
        bg="#355C7D",
        fg="white",
        font=buttonFont,
        command = lambda : destroy_window(frame_a, frame_b, frame_c, frame_d, frame_z, frame_y, frame_x, frame_w, window)
    )
    button8 = tk.Button(
        master=frame_w,
        text="Mode 2: (350ms)",
        width=round(37*scalerx),
        height=round(5*scalery),
        bg="#355C7D",
        fg="white",
        font=buttonFont,
        command = lambda : destroy_window(frame_a, frame_b, frame_c, frame_d, frame_z, frame_y, frame_x, frame_w,window)
    )
    
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    button8.pack()
    
    
    frame_a.place(x=round(10*scalerx), y=round(100*scalery))
    frame_b.place(x=round(10*scalerx), y=round(325*scalery))
    frame_c.place(x=round(10*scalerx), y=round(550*scalery))
    frame_d.place(x=round(10*scalerx), y=round(775*scalery))

    frame_w.place(x=round(600*scalerx), y=round(100*scalery))
    frame_x.place(x=round(600*scalerx), y=round(325*scalery))
    frame_y.place(x=round(600*scalerx), y=round(550*scalery))
    frame_z.place(x=round(600*scalerx), y=round(775*scalery))
    
    
    button1.bind("<Button-1>", handle_click1)
    button2.bind("<Button-1>", handle_click2)
    button3.bind("<Button-1>", handle_click3)
    button4.bind("<Button-1>", handle_click4)
    button5.bind("<Button-1>", handle_click1)
    button6.bind("<Button-1>", handle_click2)
    button7.bind("<Button-1>", handle_click3)
    button8.bind("<Button-1>", handle_click4)
    
    window.bind("<Key>", handle_keypress)
    
    window.mainloop()

def destroy_window(a, b, c, d,e,f,g,h, win):
    time.sleep(0.01)    
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    e.destroy()
    f.destroy()
    g.destroy()
    h.destroy()
    window.destroy()