import datetime as dt
import csv
import itertools

class ExtractCSV:

    def __init__(self,connect_instance,fname,month,year):
        self.fname = fname
        self.month = month
        self.year = year
        self.connect_instance = connect_instance
        self.cur = connect_instance.crsr()
        self.ListInit = []
        self.lstpopinit = ['726','720','730','740','750','760','780','785']
        self.initializeLists()

        self.cur.execute("""SELECT *
                            FROM barkies_db
                            WHERE daterecieved::date >= %s AND daterecieved::date <%s;""",(dt.date(self.year,self.month,1),
                            dt.date(self.year,self.month+1,1)))
        self.full_DB_list = self.cur.fetchall()

    def _replaceSample(self,x):
        if x == '':
            return 'N'
        elif x == 'SAMPLE':
            return 'Y'
        else:
            return x

    def WriteGovCSV(self):

        self.full_DB_list = self.cur.fetchall()
        millnum=8641
        month_year = str(self.month) + str(self.year)
        lst_indx1 =[1,6,7]
        lst_indx2 =[8,2,14,15,16,4,3]

        lst_gov =[]
        for row in full_DB_list:
            a = [row[i] for i in lst_indx1]
            c = [row[i] for i in lst_indx2]
            b = [millnum] + a + [month_year] + c
            sample = b[-1]
            if sample == 'SAMPLE':
                sample = 'Y'
            else:
                sample = 'N'
            b[-1] = sample
            lst_gov.append(b)

            self.write_to_Csv(lst_gov)

    def WriteHaulSummaryCSV(self):

        indx = [x for x in range(5,len(self.full_DB_list[0])-4)]
        tot_list = []
        for row in self.full_DB_list:

            lst_loadslip = [None]*8
            lst_tm9 = [None]*8
            lst_intpop = map(int,self.lstpopinit)
            lst_loadslip[lst_intpop.index(row[1])]=row[1]
            lst_tm9[lst_intpop.index(row[1])] = row[4].strip('\n')
            lst_remain = [row[i] for i in indx]
            print lst_remain
            lst_remain[-2] = int(lst_remain[-2].strip('\n'))
            if row[3] == 0:
                lst_sample = [None]
            else:
                lst_sample = ['SAMPLE']

            rown = [row[0]] + lst_loadslip + lst_sample + lst_tm9 + lst_remain

            tot_list.append(rown)
        print rown

        self.write_to_Csv(tot_list)

    def WriteVbySCSV(self):
        indx = []
        DB_list = ['daterecieved',
                    'poploadslip',
                    'count',
                    'sampleloads' ,
                    'tm9_ticket',
                    'owner' ,
                    'disposition_fmanum' ,
                    'workingcircle' ,
                    'blocknum',
                    'loggingco' ,
                    'haulingcontractor',
                    'truckplate',
                    'trucknum' ,
                    'truckaxle' ,
                    'grossweight',
                    'tareweight',
                    'netweight' ]

        rows=sorted(self.full_DB_list)
        sorted_list = map(list, itertools.izip_longest(*rows))
        sorted_list = [sorted_list[i] for i in indx]
        dict_for_write = dict(zip(self.Edit_DD_lst,DB_list))

    def initializeLists(self):


        GovCSVList = ['Mill Number','Population #','Disposition','Working Circle',
        'Month/Year','Cut Block','Load Number','Gross','Tare','Net','TM9 Number','Sample']


        listheader1 = ['Owner','Disposition/FMA#','Working Circle',
        'Block #','Logging Co.','Hauled By','Truck License Plate #',
        'Truck #','Truck Axle','Gross Weight','Tare Weight','Net Weight','Received # of Pieces']

        listheader2 = []

        lstpopnum = []
        lsttm9 = []

        for entr in self.lstpopinit:
            popnum = ''.join(['pop. ',entr,' Load slip #'])
            tm9 = ''.join(['pop. ',entr,' TM9 #'])
            lstpopnum.append(popnum)
            lsttm9.append(tm9)
        list_barkies_hauling = ['Date'] + lstpopnum + ['Sample Loads'] + lsttm9 + listheader


        self.ListInit.append(GovCSVList)
        self.ListInit.append(list_barkies_hauling)

    def create_dict(self):


    def write_to_Csv(self,lst):
        with open(self.fname, "wb") as f:
            writer = csv.writer(f)
            writer.writerow(self.ListInit[1])
            writer.writerows(lst)
