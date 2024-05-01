from setuptools import setup, find_packages

setup(
    name='voscan',  # Proje adınızı buraya yazın
    version='1.0',  # Proje sürümünüzü buraya yazın
    packages=find_packages(),  # Tüm paketleri otomatik olarak bulun
    install_requires=[  # Bağımlılıkları burada listele
        'requests',
        'aiohttp',
        'colorama',
    ],
    author='The Vodka',
    description='Dizin Tarama Aracı',  # Proje açıklamanızı buraya yazın
    url='https://github.com/vooolab/voscan', 
    license='MIT'
)
