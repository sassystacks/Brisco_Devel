# from Connect_Brisco_DB import Connect_DB
# from DB_searchandFill import DB_search
# import csv
#
# Connect_Brisco_DB = Connect_DB('postgres','postgres','192.168.0.200','coffeegood')
# cur1 = Connect_Brisco_DB.crsr()
#
#
# cur1.execute('SELECT * from barkies_db;')
#
# rows = cur1.fetchall()
#
# b = [12,11,10,13]
#
# new_trucker_list = []
# for row in rows:
#     trucknum = row[12]
#     c = [ row[i] for i in b]
#
#     if not new_trucker_list:
#         new_trucker_list.append(c)
#
#
#
#     else:
#         a = [sublist[0] for sublist in new_trucker_list]
#         if trucknum  not in a:
#             new_trucker_list.append(c)
#
# print(new_trucker_list)
# print(len(new_trucker_list))
#
# with open("trucknum.csv", "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(new_trucker_list)
#
a = []
mylist=[['a', 9, 3], ['we', 2], ['will', 2, 10], ['x', 4], ['z', 4]]
for sublist in mylist:
    sublist = sorted(sublist, reverse=True)
    a.append(sublist)
print(a)
