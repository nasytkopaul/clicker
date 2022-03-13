import time, threading, keyboard, pyautogui
from pynput import keyboard as pkeyboard

def ExitProgram():
    def OnPress(key):        
        if str(key) == 'Key.esc':
            
            main.stat = 'pause'
            UsInput = input('Пауза, продолжаем? (y/n): ')

            while UsInput != 'y' and UsInput != 'n' and UsInput != 'Y' and UsInput != 'N':
                UsInput = input('Только  "y", "Y", "n" or "N": ')

            if UsInput == 'y' or UsInput == 'Y':
                ti = 1
                print("Успей навести на кнопку, даю тебе 5 сек 😊")
                while True:
                    if ti < 6:
                        print(ti)
                        ti += 1
                        time.sleep(1)
                    else:
                        main.stat = 'start'
                        break
                

            elif UsInput == 'n' or UsInput == 'N':
                main.stat = 'close'
                exit()

    with pkeyboard.Listener(on_press=OnPress) as listener:
        listener.join()


def main():
    main.stat = '0'
    main.count = 0

    print('Меню')
    print('Старт - Кнопка "1"')
    print('Стоп - Кнопка "Esc"')
    print('Жду')
    main.stat = 'start'

    while True:
        if keyboard.is_pressed('1'):
            while True:
                if keyboard.is_pressed('esc'):
                    main.stat = 'wait'
                    break

                if main.stat == 'start':
                    pyautogui.click()

                    main.count += 1
                    print("Click", main.count)
                    
                    time.sleep(0.2)

                while main.stat == 'pause':
                    time.sleep(1)

                if main.stat == 'close':
                    break


        if keyboard.is_pressed('esc') or main.stat == 'close':
            main.stat = 'pause'
            print('Закрываю')
            break

threading.Thread(target=main).start()
threading.Thread(target=ExitProgram).start()