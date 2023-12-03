Textový analyzátor - program, který zanalyzuje libovolně dlouhým textem a zjistí o něm různé informace.

 1)   	Vyžádá si od uživatele přihlašovací jméno a heslo,
 2)	Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů, 
		a)	pokud je registrovaný, pozdraví jej a umožní mu analyzovat texty
    		b)	pokud není registrovaný, upozorní jej a ukončí program.

Registrováni jsou následující uživatelé:

+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+

  3)	Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:
        	a)pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí
        	b)pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.

    Program pro vybraný text spočítá následující statistiky:
      	- počet slov,
        - počet slov začínajících velkým písmenem,
        - počet slov psaných velkými písmeny,
        - počet slov psaných malými písmeny,
        - počet čísel (ne cifer),
        - sumu všech čísel (ne cifer) v textu
    	- program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 

Po spuštění by měl průběh vypadat následovně:

příklad průběhu:

- Pokud uživatel je registrovaný a nedojde k chybě:

$ python projekt1.py
username:bob
password:123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all the numbers 8510
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
  1|*             |1
  2|*********     |9
  3|******        |6
  4|***********   |11
  5|************  |12
  6|***           |3
  7|****          |4
  8|*****         |5
  9|*             |1
 10|*             |1
 11|*             |1

- Pokud uživatel není registrovaný:

$ python projekt1.py
username:marek
password:123
unregistered user, terminating the program..