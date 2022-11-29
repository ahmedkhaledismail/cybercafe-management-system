import pandas as pd
from datetime import datetime
class session:
bookpath='./databases/OOP Project/Book1.csv'
userpath='./databases/OOP Project/Users.csv'
    def __init__(self):
        self.session_id = None
        self.computer_id = None
        self.user_id = 0
        self.start = None
        self.end = 0
        self.fees = None
        
        self.calculate_session_time()
        self.login():
        self.logout()
        self.guest_login()
        self._calculate_fees()
    
   
    def calculate_session_time(self):  
            sec=(_end-_start).total_seconds()
            return sec
            

    def login(self):
        dfu=pd.read_csv(userpath)
        dft=pd.read_csv(bookpath)
        _user_id =input(print("Please Enter The User ID"))
        print(dfu)
        check=0 
        check=dfu['Users'].str.contains(_user_id).sum()
        if check==1:
            _start=datetime.now().strftime("%H:%M:%S")
            new_row = {'Session_ID': '4', 'User_ID':_user_id	,'Computer_ID':'4'	,'Start':_start	,'End':_end	,'Drinks':'0'}
            dft=dft.append( new_row , ignore_index=True )
            dft.to_csv(bookpath)
            
        else:
            print("The User ID is WRONG !!")       

    def logout(self,_session_id):
        
        _end=datetime.now().strftime("%H:%M:%S")
        df = pd.read_csv(bookpath,index_col="Session_ID")
        new_row['End']=_end
        df = df.drop(_session_id,axis='rows') 
        df.to_csv(bookpath)
        print("Session has been ended")
        print(df)

    def guest_login(self):
        dft=pd.read_csv(bookpath)
        new_row = {'Session_ID': '5', 'User_ID':"Guest"	,'Computer_ID':'5'	,'Start':'0'	,'End':'0'	,'Drinks':'0'}
        dft=dft.append( new_row , ignore_index=True )
        _start=datetime.now().strftime("%H:%M:%S")



    def _calculate_fees(self,Drinks):
         _fees= self.calculate_session_time() *3.5 + Drinks*15 
         return _fees
