from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def clima(request):
	import requests
	html_content = requests.get(f'https://www.google.com/search?q=clima+lanco').content
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html_content, 'html.parser')
	clima = dict()
	clima['region'] = soup.find("span", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
	clima['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
	clima['dayhour'], clima['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split('\n')
	return render(request, 'clima.html', {'clima': clima})

'''


def clima(request):
	import requests

	html_contentdos = requests.get(f'https://www.binance.com/es').content
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html_contentdos, 'html.parser')
	data = soup.find('div',{'class':'css-1i04fkn'})

	context = {
		'data': data,
	}

	return render(request, 'clima.html', {'clima': context})


def clima(request):
	import requests

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

	return render(request, 'clima.html', {'clima': context})







def get_html_content(request):
	import requests
	city = request.GET.get('city')
	city = city.replace(' ', '+')

	USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
	LANGUAGE = "en-US,en;q=0.5"
	session = requests.Session()
	session.headers['User-Agent'] = USER_AGENT
	session.headers['Accept-Language'] = LANGUAGE
	session.headers['Content-Language'] = LANGUAGE
	html_content = session.get(f'https://www.google.com/search?q=clima+{city}').text

	return html_content










def clima(request):
	clima = None
	if 'city' in request.GET:
		html_content = get_html_content(request)
		from bs4 import BeautifulSoup
		soup = BeautifulSoup(html_content, 'html.parser')
		clima = dict()
		clima['region'] = soup.find("div", attrs={"class": "wob_loc mfMhoc"}).text
		clima['temp_now'] = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text

		# get the day, hour and actual weather
		clima['dayhour'], clima['weather_now'] = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text.split(
		'\n')
	return render(request, 'clima.html', {'clima': clima})
	'''
