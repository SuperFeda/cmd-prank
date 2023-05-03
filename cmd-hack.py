import os, pyautogui, time

os.system("start cmd") # Открываем окно командной строки
time.sleep(0.5) # Ждем, пока окно загрузится
pyautogui.press("f11") # Нажимаем F11, чтобы перевести окно в полноэкранный режим
time.sleep(0.2) # Ждем, пока окно переключится в полноэкранный режим
pyautogui.typewrite("color 2\n") # Вводим команду "color 2"
time.sleep(0.2) # Ждем, пока команда выполнится
pyautogui.typewrite("dir/s\n") # Вводим команду "dir/s"
time.sleep(0.2) # Ждем, пока команда выполнится