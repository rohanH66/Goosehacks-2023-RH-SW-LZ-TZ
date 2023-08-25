button_one = False
button_two = False
button_three = False
button_four = False

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

def handle_click1(event):
    global button_one
    button_one = True
    print("Button 1 was clicked!")
    print(button_one)
def handle_click2(event):
    global button_two
    print("Button 2 was clicked!")
    button_two = True
def handle_click3(event):
    global button_three
    print("Button 3 was clicked!")
    button_three = True
def handle_click4(event):
    global button_four
    print("Button 4 was clicked!")
    button_four = True
    

    

    

    