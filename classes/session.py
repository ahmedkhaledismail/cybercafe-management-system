import pandas as pd
from classes.drinks import drinks
from datetime import datetime

bookpath = r"databases\Book1.csv"
userpath = r"databases\Users.csv"
computerpath = r"databases\Computer_Tbl.csv"


class session:
    def __init__(self, user_name):
        self.session_id = None
        self.computer_id = None
        self.user_name = user_name
        self.start = 0
        self.end = 0
        self.fees = 0

    
    def start_session(self):
        self.start = datetime.now().strftime("%H:%M:%S")

        dfs = pd.read_csv(bookpath)
        dfc = pd.read_csv(computerpath)

        for x in range(len(dfc)):
            flagavailabe = 0

            if dfc.at[x, "available"] == 0:
                flagavailabe = 1
                dfc.at[x, "available"] = 1
                

                self.computer_id = x
                self.session_id = len(dfs)

                new_row = {
                    "Session_ID": self.session_id,
                    "User_ID": self.user_name,
                    "Computer_ID": self.computer_id,
                    "Start": self.start,
                    "End": self.end,
                    "Drinks": "",
                    "Fees": self.fees,
                }
                dfs = dfs.append(new_row, ignore_index=True)
                

                break

        if flagavailabe == 0:
            print("Sorry no available computer")
        dfc.to_csv(computerpath, index=False)
        dfs.to_csv(bookpath, index=False)

    def sessions_running():
        dfs = pd.read_csv(bookpath)
        flag=False
        for row in range(len(dfs)):
            if dfs.at[row, "Fees"] == 0:
                print(dfs.iloc[[row]])  
                flag=True
        return flag


    @staticmethod
    def end_session():
        dfs = pd.read_csv(bookpath)
        dfc = pd.read_csv(computerpath)

        session_run=session.sessions_running()

        if session_run == True:
            try:
                session_id=int(input("Please Enter The Session ID : "))

                end = datetime.now().strftime("%H:%M:%S")
                if dfs.at[session_id, "End"] == 0:
                        dfs.at[session_id, "End"] = end
                        t2 = datetime.strptime(end, "%H:%M:%S")

                        computer_id = int(dfs.at[session_id, "Computer_ID"])
                        dfc.at[computer_id, "available"] = 0
                        
                        drinkscost = drinks()
                        drinkscost = drinkscost.Calculate_Drinks_Cost(session_id)
                        dfs.at[session_id, "Drinks"] = drinkscost

                        start = dfs.at[session_id, "Start"]
                        t1 = datetime.strptime(start, "%H:%M:%S")

                        if t2>t1:
                            sec = (t2 - t1).total_seconds()
                        else:
                            
                            sec = (t2 - t1).total_seconds()
                            sec+=86400

                    
                        fees = (sec * 2) + drinkscost
                        dfs.at[session_id, "Fees"] = fees

                        dfs.to_csv(bookpath, index=False)
                        dfc.to_csv(computerpath, index=False)
                        print("Session has been ended")

                else:
                    print("This Session ID is not assigned to any Session running") # handle if the session id in sessions table but already ended  
            except:
                print("This Session ID is not assigned to any Session running") # handle if the session id enterd is not in the sessions table 
        else:
            print("<<There is no sessions running>> ")
            
        

        

