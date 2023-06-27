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
        self.sc.add_main_menu_item("RUN", self.run)
        self.sc.add_main_menu_item("EDIT LIST", self.edit_list)
        self.sc.add_main_menu_item("EDIT SCRIPT", self.edit_script)

        # get settings
        self.script = self.sc.get_setting("Script Location")

        # make sure script exists
        self.sc.test_path(self.script)
        self.sc.test_path("List.csv")

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
        functions["INPUT"] = (self.INPUT, ("PROMPT",))
        functions["LOOP"] = (self.LOOP, ("CYCLES",))
        functions["END_LOOP"] = (self.END_LOOP, ())
        functions["KEYBOARD_WRITE"] = (self.KEYBOARD_WRITE, ("TEXT",))
        self.script_input = ""
        self.looping_cycles = ""
        self.list_of_loop_commands = []
        self.looping_activated = False
        self.sc.run_script(self.script, functions)
        self.list_row = ""

        # restart
        self.sc.restart()
    
    def edit_list(self):
        os.popen("List.csv")
        # restart
        self.sc.restart()
    
    def edit_script(self):
        os.popen(self.script)
        # restart
        self.sc.restart()
    
    def MOUSE_POS_SET(self, arguments):
        try:
            if not self.looping_activated:
                x = int(arguments[0])
                y = int(arguments[1])
                pyautogui.moveTo(x,y)
            else:
                self.list_of_loop_commands.append((self.MOUSE_POS_SET,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))

    def MOUSE_CLICK(self, arguments):
        try:
            if not self.looping_activated:
                btn = arguments[0]
                pyautogui.click(button=btn)
            else:
                self.list_of_loop_commands.append((self.MOUSE_CLICK,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))
    
    def MOUSE_DOWN(self, arguments):
        try:
            if not self.looping_activated:
                btn = arguments[0]
                pyautogui.mouseDown(button=btn)
            else:
                self.list_of_loop_commands.append((self.MOUSE_DOWN,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))

    def MOUSE_UP(self, arguments):
        try:
            if not self.looping_activated:
                btn = arguments[0]
                pyautogui.mouseUp(button=btn)
            else:
                self.list_of_loop_commands.append((self.MOUSE_UP,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))

    def KEYBOARD_CLICK(self, arguments):
        try:
            if not self.looping_activated:
                btn = arguments[0]
                keyboard.press_and_release(btn)
            else:
                self.list_of_loop_commands.append((self.KEYBOARD_CLICK,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))

    def KEYBOARD_PRESS(self, arguments):
        try:
            if not self.looping_activated:
                btn = arguments[0]
                keyboard.press(btn)
            else:
                self.list_of_loop_commands.append((self.KEYBOARD_PRESS,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))
    
    def KEYBOARD_RELEASE(self, arguments):
        try:
            if not self.looping_activated:
                btn = arguments[0]
                keyboard.release(btn)
            else:
                self.list_of_loop_commands.append((self.KEYBOARD_RELEASE,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))
    
    def KEYBOARD_WRITE(self, arguments):
        try:
            if not self.looping_activated:
                text = arguments[0]
                text = text.split("#")
                if text[0].upper() == "LSTVAL":
                    keyboard.write(self.list_row[int(text[1])])
                else:
                    keyboard.write(int(text[0]))
            else:
                self.list_of_loop_commands.append((self.KEYBOARD_WRITE,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))

    def SLEEP(self, arguments):
        try:
            if not self.looping_activated:
                sec = arguments[0]
                self.sc.print("Waiting for "+sec+" seconds...")
                sec = int(sec)
                time.sleep(sec)
            else:
                self.list_of_loop_commands.append((self.SLEEP,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))
    
    def SET_ALARM(self, arguments):
        try:
            if not self.looping_activated:
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
            else:
                self.list_of_loop_commands.append((self.SET_ALARM,arguments))

        except Exception as e:
            self.sc.fatal_error(str(e))
    
    def INPUT(self, arguments):
        try:
            if not self.looping_activated:
                text = arguments[0]
                self.script_input = self.sc.input(text)
            else:
                self.list_of_loop_commands.append((self.INPUT,arguments))
        except Exception as e:
            self.sc.fatal_error(str(e))
    
    def LOOP(self, arguments):
        try:
            self.looping_cycles = arguments[0]
            if self.looping_cycles.upper() != "LIST":
                self.looping_cycles = int(self.looping_cycles)
            else:
                self.looping_cycles = "LIST"
            self.looping_activated = True
        except Exception as e:
            self.sc.fatal_error(str(e))
    
    def END_LOOP(self, arguments):
        try:
            self.looping_activated = False
            if self.looping_cycles != "LIST":
                i = 0
                self.looping_cycles = int(self.looping_cycles)
                while i < self.looping_cycles:
                    i += 1
                    for command_args in self.list_of_loop_commands:
                        command = command_args[0]
                        args = command_args[1]
                        command(args)
            else:
                file = open("List.csv", 'r')
                lines = file.readlines()
                file.close()

                for line in lines:
                    line = line.replace("\n", "")
                    line = line.split(",")
                    self.list_row = line
                    for command_args in self.list_of_loop_commands:
                        command = command_args[0]
                        args = command_args[1]
                        command(args)
        except Exception as e:
            self.sc.fatal_error(str(e))
main()