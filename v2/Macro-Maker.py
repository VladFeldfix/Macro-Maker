from SmartConsole import *
import pyautogui
import keyboard
import time

class main:
    # constructor
    def __init__(self):
        # load smart console
        self.sc = SmartConsole("Macro Maker", "1.0")
        
        # set-up main memu
        self.sc.main_menu["RUN"] = self.run

        # get settings
        self.script = self.sc.get_setting("Script Location")

        # make sure script exists
        self.sc.test_path(self.script)

        # display main menu
        self.sc.start()
    
    def run(self):
        # read script
        functions = {}
        functions["MOUSE_POS_SET"] = (self.MOUSE_POS_SET, ("X", "Y"))
        functions["MOUSE_CLICK"] = (self.MOUSE_CLICK, ("BUTTON",))
        functions["MOUSE_DOWN"] = (self.MOUSE_DOWN, ("BUTTON",))
        functions["MOUSE_UP"] = (self.MOUSE_UP, ("BUTTON",))
        functions["KEYBOARD_CLICK"] = (self.KEYBOARD_CLICK, ("BUTTON",))
        functions["KEYBOARD_PRESS"] = (self.KEYBOARD_PRESS, ("BUTTON",))
        functions["KEYBOARD_RELEASE"] = (self.KEYBOARD_RELEASE, ("BUTTON",))
        functions["SLEEP"] = (self.SLEEP, ("SECONDS",))
        functions["SET_ALARM"] = (self.SET_ALARM, ())
        self.sc.run_script(self.script, functions)

        # restart
        self.sc.restart()
    
    def MOUSE_POS_SET(self, arguments):
        try:
            x = int(arguments[0])
            y = int(arguments[1])
            pyautogui.moveTo(x,y)
        except Exception as e:
            self.sc.error(str(e))

    def MOUSE_CLICK(self, arguments):
        try:
            btn = arguments[0]
            pyautogui.click(button=btn)
        except Exception as e:
            self.sc.error(str(e))
    
    def MOUSE_DOWN(self, arguments):
        try:
            btn = arguments[0]
            pyautogui.mouseDown(button=btn)
        except Exception as e:
            self.sc.error(str(e))

    def MOUSE_UP(self, arguments):
        try:
            btn = arguments[0]
            pyautogui.mouseUp(button=btn)
        except Exception as e:
            self.sc.error(str(e))

    def KEYBOARD_CLICK(self, arguments):
        try:
            btn = arguments[0]
            keyboard.press_and_release(btn)
        except Exception as e:
            self.sc.error(str(e))

    def KEYBOARD_PRESS(self, arguments):
        try:
            btn = arguments[0]
            keyboard.press(btn)
        except Exception as e:
            self.sc.error(str(e))
    
    def KEYBOARD_RELEASE(self, arguments):
        try:
            btn = arguments[0]
            keyboard.release(btn)
        except Exception as e:
            self.sc.error(str(e))

    def SLEEP(self, arguments):
        try:
            sec = arguments[0]
            time.sleep(sec)
        except Exception as e:
            self.sc.error(str(e))
    
    def SET_ALARM(self, arguments):
        try:
            self.sc.print("Now setting when your alarm should go off:")
            YYYY = int(self.sc.input("Insert year in 4 digits: [For example: 2023]"))
            MO = int(self.sc.input("Insert month in 2 digits: [For example: 06]"))
            DD = int(self.sc.input("Insert day in 2 digits: [For example: 21]"))
            HH = int(self.sc.input("Insert hour in 2 digits: [For example: 19]"))
            MM = int(self.sc.input("Insert minute in 2 digits: [For example: 45]"))
            self.sc.print("Script will continue at: "+str(YYYY)+"-"+str(MO)+"-"+str(DD)+" "+str(HH)+":"+str(MM))
            while True:
                rn = str(datetime.datetime.now().time())
                if rn >= "%s:%s:00.000000" % (HH,MM) and datetime.datetime(int(YYYY),int(MO),int(DD)).date() == datetime.datetime.now().date():
                    break

        except Exception as e:
            self.sc.error(str(e))
main()