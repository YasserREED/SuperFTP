from ftplib import FTP
from Class.Outputs import *
import json

# Colors Here
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[31m'
WHITE = '\33[97m'
BOLD = '\033[1m'
BLUE = '\033[36m'
print(BOLD)


# Read the File
IPS = open("List/IP_List.txt", "r")
IPlist = IPS.readlines()

class Check():

    # Anonymous login function
    def anonymous():
        # Data structur for json file
        Data = """
            {
            "IP": "",
            "Anonymous": true,
            "Date": ""
            }
        """
        Outputs.logo()
        loginJSON = open("Files\Login.json", "w")
        loginJSON.write("[")
        loginTXTs = open("Files\SuceessLogin.txt", "a")
        loginTXTs.write(f"\nScan Date : {Outputs.time()}")
        loginTXTf = open("Files\FailLogin.txt", "a")
        loginTXTf.write(f"\nScan Date : {Outputs.time()}")

        for IP in IPlist:
            IP = IP.strip()
            obj = json.loads(Data)
            obj["IP"] = IP
            obj["Date"] = Outputs.time()

            try:
                Success = FTP(IP, timeout=1.4)
                login = Success.login()
                if "230" in login:
                    obj["Anonymous"] = True
                    print(
                        f"{GREEN}[INFO] Success \t {WHITE} | {YELLOW}{IP} {GREEN}=> Login Successfully! =D {WHITE}")
                    if IP != IPlist[-1]:
                        loginJSON.write(
                            f"\n{json.dumps(obj, indent = 4)}, \n")
                    else:
                        loginJSON.write(f"\n{json.dumps(obj, indent = 4)} \n")
                    loginTXTs.write(f"\n{IP}")
            except:
                obj["Anonymous"] = False
                print(
                    f"{RED}[ERR] Failed \t {WHITE} | {YELLOW}{IP} {RED}=> Login Failed =({WHITE}")
                if IP != IPlist[-1]:
                    loginJSON.write(f"\n{json.dumps(obj, indent = 4)}, \n")
                else:
                    loginJSON.write(f"\n{json.dumps(obj, indent = 4)} \n")
                loginTXTf.write(f"\n{IP}")
        loginJSON.write("]")
        print(
            f"\n\n \t {YELLOW}[FILE] Please Check {WHITE} Files\Login.json{WHITE}\n\n \t {GREEN}[FILE] Please Check {WHITE} Files\SuceessLogin.txt\n{WHITE}")
        print(
            f"\t {RED}[FILE] Please Check {WHITE} Files\FailLogin.txt\n{WHITE}\t")

    # check FTP status function
    def checkStatus():
        Data = """
            {
            "IP": "",
            "Live": "",
            "Date": ""
            }
        """
        Outputs.logo()
        checkJSON = open("Files\Status.json", "w")
        checkJSON.write("[")
        checkTXTs = open("Files\SuceessCheck.txt", "a")
        checkTXTs.write(f"\nScan Date : {Outputs.time()}")
        checkTXTf = open("Files\FailCheck.txt", "a")
        checkTXTf.write(f"\nScan Date : {Outputs.time()}")

        for IP in IPlist:
            IP = IP.strip()
            obj = json.loads(Data)
            obj["IP"] = IP
            obj["Date"] = Outputs.time()

            try:
                Success = FTP(IP, timeout=1.4)
                obj["Live"] = True
                print(
                    f"{GREEN}[INFO] Success \t  | {YELLOW}{IP} {GREEN} => Find FTP =){WHITE}")
                if IP != IPlist[-1]:
                    checkJSON.write(f"\n{json.dumps(obj, indent = 4)}, \n")
                else:
                    checkJSON.write(f"\n{json.dumps(obj, indent = 4)} \n")
                checkTXTs.write(f"\n{IP}")

            except:
                obj["Live"] = False
                print(
                    f"{RED}[ERR] Failed \t  | {YELLOW}{IP} => {RED}No FTP =( {WHITE}")
                if IP != IPlist[-1]:
                    checkJSON.write(f"\n{json.dumps(obj, indent = 4)}, \n")
                else:
                    checkJSON.write(f"\n{json.dumps(obj, indent = 4)} \n")
                checkTXTf.write(f"\n{IP}")

        checkJSON.write("]")

        print(
            f"\n\n \t {YELLOW}[FILE] Please Check {WHITE} Files\Status.json{WHITE}\n\n \t {GREEN}[FILE] Please Check {WHITE} Files\SuceessCheck.txt\n{WHITE}")
        print(
            f"\t {RED}[FILE] Please Check {WHITE} Files\FailCheck.txt\n{WHITE}\t")
