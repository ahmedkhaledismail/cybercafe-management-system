import pandas as pd
from datetime import datetime
class session:

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
    
   
    def calculate_session_time():  
            sec=(_end-_start).total_seconds()
            return sec
            

    def login():
        dfu=pd.read_csv(r'Desktop\OOP Project\Users.csv')
        dft=pd.read_csv('Desktop\OOP Project\Book1.csv')
        _user_id =input(print("Please Enter The User ID"))
        print(dfu)
        check=0 
        check=dfu['Users'].str.contains(_user_id).sum()
        if check==1:
            _start=datetime.now().strftime("%H:%M:%S")
            new_row = {'Session_ID': '4', 'User_ID':_user_id	,'Computer_ID':'4'	,'Start':_start	,'End':_end	,'Drinks':'0'}
            dft=dft.append( new_row , ignore_index=True )
            dft.to_csv('Desktop\OOP Project\Book1.csv')
            
        else:
            print("The User ID is WRONG !!")       

    def logout(_session_id):
        
        _end=datetime.now().strftime("%H:%M:%S")
        df = pd.read_csv('Desktop\OOP Project\Book1.csv',index_col="Session_ID")
        new_row['End']=_end
        df = df.drop(_session_id,axis='rows') 
        df.to_csv('Desktop\OOP Project\Book1.csv')
        print("Session has been ended")
        print(df)

    def guest_login():
        dft=pd.read_csv('Desktop\OOP Project\Book1.csv')
        new_row = {'Session_ID': '5', 'User_ID':"Guest"	,'Computer_ID':'5'	,'Start':'0'	,'End':'0'	,'Drinks':'0'}
        dft=dft.append( new_row , ignore_index=True )
        while(_end !=1):
            _start+=0.01


    def _calculate_fees(Drinks):
         _fees= calculate_session_time() *3.5 + Drinks*15 
         return _fees
