import elements
from urllib.parse import urlparse, urljoin, urlencode
import os
import asyncio
import aiohttp
from aiohttp import ClientSession
from collections import Counter
import shutil
local_term_width = 40
if elements.term_width > 40 and elements.term_width < 100:
	local_term_width = 50

def scan_dir_conf(scheme, netloc, wordlistc):
	base_url = f"{scheme}://{netloc}"
	if wordlistc == "df":
		wordlist = "wordlists/dirs.txt"
	else:
		wordlist = wordlistc


	if os.path.exists(wordlist):
		with open(wordlist, 'r', errors='ignore', encoding='utf-8') as f:
			lines = f.read().splitlines()
			lines_count = len(lines)
		ptaout = int(lines_count / 186)
		ptaout_text = elements.convert_seconds(ptaout)
		formatted_size_line = elements.format_bytes(lines_count)
		elements.printf(f"-" * (local_term_width + 20))
		elements.printf(f" URL".ljust(23) + ":",base_url)
		elements.printf(f" Wordlist".ljust(23) + ":", wordlist)
		elements.printf(f" Tahmini İşlem Süresi".ljust(23) + ":", ptaout_text + f" [{formatted_size_line}]")
		elements.printf(f" Threads".ljust(23) + ":", "Maksimum")
		elements.printf(f" Vektör".ljust(23) + ":", "Dizin Saldırısı")
		elements.printf(f"-" * (local_term_width + 20))
		async def main():
			await scan_dir(base_url, wordlist)
		asyncio.run(main())
	else:
		elements.error("Wordlist Bulunamadı")
		if wordlistc == "df":
			elements.system("Varsayılan Wordlist Dosyası Silinmiş veya Bozulmuş Olabilir. Aracı Güncellemenizi Öneriyoruz!")
		exit()


async def fetch(url, session, line, scan_count, lines_count, black_list_size):
	try:
		async with session.get(url) as response:
			html_content = await response.text()
			status_code = response.status
			size = len(html_content)
			black_list_size.append(size)
			black_list_size_count = Counter(black_list_size)
			elements.uline(f"  --> [{scan_count}/{lines_count}] {url}")
			formatted_size = elements.format_bytes(size)
			if black_list_size_count[size] > 6:
				pass
			else:
				if status_code in {200, 301, 401, 503}:
					if status_code == 200:
						print(f"  {elements.star} {url.ljust(local_term_width)} ({elements.c.bright_green}{status_code}{elements.c.r}) [{formatted_size}]")
					elif status_code == 301:
						location = response.headers.get('Location')
						if url == location:
							print(f"  {elements.star} {url.ljust(local_term_width)} ({elements.c.yellow}{status_code}{elements.c.r}) [{formatted_size}]")
						else:
							print(f"  {elements.star} {url.ljust(local_term_width)} ({elements.c.yellow}{status_code}{elements.c.r}) [{formatted_size}] --> {elements.c.yellow}{location}{elements.c.r}")
					elif status_code == 401 or status_code == 503:
						print(f"  {elements.star} {url.ljust(local_term_width)} ({elements.c.bright_red}{status_code}{elements.c.r}) [{formatted_size}]")
					else:
						print(f"  {elements.star} {url.ljust(local_term_width)} ({status_code}) [{formatted_size}]")	
	except Exception as e:
		pass

async def scan_dir(url, wordlist):
	async with ClientSession() as session:
		scan_count = 0
		black_list_size = []
		with open(wordlist, 'r', errors='ignore', encoding='utf-8') as f:
			lines = f.read().splitlines()
			lines_count = len(lines)

		tasks = []
		for line in lines:
			target_url = f"{url}/{line}"
			scan_count += 1
			tasks.append(fetch(target_url, session, line, scan_count, lines_count, black_list_size))

		await asyncio.gather(*tasks)
