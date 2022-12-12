import pandas as pd
from classes.drinks import drinks
from datetime import datetime

bookpath = r'databases\Book1.csv'
userpath = r'databases\Users.csv'
computerpath = r'databases\Computer_Tbl.csv'


class session:
    def __init__(self,user_name):
        self.session_id = None
        self.computer_id = None
        self.user_name = user_name
        self.start = None
        self.end = None
        self.fees = None


    def calculate_session_time(self,session_id):
        dfs = pd.read_csv(bookpath)
        self.start = dfs.at[session_id,'Start']
        t1 = datetime.strptime(self.start, "%H:%M:%S")
        self.end = dfs.at[session_id,'End']
        t2 = datetime.strptime(self.end, "%H:%M:%S")
        sec = (t2 - t1 ).total_seconds()
        return sec

    def start_session(self):
        self.start = datetime.now().strftime("%H:%M:%S")
        dfs = pd.read_csv(bookpath)
        dfc=pd.read_csv(computerpath)

        for x in range(len(dfc)):
                flagavailabe=0
                if dfc.at[x,'available'] == 0:
                        flagavailabe=1
                        dfc.at[x,'available'] = 1
                        dfc.to_csv(computerpath,index=False)
                        self.computer_id = x
                        self.session_id=len(dfs)
                        new_row = {
                        "Session_ID":self.session_id,
                        "User_ID": self.user_name,
                        "Computer_ID": self.computer_id,
                        "Start": self.start,
                        "End": self.end,
                        "Drinks": "",
                        "Fees":self.fees}                                    
                        dfs = dfs.append(new_row , ignore_index=True)
                        dfs.to_csv(bookpath,index=False)
                        break 
                    
        if flagavailabe == 0:
            print("Sorry no available computer")
            

    def end_session(self,session_id):

        self.end = datetime.now().strftime("%H:%M:%S")
        dfs = pd.read_csv(bookpath)
        dfc = pd.read_csv(computerpath)
        self.computer_id = dfs.at[session_id,'Computer_ID']
        self.computer_id=int(self.computer_id)
        dfc.at[self.computer_id,'available'] = 0
        dfc.to_csv(computerpath,index=False)
        dfs.at[session_id,'End'] = self.end
        dfs.to_csv(bookpath,index=False)
        self.fees = self.calculate_session_time(session_id)*2 + drinks.Calculate_Drinks_Cost(session_id)
        dfs.at[session_id,'Fees'] = self.fees
        dfs.to_csv(bookpath,index=False)
        print("Session has been ended")
  