# -*- coding: utf-8 -*-
import socket
import os
import geoip2.database
import nmap

cdb = geoip2.database.Reader('./GeoLite2-City.mmdb')
asndb=  geoip2.database.Reader('./GeoLite2-ASN.mmdb')

N = nmap.PortScanner()

def menu():
	os.system('clear')

	print("\033[1;31m d888888b d8888b. \033[1;34m   .d8888.  .o88b.  .d8b.  d8b   db d8b   db d88888b d8888b. ")
	print("\033[1;31m   `88'   88  `8D \033[1;34m   88'  YP d8P  Y8 d8' `8b 888o  88 888o  88 88'     88  `8D ")
	print("\033[1;31m    88    88oodD' \033[1;34m   `8bo.   8P      88ooo88 88V8o 88 88V8o 88 88ooooo 88oobY' ")
	print("\033[1;31m    88    88~~~   \033[1;34m     `Y8b. 8b      88~~~88 88 V8o88 88 V8o88 88~~~~~ 88`8b   ")
	print("\033[1;31m   .88.   88      \033[1;34m   db   8D Y8b  d8 88   88 88  V888 88  V888 88.     88 `88. ")
	print("\033[1;31m Y888888P 88      \033[1;34m   `8888Y'  `Y88P' YP   YP VP   V8P VP   V8P Y88888P 88   YD ")
	print('				  			      MATHEUS CASSIANO\033[0;0m')
    # Link: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Matheus%20Cassiano                                             
	
	print ('\033[1;37m\n [01] \033[0;33m= Obter IP de Site')
	print ('\033[1;37m [02] \033[0;33m= Localizar IP')
	print ('\033[1;37m [03] \033[0;33m= Escanear Portas')
	print ('\033[1;37m [04] \033[0;33m= Sair\n')
	return int(input('Escolha a opção desejada: '))

def get_ip(site):
	site = socket.gethostbyname(site)
	print('\n\033[0;33mEndereço IP: \033[1;34m{} \033[0;33m'.format(site))
	return site

def loc_ip(ip):
	rasndb = asndb.asn(ip)
	rcdb = cdb.city(ip)
	print('\033[0;0m\n[+]\033[1;34mPaís: \033[0;36m{} - {}\033[0;0m'.format(rcdb.country.name, rcdb.country.iso_code))
	print('[+]\033[1;34mEstado: \033[0;36m{} - {}\033[0;0m'.format(rcdb.subdivisions.most_specific.name, rcdb.subdivisions.most_specific.iso_code))
	print('[+]\033[1;34mCidade: \033[0;36m{}\033[0;0m'.format(rcdb.city.name))
	print('[+]\033[1;34mCod-Postal: \033[0;36m{}\033[0;0m'.format(rcdb.postal.code))
	print('[+]\033[1;34mLatitude: \033[0;36m{}\033[0;0m'.format(rcdb.location.latitude))
	print('[+]\033[1;34mLongitude: \033[0;36m{}\033[0;0m'.format(rcdb.location.longitude))
	
	print('[+]\033[1;34mProvedor: \033[0;36m{}\033[0;0m'.format(rasndb.autonomous_system_organization))
	print('[+]\033[1;34m Alguma Coisa: \033[0;36m{}\033[0;33m'.format(rasndb.autonomous_system_number))

def scan_door(alvo, porta):
	N.scan(alvo, porta)

	for host in N.all_hosts():
		print('\n\033[0m[+]\033[1;34mEndereço: \033[0;36m{}\033[0m'.format(N[host].hostname()))
		print('[+]\033[1;34mIP: \033[0;36m{}\033[0m'.format(host))
		print('[+]\033[1;34mState: \033[0;36m{}\033[0m'.format(N[host].state()))
		for proto in N[host].all_protocols():
			print('[+]\033[1;34mProtocolo: \033[0;36m{}\033[0m'.format(proto))
			lport = N[host][proto].keys()
			lport = list(lport)
			lport.sort()
			for port in lport:
				print ('[+]\033[1;34mPorta: \033[0;36m{}\t\033[1;34mEstado: \033[0;36m{}\033[0m'.format(port, N[host][proto][port]['state']))

while True:
	try:
		opcao = menu()
		if opcao ==1:
			dom = str(input('Entre com o dominio: \033[1;34m')).strip().lower()
			ip = get_ip(dom)
			loc = str(input('Deseja localizar o IP? (S/N) ')).lower()
			if loc == 's':
				try:
					loc_ip(ip)				
				except:
					print('\033[0;0m\033[1;31mO Endereço IP não encontrado\033[0m')

			scan = str(input('Deseja escanear as portas? (S/N) ')).lower()
			if scan == 's':
				try:
					porta = input("\033[0;33mPortas: \033[1;34m")
					scan_door(dom, porta)
				except:
					pass
		elif opcao == 2:
			ip = str(input('Digite o seu IP: \033[1;34m'))
			loc_ip(ip)

		elif opcao == 3:
			alvo = str(input("\033[0;33mAlvo: \033[1;34m")).strip().lower()
			porta = input("\033[0;33mPortas: \033[1;34m")

			scan_door(alvo, porta)

		elif opcao == 4:
			print ('Finalizado')
			break
		
	except ValueError:
		print ('Oops Opção invalida\n')

	input('\033[0;33mPrecione ENTER ')