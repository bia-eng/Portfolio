import os
import sqlite3
import numpy as np
import matplotlib.pyplot as plt 

student_id = int(input("Enter student ID: "))
test_name = input("Enter test name: ")

def student_grade(student_id, test_name):
    path = 'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/Resultdatabase.db'
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    
    if test_name == 'Test_Mock':    
        query = f"""
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10
        FROM Test_Mock
        WHERE research_id = {student_id};
        """   
    elif test_name == 'Test_1':
        query = f"""
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6
        FROM Test_1
        WHERE research_id = {student_id};
        """    
    elif test_name == 'Test_2':
        query = f"""
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6
        FROM Test_2
        WHERE research_id = {student_id};
        """    
    elif test_name == 'Test_3':
        query = f"""
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6
        FROM Test_3
        WHERE research_id = {student_id};
        """
    elif test_name == 'Test_4':
        query = f"""
        SELECT research_id, grade,
        Q1, Q2
        FROM Test_4
        WHERE research_id = {student_id};
        """
    elif test_name == 'Test_Sum':
        query = f"""
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13
        FROM Test_Sum
        WHERE research_id = {student_id};
        """
        
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data

def test_average(test_name):
    path = 'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/Resultdatabase.db'
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    
    if test_name == 'Test_Mock':    
        query = """
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10
        FROM Test_Mock;
        """    
    elif test_name == 'Test_1':
        query = """
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6
        FROM Test_1;
        """
    elif test_name == 'Test_2':
        query = """
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6
        FROM Test_2;
        """    
    elif test_name == 'Test_3':
        query = """
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6
        FROM Test_3;
        """    
    elif test_name == 'Test_4':
        query = """
        SELECT research_id, grade,
        Q1, Q2
        FROM Test_4;
        """    
    elif test_name == 'Test_Sum':
        query = """
        SELECT research_id, grade,
        Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13
        FROM Test_Sum;
        """
    
    cursor.execute(query)
    data = cursor.fetchall()
    grades = [i[1] for i in data]
    average = round(sum(grades) / len(grades), 2)
    connection.close()
    return average

def calculate_performance(data, average):
    student_grades = [row[2:] for row in data]
    student_grades = np.array(student_grades).flatten()
    absolute_performance = student_grades / max(student_grades) * 100
    relative_performance = student_grades - average
    return absolute_performance, relative_performance

def visualize_performance(absolute_performance, relative_performance):
    question_labels = [f"Q{i+1}" for i in range(len(absolute_performance))]
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.bar(question_labels, absolute_performance, color='lightblue')
    plt.title("Absolute Performance (Percentage)")
    plt.xlabel("Questions")
    plt.ylabel("Grade (%)")

    plt.subplot(1, 2, 2)
    plt.bar(question_labels, relative_performance, color='lightgreen')
    plt.title("Relative Performance (Difference from Average)")
    plt.xlabel("Questions")
    plt.ylabel("Difference")

    plt.tight_layout()
    plt.show()
    
data = student_grade(student_id, test_name)
average = test_average(test_name)    
absolute_performance, relative_performance = calculate_performance(data, average)
visualize_performance(absolute_performance, relative_performance)