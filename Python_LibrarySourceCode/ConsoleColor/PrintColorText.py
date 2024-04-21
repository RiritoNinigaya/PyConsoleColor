import ctypes
import os
def ConnectConsoleColorDLL():
    try:
        dllpath = os.path.join(os.path.dirname(__file__), 'resource\\ConsoleColor.dll')
        consdll = ctypes.windll.LoadLibrary(dllpath)
        return consdll
    except:
        raise FileNotFoundError("[CONSOLE_COLOR] Failed to Found ConsoleColor.dll Library!!!")
class PrintColorTxt:
    def printfviaColor(txt : str, r : int, g : int, b : int):
        ConnectConsoleColorDLL().Printfviacolor(txt, r, g ,b)