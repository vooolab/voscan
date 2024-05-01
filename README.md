<div align="center">
  <img src="https://raw.githubusercontent.com/vooolab/voscan/main/git-images/banner.jpeg" style="width: 350px;"/>
</div>

<h1 align="center">
Voscan v1.0 Demo
</h1>
Web sitelerinin gizlenmiş dizinlerini tarayabilirsiniz. Admin Panellerini rahatlıkla bulabilirsiniz. Araç demo sürecindedir ve eksikikler en kısa sürede giderilecektir.
<h2 align="center">
Kurulum
</h2>
<h3>GitHub Kurulumu</h3>
<b>Termux</b>
<pre>pkg install python
git clone https://github.com/vooolab/voscan/
cd voscan
python setup.py install
python voscan.py --help</pre>
<b>Linux Dağıtımları</b>
<pre>sudo apt-get update
sudo apt-get install python3 python3-pip
git clone https://github.com/vooolab/voscan/
cd voscan
python setup.py install
python3 vosql.py --help</pre>
<b>

<h3>Kullanım</h3>
<pre>python voscan.py -u [URL] -d [WORDLIST]</pre>

Örnek:
<pre>python voscan.py -u www.mudp.gov.bd -d df</pre>
Not: Eğer Wordlist dosyanız yoksa "-d df" yazarak default olarak voscan wordlistini belirtebilirsiniz.

<h2 align="center">
Ekran Görüntüsü
</h2>
<div align="center">
  <img src="https://raw.githubusercontent.com/vooolab/voscan/main/git-images/ss1.png"/>
</div>

<h2 align="center">
Taglar
</h2>
dirb, gobuster, admin-pabel-finder, admin panel finder, dir, subdomain, demo, scan, admin panel bulucu
