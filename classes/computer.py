import pandas as pd
class computer:
    
    def __init__(self):     
        self.__cpu = None
        self.__ram = None
        self.__gpu = None
        self.__storage = None
        self.__computer_id = None
       

    def Add_New_Computer(self,cpu,ram,gpu,storage):
        self.__cpu = cpu
        self.__ram = ram
        self.__gpu = gpu
        self.__storage = storage
        self.__available = 0

        df1 = pd.read_csv('databases\Computer_Tbl.CSV', index_col=[0])

        df2 = pd.DataFrame({"cpu":self.__cpu,
                                 'ram':self.__ram,
                                 'gpu':self.__gpu,
                                 'storage':self.__storage,
                                 'available':self.__available}
                                 ,index=[1])

        df = pd.concat([df1,df2],ignore_index=True)
        df.to_csv('databases\Computer_Tbl.CSV')
        print('Computer was Added successfully!')
        

        
        
    def Show_All_Computers(self):
       return (pd.read_csv('databases\Computer_Tbl.CSV', index_col=[0]))

    def Update_Record(self,computer_id,cpu,ram,gpu,storage):
        df = pd.read_csv('databases\Computer_Tbl.CSV', index_col=[0])

        self.__cpu = cpu
        self.__ram = ram
        self.__gpu = gpu
        self.__storage = storage 
        self.__computer_id = computer_id 

        df.at[self.__computer_id,"cpu"] = self.__cpu
        df.at[self.__computer_id,"ram"] = self.__ram
        df.at[self.__computer_id,"gpu"] = self.__gpu
        df.at[self.__computer_id,"storage"] = self.__storage

        #df.loc[self.__computer_id] = [self.__ram,self.__gpu,self.__storage,self.__cpu]
        df.to_csv('databases\Computer_Tbl.CSV')
        print('Computer was updated successfully!')

        

    def Delete_Computer_by_index(self,x):
        df = pd.read_csv('databases\Computer_Tbl.CSV', index_col=[0])
        df = df.drop(x)
        df.to_csv('databases\Computer_Tbl.CSV')
        print('Computer was deleted successfully!')

    def Search_Record(self,Key_word):
        df = pd.read_csv('databases\Computer_Tbl.CSV', index_col=[0])        
        return(df[df.apply(lambda row: row.astype(str).str.contains(Key_word).any(), axis=1)])
