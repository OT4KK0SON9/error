import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""_____

1. SMS Gratis
2. OTP Matahari
3. OTP Hallodok
4. OTP Olx.co.id
5. OTP Sociolla.com
6.OTP Cermati
7.OTP Kredit Pintar
- selamat puasa -
____""")
		pilih=int(input('apa/> '))
		if pilih == 1:
			import src.payu
		elif pilih == 2:
			import src.matahari
		elif pilih == 3:
			import src.alodok
		elif pilih == 4:
			import src.olx
		elif pilih == 5:
			import src.socil
		elif pilih == 6:
			import src.cermati
		elif pilih == 7:
			import src.kreditpintar
		else: print("[!] Ngasal Jir(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] -->')
except Exception as F:
	print('Err: %s'%(F))
