from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import redirect, render

from home.models import Home

def home(request):
    encabezado = Home.objects.all()
    context = {
        'encabezado': encabezado,
    }
    return render(request, 'skeleton.html')


def clima(request):
	import requests

	USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
	LANGUAGE = "es-CL,es;q=0.5"
	session = requests.Session()
	session.headers['User-Agent'] = USER_AGENT
	session.headers['Accept-Language'] = LANGUAGE
	session.headers['Content-Language'] = LANGUAGE

	html_content = session.get(f'https://www.google.cl/search?q=clima+lanco').content
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html_content, 'html.parser')



	clima = dict()
	clima['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
	clima['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
	clima['dayhour'], clima['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split('\n')

	html_contentdos = requests.get(f'https://www.bcentral.cl').content
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html_contentdos, 'html.parser')
	data = soup.find_all('p', class_='mb-0 text-center')

	items = []

	for item in data:
	    if item.span == None:
	        items.append(item.string.strip())

	context = {
		'UF': items[0],
		'UTM': items[1],
		'USD': items[2], 
		'EU': items[3]
	}
	template = 'home_base/home_base.html'

	return render(request, template, {'clima': clima,'inter': context})
