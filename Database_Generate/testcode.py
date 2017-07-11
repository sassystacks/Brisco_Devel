import itertools
from Connect_Brisco_DB import Connect_DB
from psycopg2 import sql

def initializeLists(table,cur1):

    query = 'select * from "{}"'.format(table)
    cur1.execute(query)
    rows = cur1.fetchall()
    rows=sorted(rows)
    sorted_list = map(list, itertools.izip_longest(*rows))
    return sorted_list

Connect_Brisco_DB = Connect_DB('postgres','postgres','192.168.0.200','coffeegood')
cur = Connect_Brisco_DB.crsr()

init_list_truck = initializeLists('truckers_db',cur)
init_list_owner = initializeLists('owner_db',cur)

print init_list_truck[0]
print(type(init_list_truck[0]))
