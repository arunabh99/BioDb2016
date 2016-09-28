Excercise 3
# coding: utf-8

# In[ ]:

def my_print():
    import string
    alphabets='abcdefghijklmnopqrstuvwxyz'
    alphabets=string.ascii_lowercase
    concat=alphabets[2]+alphabets[4]+alphabets[6:10] 
    for a in concat:
        print(a)

my_print()


# In[ ]:

a=[1,2,3]

def first(a):
    if isinstance(a, tuple):
        val=a[0]
        print('tuple')
    elif isinstance(a, list):
        val=a[0]
        print('list')
    else:
        val=a
        print('value')
    
    return val

    
print(first(a))
    
    



# In[ ]:

#print(round(1234.56789, 1),round(1234.56789, 2),round(1234.56789, 3))


'1234.56789'.format(1,1)

a=1234.56789

print ('%.1f' % 1234.56789) 
print ('%.2f' % 1234.56789) 
print ('%.3f' % 1234.56789) 
print ('%E' % 1234.56789)

print("{0:.1f}".format(round(a,1)))
print("{0:.2f}".format(round(a,2)))
print("{0:.3f}".format(round(a,3)))

'1234.56789'.format('%E')



# In[ ]:

greetings = {
    'spanish': 'hola',
    'german': 'hallo',
    'english': 'good day',
    'american': 'howdy'
}

for key in  greetings:
    print(key,greetings[key])


# In[ ]:

pairs = [[1, 2], [3, 4], [5, 6]]

def get_seconds(pairs):
    second_list=[]
    for value in pairs:
        #print(value[1])
        second_list.append(value[1])
    return second_list
        
print(get_seconds(pairs))







# In[ ]:

power_levels = {
   'Christian': 9001,
   'Charlie': 6,
   'Nanditha': 6.1
}
   
   
   
def biggest_key(power_levels):
   max_val=max(power_levels.values())
   for key in power_levels :
       if ( power_levels[key]==max_val ):
           return( key)
   
print(biggest_key(power_levels))
   


# In[ ]:




def div7(num):
    quoRem = divmod(num,7)
    listofNum = []
    for x in range(quoRem[0]):
        listofNum.append(x*7)
    
    print(listofNum)


div7(29)





# In[ ]:

from itertools import chain

l = [[1,2,3],['a','b','c'],[7,8,9]]

print(list(chain(*l)))


# In[ ]:

from itertools import product

x = [1,2,3]
y = ['a', 'b']
print(product(x,y))

prod=product(x,y)

for p in prod:
    print(p)





# In[118]:

x = [1, 2, 3, 2, 3, 4, 3, 5]
x.remove(2)


# In[121]:




# In[122]:

x


# In[ ]:

x


# In[126]:

x = [1, 2, 3, 4]

for i in x:
    for j in x:
        if (j>i):
           print(i,j) 


# In[8]:

n=7
sum=0
for i in range(n+1):
 print(i)   
 sum=sum+i


# In[9]:

print(sum)


# In[ ]:



