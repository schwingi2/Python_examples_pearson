
# Beispielsammlung pearson.py
def run_example(which_example):
    if which_example==beispiel1:
        decodestring1='blupluplup1'
        beispiel1(decodestring1)
    elif which_example == beispiel2:
        decodestring2='blupluplup2'
        beispiel2(decodestring2)
    elif which_example == beispiel3:
        beispiel3()

#Beispiel 1 für Sicherstellung von UTF8 Datentypen

# bytes-Instanzen enthalten immer reine 8-Bit Werte, str Instanzen 
# beinhalten hingegen Unicode Zeichen

def beispiel1(bytes_or_string):
    if isinstance(bytes_or_string,bytes):
        value=bytes_or_string.decode('utf-8')
    else:
        value=bytes_or_string
    print(value)
    return value #string-Instanz

#Beispiel 2 für Sicherstellung von byte Datentypen

# bei str handelt es sich immer um Unicode-Datentypen, 
# denen keine Textkodierung zugewiesen ist
def beispiel2(bytes_or_string):
    if isinstance(bytes_or_string,str):
        value=bytes_or_string.encode('utf-8')
    else:
       value=bytes_or_string
    print(value)
    return(value)

#Beispiel 3 Listenzugriff und -manipulation

a=[1,2,3,4,5,6,7,8,9,10]
type(a)
print(type(a)==list)
b=a
b_new=[x**2 for x in b]
b_new1=[x**0.5 for x in b_new]

#Beispiel 4 Dictionaries und Sets - repariere Dictionary/ vertauschte Keys und Values

obst={'Apfel':1,'Banane':2,'Pfirsich':3,'Kirsche':4}
repaired_dict1={x:name for name, x in obst.items()}
#Länge der Einträge - werden als set gespeichert
length={len(name) for name in repaired_dict1.values()}

#Beispiel 5 Mache Matrix "flat"

matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat= [x for row in matrix for x in row]

#Beispiel 6 Zugriff auf die Elemente einer Matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]
squared_matrix=[[x**2 for x in row] for row in matrix]
squared_matrix1=[x**2 for row in matrix for x in row]

#Beispiel 7 Selektion bzw. Filterung aus einer Matrix

a=[1,2,3,4,5,6,7,8,9,10]
b=[x for x in a if x >4 if x % 2 == 0]
c=[x for x in a if x > 4 and x % 2 == 0]

#Beispiel 8a basics of generators explained:
#A generator is like return with a little magic
#https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/

def simple_generator_function():
   yield 1
   yield 2
   yield 3
#And here are two simple ways to use it:

for value in simple_generator_function():
    print(value)
#>1
#>2
#>3
our_generator = simple_generator_function()
next(our_generator)
1
next(our_generator)
2
next(our_generator)
3

#Beispiel 8b Datei erzeugen und mit Generator auslesen
#Die von den Generatoren zurückgelieferten Iteratoren sind zustandsbehaftet und dürfen nicht mehrfach verwendet werden
#Im vorliegenden Beispiel besteht das Problem, dass in file1 strings eingelesen werden, mit denen keine Rechenoperationen 
#möglich sind.

file1 = open("TestFile1.csv","w")
for i in range(0,10+1):
        if i == 0:
            file1.write("example_variablename;\n")
        else:
        #print(i)
            file1.write(str(i))
            file1.write(";\n")
file1.close()

it=(x for x in open('TestFile1.csv'))
print (it)
print(next(it))

#csv Datei einlesen: z.B. mit pandas module - generiert data frame, der z.B. i.V.m. Seaborn verwendet werden kann
import pandas as pd

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df = pd.read_csv('TestFile1.csv', delimiter=';')
