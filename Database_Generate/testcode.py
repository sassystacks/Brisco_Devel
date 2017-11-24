
full_dict = {
            'daterecieved': 'entry daterecieved',
            'poploadslip' : 'entry poploadslip',
            'count' : 'entry 1' ,
            'tm9_ticket' : 'entry tm9_ticket',
            'disposition_fmanum' : 'entry disposition_fmanum',
            'owner' : 'entry ownerName',
            'haulingcontractor' : 'entry hauled by',
            'numpcsreceived' : 'entry num of pieces',
            'blocknum' : 'entry Block Number'
           }
DB_list = ['daterecieved',
            'poploadslip',
            'count',
            'sampleloads' ,
            'tm9_ticket',
            'owner' ,
            'disposition_fmanum' ,
            'blocknum',
            'haulingcontractor',
            ]

indxSample = [0,1,2,4,6]

keys = [DB_list[i] for i in indxSample]
A ={x:full_dict[x] for x in keys}
print(A)
