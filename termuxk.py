#Import
import os, sys, time

#Warna Teks
red = '\033[91m'
redwhite = '\033[41;97m'
white = '\033[97m'

#Functions
def textr(text):
	for a in text:
		sys.stdout.write(a)
		sys.stdout.flush()
		time.sleep(0.0001)

def banner():
	textr(red + '▅▅▅▅▅' + white + '╗⠀' + red + '▅▅▅▅▅' + white + '╗⠀' + red + '▅▅▅▅▅' + white + '╗⠀' + red + '▅▅⠀▅▅' + white + '╗⠀' + red + '▅⠀⠀⠀▅' + white + '╗⠀' + red + '▅⠀⠀⠀▅' + white + '╗⠀' + red + '▅⠀⠀▅▅' + white + '╗\n⠀⠀' + red + '█' + white + '╔═╝⠀' + red + '█▅▅▅▅' + white + '╣⠀' + red + '█⠀⠀⠀█' + white + '║⠀' + red + '█' + white + '║' + red + '█' + white + '║' + red + '█' + white + '║⠀' + red + '█⠀⠀⠀█' + white + '║⠀⠀' + red + '█▅█' + white + '╔╝⠀' + red + '█▅█' + white + '╔═╝\n⠀⠀' + red + '█' + white + '║⠀⠀⠀' + red + '█' + white + '════╝⠀' + red + '█▅▅▅█' + white + '╝⠀' + red + '█' + white + '║' + red + '█' + white + '║' + red + '█' + white + '║⠀' + red + '█⠀⠀⠀█' + white + '║⠀⠀' + red + '▅█▅' + white + '╚╗⠀' + red + '██▅' + white + '╚═╗⠀\n⠀⠀' + red + '█' + white + '║⠀⠀⠀' + red + '█▅▅▅▅' + white + '╗⠀' + red + '█' + white + '║' + red + '█▅▅' + white + '╗⠀' + red + '█' + white + '║╚╝' + red + '█' + white + '║⠀' + red + '█▅▅▅█' + white + '║⠀' + red + '█' + white + '╔══' + red + '█' + white + '║⠀' + red + '█' + white + '╔' + red + '█▅▅' + white + '║\n⠀⠀╚╝⠀⠀⠀╚════╝⠀╚╝⠀╚═╝⠀╚╝⠀⠀╚╝⠀╚════╝⠀╚╝⠀⠀╚╝⠀╚╝╚══╝\n\n' + red + 'Youtube: ' + white + 'https://youtube.com/channel/UCqBuURb1zkId7HdMhakJtMw\n' + red + 'Github: ' + white + 'https://github.com/Mhurifams\n\n\n')

#Main
os.system('clear') 
banner()
textr('Tunggu sebentar...\n')
time.sleep(5)
try:
	os.mkdir('/data/data/com.termux/files/home/.termux') 
except:
	pass
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
filew = open('/data/data/com.termux/files/home/.termux/termux.properties','w') 
filew.write(key)
filew.close()
os.system('termux-reload-settings')
textr('Selesai!\n')