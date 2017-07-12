
tst_lst = []
for x in range(5):
    Weighin_dict = {
                'daterecieved': 23+x,
                'poploadslip' : 54,
                'count' : 45*x,
                'sampleloads' : 34,
                'tm9_ticket' : 1*x,


               }
    tst_lst.append(Weighin_dict)

print tst_lst
tm9_indx = next(index for (index, d) in enumerate(tst_lst) if d['tm9_ticket'] == 0)

print tm9_indx

a = tst_lst[tm9_indx]
for key in a:
    print(a[key])
    print(key)
