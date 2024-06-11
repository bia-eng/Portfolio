import sqlite3
import pandas as pd

# Function for getting hardworking students
class HardworkingStudentFinder:
    
    def __init__(self, test_database):
        self.test_database = test_database
        self.test_database = self.load_database()
        
    def load_database(self):
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        query = """SELECT a.research_id, a.Grade as Test_Sum_Grade, \
            b.Your_programming_knowledge_level  
            FROM Test_Sum AS a
            INNER JOIN Student_Rate AS b 
            ON a.research_id = b.research_id;"""

        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    def display_data(self, load_database):
        for research_id, Test_Sum_Grade, Your_programming_knowledge_level in load_database:
            if Test_Sum_Grade > 60:
                if Your_programming_knowledge_level in ('Below Beginner', 'Beginner'):
                    Classification = 'Hardworking'
                else:
                    Classification = 'Not Hardworking'
            else:
                Classification = 'Not Hardworking'
            
            print(f"Student ID: {research_id}")
            print(f"Summative Test Grade: {Test_Sum_Grade}")
            print(f"Programming Knowledge Rating: {Your_programming_knowledge_level}")
            print(f"Student Classification: {Classification}")
            print("---------------")
            
# Fetch results

path = 'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/Resultdatabase.db'
finder = HardworkingStudentFinder(path)
hardworking_students = finder.load_database()
finder.display_data(hardworking_students)