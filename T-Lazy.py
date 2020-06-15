
# <----- Coded by R37r0.Gh057 ----->

import subprocess,requests,os, stat
from zipfile import ZipFile


banner = '''
████████╗   ██╗      █████╗ ███████╗██╗   ██╗
╚══██╔══╝   ██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝
   ██║█████╗██║     ███████║  ███╔╝  ╚████╔╝ 
   ██║╚════╝██║     ██╔══██║ ███╔╝    ╚██╔╝  
   ██║      ███████╗██║  ██║███████╗   ██║   
   ╚═╝      ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
				
			Made for all the lazy skids out there.                                             
'''
r = ''

YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
GREEN = '\033[32;1m'
RED = '\033[31;1m'
WHITE = '\033[m'

authtoken = ''

def termux_bool():
	try:
		if 'termux' in os.environ['HOME']:
			return True
		else:
			return False
	except Exception:
		return False

def print_status(msg):
	print('['+GREEN+'+'+WHITE+'] '+msg)

def err(msg):
	print('['+RED+'!'+WHITE+']'+RED+' ERROR: '+WHITE+msg)

def msf():
	if os.path.isfile('/data/data/com.termux/files/usr/bin/msfconsole'):
		print_status('It looks like Metasploit Framework is already installed. Do you still want to proceed with the installation? [y/n]')
		x = input('ENTER CHOICE: ')
		if x.lower() != 'y':
			exit()

	a = subprocess.getoutput('neofetch | grep Android').split(' ')[2].split('.')[0]
	if int(a) <= 6:
		print_status('Android 6 or below detected...')
		print_status('Downloading metasploit installation script...')
		u=requests.get('https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh')
		with open('metasploittlz.sh','wb') as f:
			f.write(str(u.content.decode()))
		os.chmod('metasploittlz.sh',stat.S_IEXEC)
		subprocess.call('bash metasploittlz.sh',shell=True)
		if os.path.isfile('/data/data/com.termux/files/usr/bin/msfconsole'):
			print_status('Metasploit Framework installed.')
		else:
			err('Some Error Occured. Aborting Installation...')
	else:
		print_status('Android 7 or above detected...\n')
		print_status('installing metasploit...')
		subprocess.call(['pkg','install','unstable-repo'])
		subprocess.call(['pkg','install','metasploit'])
		if os.path.isfile('/data/data/com.termux/files/usr/opt/metasploit-framework/msfconsole'):
			print_status('Metasploit Framework installed')
		else:
			err('Some Error Occured. Aborting Installation...')
	

def ngrok():
	global r
	downloaded = 0
	print_status('Initializing Ngrok Download\n')
	with open('_ngrok.zip','wb') as f:
		r = requests.get('https://bin.equinox.io/a/e93TBaoFgZw/ngrok-2.2.8-linux-arm.zip',stream=True)
		length = int(r.headers.get('content-length'))
		print_status('SIZE: '+str(length)+' BYTES')
		for i in r.iter_content(chunk_size=1024):
			downloaded+=len(i)
			f.write(i)
			d = int(50*downloaded/length)
			print('\rDownloading:'+'['+RED+'%s%s'% ('+'*d,' '*(50-d))+WHITE+']',end='')
		print('\n')
	print_status('Downloaded.')
	print_status('Unzipping...')
	ZipFile('_ngrok.zip','r').extractall()
	print_status('Unzipped.')
	os.remove('_ngrok.zip')
	subprocess.call('mv ngrok /data/data/com.termux/files/usr/bin/',shell=True)
	os.chmod('/data/data/com.termux/files/usr/bin/ngrok',stat.S_IEXEC)
	print_status('Gave executable permission to ngrok binary.')
	print_status('Moved ngrok binary to ~/../usr/bin/')
	if authtoken != '':
		print_status('Adding authtoken.')
		subprocess.call('ngrok authtoken '+authtoken,shell=True)
		print_status('authtoken added.')

def apkmod():
	print_status('Downloading APKMOD installer script.')
	with open('apkmod_setup.sh','w') as f:
		r = requests.get('https://raw.githubusercontent.com/Hax4us/Apkmod/master/setup.sh').content.decode()
		f.write(str(r))
	os.chmod('apkmod_setup.sh',stat.S_IRWXU)
	print_status('Exitting tool... Run the apkmod_setup.sh manually')
	exit()

def menu():
	global authtoken
	while True:
		try:
			print(WHITE + '\n'+'\t['+RED+'1'+WHITE+']'+' Install Metasploit Framework')
			print('\t['+RED+'2'+WHITE+']'+' Download Ngrok')
			print('\t['+RED+'3'+WHITE+']'+' Install APKMOD (apktool for termux with a payload binding feature)')
			print('\t['+RED+'4'+WHITE+']'+' Exit')
			x = input('\n\t'+RED+'Enter Choice: '+WHITE)
			if x.isdigit():
				if x == '1':
					msf()
				elif x == '2':
					while True:
						a = input('Enter your authtoken for ngrok["skip" to skip it]: ')
						if len(a) > 30:
							authtoken = a
							break
						elif len(a) < 30 and a == 'skip':
							break
						else:
							err('Invalid authtoken')

					ngrok()
				elif x == '3':
					apkmod()
				elif x == '4':
					exit()
				else:
					err('Invalid Choice')
			else:
				err('Enter a number')
		except Exception as e:
			err('SOME UNKNOWN ERROR OCCURED: '+str(e.args))
			exit()
def main():
	if not termux_bool():
		err('This is script is for Termux only.')
		exit()
	print(banner)
	print("[+] Authors:- " + RED + "cYBER kNIGHT & R37r0.Gh057 ")
	print(GREEN + "[+] Team Github:- " + YELLOW + "https://github.com/Ethical-Hacking-Zone")
	print(BLUE + "[+] Telegrams:- " + CYAN + "@Cyb3r_kn1ghT & @R37R0_GH057")
	menu()
main()
