WeighOut_dict = {
            'tareweight': self.tare_weight,
            'netweight' : self.net_weight,
            'timeOut'   : timeOut_now
           }

columns = WeighOut_dict.keys()
values = [WeighOut_dict[column] for column in columns]

insert_statement = 'INSERT INTO testscale (%s) VALUES %s WHERE tareweight IS NULL AND trucknum = %s;'
strng = 'test'
A = self.cur1.mogrify(insert_statement, (AsIs(','.join(columns)), tuple(values)))
