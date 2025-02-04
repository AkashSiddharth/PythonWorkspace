import os

class Font:
    @staticmethod
    def set_style(f_style, fcolor, bcolor = "black"):
        style = {
            "NORMAL": "\033[0m",
            "BOLD": "\033[1m",
            "FAINT": "\033[2m",
            "ITALIC": "\033[3m",
            "UNDERLINE": "\033[4m",
            "BLINK": "\033[5m",
            "NEGATIVE": "\033[7m",
            "STRIKE": "\033[9m"
        }

        fgcolor = {
            "BLACK": "\033[0;30m",
            "RED": "\033[0;31m",
            "GREEN": "\033[0;32m",
            "BROWN": "\033[0;33m",
            "BLUE": "\033[0;34m",
            "PURPLE": "\033[0;35m",
            "CYAN": "\033[0;36m",
            "LIGHT_GRAY": "\033[0;37m",
            "DARK_GRAY": "\033[1;30m",
            "LIGHT_RED": "\033[1;31m",
            "LIGHT_GREEN": "\033[1;32m",
            "YELLOW": "\033[1;33m",
            "LIGHT_BLUE": "\033[1;34m",
            "LIGHT_PURPLE": "\033[1;35m",
            "LIGHT_CYAN": "\033[1;36m",
            "LIGHT_WHITE": "\033[1;37m"
        }

        bgcolor = {
            "BLACK": "\033[40m",
            "RED": "\033[41m",
            "GREEN": "\033[42m",
            "BROWN": "\033[43m",
            "BLUE": "\033[44m",
            "MAGENTA": "\033[45m",
            "CYAN": "\033[46m",
            "GRAY": "\033[47m"
        }

        code = "{0}{1}{2}".format(style[f_style.upper()], 
                                 fgcolor[fcolor.upper()], 
                                 bgcolor[bcolor.upper()])

        return code
    
    @staticmethod
    def end_style():
        END_FONT_STYLE = "\033[0m"
        return END_FONT_STYLE

class Banners:
    @staticmethod
    def title_banner() -> None:
        banner = """
            ___________.__         ___________               ___________            
            \__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  
              |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
              |    |   |  \  \___    |    |   / __ \\  \___     |    |(  <_> )  ___/ 
              |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >
                               \/                 \/     \/                      \/ 
        """
        print("\t\t{0}{1}{2}\n\n".format(Font.set_style("BLINK", "LIGHT_BLUE"), banner, Font.end_style()))

    @staticmethod
    def winner_banner() -> None:
        banner = """
            _________                                     __           ._._._.
            \_   ___ \  ____   ____    ________________ _/  |_  ______ | | | |
            /    \  \/ /  _ \ /    \  / ___\_  __ \__  \\   __\/  ___/ | | | |
            \     \___(  <_> )   |  \/ /_/  >  | \// __ \|  |  \___ \   \|\|\|
             \______  /\____/|___|  /\___  /|__|  (____  /__| /____  >  ______
                    \/            \//_____/            \/          \/   \/\/\/
        """
        print("\t\t{0}{1}{2}\n\n".format(Font.set_style("BLINK", "LIGHT_GREEN"), banner, Font.end_style()))

    @staticmethod
    def game_draw_banner() -> None:
        banner = """
             ________                        ________                       
            /  _____/_____    _____   ____   \______ \____________ __  _  __
           /   \  ___\__  \  /     \_/ __ \   |    |  \_  __ \__  \\ \/ \/ /
           \    \_\  \/ __ \|  Y Y  \  ___/   |    `   \  | \// __ \\     / 
            \______  (____  /__|_|  /\___  > /_______  /__|  (____  /\/\_/  
                    \/     \/      \/     \/          \/           \/            
        """
        print("\t\t{0}{1}{2}\n\n".format(Font.set_style("BLINK", "LIGHT_PURPLE"), banner, Font.end_style()))
        

class Utility:
    @staticmethod
    def clear() -> None:
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')
