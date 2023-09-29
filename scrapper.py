from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp").content

soup = BeautifulSoup(site, "html.parser")

#print(soup.prettify()) #tranformar html em sting

#temperatura = soup.find("span", class_="-gray-light", id_="min-temp-1")
tempmin = soup.find('span', {'id': 'min-temp-1'})
tempmax = soup.find('span', {'id': 'max-temp-1'})
print(f"Temperatura mínima: {tempmin.string} - Temperatura máxima: {tempmax.string}")