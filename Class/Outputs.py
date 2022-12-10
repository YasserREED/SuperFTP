from datetime import datetime
from os import system, name

# Colors Here
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[31m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'

class Outputs():

    def time():
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        time = now.strftime("%H:%M:%S")
        Date = f"{date} - {time}"
        #return date - time
        return Date

    def logo():
        Outputs.clear()
        print(f'''{BOLD}
       _______________________________
      /                              /
     /        {RED}Super FTP Tool{WHITE}        / 
    /______________________________/
    |________  ___________________|      
    /_____  /||  |							
    |".___."|||  |
    |_______|/|  |
    ||".___."||  /  {BLUE}Twitter {WHITE}:{RED} @YasserREED{WHITE}
    ||_______|| /    
    |_________|/   
             
            	
        ''')

    def front():
        Outputs.clear()
        Outputs.logo()
        print(f"{RED}[REQ] {WHITE} Which Function do you want to use: \n\n")
        print(f"\t{RED}[{WHITE}01{RED}]{WHITE} Check FTP Connection\n")
        print(f"\t{RED}[{WHITE}02{RED}]{WHITE} Anonymous Login Check{YELLOW} [ Hackeble server ]\n")
        print(f"\t{RED}[{WHITE}03{RED}]{YELLOW} EXIT \n\n")

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')