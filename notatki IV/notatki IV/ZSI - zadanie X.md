# ZSI - zadanie konkurosowe

Grzegorz Koperwas 2/C www.grzegorzkoperwas.site

![[Zadanie X.svg]]
Dane dla kontenrerów przechowujemy za pomocą `glusterfs`, jakiś miks replik oraz mirrorów dla prędkości oraz redundancji. Dodatkowo możemy kożystać z georeplikacji w tym systemie plików. Niby słaby jest dla baz danych, ale te już na tej skali posiadają własne mechanizmy. Dla zdjęć itp jest wspaniały.

Dla swojego Home<del>Laba</del>DataCenter stosuje 3 repliki + snapshoty btrfs ale to tylko infrastruktura hostująca bloga.

## Załącznik 1: Config nginx
```nginx
http {
	# cośtam cośtam
	geoip_country /usr/share/GeoIP/GeoIP.dat;
    map $geoip_country_code $allowed_country {
        US no;
        PL yes;
        #…
        default yes;
    }
    # load balancer
    upstream zsieu {
	    server a.eu.adminakademia.pl;
	    server b.eu.adminakademia.pl;
	    #…
    }
    upstream zsius {
	    server a.us.adminakademia.pl;
	    server b.us.adminakademia.pl;
	    #…
    }
	server {
		# cośtam listen cośtam ssl
		location /eu/ {
			# cośtam cache-headers cośtam
			if ($allowed_country = no) {
				return 301 https://fqdn/us;
			}
			# cośtam proxy_headers cośtam
			proxy_pass http://zsieu/
		}
		# na wypadek jak Noe zrobi powódź i amerykanie
		# przyjadą do nas, nie powinno nastąpić przez Geo LB
		# ale statystyki 518 wyglądają źle w logach
		location /us/ {
			# cośtam cache-headers cośtam
			if ($allowed_country = yes) {
				return 301 https://fqdn/eu;
			}
			# cośtam proxy_headers cośtam
			proxy_pass http://zsius/
		}
	}
}
```

Config plików statycznych jest trywialny i został pozostawiony jako zadanie dla sprawdzającego, `try_files message.txt =404`

## Załącznik 2: O hasłach dostępowych

Hasła są złe, tyle pisania przy logowaniu się do serwera po `ssh`, klucze na kartach `OpenPGP`, `gpg-agent` działający jako agent kluczy `ssh` do dostępu oraz inne MFA (google authenticator działa z PAM).

Jeśli chodzi o dane i hasła userów, tej *usługi nginx*, to jeśli jest to faktycznie nginx to robimy wymaganie kluczy klienckich. Jeżeli jest to usługo ogólnodostępna to hashe + salt haseł, nie wysyłamy przypadkowo danych za ocean itp. Ja w ramach projektu PBL kożystam z biblioteki `fastapi_users` do naszych userowych sprawek.