
from Connect_Brisco_DB import Connect_DB

Connect_Brisco_DB = Connect_DB('postgres','postgres','192.168.0.200','coffeegood')
cur1 = Connect_Brisco_DB.crsr()
cur1.execute("DELETE FROM testscale")
