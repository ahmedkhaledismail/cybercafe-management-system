import pandas as pd
class drinks:
    
   
    __Drink_id = None

    def __init__(self,drink_name,drink_Price):
        self.__drink_name = drink_name
        self.__drink_Price = drink_Price

        df1 = pd.read_csv('databases\Drinks_menu_Tbl.CSV', index_col=[0])

        df2 = pd.DataFrame({"drink_name":self.__drink_name,
                                 'drink_price':self.__drink_Price,}
                                 ,index=[1])

        df = pd.concat([df1,df2],ignore_index=True)
        df.to_csv('databases\Drinks_menu_Tbl.CSV')
        print('Drink was Added successfully!')
    
    def Show_All_Drinks(self):
       return (pd.read_csv('databases\Drinks_menu_Tbl.CSV', index_col=[0]))


    def Update_Record(self,Drink_id,drink_name,drink_Price):
        df = pd.read_csv('databases\Drinks_menu_Tbl.CSV', index_col=[0])

        self.__drink_name = drink_name
        self.__drink_Price = drink_Price
        self.__Drink_id = Drink_id

        #df.at[Drink_id,["drink_name","drink_price"]] =['yyy',5555]
        df.loc[self.__Drink_id] = [self.__drink_name,self.__drink_Price]
        df.to_csv('databases\Drinks_menu_Tbl.CSV')
        print('Drink was updated successfully!')

    
    def Delete_Drink_by_index(self,Drink_id):
        self.__Drink_id = Drink_id
        df = pd.read_csv('databases\Drinks_menu_Tbl.CSV', index_col=[0])
        df = df.drop(self.__Drink_id)
        df.to_csv('databases\Drinks_menu_Tbl.CSV')
        print('Drink was deleted successfully!')

    def Search_Record(self,Key_word):
        
        df = pd.read_csv('databases\Drinks_menu_Tbl.CSV', index_col=[0])        
        return(df[df.apply(lambda row: row.astype(str).str.contains(Key_word).any(), axis=1)])

    def Buy_a_drink(self,Session_id,Drink_id):
        df1 = pd.read_csv('databases\Sold_drinks_Tbl.CSV', index_col=[0])

        df2 = pd.DataFrame({"Drink_id":Drink_id,
                                 'Session_id':Session_id,}
                                 ,index=[1])

        df = pd.concat([df1,df2],ignore_index=True)
        df.to_csv('databases\Sold_drinks_Tbl.CSV')
        print('Drink was Added successfully!')

    def Calculate_Drinks_Cost(self,Session_id):
        Sold_drinks_Tbl = pd.read_csv('databases\Sold_drinks_Tbl.CSV', index_col=[0])
        Drinks_menu_Tbl = pd.read_csv('databases\Drinks_menu_Tbl.CSV', index_col=[0])

        df = pd.merge(Sold_drinks_Tbl,Drinks_menu_Tbl['drink_price'],how ='inner',left_on='Drink_id', right_index=True)
        return(df[df['Session_id'] == Session_id]['drink_price'].sum())
