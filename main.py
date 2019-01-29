# -*- coding: utf-8 -*-
import socket
import os
import geoip2.database

cdb = geoip2.database.Reader('./GeoLite2-City.mmdb')
asndb=  geoip2.database.Reader('./GeoLite2-ASN.mmdb')

def get_ip(x, y):
	x = socket.gethostbyname(y)
	print('\nEndereço IP [{}]'.format(x))

def menu():
	os.system("clear")

	print("d888888b d8888b.    .d8888.  .o88b.  .d8b.  d8b   db d8b   db d88888b d8888b. ")
	print("  `88'   88  `8D    88'  YP d8P  Y8 d8' `8b 888o  88 888o  88 88'     88  `8D ")
	print("   88    88oodD'    `8bo.   8P      88ooo88 88V8o 88 88V8o 88 88ooooo 88oobY' ")
	print("   88    88~~~        `Y8b. 8b      88~~~88 88 V8o88 88 V8o88 88~~~~~ 88`8b   ")
	print("  .88.   88         db   8D Y8b  d8 88   88 88  V888 88  V888 88.     88 `88. ")
	print("Y888888P 88         `8888Y'  `Y88P' YP   YP VP   V8P VP   V8P Y88888P 88   YD ")
                                                 
	print ("\n1 = Obter IP de Site")
	print ("2 = Localizar IP")
	print ("3 = Sair\n")
	return int(input("Escolha a opção desejada: ")) 



while True:
	try:
		opcao = menu()
		if opcao ==1:
			dominio = str(input("Entre com o dominio: ")).strip()
			get_ip(dominio, dominio)

		elif opcao == 2:
			z = input("Digite o seu IP: ").strip()
			rasndb = asndb.asn(z)
			rcdb = cdb.city(z)
			print('País: {} - {}'.format(rcdb.country.name, rcdb.country.iso_code))
			print('Estado: {} - {}'.format(rcdb.subdivisions.most_specific.name, rcdb.subdivisions.most_specific.iso_code))
			print('Cidade: {}'.format(rcdb.city.name))
			print('Cod-Postal: {}'.format(rcdb.postal.code))
			print('Latitude: {}'.format(rcdb.location.latitude))
			print('Longitude: {}'.format(rcdb.location.longitude))
			cdb.close()
			print('\nPrvedor de Internet: {}'.format(rasndb.autonomous_system_organization))
			print(rasndb.autonomous_system_number)

		elif opcao == 3:
			print ("Finalizado")
			break
		
	except ValueError:
		print ("Oops Opção invalida\n")

	input("Precione ENTER ")