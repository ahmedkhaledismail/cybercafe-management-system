import pandas as pd
from datetime import datetime

bookpath = './databases/Book1.csv'
userpath = './databases/Users.csv'
computerpath = './databases/Computer_Tbl.csv'


class session:
    def __init__(self):
        self.session_id = None
        self.computer_id = None
        self.user_id = 0
        self.start = None
        self.end = 0
        self.fees = None

        self.calculate_session_time()
        self.start_session()
        self.end_session()
        # self.guest_login()
        self._calculate_fees()

    def calculate_session_time(self):
        sec = (self.end - self.start).total_seconds()
        return sec

    def start_session(self):
        dfu = pd.read_csv(userpath)
        dft = pd.read_csv(bookpath)
        _user_id = input(print("Please Enter The User ID"))
        print(dfu)
        check = 0
        check = dfu["Users"].str.contains(_user_id).sum()
        if check == 1:
            self.start = datetime.now().strftime("%H:%M:%S")
            self.new_row = {
                "Session_ID": "4",
                "User_ID": _user_id,
                "Computer_ID": "4",
                "Start": self.start,
                "End": self.end,
                "Drinks": "0",
            }
            dft = dft.append(self.new_row, ignore_index=True)
            dft.to_csv(bookpath)

        else:
            print("The User ID is WRONG !!")

    def end_session(self, session_id,computer_id):

        self.end = datetime.now().strftime("%H:%M:%S")
        dfs = pd.read_csv(bookpath, index_col="Session_ID")
        dfc=pd.read_csv(computerpath,index_col="computer_id")
        dfc.at[computer_id,"avalibale"] = 0
        dfc.to_csv(computerpath)
        self.new_row["End"] = self.end
        dfs = dfs.drop(session_id, axis="rows")
        dfs.to_csv(bookpath)
        print("Session has been ended")
        print(dfs)


    def _calculate_fees(self, Drinks):
        _fees = self.calculate_session_time() * 3.5 + Drinks * 15
        return _fees
