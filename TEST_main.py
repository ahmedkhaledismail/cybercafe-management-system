from classes import computer,drinks
import pandas as pd
#comp = computer.computer()

drink_df = pd.read_csv('databases\Drinks_menu_Tbl.CSV', index_col=[0])
#print(drink_df.index)
drink = drinks.drinks()
drink.Buy_a_drink(1,1)
#drink = drinks.drinks('tt',66)
#print(drink.Calculate_Drinks_Cost(2))
#drink_1 = drinks.drinks('tt',15)

#comp.Add_New_Computer('I9','128 GB','RTX 4090','2000 TB')
#comp.Update_Record(13,'I99','166 GB','RTX 44090','22 TB')
#comp.Delete_Computer_by_index(150)
#print(comp.Show_All_Computers())

#print(comp.Show_All_Computers())
#comp.Update_Record(0)
#print(comp.Show_All_Computers())
#print(comp.Search_Record('I9'))

#drink.add_drink('Tea',5)
#drink.add_drink('Cola',10)
#drink.add_drink('yy',15)

#print(drink.Show_All_Drinks())
#drink.Delete_Drink_by_index(3)uuyy
#print(drink.Show_All_Drinks())
#drink.Update_Record(2,'ttt',88888)
#drink.Delete_Drink_by_index(2)
#print(drink.Show_All_Drinks())
#print(drink.Search_Record('T'))
#drink.Buy_a_drink(1,0)
#drink.Buy_a_drink(1,1)
#drink.Buy_a_drink(1,2)


#print(drink.Calculate_Drinks_Cost(1))
#try :
#    df = pd.read_csv('databases\Computl.CSV', index_col=[0])
#except FileNotFoundError:
#    print('t') 
