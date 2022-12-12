import pandas as pd
from classes.drinks import drinks
from datetime import datetime

bookpath = './databases/Book1.csv'
userpath = './databases/Users.csv'
computerpath = './databases/Computer_Tbl.csv'


class session:
    def __init__(self,user_name):
        self.session_id = None
        self.computer_id = None
        self.user_name = user_name
        self.start = None
        self.end = None
        self.fees = None


    def calculate_session_time(self):
        sec = (self.end - self.start).total_seconds()
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
                        "Drinks": "0",}                                    
                        dfs = dfs.append(new_row , ignore_index=True)
                        dfs.to_csv(bookpath,index=False)
                        break 
                    
        if flagavailabe == 0:
            print("Sorry no available computer")
            

    def end_session(self,user_name):

        self.end = datetime.now().strftime("%H:%M:%S")
        dfs = pd.read_csv(bookpath)
        dfc=pd.read_csv(computerpath)
        dfc.at[self.computer_id,'available'] = 0
        dfc.to_csv(computerpath,index=False)
        dfs.at[self.session_id,'End'] = self.end
        dfs.to_csv(bookpath,index=False)
        self.fees = self.calculate_session_time() + drinks.Calculate_Drinks_Cost(self.session_id)
        print("Session has been ended")
        # dfs = dfs.drop(session_id, axis="rows")


    # def _calculate_fees(self, ):
    #     self.fees = self.calculate_session_time() + drinks.Calculate_Drinks_Cost(Session_id)
    #     return self.fees


