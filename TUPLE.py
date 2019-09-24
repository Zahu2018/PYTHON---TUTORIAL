TUPLE (#tuple) tuple = (item)
    tuple.index(item)
    tuple.count()

Tuple
(mutable-imutable, generalitati, metode aplicabile, slice-ing, prelucrarea datelor)
IMUTABLE # ramane asa cum a fost creat la inceput (no update, remove el, ...)
tuple_empty = ()
tuple_1 = ('fizica', 'chimie', 1997, 2000)
tuple_2 = (1, 2, 3, 4, 5, 6)
tuple_3 = 'a', 'b', 'c'
tuple_4 = (50,) # trebuie folosita virgula chiar daca este doar o singura valoare


# 1. Sunt mai rapide ca listele
# 2. Sunt sigure, nu le poti modifica din greseala
metode:
cmp(tuple_1, tuple_2) # Nu exista in PYTHON3 <=> ((a>b)-(a<b))
if tuple are the same type (numers) > compare > = 1 # sum of elem. in tuple_1 > tuple_2
						    0 # sum of elem. tie (egal)
			        	   		   -1 # sum of elem. in tuple_1 < tuple_2
if tuple are the same type (char) > compare > = 	1 # sum nr of lett. in tuple_1 > tuple_2 (z>a)
daca suma numerelor ce reprezinta   		0 # sum nr of lett. tie (egal) (z>a)
literele (nu nr de char) este mai mare (a>A)=>   -1 # sum nr of lett. in tuple_1 < tuple_2 (z>a)
"1" < "A" < "a" //  "AAA" < "yy" 

tuple.index(item) - afiseaza indexul la care se gaseste itemul
tuple.count(item) - return the number of items that is equal to item

len(tuple) - afiseaza lungimea listei (nr de elemente)
min(tuple) - afiseaza minimul din lista
max(tuple) - afiseaza maximul din lista
all() - return True if all elements of tuple are true (or the tuple is not empty)
any() - return True if any element of tuple is true; if tuple empty -->False
enumerate() - 
sorted() - 
sum() - sum of all elements in tuple

tuple[start: end] - feliaza o lista (slice) intre indexul (start / end)
tuple(list) - transforma o lista in tuplet [, sau tuple(secventa)]

Exemple de tupleti:
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

Accesing value
tuplet = (‘a’,’b’,’c’,’d’,’e’)
tuplet[2] :=>c
tuplet[1:4] :=> b, c, d

Operation with tuplet (basic operation)
 
Description	Python Expression	Results	   
Length	len((1, 2, 3))	3	   
Concatenation	(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	   
Repetition	('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	   
Membership	3 in (1, 2, 3)	TRUE	   
Iteration	for x in (1,2,3) : print (x, end = ' ')	1 2 3	 

Index, slicing and matrix
tuplet = (‘a’,’b’,’c’,’d’,’e’)
 
Python Expression	Results	Description	   
tuplet[2] 	c	Offsets start at zero	   
tuplet[-1]	e	Negative: count from the right	   
tuplet[1:]	b, c, d, e	Slicing fetches sections	 


Update tuple
1. Nu poate fi update-up
2. Se poate crea un nou tuplet pt. a simula un update
tuplet = tuplet_1 + tuplet_2 (elementele dorite)

Delete tuple element
1. Nu poate fi update-up
2. Se poate crea un nou tuplet fara elementele dorite
tuplet = tuplet_1 - tuplet_2 (elementele dorite)
del tuplet # sterge intreg tupletul (ca variabila)


LOOP
for i, j in enumerate(['a', 'b', 'c']):
    print(i, j)  # rezulta 0 a; 1 b; 2 c (i este un numar cu incepere de la 0; j este valoarea din tuple sau list)

===================
input = [("Mary", 27), ("Joe", 30), ("Ruth", 43), ("Bob", 17), ("Jenny", 22)]

youngPeople = []

for (person, age) in input:
    if age < 30:
        youngPeople.append(person)
    else:
        print("HAHA " + person + " is too old!")

print("There are " + str(len(youngPeople)) + " young people")
print(youngPeople)
========================