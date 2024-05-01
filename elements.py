from colorama import Fore, Back, Style, init
import shutil

def printf(*args):
	print(f" {c.r}", *args)

class c:
	bright_black = Fore.LIGHTBLACK_EX
	bright_red = Fore.LIGHTRED_EX
	bright_green = Fore.LIGHTGREEN_EX
	bright_yellow = Fore.LIGHTYELLOW_EX
	bright_blue = Fore.LIGHTBLUE_EX
	bright_magenta = Fore.LIGHTMAGENTA_EX
	bright_cyan = Fore.LIGHTCYAN_EX
	bright_white = Fore.LIGHTWHITE_EX
	black = Fore.BLACK
	red = Fore.RED
	green = Fore.GREEN
	yellow = Fore.YELLOW
	blue = Fore.BLUE
	magenta = Fore.MAGENTA
	cyan = Fore.CYAN
	white = Fore.WHITE
	bold = Style.BRIGHT
	r = Style.RESET_ALL


class b:
	bright_black = Back.LIGHTBLACK_EX
	bright_red = Back.LIGHTRED_EX
	bright_green = Back.LIGHTGREEN_EX
	bright_yellow = Back.LIGHTYELLOW_EX
	bright_blue = Back.LIGHTBLUE_EX
	bright_magenta = Back.LIGHTMAGENTA_EX
	bright_cyan = Back.LIGHTCYAN_EX
	bright_white = Back.LIGHTWHITE_EX
	black = Back.BLACK
	red = Back.RED
	green = Back.GREEN
	yellow = Back.YELLOW
	blue = Back.BLUE
	magenta = Back.MAGENTA
	cyan = Back.CYAN
	white = Back.WHITE
	bold = Style.BRIGHT
	r = Style.RESET_ALL


def generate_random_string(num):
	characters = string.digits + string.ascii_letters
	random_string = ''.join(random.choices(characters, k=num))
	return random_string


def error(*args):
	printf(f"{b.bright_red}{c.white} H {c.r}{b.red} {c.r}", *args)
def success(*args):
	printf(f"{b.bright_green}{c.white} B {c.r}{b.green} {c.r}", *args)
def alert(*args):
	printf(f"{b.bright_yellow}{c.white} U {c.r}{b.yellow} {c.r}", *args)
def system(*args):
	printf(f"{b.bright_blue}{c.white} S {c.r}{b.blue} {c.r}", *args)

def uline(*args):
	# Önceki satırı temizle ve yeni metni yaz
	print("\033[2K", end="\r", flush=True)  # Önceki satırı temizle
	print(*args, end="\r", flush=True)   # Yeni metni yaz

star = f"[{c.cyan}*{c.r}]"
qc = f"[{c.bright_yellow}?{c.r}]"

term_width, term_height = shutil.get_terminal_size()

def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0: 'B', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB', 5: 'PB', 6: 'EB', 7: 'ZB', 8: 'YB'}
    while size > power:
        size /= power
        n += 1
    return f"{size:.2f}{power_labels[n]}"


banner = f"""{c.cyan}
+----------------------------------------------------+
|  ┓┏┏┓┏┓┏┓┏┓┳┓ {c.cyan}|{c.r} {c.yellow}Developer :{c.r} The Vodka{c.cyan}              |
|  ┃┃┃┃┗┓┃ ┣┫┃┃ {c.cyan}|{c.r} {c.yellow}Version   :{c.r} 1.0.0{c.cyan}                  |
|  ┗┛┗┛┗┛┗┛┛┗┛┗ {c.cyan}|{c.r} {c.yellow}GitHub    :{c.r} https://vooolab/voscan{c.cyan} |
+----------------------------------------------------+                                                                           
{c.r}                                                                   
"""


def convert_seconds(seconds):
	hours = seconds // 3600
	seconds %= 3600
	minutes = seconds // 60
	seconds %= 60
	ptaout_text = ""
	if hours > 0:
		ptaout_text += f"{hours} saat, "
	if minutes > 0:
		ptaout_text += f"{minutes} dakika, "
	if seconds > 0 or ptaout_text == "":
		ptaout_text += f"{seconds} saniye"
	ptaout_text = ptaout_text.rstrip(", ")
	return ptaout_text


