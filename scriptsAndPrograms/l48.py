import pyautogui
pyautogui.size()

width, height = pyautogui.size()
print(width, height)

pyautogui.position()

pyautogui.moveTo(10,10)
pyautogui.moveTo(20,20, duration=1.5)
pyautogui.moveRel(20,0)
pyautogui.moveRel(200,0)
pyautogui.moveRel(200,0)
pyautogui.moveRel(200,0, duration=2)
pyautogui.moveRel(0,-100)
pyautogui.moveRel(0,-100, duration=1)
pyautogui.position()
pyautogui.click(339, 38)
pyautogui.click()


# cmd > python
# import pyautogui
# pyautogui.displayMousePosition()
