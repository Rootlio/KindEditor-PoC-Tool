from colorama import init, Fore
import requests
import urllib3
from multiprocessing.dummy import Pool
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init()

print(Fore.BLUE + "|________________________|")
print(Fore.BLUE + "| KindEditor EXP Scanner |")
print(Fore.BLUE + "|    coded by Rootlio    |")
print(Fore.BLUE + "|________________________|")

path1 = "/kindeditor/examples/uploadbutton.html"
path2 = "/admin/kindeditor/examples/uploadbutton.html"
path3 = "/html/kindeditor/examples/uploadbutton.html"
path4 = "/html/js/kindeditor/examples/uploadbutton.html"
path5 = "/assets/js/kindeditor/examples/uploadbutton.html"
path6 = "/Public/kindeditor/examples/uploadbutton.html"
path7 = "/includes/kindeditor/examples/uploadbutton.html"
path8 = "/admin_2/kindeditor/examples/uploadbutton.html"
path9 = "/assets/kindeditor/examples/uploadbutton.html"
path10 = "/js/plugin-kindeditor/examples/uploadbutton.html"

y1 = 1
y2 = 1

headers_list = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

target_list_name = input("Name of List File:")
target_urls = open(target_list_name, 'r').read().splitlines()

def scanproc(machine):
    bingo = False

    full_url = machine + path1
    try:
        response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
        if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
            print(Fore.GREEN + machine +" BINGO!")
            with open("uploaders.txt", 'a') as f:
                f.write(full_url + "\n")
            bingo = True
    except:
        pass

    if y1 == y2:
        full_url = machine + path2
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if y1 == y2:
        full_url = machine + path3
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if y1 == y2:
        full_url = machine + path4
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if y1 == y2:
        full_url = machine + path5
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if y1 == y2:
        full_url = machine + path6
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if y1 == y2:
        full_url = machine + path7
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if y1 == y2:
        full_url = machine + path8
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if y1 == y2:
        full_url = machine + path9
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if y1 == y2:
        full_url = machine + path10
        try:
            response_body = requests.get(full_url, verify=False, headers=headers_list, timeout=3)
            if response_body.status_code == 200 and "<title>Upload Button Examples</title>" in response_body.text:
                print(Fore.GREEN + machine +" BINGO!")
                with open("uploaders.txt", 'a') as f:
                    f.write(full_url + "\n")
                bingo = True
        except:
            pass

    if not bingo:
        print(Fore.RED + machine +" UGH!")

    time.sleep(0.1)

tpool = Pool(30)
tpool.map(scanproc, target_urls)
tpool.close()
tpool.join()