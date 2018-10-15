#!/usr/bin/python
import collections
from random import randint
Countries=['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cameroon','Cape Verde','Central African Republic','Chad','Democratic Republic of Congo','Republic of Congo','Cote d\'Ivoire','Djibouti',
'Egypt','Equatorial Guinea','Erritrea','Ethiopia','Gabon','Gambia','Ghana','Guinea','Guinea Bissau','Kenya','Lesotho','Liberia','Libya','Madagascar','Malawi',
'Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria','Reunion','Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia',
'South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia','Zimbabwe']
AreaCodes={'Algiers':'Algeria','Luanda':'Angola','Porto Novo':'Benin','Gaborone':'Botswana','Ouagadaugou':'Burkina Faso','Bujumbura':'Burundi','Yaounde':'Cameroon','Praia':'Cape Verde','Bangui':'Central African Republic','N\' Djamena':'Chad','Kinshasa':'Democratic Republic of Congo','Brazzaville':'Republic of Congo','Yamoussoukro':'Cote d\'Ivoire','Djibouti':'Djibouti',
'Cairo':'Egypt','Malabo':'Equatorial Guinea','Asmara':'Erritrea','Addis Ababa':'Ethiopia','Libreville':'Gabon','Banjui':'Gambia','Accra':'Ghana','Conakry':'Guinea','Bissau':'Guinea Bissau','Nairobi':'Kenya','Maseru':'Lesotho','Monrovia':'Liberia','Tripoli':'Libya','Antannarivo':'Madagascar','Lilongwe':'Malawi',
'Bamako':'Mali','Nouakchott':'Mauritania','Port louis':'Mauritius','Rabat':'Morocco','Maputo':'Mozambique','Windhoek':'Namibia','Niamey':'Niger','Abuja':'Nigeria','Saint Denis':'Reunion','Kigali':'Rwanda','Sao Tome':'Sao Tome and Principe','Dakar':'Senegal','Victoria':'Seychelles','Freetown':'Sierra Leone','Mogadishu':'Somalia',
'Pretoria':'South Africa','Juba':'South Sudan','Khartoum':'Sudan','Mbambane':'Swaziland','Dodoma':'Tanzania','Lome':'Togo','Tunis':'Tunisia','Kampala':'Uganda','Lusaka':'Zambia','Harare':'Zimbabwe'}
Capitals=AreaCodes.keys()
Countries.sort()
SevenWonders=['The Pyramids of Egypt','The Hanging Gardens of Babylon','The Tomb of Mausolus','The Temple of Artemis(Diana) at Ephesus','The Colossus of Rhodes','The Statue of Zeus at Olympia','The Pharos of Alexandria']

def test():
	for country in Countries:
		print("#%i\t----->%s\n"%(Countries.index(country)+1,country))
#test()#prints all items in list
for i in range(0,5):
	b=randint(0, 53)
	for city in Capitals:
		if AreaCodes[city]==Countries[b]:
			print("Random African Nation %s --> %s"%(Countries[b],city))
print("The Seven Wonders of the World..:")
for wonder in SevenWonders:
	print(wonder)


