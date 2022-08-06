# input
# val = input("Dati o valoare: ")
# print("Valoarea citita:", val)
# print("Tipul valorii:", type(val))

# input int
# val_int = input("Dati o valoare intreaga: ")
# nr = int(val_int)

# # nr = int(input("Dati o valoare intreaga: "))

# print("Valoarea citita:", nr)
# print("Tipul valorii:", type(nr))

# input float
# val_float = input("Valoare float: ")
# nr_float = float(val_float)

# nr_float = float(input("Valoare float: "))

# print("Valoarea citita:", nr_float)
# print("Tipul valorii:", type(nr_float))

# input complex
# val_complex = input("Valoare complex: ")
# nr_complex = complex(val_complex)

# # nr_complex = complex(input("Valoare complex: "))

# print("Valoarea citita:", nr_complex)
# print("Tipul valorii:", type(nr_complex))


## f-string
# x = 3.554
# y = 5.1
# z = 2.000002
# print("x egal cu " + str(x) + " ,y egal cu " + str(y) + ", z egal cu " + str(z))
# print(f"x egal cu {x:.2f}, y egal cu {y:.2f}, z egal cu {z:.2f}")

# nume1 = "George"
# nume2 = "Andrei"
# nume3 = "Mihaela"
# print(f"{nume1.rjust(20)}, {nume2.ljust(20)} și {nume3.center(20)} sunt colegi la facultate")

## slicing
my_string = "this is a string"
my_list = [4, 5, 2, 6, 1, 4, 23]

# print(my_string[2:5])
# print(my_list[2:5])

# print(my_string[:5])
# print(my_string[5:])

# print(my_list[2:10:2])
# print(my_string[10:2:-1])
# print(my_string[10:2:-2])

# # lista  [4,   5,   2,   6,   1,   4,  23]
# # indice  0    1    2    3    4    5    6
# # indice  -7   -6   -5  -4   -3   -2   -1

# print(id(my_string), id(my_string[3:6]))

## extragerea unui element
my_tuple = (0, 1, 2, 3, 5, 6, 7)
# x = my_string[5]
# elem = my_list[5]
# t1 = my_tuple[5]
# print(x, elem, t1)

# # my_string[5] = "a"  # eroare - tip imutabil
# my_list[5] = 99  # ok - tip mutabil
# print(my_list)
# my_tuple[5] = 99 # eroare - tip imutabil

#### obiecte in interiorul altor obiecte

# lista in lista
# l1 = [1, 2, 3, "abcd", "ceva", [5, 6, 7, [1, 2, 3]]  ]
# print(l1[5])

# print(l1[3].upper())
# l1[5].append(17)

# print(l1)

# # l1[5] = 4
# # print(l1)

# l1[5][0] = 10
# print(l1)



# print(l1[5][3][1])

# lista_interioara1 = l1[5]
# print(lista_interioara1[3][1])

# lista_interioara2 = lista_interioara1[3]
# print(lista_interioara2[1])

# tuplu in lista
new_list = [1, 2, 3, (4, 5)]
# print(new_list[3][1])

# dictionar in lista
my_dict = {
    "cheie1": 1,
    "cheie2": 2
}
new_list.append(my_dict)
# print(new_list)

# print(new_list[4])
# print(new_list[4]["cheie1"])

# lista in dictionar
new_dict = {
    "cheie1": 1,
    "numere": [1, 3, 5, 2, 4, 6]
}
# print(new_dict)
# # new_dict["numere"] = 3
# print(new_dict)
# print(new_dict["numere"][3])
# new_dict["numere"].append([1, 2, 3])
# new_dict["numere"].append({"a": "aaa"})
# print(new_dict)

# print(new_dict["numere"][6][1])


## slicing (2)
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [1, 2, 3, 4, 5, 6, 7, 8]

print("Prima jumătate: ", list2[:(len(list2) + 1)//2])
print("A doua jumătate: ", list2[(len(list2) + 1)//2:])

# list2 
# lungimea 8    8 // 2 = 4
#          9    9 // 2 = 4

# list1
# lungimea 7    7 // 2 = 3
#          8    8 // 2 = 4

index = (len(list1) + 1) // 2
print("Prima jumătate: ", list1[:index])
print("A doua jumătate: ", list1[index:])


# .count() & .index()
new_tuple = (4, 6, 5, 6, 6, 7)
new_list = [10, 11, 12, 13]

print(new_tuple.count(6))
print(new_tuple.index(5))

print(new_list.count(12))
print(new_list.index(12))

# tupluri ca chei ale dicționarelor
d = {
    (0, 1): "ceva",
    (1, 2, 3): "altceva",
}
print(d[(0, 1)])

# 
my_set = {1, 2, 3, 4, 4, 5, 3, 2, 5, 6, 7}
# my_list = [1, 2, 3, 4, 4, 5, 3, 2, 5, 6, 7]
# my_set = set(my_list)

print(my_set)

if 2 in my_set:
    print("Există")

# my_set.add([1, 2, 3]) # eroare - se pot adăuga doar tipuri mutabile în set

# verificare mutabilitate
print(hash(15))
# print(hash(my_set))  # eroare - nu e imutabil

new_set = {100, 200, 300}
my_set.update(new_set)
print(my_set)

my_set.remove(100)  # dă eroare dacă nu există elementul
my_set.discard(100)  # nu dă eroare dacă nu există elementul

# operații cu mulțimi
my_set.union(new_set)  # toate elemente din ambele seturi
my_set.intersection(new_set)  # doar elementele comune ambelor seturi 
my_set.difference(new_set)  # elementele care sunt în my_set, dar nu și în new_set

# dictionare
new_dict = {
    "cheie1": 1,
    "numere": [1, 3, 5, 2, 4, 6]
}
print(new_dict.get("numere"))
print(new_dict.get("produse"))
print(new_dict.get("produse", "Nu există cheia"))
print(new_dict.get("produse", ""))

fructe = {
    "mere": 4,
    "banane": 5,
    "cheie1": 12
}
print(fructe.get("pere", 0))

new_dict.update(fructe)
print(new_dict)

# uniune
other_dict = new_dict | fructe
print(other_dict)

del(new_dict["cheie1"])

fructe1 = {
    "mere": 4,
    "banane": 5,
}
fructe2 = {
    "banane": 5,
    "mere": 4,
}
print(fructe1 == fructe2)

print(fructe.keys())
print(fructe.values())
print(fructe.items())


# functiile max și min
max1 = max(1, 2, 3, 4, 5)
max1 = max([1, 2, 3, 4, 5])
max1 = max((1, 2, 3, 4, 5))
print(max1)

min1 = min(1, 2, 3, 4, 5)
min1 = min([1, 2, 3, 4, 5])
min1 = min((1, 2, 3, 4, 5))
print(min1)

my_sum = sum([1, 23, 4, 5, 66])
print(my_sum)

l1 = [1, 23, 4, 5, 66]
my_avg = sum(l1) / len(l1)
print(my_avg)
