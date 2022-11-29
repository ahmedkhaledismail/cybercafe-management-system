import pandas as pd
class computer:
    
    __cpu = None
    __ram = None
    __gpu = None
    __storage = None

    def Add_New_Computer():
        __cpu = input('Please enter the CPU model: ')
        __ram = input('Please enter the ram siza: ')
        __gpu = input('Please enter the gpu model: ')
        __storage = input('Please enter the storage size: ')

        df1 = pd.read_csv('databases\Computer_Tbl.CSV', index_col=[0])

        df2 = df = pd.DataFrame({"cpu":__cpu,
                                 'ram':__ram,
                                 'gpu':__gpu,
                                 'storage':__storage}
                                 ,index=[1])

        df1 = df1.append(df2, ignore_index=True)

        df = pd.concat([df1,df2],ignore_index=False)
        df.to_csv('databases\Computer_Tbl.CSV')
        


        
    def Show_All_Computers():
       return (pd.read_csv('databases\Computer_Tbl.CSV', index_col=[0]))

    def _Update_Record():
        pass

    def Delete_Computer_by_index(x):
        df = pd.read_csv('databases\Computer_Tbl.CSV', index_col=[0])
        df = df.drop(x)
        df.to_csv('databases\Computer_Tbl.CSV')
        print('Computer was deleted successfully!')

    def _Search_Record():
        pass
