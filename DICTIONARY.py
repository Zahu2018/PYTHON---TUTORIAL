DICTIONARY(#dictionary, #dict, #dictionar) dict = {'key':'value'}
	dict={'key':'value'}
	dict.items() --> list of tuplet
	dict.keys() 
	dict.values() 
	dict.pop('key' [, default]) fara default => KeyError
	dict.popitem() 
	dict.setdefault('key' [, value_default=None]) = returneaza sau adauga
	dict.update([secventa]) = d.update('un', 'na') => 'u':'n'//d.update(red=1) 
	dict.clear()
	dict.copy() =
	dict.fromkeys(secventa [, valoare = deafault None])
	dict.get(key [, default=None])
	- - - - - - - - - - - - - - - - - - - - - - - - - - -
	len(dict)
	len(dictview)
	del dict['key']
	dict(secventa) 
	iter(dict) 
	iter(dictview) 
	dict['key']
	dict['key']=valueNew
	dict['key']=value 
		
	list(dict)
	list(dict.keys())
	list(dict.values())
	sorted(dict.keys())
	dict = zip(lista_1, lista_2)

dict={'key':'value'} # Ex: dict={'unu':1, 'doi':'doi', 3:'trei', 4:4}, doua key cu aceeasi valoare=ultima castiga, key poate fi: tuple, string, dict. NU: list,
dict.items() = returneaza o lista de tupleti din key, value (e un "dictview"). #Ex: dict_items([('sape', 20), ('guido', 30)])
dict.keys() = returneaza o lista  din key of dictionar (e un "dictview") #Ex: dict_keys(['guido', 'sape'])
dict.values() = returneaza o lista  din valorile dictionarului (e un "dictview") #Ex: dict_keys(['guido', 'sape'])
dict.pop('key' [, default]) = returneaza si sterge key daca este in dictionar, altfel returneaza default. Daca nu este default => KeyError
dict.popitem() = returneaza si sterge un element ales arbitrar din dictionar. Daca dictionar gol => KeyError
dict.setdefault('key' [, value_default=None]) = returneaza valoare key daca este in dictionar. Daca nu, este adauga un nou element 'key':default. Daca default nu este specificat, default = None; Ex dict.setdefault(key, value); dict.setdefault('alfa':1)
dict.update([secventa]) = update la un dictionar cu perechi din secventa (tuple sau iterabile de doua caractere), rescrie keyile existente. returneaza None. Daca are argumente update se face cu acelea #Ex: d.update(red=1, blue=2) Ex: d.update('un', 'na') => 'u':'n'; dict_1.update(dict_0) etc. Adauga un dictionar la un altul deja existent. 
dict.clear() = sterge toate elementele din dictionar
dict.copy() = return a shallow (superficial) copy a dictionarului. Cand se modifica dict principal se modifica si dictionarul copie
dict.fromkeys(secventa [, valoare]) = creaza un nou dict cu key din secventa si valori setate de valoare. Daca valoarea nu e setata atunci e None.
dict.get(key [, default=None]) #returneaza valoarea key daca este in dictionar, altfel 'default'. Daca 'default' nu este data este None. nu ridica erori

len(dict) #returneaza nr. de elemente dintr-un dictionar dict
len(dictview) #returneaza nr. de elemente dintr-un "dictview" (dict.items(), dict.keys() sau dict.values())
del dict['key'] #sterge o pereche key / value din dictionar
dict(secventa) #creaza un dict dintr-o secventa. Ex: dict([('unu', 100), ('doi', 200), ('trei, 300')])- sau - dict(unu=1, doi=2)
iter(dict) #returneaza un iterator din keyle dictionarului. Shortcut pentru: iter(d.keys())
iter(dictview) #returneaza un iterator din keyile, values or items in "dictview" (dict.items(), dict.keys() sau dict.values())
dict['key'] #returneaza valoarea key, daca key e in dictionar, altfel eroare
dict['key']=valueNew #update a valorii (schimba valoarea veche din dict cu valueNew) daca key exista in dict
dict['key']=value #adauga un nou element la dictionar, daca key nu exista in dict, altfel face update
key in dict #daca key in dict True, altfel False
key  not in dict #daca key not in dict True, altfel False
x in dicview #retuneaza True daca x este in elemente, key, valori. In element trebuie sa fie tuplet (key, value) DICTVIEW = dict.keys, dict.values, dict.items = view objects
x not in dicview #retuneaza True daca x nu este in elem, key, valori. In elem. trebuie sa fie tuplet (key, value)
x in dict.values # daca x este prezent in valori

list(dict) # returneaza o lista cu tupleti din keys, values
list(dict.keys()) #returneaza o lista cu keys
list(dict.values()) # returneaza o lista cu values
sorted(dict.keys()) #sorteaza keys
dict = zip(lista_1, lista_2) # rezulta o lista cu tupleti din care se face dict

ERRORS
KeyError '...'   = cand key nu este in dictionar
KeyError 0      = cand vrei sa accesezi ca intr-o lista (dictionarul nu este in ordine)
TypeError       = cand o lista este key (NU SE POATE)

1. NU POT FI DOUA KEY CU ACELASI NUME
2. KEY NU POATE FI LISTA, KEY E IMUTABIL, POATE FI string, number, tuple

ACCESARE - CITIRE
dict['key']  #rezulta valoarea
dict[dict1][dict2][...] # return val. keyii din dict... din dict2 din dict1 din dict
dict_1[dict_2['key']] # 1. valoarea corespunzatoare lui key din dict_2 devine key pt. dict_1 si afiseaza value
		      #E foarte bun pentru mapare: rom_judete{'salaj':sj, 'bihor':bh, ...}
						  sj = {'simleu':100, 'zalau'"200, ... }, etc
from dictionar.py import dict1
dict1['key']  #importam dictionarul dict1 din fila dictionar.py si ...

for item in dict:
	print(dict[item])

dict[key]  (if not exist => KeyError)
dict.get(key[, default]) (if not exist default, or None => No Error - silent mode)
if key in dict 
ADAUGARE
dict['key'] = value #adaugam la dict(ionar) o noua key / value
dict.setdefault(key [, value]) # daca key nu este in dict se adauga o noua pereche key: value in dict
COPIERE
dict_new = dict_old.copy() # face o copie a dict_old dar cu un alt nume (dict_new)

CREARE
dict = {}
dict = dict()
dict = zip(lista_1, lista_2) # rezulta o lista cu tupleti din care se face dict (primul cu primul, al doilea ...) Ex: list(zip(lista_1, lista_2)) /sau/ dict(list(zip(lista_1, lista_2))) - ZIP  este un ITERATOR care se epuizeaza dupa ce e folosit - nu este o lista
dict([('key1', 10), ('key2', 20), ('key3', 30)]) # rezulta dict = {'key1': 10, 'key2':20, ... }
dict(key1 = 10, key2 = 20, key3 = 30)  # rezulta {'key1': 10, 'key2':20, ... }
{x: X**2 for x in (2, 4, 6)}  # rezulta {2:4, 4: 16, ... }

( COUNTING )
dictionar = {'alfa':1, 'beta':2} # creezi un dictionar din alt dictionar
dictionar_count = {}
for element in dictionar:
    dictionar_count[element] = count.get(element, 0) + 1
print (count)

DELETE
del dict['key'] # sterge itemul din dict
dict.clear() #goleste dict de itemi
del dict()  #sterge dictionarul dar va rezulta o eroare

INCREMENT VALUES
for key, value in d_old.items():
    value = value*2
    d_new.setdefault(key, value)


INVERSARE DICTIONAR
d0 = {}
d1 = {1 : 'unu', 2 : 'doi', 3 : 'trei'}
for key, value in d1.items():
    d0.setdefault(value, key)
print(d0)


LOOPING - ITERATOR
ITERATORII SE EPUIZEAZA DUPA CE SUNT FOLOSITI !!!
for key, value in dict.items():
    print(key, value)

READ DICT FROM FILE
import dict_fm # e dict_fm.py
print(dict_fm.dicti) # dicti = {'fd':'dd', ...} = dictionarul din fila dict_fm.py
------------------------
import csv
csvfile = csv.reader(open('aero.csv'))
var = dict(csvfile)

aero.csv
	"ddd","ew"
	"fdsa","dsa"
---------------------------
f = open('somefile.csv')
reader = csv.DictReader(f, (airport, iatacode))
for row in reader:
   print row

airport   | iata_code
_______________
aberden | abd

SORTARE ALFABETICA
for item in sorted(dict, key = len):
	print(item, dict[item])
----------------------------------------
for key,value in sorted(dic.items()):

UPDATE VALUE AND DICTIONARY
UPDATE A DICTIONARY WITH A NEW VALUE
dict['key'] = value  # ('value', cu ghilimele daca e string) adauga un nou element la dictionar
UPDATE A DICTIONARY WITH ITEMS FROM OTHER DICTIONARY
dict_1.update(dict_2)  # adauga itemii din dict_2 in dict_1
dict.update({key:value}) #adauga item la dict, sau daca exista face update la 
UPDATE // ADD A VALUE IN A DICTIONARY (CHANGE VALUE OF A KEY IN A DICT - allready exist)
dict.update(y=2, z=4, key = "John") # key sa fie fara ghilimele
dict['key'] = valoare #key sa fie cu ghilimele = str(key); pt. iteration








Ex_1:  - CREAZA DICTIONAR DIN FOR LOOP
di = {}
for nr, file in enumerate(listdir()):
	#deschide fila

	a = open(file, "r")
	last_line = a.readlines()[-1]
	di[file] = last_line
print(di)

Ex_2: DICTIONARE 
dict = {'SJ':{'Simleu':{'populatie':1250, 'segmente':10},
                 {'Uileac':{'populatie':500, 'segmente':2}},
          {'BH':{'Oradea':{'populatie':152652, 'segmente':52}}}
#ACCESARE SIMPLA DACA ACESTE REZULTATE SUNT INTR-UN FISIER CU NUMELE census.py
import census
census.allData['SJ']['Simleu'] # => {'populatie':1250, 'segmente':10} #allData pentru ca asa este numit dictionarul 
census.allData['SJ']['Uileac']['populatie'] # => 500 # spui de fapt: fisierul census > dictionarul allData > itemul SJ > itemul > Uileac > itemul pop

