import tkinter as tk
from PIL import ImageTk
from PIL import Image
from PIL import ImageOps
from mode_selector import select_mode
from mode_1 import mode_one
from mode_2_v1 import mode_two_v1
from mode_2_v2 import mode_two_v2
from mode_2_v3 import mode_two_v3
from mode_2_v4 import mode_two_v4
from mode_3_v1 import mode_3
from border import border_effects
import time

def main():
    select_mode()
    from handle_selector import button_one, button_two, button_three, button_four, button_five, button_six, button_seven, button_eight
    
    try:
        if button_one:
            mode_one()
        elif button_two:
            mode_two_v1()
        elif button_three:
            mode_3()
        elif button_four:
            mode_3()
        elif button_five:
            mode_two_v1()
        elif button_six:
            mode_two_v2()
        elif button_seven:
            mode_two_v3()
        elif button_eight:
            mode_two_v4()
        else:
            print("No Option was Selected")
  
    except tk.TclError:
        print("Closed Window Early")
    print("Completed")
    

if __name__ == '__main__':
    main()


