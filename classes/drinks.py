import pandas as pd
class drinks:
    
    __drink_name = None
    __drink_Price = None
    

    def add_drink():
        __drink_name = input('Please enter the drink name: ')
        __drink_Price = input('Please enter the drink Price: ')

        df1 = pd.read_csv('databases\Drinks_Tbl.CSV', index_col=[0])

        df2 = pd.DataFrame({"drink_name":__drink_name,
                                 'drink_price':__drink_Price,}
                                 ,index=[1])

        df = pd.concat([df1,df2],ignore_index=True)
        df.to_csv('databases\Drinks_Tbl.CSV')
        print('Drink was Added successfully!')
    
    def Show_All_Drinks():
       return (pd.read_csv('databases\Drinks_Tbl.CSV', index_col=[0]))


    def Update_Record(x):
        df = pd.read_csv('databases\Drinks_Tbl.CSV', index_col=[0])

        __drink_name = input('Please enter the drink name: ')
        __drink_Price = input('Please enter the drink Price: ')

        df.at[x,["drink_name","drink_price"]] =[__drink_name,__drink_Price]
        df.to_csv('databases\Drinks_Tbl.CSV')
        print('Drink was updated successfully!')

    def Delete_Drink_by_index(x):
        df = pd.read_csv('databases\Drinks_Tbl.CSV', index_col=[0])
        df = df.drop(x)
        df.to_csv('databases\Drinks_Tbl.CSV')
        print('Drink was deleted successfully!')

    def Search_Record(Key_word):
        df = pd.read_csv('databases\Drinks_Tbl.CSV', index_col=[0])        
        return(df[df.apply(lambda row: row.astype(str).str.contains(Key_word).any(), axis=1)])
