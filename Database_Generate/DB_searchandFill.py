


class DB_search:
    def __init__(self, DB_instance):
        self.DB_instance = DB_instance
        self.cur = self.DB_instance.crsr()

    def get_licensee(self):
        self.cur.execute("SELECT licensee FROM trucker_DB")
        Licensee = self.cur.fetchall()
        init_list_Licensee = set(Licensee)
        print(init_list_Licensee)
        return init_list_Licensee

    # def Query_DB(self):
    #     self.cur.execute("SELECT * FROM trucker_DB")
    #     full_DB_list = self.cur.fetchall()
    #
    #     for row in full_DB_list:
    #         print(row[3])
