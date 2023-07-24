import os
import subprocess
import random

def display_logo():
    logo1 = """
.------..------..------..------..------..------..------..------.
|R.--. ||P.--. ||-.--. ||F.--. ||Q.--. ||3.--. ||..--. ||0.--. |
| :(): || :/\: || (\/) || :(): || (\/) || :(): || :(): || :/\: |
| ()() || (__) || :\/: || ()() || :\/: || ()() || ()() || :\/: |
| '--'R|| '--'P|| '--'-|| '--'F|| '--'Q|| '--'3|| '--'.|| '--'0|
`------'`------'`------'`------'`------'`------'`------'`------'

本程序仅供学习、交流,以及合法范围内的测试,切勿用作非法用途,否则一切责任、后果自负.
This program is only for learning, communication, and testing within the legal scope, do not use for illegal purposes, otherwise all responsibilities, consequences.
"""

    logo2 = """
   __    ___        ___  ____ _____  ___  
  /__\  / _ \      / __\/___ \___ / / _ \ 
 / \// / /_)/____ / _\ //  / / |_ \| | | |
/ _  \/ ___/_____/ /  / \_/ / ___) | |_| |
\/ \_/\/         \/   \___,_\|____(_)___/ 

本程序仅供学习、交流,以及合法范围内的测试,切勿用作非法用途,否则一切责任、后果自负.           
This program is only for learning, communication, and testing within the legal scope, do not use for illegal purposes, otherwise all responsibilities, consequences.                               
"""

    logos = [logo1, logo2]
    print(random.choice(logos))

display_logo()


try:
    import _bootlocale
except ImportError:
    pass

def main():
    print("请选择：")
    print("1: RPbasics")
    print("2: RP-foolproof")
    print("3: RP-notsign")
    print("4: RP-letter")
    print("5: RP-Dletter")
    print("6: help")
    current_path = os.path.dirname(os.path.realpath(__file__))

    choice = input("直接输入序号1~6：")

    if choice == '1':
        subprocess.run(["python3", os.path.join(current_path, "RP-basics")])
    elif choice == '2':
        subprocess.run(["python3", os.path.join(current_path, "RP-foolproof")])
    elif choice == '3':
        subprocess.run(["python3", os.path.join(current_path, "RP-notsign")])
    elif choice == '4':
        subprocess.run(["python3", os.path.join(current_path, "RP-letter")])
    elif choice == '5':
        subprocess.run(["python3", os.path.join(current_path, "RP-Dletter")])
    elif choice == '6':
        subprocess.run(["python3", os.path.join(current_path, "instructionbook")])
    else:
        print("无效的选择，请重新运行程序并输入有效的选择。")

if __name__ == "__main__":
    main()
