# Load libraries

import os
import pandas as pd
import sqlite3


# a
# First Load data from each CSV file into a separate DataFrame and rename columns, if needed
# Replacing null / "-" with 0 as well

dfMock_Test = pd.read_csv(r'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/TestResult/Formative_Mock_Test.csv', 
                        index_col=False).replace('-', 0)               
dfMock_Test = dfMock_Test.rename(columns={'research id' : 'research_id', 'Grade/10000' : 'Grade', 'Q 1 /500': 'Q1', 
                                        'Q 2 /300' : 'Q2', 'Q 3 /600' : 'Q3', 'Q 4 /700' : 'Q4', 'Q 5 /500' : 'Q5',
                                        'Q 6 /400' : 'Q6', 'Q 7 /1000' : 'Q7', 'Q 8 /2000' : 'Q8',
                                        'Q 9 /2000' : 'Q9', 'Q 10 /2000' : 'Q10'})


dfTest_1 = pd.read_csv(r'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/TestResult/Formative_Test_1.csv', 
                       index_col=False).replace('-', 0)
dfTest_1 = dfTest_1.rename(columns={'research id' : 'research_id', 'Grade/600' : 'Grade', 'Q 1 /100': 'Q1',
                                    'Q 2 /100' : 'Q2', 'Q 3 /100' : 'Q3', 'Q 4 /100' : 'Q4', 'Q 5 /100' : 'Q5',
                                    'Q 6 /100' : 'Q6'})


dfTest_2 = pd.read_csv(r'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/TestResult/Formative_Test_2.csv', 
                       index_col=False).replace('-', 0)
dfTest_2 = dfTest_2.rename(columns={'research id' : 'research_id', 'Grade/700' : 'Grade', 'Q 1 /100': 'Q1', 
                                    'Q 2 /100' : 'Q2', 'Q 3 /100' : 'Q3', 'Q 4 /200' : 'Q4', 'Q 5 /100' : 'Q5',
                                    'Q 6 /100' : 'Q6'})


dfTest_3 = pd.read_csv(r'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/TestResult/Formative_Test_3.csv', 
                       index_col=False).replace('-', 0)
dfTest_3 = dfTest_3.rename(columns={'research id' : 'research_id', 'Grade/600' : 'Grade', 'Q 1 /100': 'Q1', 
                                    'Q 2 /100' : 'Q2', 'Q 3 /100' : 'Q3', 'Q 4 /100' : 'Q4', 'Q 5 /100' : 'Q5',
                                    'Q 6 /100' : 'Q6'})


dfTest_4 = pd.read_csv(r'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/TestResult/Formative_Test_4.csv', 
                       index_col=False).replace('-', 0)
dfTest_4 = dfTest_4.rename(columns={'research id' : 'research_id', 'Grade/1000' : 'Grade', 'Q 1 /500': 'Q1',
                                    'Q 2 /500' : 'Q2'})


dfSum_Test = pd.read_csv(r'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/TestResult/SumTest.csv', 
                         index_col=False).replace('-', 0)
dfSum_Test = dfSum_Test.rename(columns={'research id' : 'research_id', 'Grade/10000' : 'Grade', 'Q 1 /500': 'Q1', 
                                        'Q 2 /300' : 'Q2', 'Q 3 /600' : 'Q3', 'Q 4 /700' : 'Q4', 'Q 5 /400' : 'Q5',
                                        'Q 6 /500' : 'Q6', 'Q 7 /1500' : 'Q7', 'Q 8 /1500' : 'Q8',
                                        'Q 9 /1500' : 'Q9', 'Q 10 /1000' : 'Q10', 'Q 11 /400' : 'Q11',
                                        'Q 12 /500' : 'Q12', 'Q 13 /600' : 'Q13'})

dfStudent_Rate = pd.read_csv(r'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/TestResult/StudentRate.csv', 
                             index_col=False).replace('-', 0)
dfStudent_Rate = dfStudent_Rate.rename(columns={'research id' : 'research_id', 'Which of followings are true for you' : 'Which_are_true',
                                                 'Which of the followings have you studied or had experience with' : 'Which_have_you_studied_or_experienced',
                                                  'What level programming knowledge do you have?' : 'Your_programming_knowledge_level',
                                                  'Do you like programming' : 'Like_programming', 'What do you think about sci-fi movies ?' : 'Scifi_movies_opinion',
                                                  'What do you think about learning to program  ?' : 'Learning_to_program_opinion', 
                                                  'Can you please specify the programming language you know which a' : 'Programming_languages_you_know'})

# a
# Changing datatype to float for grades and questions

dfMock_Test[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']] = \
dfMock_Test[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10']].astype(float)

dfTest_1[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']] = \
dfTest_1[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']].astype(float)


dfTest_2[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']] = \
dfTest_2[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']].astype(float)


dfTest_3[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']] = \
dfTest_3[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']].astype(float)


dfTest_4[['Grade', 'Q1', 'Q2']] = \
dfTest_4[['Grade', 'Q1', 'Q2']].astype(float)


dfSum_Test[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13']] = \
dfSum_Test[['Grade', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13']].astype(float)

# b
# Replace null values with 0. Testing for null values

dfMock_Test.notnull().values.all()
dfTest_1.notnull().values.all()
dfTest_2.notnull().values.all()
dfTest_3.notnull().values.all()
dfTest_4.notnull().values.all()
dfSum_Test.notnull().values.all()
dfStudent_Rate.notnull().values.all() #False (null values present)

# Replacing null values with 0
dfCleanStudent_Rate = dfStudent_Rate.fillna(0)

# Removing duplicates and keeping the highest grade

dfCleanTest_Mock = dfMock_Test.sort_values('Grade', ascending=False).groupby('research_id').head(1)
dfCleanTest_1 = dfTest_1.sort_values('Grade', ascending=False).groupby('research_id').head(1)
dfCleanTest_2 = dfTest_2.sort_values('Grade', ascending=False).groupby('research_id').head(1)
dfCleanTest_3 = dfTest_3.sort_values('Grade', ascending=False).groupby('research_id').head(1)
dfCleanTest_4 = dfTest_4.sort_values('Grade', ascending=False).groupby('research_id').head(1)
dfCleanTest_Sum = dfSum_Test.sort_values('Grade', ascending=False).groupby('research_id').head(1)

# Removing redundant columns

dfCleanTest_Mock = dfCleanTest_Mock.drop(['State', 'Time taken'], axis=1)
dfCleanTest_1 = dfCleanTest_1.drop(['State', 'Time taken'], axis=1)
dfCleanTest_2 = dfCleanTest_2.drop(['State', 'Time taken'], axis=1)
dfCleanTest_3 = dfCleanTest_3.drop(['State', 'Time taken'], axis=1)
dfCleanTest_4 = dfCleanTest_4.drop(['State', 'Time taken'], axis=1)
dfCleanTest_Sum = dfCleanTest_Sum.drop(['State', 'Time taken'], axis=1)

# Standardizing the grades

dfCleanTest_Mock_max_grade = dfCleanTest_Mock['Grade'].max()
dfCleanTest_Mock['Grade'] = round((dfCleanTest_Mock['Grade'] / dfCleanTest_Mock_max_grade) * 100, 2)
dfFormattedCleanTest_Mock = dfCleanTest_Mock

dfCleanTest_1_max_grade = dfCleanTest_1['Grade'].max()
dfCleanTest_1['Grade'] = round((dfCleanTest_1['Grade'] / dfCleanTest_1_max_grade) * 100, 2)
dfFormattedCleanTest_1 = dfCleanTest_1

dfCleanTest_2_max_grade = dfCleanTest_2['Grade'].max()
dfCleanTest_2['Grade'] = round((dfCleanTest_2['Grade'] / dfCleanTest_2_max_grade) * 100, 2)
dfFormattedCleanTest_2 = dfCleanTest_2

dfCleanTest_3_max_grade = dfCleanTest_3['Grade'].max()
dfCleanTest_3['Grade'] = round((dfCleanTest_3['Grade'] / dfCleanTest_3_max_grade) * 100, 2)
dfFormattedCleanTest_3 = dfCleanTest_3

dfCleanTest_4_max_grade = dfCleanTest_4['Grade'].max()
dfCleanTest_4['Grade'] = round((dfCleanTest_4['Grade'] / dfCleanTest_4_max_grade) * 100, 2)
dfFormattedCleanTest_4 = dfCleanTest_4

dfCleanTest_Sum_max_grade = dfCleanTest_Sum['Grade'].max()
dfCleanTest_Sum['Grade'] = round((dfCleanTest_Sum['Grade'] / dfCleanTest_Sum_max_grade) * 100, 2)
dfFormattedCleanTest_Sum = dfCleanTest_Sum

# Resetting index for all dataframes

dfFormattedCleanTest_Mock.reset_index(drop=True, inplace=True)
dfFormattedCleanTest_1.reset_index(drop=True, inplace=True)
dfFormattedCleanTest_2.reset_index(drop=True, inplace=True)
dfFormattedCleanTest_3.reset_index(drop=True, inplace=True)
dfFormattedCleanTest_4.reset_index(drop=True, inplace=True)
dfFormattedCleanTest_Sum.reset_index(drop=True, inplace=True)
dfCleanStudent_Rate.reset_index(drop=True, inplace=True)

# Dropping SQL database, if it exists

path = 'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/Resultdatabase.db'

connection = sqlite3.connect(path)
cursor = connection.cursor()
query = """DROP TABLE IF EXISTS Test_Mock;"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
query = """DROP TABLE IF EXISTS Test_1;"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
query = """DROP TABLE IF EXISTS Test_2;"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
query = """DROP TABLE IF EXISTS Test_3;"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
query = """DROP TABLE IF EXISTS Test_4;"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
query = """DROP TABLE IF EXISTS Test_Sum;"""
cursor.execute(query)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
query = """DROP TABLE IF EXISTS Student_Rate;"""
cursor.execute(query)
connection.commit()
connection.close()

# Creating a SQL database and transferring dataframe to SQL tables

connection = sqlite3.connect(path)
cursor = connection.cursor()
dfFormattedCleanTest_Mock.to_sql('Test_Mock', connection, index=False)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
dfFormattedCleanTest_1.to_sql('Test_1', connection, index=False)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
dfFormattedCleanTest_2.to_sql('Test_2', connection, index=False)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
dfFormattedCleanTest_3.to_sql('Test_3', connection, index=False)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
dfFormattedCleanTest_4.to_sql('Test_4', connection, index=False)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
dfFormattedCleanTest_Sum.to_sql('Test_Sum', connection, index=False)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
dfStudent_Rate.to_sql('Student_Rate', connection, index=False)
connection.commit()
connection.close()

connection = sqlite3.connect(path)
cursor = connection.cursor()
query = """SELECT * FROM  Test_Sum;"""
x = cursor.execute(query)
connection.commit()
connection.close()
print(x)