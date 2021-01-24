# Instagram-Auto-Acceptor
A script that automatically accepts all your pending follow requests.

## About
This tool bulk accepts follow requests, meaning it accepts all pending requests in your account . It then checks/ scans your account every 9 seconds in default for any pending requests. You may change the delay in seconds, and limit the accounts you will accept in each iteration. Make sure you 
are already logged on Instagram in the pc you will be using this 
script in as this does not have a challenge solver yet.

Your account must be private to use this tool. 
## Picture
![Picture](https://i.ibb.co/qDFqw21/Screenshot-35.png)

## Installation
### Get Python
If you dont have python installed, downlaod python
and make sure you click on the 'ADD TO PATH' option during
the installation.

### pip install these
```
pip install colorama
pip install halo
pip install requests
```

### then run the script..
```
python autoacceptor.py
```
Make sure you are in the same directory as the 
python file.

### How to Use
[DELAY/SLEEP FEATURE] Check follow requests queue every (in seconds) - This tells the program how long to sleep/wait for until it will refresh Instagram  again 
and check for any pending follow requests. 

For this ,you can leave it blank if you don't want any delays but it is RECOMMENDED to put a delay. If you dont, the program will constantly referesh Instagram
and you might get detected.
1800 seconds is good (It checks every 30 minutes for requests). 
If you dont' get that much follower requests, you can check every 3600 seconds (better). I recommend puting delays to avoid overloading/spamming the Instagram API.

[LIMIT FEATURE]Limit number of accounts to accept in each iteration (int value) [Optional] - This tells the program how many accounts you can accept in each iteration.
The default value is 75, meaning in each iteration, 75 accounts can be followed in bulk . You can leave this blank, but if you get a large amount of follow requests
in a short period of time, you should limit it to under 100.  You can customize this. For example, you only want to accept 5 people in each iteration so just type 5.


Examples:
Puting the delay to 3600 and limiting the program to 5. What this will do is it will check the follow requests queue every 3600 seconds and it will only accept 5 accounts
for each iteration. For example, you have 100 follow requests. The program will only accept 5 people and you will have to wait 3600 seconds before the next batch of 5 is accepted.

Close the application or Control + C to stop accepting requests.
### To Do
- Add method of solving challenge 
- GUI
- More options
