keypress = False
temp_char = ''
def handle_keypress(event):
    global keypress
    global temp_char
    #using event.char to pass in positional argument to call class with event as object
    temp_char = event.char
    # Print the character associated to the key pressed
    # print(temp_char)
    

    
    