import PIL.ImageGrab, keyboard, pyautogui, pyperclip

hex2rgb = lambda rgb: '#' + ''.join(f'{i:02X}' for i in rgb)
print('Press "ctrl + shift + alt" to pick colour on mouse position')
keyboard.wait('ctrl + shift + alt')
rgb = PIL.ImageGrab.grab().load()[pyautogui.position()[0],pyautogui.position()[1]]
print(f"\nrgb{rgb}\n: {hex2rgb(rgb)} copied to the clipboard.")
pyperclip.copy(hex2rgb(rgb))