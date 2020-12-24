import requests
import re
import json
from colorama import Fore, init ,Style
import time
import os
from halo import Halo

init(convert=True)

class InstagramAccept: 
    def __init__(self,login_data):

        self.url_login = "https://www.instagram.com/accounts/login/ajax/"
        self.url_activity = "https://www.instagram.com/accounts/activity/"
        self.url = "https://www.instagram.com/"        
        self.s = requests.Session()
        
        self.temp_headers = {
         "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    
        }
        self.csrf_token = self._get_csrf()

        self.headers = {
         "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "x-csrftoken": self.csrf_token,
     
        }

        self.login_data =  login_data

    def login(self) -> bool:
        log_in = self.s.post(self.url_login,data=self.login_data,headers=self.headers)


        log_in_dict = json.loads(log_in.text)


        print("[!] Authentication:", log_in_dict['authenticated'])

        if log_in_dict['authenticated']:
            return True
        return False


    def _get_activity(self) -> list:
        print("[!] Getting activity..")
        account_activity = self.s.get(self.url_activity)    

        sharedData = re.search("window._sharedData = (.*?);</script>", account_activity.text, re.DOTALL).group(1)
        
        self.activity = json.loads(sharedData)

        return self.activity                                   

    def _analyze_requests(self):

        self.edge_follow_requests = self.activity['entry_data']['ActivityFeed'][0]['graphql']['user']['edge_follow_requests']['edges']

        if not self.edge_follow_requests:
            print("[!] No pending users to accept!")

        self.pending_usersID = []
        self.pending_usersUSERNAME = []
        self.pending_usersPFP = []
        self.pending_DICT = []

        for x in self.edge_follow_requests:
            self.pending_usersID.append(x['node']['id'])
            self.pending_usersUSERNAME.append(x['node']['username'])
            self.pending_usersPFP.append(x['node']['profile_pic_url'])
            self.pending_DICT.append(x)

    def _get_csrf(self):
        r = self.s.get(self.url, headers=self.temp_headers)
        self.csrf_token =  re.search('(?<="csrf_token":")\w+', r.text).group(0) 
        return self.csrf_token
   

    def accept_requests(self):
        #Accept all requests after getting user ids
        self.csrf_token = self._get_csrf()
        self._analyze_requests()


        for a, b in zip(self.pending_usersID,self.pending_usersUSERNAME):
            accept_req = self.s.post(f'https://www.instagram.com/web/friendships/{a}/approve/',headers={"x-csrftoken": self.csrf_token})

            accept_req_dict = json.loads(accept_req.text)
            
            if accept_req_dict['status'] == "ok":
                print(f"[*] Approved {b}'s follow request | id: {a}")

            else:
                print("An error has occured.") 
                
    def loop(self):
        self._get_activity()
        self.accept_requests()   


def title():
    print(f'''{Fore.LIGHTBLACK_EX}https://github.com/nightfall2512{Style.RESET_ALL}{Fore.LIGHTRED_EX}
    ___         __           ___                        __            
   /   | __  __/ /_____     /   | _____________  ____  / /_____  _____
  / /| |/ / / / __/ __ \   / /| |/ ___/ ___/ _ \/ __ \/ __/ __ \/ ___/
 / ___ / /_/ / /_/ /_/ /  / ___ / /__/ /__/  __/ /_/ / /_/ /_/ / /    
/_/  |_\__,_/\__/\____/  /_/  |_\___/\___/\___/ .___/\__/\____/_/     
                                             /_/                      
    
                                                    {Style.RESET_ALL} by Nightfall#2512                                                                                              
                                                                                                 ''')
def main():
    s = Style.RESET_ALL 
    c = Fore.LIGHTRED_EX
    os.system('cls')
    title()
    os.system('title Instagram Auto Acceptor V3.1 ^| Menu')

    input_username = input(f"[!] Instagram Username {c}>{s} ")
    input_password = input(f"[!] Instagram Password {c}>{s} ")
    try:
        input_delay = int(input(f"[!] Check every (in seconds) [Optional] {c}>{s} "))
    except ValueError:
        input_delay = 9
    post =  {'username': input_username, 'enc_password': '#PWD_INSTAGRAM_BROWSER:0:0:' +input_password}

    spinner = Halo(text='Loading', spinner='dots', color='red')

    spinner.start()
    i = InstagramAccept(post)
    spinner.stop()
    os.system('cls')
    title()

    if i.login()== True:     
            while True:   
                i.loop()
                spinner.start()
                time.sleep(input_delay)
                spinner.stop()
    else:
        print('[!] User has failed to log in')
        input()
        main()

if __name__ == "__main__":
    main()


