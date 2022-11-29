import pandas as pd
class session:
    _session_id = None
    _computer_id = None
    _user_id = 0
    _start = None
    _end = 0
    _fees = None
          

    def calculate_session_time(): #<--  No Need 
            pass

    def login():
        dfu=pd.read_csv(r'Desktop\OOP Project\Users.csv')
        dft=pd.read_csv('Desktop\OOP Project\Book1.csv')
        _user_id =input(print("Please Enter The User ID"))
        print(dfu)
        check=0 
        check=dfu['Users'].str.contains(_user_id).sum()
        if check>=1:
            new_row = {'Session_ID': '4', 'User_ID':_user_id	,'Computer_ID':'4'	,'Start':'0'	,'End':'0'	,'Drinks':'0'}
            dft=dft.append( new_row , ignore_index=True )
            dft.to_csv('Desktop\OOP Project\Book1.csv')
            while(_end !=1):
                _start+=0.01
        else:
            print("The User ID is WRONG !!")       

    def logout(_session_id):
        
        _end=1
        df = pd.read_csv('Desktop\OOP Project\Book1.csv',index_col="Session_ID")
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
         _fees= _start *3.5 + Drinks*15 
         return _fees
