import os, pyautogui, time

os.system("start cmd")                 # Открываем окно командной строки                             ///      Open a command line window
time.sleep(0.5)                        # Ждем, пока окно загрузится                                  ///      Wait for the window to load
pyautogui.press("f11")                 # Нажимаем F11, чтобы перевести окно в полноэкранный режим    ///      Press F11 to put the window in full screen mode
time.sleep(0.2)                        # Ждем, пока окно переключится в полноэкранный режим          ///      Wait for the window to switch to full screen mode
pyautogui.typewrite("color 2\n")       # Вводим команду "color 2"                                    ///      Enter command "colour 2"
time.sleep(0.2)                        # Ждем, пока команда выполнится                               ///      Waiting for the command to execute
pyautogui.typewrite("dir/s\n")         # Вводим команду "dir/s"                                      ///      Enter the command "dir/s"
time.sleep(0.2)                        # Ждем, пока команда выполнится                               ///      Waiting for the command to execute
