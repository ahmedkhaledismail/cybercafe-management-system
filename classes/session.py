class session:
    _session_id = None
    _computer_id = None
    _user_id = None
    _start = None
    _end = 0
    _fees = None

    def _calculate_fees(Drinks):
        _fees=Start *3.5 + Drinks*15 # <--Need to have Data base to decide if we want to have diffrent Drinks
        return Total

    #def calculate_session_time(): <--  No Need 
       # pass

    def login():
         _user_id =input(print("Please Enter The User ID"))
        for i in Users: #Check the Users in Data base 
            if i ==  _user_id:
             while(_end!=1):
                 _start+=0.01
            else:
                print("The User_ID not found ")

    def logout(_session_id):
        
        _end=1
        df = pd.read_csv('Desktop\OOP Project\Book1.csv',index_col="Session_ID")
        df = df.drop(_session_id,axis='rows')
        df.to_csv('Desktop\OOP Project\Book1.csv')
        print("Session has been ended")
        print(df)


    def guest_login():
        pass
