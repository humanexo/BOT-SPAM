
import pyautogui
import time

print("¿Mensaje?")
mensaje = str(input())
print("¿Veces?")
n = int(input())

time.sleep(3)
for i in range(n):
    pyautogui.typewrite(mensaje)
    pyautogui.press("enter")
    

