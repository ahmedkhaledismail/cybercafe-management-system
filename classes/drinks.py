import pandas as pd
class drinks:
    
    __drink_name = None
    __drink_Price = None
    

    def add_drink():
        __drink_name = input('Please enter the drink name: ')
        __drink_Price = input('Please enter the drink Price: ')

        df1 = pd.read_csv('databases\Drinks_Tbl.CSV', index_col=[0])

        df2 = df = pd.DataFrame({"drink_name":__drink_name,
                                 '__drink_Price':__drink_Price,}
                                 ,index=[1])

        df1 = df1.append(df2, ignore_index=True)

        df = pd.concat([df1,df2],ignore_index=False)
        df.to_csv('databases\Drinks_Tbl.CSV')
        print('Drink was Added successfully!')
    
    def Show_All_Drinks():
       return (pd.read_csv('databases\Drinks_Tbl.CSV', index_col=[0]))
