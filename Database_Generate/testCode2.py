

class testInherit:

    def __init__(self):
        from print_labels import print_label

        full_dict = {
                    'daterecieved': 'daterecieved',
                    'poploadslip' : 'poploadslip',
                    'count' : '1' ,
                    'tm9_ticket' : 'tm9_ticket',
                    'disposition_fmanum' : 'disposition_fmanum',
                    'owner' : 'ownerName',
                    'haulingcontractor' : 'hauled by',
                    'numpcsreceived' : 'num of pieces',
                    'blocknum' : 'Block Number'
                   }
        print_label(full_dict).add_SampleLoad_text()
        print_label(full_dict).add_LoadReceived_text()

if __name__ == '__main__':
    testInherit()
