# PERSONAL REMINDER OF STRING METHODS
STRING (#string, #sir) str = '...text...'
    str.count('sir'[, inceput[, sfarsit]]) 
    str.find('sir'[, inceput[, sfarsit]])  --> index/-1
    str.rfind('sir'[, inceput[, sfarsit]]) --> index/-1
    str.replace('vechi', 'nou'[, max])
    str.index('sir'[, inceput[, sfarsit]]) --> ERROR
    str.rindex('sir'[, inceput[, sfarsit]])--> ERROR
    str.join(lista, dic, etc) --> str = liniuta, space, ... 
    str.split('delimitator: default=space', numarul de delimitari)
    str.splitlines(numar) 
    str.endswith('sufix'[, inceput[, sfarsit]]) --> True/False
    str.startwith('prefix'[,inceput[,sfarsit]]) --> True/False
    str.strip(['caractere: default=space'])
    str.rstrip(['caractere'])
    str.lstrip(['caractere'])
    str.isallnum() --> True/False (&, *, ...)
    str.isalpha() --> True/False (1, ...)
    str.isnumeric() --> True/False [ONLY FOR UNICODE]
    str.isdigit() --> True/False (a, *, ...)
    str.isdecimal() --> True/False (a, *, ...) 
    str.isspace() --> True/False 
    str.islower() --> True/False 
    str.isupper()  --> True/False
    str.istitle()  --> True/False
    str.lower() 
    str.upper() 
    str.capitalize()
    str.swapcase() --> inverseaza literele
    str.title() --> prima litera din fiecare cuv
    str.center(latimea [,'fillchar=umplutura']) -->
    str.ljust(latime [,'fillchar=umplutur']) 
    str.rjust(latime [,'fillchar=umplutur'])
    str.zfill(latime) --> zerouri pe stanga
    str.decode(encoding='UTF-8', errors='strict, ignore, replace, smlcharrefreplace,backslashreplace')
    str.encode(encoding='UTF-8', errors='strict, ignore, replace, smlcharrefreplace,backslashreplace')
    str.translate(table [, deletechars='']) 
    maketrans('chars_de_inlocuit', 'chars_ce_vor_inlocui') = 1. import string. Ex: table=maketrans('av1','AW2')
    str.format(*args, **kwargs)
    - - - - - - - - - - - - - - - - - - - - - - - - - - -
    FUNCTII = eval, len, max, min, ord, str
    SLICE   = str[a[,:z]
    "...%2.f...%s..." %(1.6352, '..text..') --> 1.63
    "...{}...{}...".format(3, 'text')
    "..{var1}..{var2}..".format(var1=3, var2="..text..")

String Methods
str.count('sir'[, inceput[, sfarsit]]) = returneaza de cate ori apare 'sir' in str
str.find('sir'[, inceput[, sfarsit]]) = returneaza indexul lui sir daca exista in str, sau -1 daca nu este in str
str.rfind('sir'[, inceput[, sfarsit]]) = returneaza ultimul index a lui sir gasit in str, sau -1 daca nu este in str
str.replace('vechi', 'nou'[, max]) = returneaza o copie a str unde 'vechi' a fost inlocuit cu 'nou'. 'max' nr de inlocuiri dorite. Daca 'max' nu este prezent 'vechi' va fi inlocuit cu 'nou' peste tot in sir
str.index('sir'[, inceput[, sfarsit]]) = returneaza pozitia (indexul) la care se afla 'sir'. Daca 'sir' nu este in str = eroare
str.rindex('sir'[, inceput[, sfarsit]]) = returneaza ultima pozitie (index) la care 'sir' se afla in str. Daca 'sir' nu este in str = eroare
str.join(secventa) = returneaza un sir unde elementele 'secventa' (lista, sir, etc) au fost unite cu separatorul str. Ex: "".join(['1','2','3']) = 123; Ex: s="-", seq=('a', 'b'), s.join(seq) : =>a-b
str.split('delimitator', numar) = returneaza o lista a tuturor cuvintelor dintr-un sir. Daca 'delimitator' nu e specificat atunci e 'spatiu'. 'numar' = numar de delimitari. Ex: s = "acasa e bine" : s.split(a) :=>['', 'c', 's', ' e bine']. Delimitatorul se transf in virgul
str.splitlines(numar) = returneaza o lista cu toate liniile dintr-un str. Fiecare linie = un element in lista. 
str.endswith('sufix'[, inceput[, sfarsit]]) = returneaza True daca str se sfarseste cu 'sufix', altfel False
str.startwith('prefix'[,inceput[,sfarsit]]) = returneaza True daca str incepe cu 'prefix', altfel False
str.strip(['caractere']) = returneaza o copie a sirului unde toate 'caractere' au fost indepartate de la inceput sau sfarsit. Daca nu sunt 'caractere' se indeparteaza spatiile goale
str.rstrip(['caractere']) = returneaza o copie a sirului unde toate 'caractere' au fost indepartate de la sfarsitul str
str.lstrip(['caractere']) = returneaza o copie a sirului unde toate 'caractere' au fost indepartate de la inceputul str
str.isallnum() = returneaza True daca str e format doar din litere si numere sau False daca mai are si alte caractere (, &, etc)
str.isalpha() = returneaza True daca str e format doar din litere sau False daca mai are cifre si caractere
str.isnumeric() =[ONLY FOR UNICODE] returneaza True daca str e format doar din numere sau False daca mai are litere si caractere d = unicode('42', 'utf-8') > d.isnumeric()
str.isdigit() = returneaza True daca str e format doar din numere sau False daca mai are litere si caractere
str.isdecimal() = returneaza True daca str e format doar din numere sau False daca mai are litere si caractere
str.isspace() = returneaza True daca str e foramt doar din spatii (whitespace, tab) sau False daca mai are si altceva
str.islower() = returneaza True daca toate caracterele sunt litere mici sau False daca este o singura litera mare
str.isupper() = returneaza True daca toate caracterele sunt litere mari sau False daca este o singura litera mica
str.istitle() = returneaza True daca prima litera a fiecarui cuvant este litera mare sau False daca este altfel
str.lower() = returneaza a copy of str unde toate literele au fost transformate in litere mici
str.upper() = returneaza a copy of str unde toate literele au fost transformate in litere mari
str.capitalize() = returneaza a copy of str unde prima litera a str a fost transformata in litera mare
str.swapcase() = returneaza a copy of str unde toate literele au inversate; cele mici in mari si invers
str.title() = returneaza a copy of str unde prima litera din fiecare cuvant a fost transformata in litere mari
str.center(latime [,'fillchar']) = returneaza un str aliniat in centru. latime = un int care arata lungimea unde str va fi in centru.'fillchar' umple spatiile libere inainte si dupa str daca 'latime' mai mare ca len(str)
str.ljust(latime [,'fillchar']) = returneaza un str aliniat pe stanga.'fillchar' umple spatiile libere dupa str daca 'latime' mai mare ca len(str)
str.rjust(latime [,'fillchar']) = returneaza un str aliniat dreapta. 'fillchar' umple spatiile libere inainte str daca 'latime' mai mare ca len(str)
str.zfill(latime) = returneaza un str plin de zerouri pe partea stanga daca 'latime' este mai mare la len(str)
str.decode(encoding='UTF-8', errors='strict') = returneaza versiunea decodata a str. 'UTF-8' codecul utilizat, 'errors' ridicate daca ceva nu merge bine. Codec: (UTF-8, base64,)Erori: (strict, ignore, replace, smlcharrefreplace,backslashreplace)
str.encode(encoding='UTF-8', errors='strict') = returneaza versiunea codata a str. ...
str.translate(table [, deletechars='']) = returneaza o copie a str unde caracterele au fost translatate conform tabelului de translatie 'table' (vezi urmatoarea instructiune). 'table' creat cu "maketrans" (vezi mai jos). 'deletechars' litere ce vor fi sterse in str
maketrans('in', 'out') = 1. import string. 2. returneaza 'table' folosita in translatie (in instr. de mai sus). 'in' caractere de inlocuit; 'out' caractere ce vor inlocui. Ex: table=maketrans('av1','AW2')
str.format(*args, **kwargs) = return a formatted copy of string

eval(str) # evaluate str as a Python expression and return the result
len(str) # returneaza lungimea sirului
max(str) # returneaza caracterul maxim din sir
min(str) # returneaza caracterul minim din sir
ord(str) # returneaza the numeric value of str if it is a single Unicode char; inverse chr
str(secventa) #secventa poate fi lista, dictionar(inclusiv acolade, :, etc), tuplet, set, numar, variabila, etc
str[a[,:z]] #acceseaza un element la indexul a, sau mai multe de la a-z

String operators
+ # concatenare (adunare)
* # multiplicare
[] # slice (feliere)
[:] # slice in range
in # membership (apartenenta)
not # membership (apartenenta)
R/r # sir raw, caracterul '' este anulat
u # sir Unicode (diacritice)
% # operator pentru realizarea formatarilor. 
	% # operator pentru realizarea formatarilor. Ex: 'Eu, %s declar ca am %d ani'%('Subsemnatul', 40)
	%c - caracter
	%s - conversie str inainte de formatare
	%i - signed decimal integer
	%d - signed decimal integer
	%u - unsigned decimal integer
	%o - octal integer
	%x - hexadecimal integer (litere mici)
	%X - hexadecimal integer (litere mari)
	%e - notare exponentiala (notare cu 'e' mic)
	%E - notare exponentiala (notare cu 'E' mare)
	%f - floating point real NUMBERS
	%g - the shorter of %f and %e
	%G - the shorter of %f and %e
*	argument specifies width of precision
-	left justification
+	display the sign
<sp>	leave a blank space before a positive number
#	add the octal leading zero ('0') of hexadec leading '0X' or '0x', depending if 'x' of 'X' were used
0	pad from left with zeros (instead of spaces)
%	'%%' leaves you with a single literal '%'
(var)	mapping variable (dictionary argumented)
m.n.	m is min. total width and n is nr. of digits to display after the decimal point (if appl.)
"""Text...""" = un string pe mai multe linii (ghilimele triple)

Escape characters
\ - escape character (in raw string there is no escape char) Ex: R sau r'..string..'
^ - inceput de 
a - Alerta sonora Hex:(0x07)
b - Backspace (0x08)
cx - Control-x
\C-x - Control-x
\d - numere intre 0-9
\D - caractere care nu sunt numere
\e - Escape (0x1b)
\f - Formfeed (0x0c)
\M-C-x - Meta-Control-x
\n - New line (0x0a)
nnn - Octal notation, where n is in range 0.7
r - Carriage return (0x0d)
s - Space (0x20)
\s - majuscule si minuscule
\S - caractere care nu sunt spatii, sau spatii goale
t - Tab (0x09)
uhex - Unicode (Ex: u2562)
v - Vertical tab (0x0b)
\w - Litere mici
\W - Litere mari
x - Caracter x (Ex: 266, xC0)
xnn - Hexadecial notation, where n is in range 0.9, A.F (Ex: xF7)
* - argument ce specifica latimea sau precizia
- - aliniere pe stanga
formatted string sau f-string (prefixed by f or F; expresion from {} replaced by value; {{}}
unicode <=> \uXXXX (4 hexadecimal digits) <=> \N{name_of_Unicode_char}
__doc__  (var. __doc__) in function, method, class = documentation string

- afiseaza semnul (pozitiv sau negativ)
- lasa un spatiu liber inainte de un nr pozitiv
# - adauga un '0' (leading 0) inainte de valori octale, '0x' sau '0X' inainte de hexazecimale
0 - pad from left with 0 in loc de spatii goale
(var) - mapeaza variabile (argument in dictionare)
m.n. - m = latimea minima totala, n = numarul de digiti de afisat dupa punctul zecimal

FORMATING
[[fill]align][sign][#][0][width][,][.precision][type]
-fill = fill char when data too small
-align = <:left;>:right;^:centered;=:justified
-sign = +:pozitive value has +; -:negative value has -; :pozitive has space negative has -
-# = alternative display for numbers (Ex: hex value has "0x" in front of)
-0 = output padded with 0
-width = width of data field
-, = numeric data has "," separator for thousand
.precision = number of char after decimal point

Sybols used with %

 
%c	character	   
%s	string conversion via str() prior to formating	   
%i	signed decimal integer	   
%d	signed decimal integer	   
%u	unsigned decimal integer	   
%o	octal integer	   
%x	hexadecimal integer(lowercase letters)	   
%X	hexadecimal integer (UPPERcase letters)	   
%e	exponential notation (with lowercase ‘e’)	   
%E	exponential notation (with UPPERCASE ‘E’)	   
%f	floatin point real number	   
%g	the shorter of %f and %e	   
%G	the shorter of %f and %E	 
"%.2f" %(1.6352) => 1.64


Other symbols and their functionality

 
*	argument specifies width or precision	   
-	left justification	   
+	display the sign	   
<sp>	leave a blank space before a positive number	   
#	add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.	   
0	pad from left with zeros (instead of spaces)	   
%	'%%' leaves you with a single literal '%'	   
(var)	mapping variable (dictionary arguments)	   
m.n.	m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)	 

Format Method
type = output type: 
1: STRING (s);
2: INTEGER (b-binary, c-char, d-decimal, o-octal, x-hexadecimal with lowercase, x-hexadecimal with upercase, n-locale sensitive for thousand decimal)
3: FLOATING (e-exponent use e as separator, e-exponent use E as separator, f-fixed point lowercase, F-fixed point uppercase, g-general format lowercase, G-general format uppercase, n-local sensitiver for thousand separator, %-percentage)
Ex: Formatted="{:d}" print(Formatted.format(7000)) => 7000
Formatted="{:,d}" print(Formatted.format(7000)) => 7,000
Formatted="{:^15,d}" print(Formatted.format(7000)) => 7,000 #central
Formatted="{:^15,d}" print(Formatted.format(7000)) => 7,000*
Formatted="{:^15.2f}" print(Formatted.format(7000)) => 7000.00
Formatted="{:>15X}" print(Formatted.format(7000)) => 1B58
Formatted="{:<#15x}" print(Formatted.format(7000)) => 0x1b58
Formatted="A {0} {1} and a {0} {2}" print(Formatted.format('blue', 'car', 'truck')) => A blue car and a blue truck
	     "{:.2f}".format(1.23456) => 1.23

format(1.6345, '.2f')) => 1.63
-----------------------------------
letter = "Text ... {0}, {1} ... "
letter.format("Name","Surname","123")
--------------------------------------
a = "text ... {} ...{} ...text".format(3, "text")
-------------------------------------------------
s = "{var1} ...{var2} ...{varn}"
s.format(var1 = "un_text", var2 = 3, ... varn = "alt text")
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
OLD STYLE
"<FORMAT>" % (<VALUES>)
"text ... %s..." % "Textul de inlocuit al pozitia %s"
"text ... %d ...%s..." % (10, "Name")
-------------------------
n1 = 3
n2 = 4
"text %d ... %d ..." % (2*10, n1, ...)
====================================
Accesing value
string = "Hello"
string[4] :=> o
string[1:3] :=> el (adica 1 si 2, exclusiv 3)

Update a string
string_1 = string +"Un alt text"
Syntax
str.center(width [, fillchar])

Parameters
width = 
fillchar = 

Description
Return Value


Example

print("100".center(10, "-")) 
# rezulta:  ---100----





