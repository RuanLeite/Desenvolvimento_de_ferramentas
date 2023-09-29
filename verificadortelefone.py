import phonenumbers

from phonenumbers import geocoder

tel = input("Digite o telefone no formato +551140028922: ")

phone_number = phonenumbers.parse(tel)

print(geocoder.description_for_number(phone_number, 'pt'))
