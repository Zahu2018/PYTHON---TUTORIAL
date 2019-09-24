LIST (#list, #lista) list = [item]
    list.append(item)
    list.extend(alta_lista)
    list.insert(pozitie, item)
    list.remove(item)
    list.pop() = sterge ultimul item din lista
    list.pop(pozitie)
    list.pop(obj) = list[-1])
    list.clear()
    list.index(item) --> Ex: (a=list.index(item))
    list.count(item)
    list.sort() --> crescator
    list.sort(key=None sau len, reverse=False) --> key=str.lower; reverse=True/False;
    list.reverse(
    list.copy() --> echivalent pt list.copy() <=> new_list[:]=old_list 
    - - - - - - - - - - - - - - - - - - - - - - - - - - -    
    FUNCTII = list, list(dict.keys()), list[index]=arg (update item),  
              del, len, max, min, sum, sorted
    SLICE   = list[a[,:z]

P  y   t h o n
0  1  2 3 4 5
-6-5-4-3-2-1

list=['item'] # Ex: list=['unu', 2]
list.append(item) = adauga un item la capatul listei (string, lista,etc.)
list.extend(alta_lista) = (extinde) adauga 'alta_lista' la 'list' (aduna doua liste) si rezulta intr-una (l1 + l2 e posibil)
list.insert(pozitie, item) = insereaza un 'item' la pozitia 'pozitie' data
list.remove(item) = sterge primul 'item' gasit din lista
list.pop() = sterge ultimul item din lista
list.pop(pozitie) = sterge item-ul de la pozitia 'pozitie' data.
list.pop(obj = list[-1]) = sterge (ultimul) item-ul din lista
list.clear() = sterge toti itemii din lista, lista devenind goala
list.index(item) = returneaza pozitia in lista a primului 'item' gasit (a=list.index(item)
list.count(item) = returneaza de cate ori 'item' apare in lista
list.sort() = sorteaza itemii dintr-o lista in ordine crescatoare
list.sort(key=None, reverse=False) = sorteaza itemii unei liste (key=str.lower,) (reverse=True sau False); sorteaza itemii unei liste in ordine crescatoare; if assing len to key then sort a list of words according to their lenght Ex:words=['girl','python','tutorial','boy','snake'] > words.sort(key=len) => ['boy', 'girl', 'snake', 'python', 'tutorial']

list.reverse() = inverseaza elementele dintr-o lista; primul e ultimul
list.copy() = returneaza o copie a listei; nu modifica lista originala ca si atunci cand ar fi lista_noua = lista_veche; echivalent pt list.copy() <=> new_list[:]=old_list 


del list[] = sterge itemii dintr-o lista; daca sunt parametrii, conform parametrilor (ex: [2: 4])
len(list)  = cate elemente are lista (lungimea listei)
max(list)
min(list)
sorted(list) #sorteaza crescator o lista de acelasi tip, doar numere, doar cuvinte
sum(list) # suma elementelor din lista

list(secventa) #transforma o secventa (sir, dictionar, etc) in lista
list(dict.keys()) #creaza o lista cu keile din dict
list[a[,:z]] #acceseaza un element la indexul a, sau mai multe de la a-z
list[index]=arg #update un element din lista la indexul dat, cu noul argument (arg)
*, +, in #repetition, concatenation, membership, (iteration se face cu for)

Basic operation on list
 
Operation	Example	Result	   
Length	len([1, 2, 3])	3	   
Concatenation	[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	   
Repetition	['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	   
Membership	3 in [1, 2, 3]	TRUE	   
Iteration	for x in [1,2,3] : print (x,end = ' ')	1 2 3	 

Index, slicing and matrix
lista = [‘a’,’b’,’c’,’d’,’e’]
 
Python Expression	Results	Description	   
lista[2] 	c	Offsets start at zero	   
lista[-1]	e	Negative: count from the right	   
lista[1:]	b, c, d, e	Slicing fetches sections	 


Accesing value - Slicing
lista = ['a','b','c','d','e']
lista[0] :=>a
lista[1:4] :=> b, c, d             #ultima exclusiv

for index, item in enumerate(lista): # enumerate permite preluarea indexului si elementului
    print(index, item)  # Ex: 0, a; 1, b; ...
Adding new value
lista = ['a','b','c','d','e']

Create a list
lista = list(range(1, 11, 2)) # si alte combinatii
string.split() # Ex: "pyton list tutorial".split()  =>['python','list','tutorial'] 

Comprehension list
[expression for var in seq] # return a list of the expression values when each var in a seq is used in expression

[expression for var in seq if condition] # return a list of the expression values when each var in the seq that satisfies the condition is used in the expression
i = [random.randint(2, 10) for i in range(11)] =>[10, 3, 9, 6, ...]
i = [i for i in range(200, 210) if i%2 == 0] => [200, 202, 204, ...]

Delete item
lista = ['a','b','c','d','e']
del lista[3] :=> lista = ['a','b','c','e']

UPDATE - Replace
lista = ['a','b','c','d','e']
lista[2] = 'X'     => lista = ['a','b','X','d','e'] # update a value that exist
lista[1:3] = [1, 2]     => lista = ['a', 1, 2, 'd', 'e']

lista[0] = value      #update/schimba elementul de la pozitia 0

lista.append(element) # update a lista cu un nou element

LOOP
lista_intrebari = ['a', 'b', 'c']
lista_raspunsuri = [1, 2, 3]
for i, j in zip(lista_intrebari, lista_raspunsuri):
    print("Care este {0}? Este {1}".format(i, j))

for f in sorted(set(lista_1)):
    print(f)


