x = 10
y = 20
z = 30
a = 100
# positional arguments
def find_max(a,b,c):
    if a > b and a > c:
        print('x is greater')
    elif b > c :
        print('y is greater')
    else:
        print('z is greater')

#find_max(10,20,30)

# named argument functions/default functions

def find_max_default(a, b, c = 10):
    if a > b and a > c:
        print('x is greater')
    elif b > c:
        print('y is greater')
    else:
        print('z is greater')

#find_max_default(10,20,200)

x = 10
y = 20
z = 30


def find_max_default(a=10, b = 200 , c=1000): ##  Positional argument after keyword argument
    if a > b and a > c:
        print('x is greater')
    elif b > c:
        print('y is greater')
    else:
        print('z is greater')

find_max_default ()


def connect_db(url,user='mahesh',password='abc@123',db_name='ganaseva')


connect_db('localhost:123',db_name='atyati')


