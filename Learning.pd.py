import pandas as pd
import numpy as np

# ser = pd.Series([20, 30, 40], index=["Munna", "Rupali", "Unka_chota_Baccha"])
# print(ser)

# Ek Series banao 5 city ke temperatures ki.
# city_temp = pd.Series([40, 45, 30, 46, 51], index = ["Monday", "Tudesday", "Wednesday", "Thursday", "Friday"])
# print(city_temp)

# Ek DataFrame banao employee name, age, salary ka (4 rows).

# salary_register = pd.DataFrame({"Name": ["a", "b", "c", "d"], "Age": [2, 4, 6, 7], "Salary": [1000, 2000, 3000, 4000]})
# print(salary_register)

# # Ek Series banao electricity bill for 6 months.
# elec_bill = pd.Series([121, 214, 412, 321, 231, 431], index=["Jan", "Feb", "Mar", "April", "May", "June"])
# print(elec_bill)

# arr = np.array([[10,20],[30,40],[50,60]])
# df_arr = pd.DataFrame(arr, columns=["odd", "even"])
# print(df_arr)

# csv_file = pd.read_csv('Education_Data.csv')
# print(csv_file.head(3))
# print(csv_file.info())
# print(csv_file.describe())


# df = pd.DataFrame({
#     'Name': ['Aman', 'Sara', 'Riya', 'Kunal'],
#     'Marks': [88, 92, 75, 81]
# })
# df['Double_Marks'] = df['Marks']*2
# # df.index = [1, 2, 3, 4]
# df['Floatmarks'] = df['Double_Marks'].astype(float)
# df_with_index = df.set_index('Name')
# print(df_with_index)
# print(df)

# df = pd.DataFrame({
#     'Student': ['Aman', 'Sara', 'Kunal', 'Riya'],
#     'Maths': [88, 76, 93, 85],
#     'Science': [90, 80, 88, 92]
# })

# Series_Maths = df["Maths"]
# Scie_Math = df["Maths", "Science"]
# Highest_Math = Series_Maths.sort_values(0)

# print(Series_Maths)

# print(csv_file.info())

# import pandas as pd

# df = pd.DataFrame({
#     'Name': ['Aman', 'Sara', 'Riya', 'Kunal'],
#     'Maths': [88, 92, 75, 81],
#     'Science': [90, 80, 88, 92]
# })

# Scie_Math = df[["Maths", "Science"]]
# Double_science = df["Science"] * 2
# new_data = df.drop("Science", axis=1)
# dropped = df.drop("Science", "Maths", axis=1)
# print(df)
# print(Scie_Math)
# print(Double_science)
# print(new_data)
# print(dropped)


print("Jhattu Bhai")