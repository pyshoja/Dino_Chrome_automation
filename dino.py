import pyautogui
def dino():
    while True:
        pxl=pyautogui.pixelMatchesColor
        cactus=pxl(920,220,(83,83,83,1))
        bird=pxl(890,188,(83,83,83,1))
        if cactus:
            pyautogui.press('up')
            continue
        elif bird:
            pyautogui.keyDown('down')
            pyautogui.keyDown('down')
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')
            #dino()

dino()
