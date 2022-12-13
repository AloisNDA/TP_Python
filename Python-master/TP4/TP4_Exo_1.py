from ast import literal_eval
from decimal import*
table = []
n = literal_eval(input("Qu'elle table de multiplication souhaitez-vous ?"))
for i in range(11):
    table = n*i
    print(f"{n}*{i} = ","%.1f" % table)