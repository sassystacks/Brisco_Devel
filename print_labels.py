from PIL import Image, ImageFont, ImageDraw
import os

class print_label:

    def __init__(self,*args):

        self.font_large = ImageFont.truetype(
            "/usr/share/fonts/truetype/droid/DroidSans-Bold.ttf", 26)
        self.font_small = ImageFont.truetype(
            "/usr/share/fonts/truetype/droid/DroidSansMono.ttf", 22)
        self.BLACK = 0,0,0
        self.full_dict = args[0]

        self.DB_list = ['daterecieved',
                    'poploadslip',
                    'count',
                    'tm9_ticket',
                    'owner' ,
                    'disposition_fmanum' ,
                    'blocknum',
                    'haulingcontractor',
                    'numpcsreceived',
                    ]
        self.inc_row = 40

    def add_SampleLoad_text(self):
        img_Sample = Image.new("RGB", (578, 271), "white")

        indxSample = [0,1,2,3,5]
        Sample_dict = self.extract_dicts(indxSample)
        loadNo = Sample_dict['poploadslip'] + "-" + Sample_dict['count']
        draw = ImageDraw.Draw(img_Sample)

        lst_titles = ["Load No.:", "TM9 No. : ", "Source  :", "Date    :"]

        lst_keys = ['ignore',3,5,0]
        row = 0

        for x in xrange(len(lst_titles)):
            draw.text((0,row), lst_titles[x] , self.BLACK, font = self.font_small)
            if x == 0:
                draw.text((150,row), loadNo , self.BLACK, font = self.font_large)
            else:
                draw.text((150,row), Sample_dict[self.DB_list[lst_keys[x]]] , self.BLACK, font = self.font_large)

            row = row + self.inc_row

        img_Sample.save('testSample.png')
        os.system("brother_ql_create --model QL-720NW ./testSample.png > testSample.bin")

    def add_LoadReceived_text(self):

        img_Load = Image.new("RGB", (578, 271), "white")
        indxLoadReceived = [0,1,2,3,4,6,7,8]

        Load_dict = self.extract_dicts(indxLoadReceived)

        loadNo = Load_dict['poploadslip'] + "-" + Load_dict['count']

        draw = ImageDraw.Draw(img_Load)

        lst_titles = ["Date           :" ,"Contractor     :" ,"TM9 No.        :" ,
                        "Brisco Load #  :","Block/Opening #:","# of Pieces    :" ,
                        "Hauler         :"]
        lst_keys = [0,6,3,'ignore',6,8,7]

        row = 0
        for x in xrange(len(lst_titles)):
            draw.text((0,row), lst_titles[x] , self.BLACK, font = self.font_small)
            if x == 3:
                draw.text((250,row), loadNo , self.BLACK, font = self.font_large)
            else:
                draw.text((250,row), Load_dict[self.DB_list[lst_keys[x]]], self.BLACK, font = self.font_large)

            row = row + self.inc_row

        img_Load.save('testLoad.png')
        os.system("brother_ql_create --model QL-720NW ./testLoad.png > testLoad.bin")

    def extract_dicts(self,*args):

        indx = args[0]

        keys = [self.DB_list[i] for i in indx]
        dict_to_print ={x:self.full_dict[x] for x in keys}
        return dict_to_print
        
if __name__ == '__main__':
    print_label()
