import pyautogui

pyautogui.click()
distance = 200
while distance > 0:
	print(distance, 0)
	pyautogui.dragRel(distance, 0, duration = 0.1)
	distance = distance - 25
	print(distance, 0)
	pyautogui.dragRel(0, distance, duration = 0.1)
	distance = distance - 25
	print(distance, 0)
	pyautogui.dragRel(-distance, 0, duration = 0.1)
	distance = distance - 25
	print(distance, 0)
	pyautogui.dragRel(0, -distance, duration = 0.1)