keypress = False
temp_char = ''
def handle_keypress(event):
    global keypress
    global temp_char
    temp_char = event.char
    # Print the character associated to the key pressed
    print(temp_char)
    

    
    