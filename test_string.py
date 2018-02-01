Bots=['asdwa','wadas','cwa','qwer','erty']

search_val='wadas'

x=0
k=0
for val in Bots:
    if val == search_val:
        k=x
    x=x+1

print(k)