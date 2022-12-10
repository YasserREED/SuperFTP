from Class.Outputs import *
from Class.Check import *


#Colors Here
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED   = '\033[91m'
print('\033[1m')

Outputs.front()

choose = str(input(f"{RED}[REQ] {WHITE} Please Enter number Ex => [ {YELLOW}1{WHITE} or {YELLOW}2{WHITE} ] : ")).lower()
match choose:
    
    case "1":      
        Check.checkStatus()
    
    case "2":
        Check.anonymous()
       
    case "3":
        print(f'\n\t{BOLD}{RED}[EXIT] {WHITE} Happy to help you, Bye!\n')
        quit()
        
    case _:
        print(f"\n\t{RED}[WARN]{WHITE} Please Dont use [{YELLOW} {choose} {WHITE}]\n")
        print(f"\t{GREEN}[INFO]{WHITE} Please use numbers from [ {YELLOW}1 {WHITE}to {YELLOW}3 {WHITE}]\n")