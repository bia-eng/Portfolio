# Load libraries

import os
import pandas as pd
import numpy as np 
import sqlite3
import matplotlib.pyplot as plt

class test_results:

    def __init__(self, test_database):
        self.test_database = test_database
        self.test_database = self.load_database()
        
    def load_database(self):
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        query = """
        SELECT a.research_id, a.Grade as Mock_Test_Grade, \
        b.Grade as Test_1_Grade, c.Grade as Test_2_Grade, \
        d.Grade as Test_3_Grade, e.Grade as Test_4_Grade, \
        f.Grade as Test_Sum_Grade 
        FROM Test_Mock AS a
        INNER JOIN Test_1 AS b 
        ON a.research_id = b.research_id
        INNER JOIN Test_2 AS c
        ON a.research_id = c.research_id
        INNER JOIN Test_3 AS d
        ON a.research_id = d.research_id
        INNER JOIN Test_4 AS e
        ON a.research_id = e.research_id
        INNER JOIN Test_Sum AS f
        ON a.research_id = f.research_id;
        """

        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()  # Terminate database connection
        return data
        
    def display_test_grades(self, load_database):
        matching_tuple = None
        for score in load_database:
            if score[0] == student_id:
                matching_tuple = score[1:]
                break   # Exit the loop once the match is found

        if not matching_tuple:
            print("Research ID not found")

        # Plot the grades
        test_names = ['Mock Test', 'Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test Sum']
        grades_to_plot = matching_tuple

        plt.figure(figsize=(8, 6))
        plt.bar(test_names, grades_to_plot, color='skyblue')
        plt.xlabel('Test Types')
        plt.ylabel('Grades')
        plt.title(f'Test Grades for Research ID {student_id}')
        plt.ylim(0, 100)
        plt.tight_layout()
        plt.show()

# Fetch results

student_id = int(input("Enter the Research ID: "))
path = 'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/Resultdatabase.db'
display_grades = test_results(path)
get_data = display_grades.load_database()
display_grades.display_test_grades(get_data)