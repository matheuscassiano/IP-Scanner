# -*- coding: utf-8 -*-
import socket
import os
import geoip2.database

cdb = geoip2.database.Reader('./GeoLite2-City.mmdb')
asndb=  geoip2.database.Reader('./GeoLite2-ASN.mmdb')

def get_ip(x, y):
	x = socket.gethostbyname(y)
	print('\n\033[0;34mEndereço IP: \033[1;34m{}\033[0;34m'.format(x))

def menu():
	os.system('clear')

	print("\033[1;31m d888888b d8888b. \033[1;34m   .d8888.  .o88b.  .d8b.  d8b   db d8b   db d88888b d8888b. ")
	print("\033[1;31m   `88'   88  `8D \033[1;34m   88'  YP d8P  Y8 d8' `8b 888o  88 888o  88 88'     88  `8D ")
	print("\033[1;31m    88    88oodD' \033[1;34m   `8bo.   8P      88ooo88 88V8o 88 88V8o 88 88ooooo 88oobY' ")
	print("\033[1;31m    88    88~~~   \033[1;34m     `Y8b. 8b      88~~~88 88 V8o88 88 V8o88 88~~~~~ 88`8b   ")
	print("\033[1;31m   .88.   88      \033[1;34m   db   8D Y8b  d8 88   88 88  V888 88  V888 88.     88 `88. ")
	print("\033[1;31m Y888888P 88      \033[1;34m   `8888Y'  `Y88P' YP   YP VP   V8P VP   V8P Y88888P 88   YD \033[0;0m")
                                                 
	
	print ('\033[1;37m\n [01] \033[0;34m= Obter IP de Site')
	print ('\033[1;37m [02] \033[0;34m= Localizar IP')
	print ('\033[1;37m [03] \033[0;34m= Sair\n')
	return int(input('Escolha a opção desejada: '))

while True:
	try:
		opcao = menu()
		if opcao ==1:
			dom = str(input('Entre com o dominio: \033[1;34m')).strip().lower()
			get_ip(dom, dom)
	
		elif opcao == 2:
			z = str(input('Digite o seu IP: \033[1;34m'))
			rasndb = asndb.asn(z)
			rcdb = cdb.city(z)
			print('\033[1;34mPaís: \033[0;36m{} - {}\033[0;0m'.format(rcdb.country.name, rcdb.country.iso_code))
			print('\033[1;34mEstado: \033[0;36m{} - {}\033[0;0m'.format(rcdb.subdivisions.most_specific.name, rcdb.subdivisions.most_specific.iso_code))
			print('\033[1;34mCidade: \033[0;36m{}\033[0;0m'.format(rcdb.city.name))
			print('\033[1;34mCod-Postal: \033[0;36m{}\033[0;0m'.format(rcdb.postal.code))
			print('\033[1;34mLatitude: \033[0;36m{}\033[0;0m'.format(rcdb.location.latitude))
			print('\033[1;34mLongitude: \033[0;36m{}\033[0;0m'.format(rcdb.location.longitude))
			cdb.close()
			print('\033[1;34mProvedor de Internet: \033[0;36m{}'.format(rasndb.autonomous_system_organization))
			print('{}\033[0;34m'.format(rasndb.autonomous_system_number))

		elif opcao == 3:
			print ('Finalizado')
			break
		
	except ValueError:
		print ('Oops Opção invalida\n')

	input('Precione ENTER ')
