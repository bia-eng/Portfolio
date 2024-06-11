import sqlite3
import pandas as pd

def get_underperforming_students(path):
    
    # Connect to database
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
    
    for research_id, Test_Sum_Grade, *Test_Grade in data:
        lowest_formative_grade = min(Test_Grade)

        # Check if all grades (summative and formative) are within the 1-50 range:
        is_underperforming = (
            1 <= Test_Sum_Grade <= 50
            or any(1 <= grade <= 50 for grade in Test_Grade)
        )
        if is_underperforming:
            Classification = 'Underperforming'
        else:
            Classification = 'Performing'

        print(f"Research_Id: {research_id}")
        print(f"Summative Test Grade: {Test_Sum_Grade}")
        for test_name, grade in zip(['Mock_Test_Grade', 'Test_1_Grade', 'Test_2_Grade', 'Test_3_Grade', 'Test_4_Grade'], Test_Grade):
            highlight = '\033[1m' if grade == lowest_formative_grade else ''
            print(f"{test_name}: {highlight}{grade}\033[0m")
        print(f"Student Performance: {Classification}")
        print("-" * 25) 

# Fetch results

path = 'C:/Users/user/OneDrive/Desktop/23COP504_CW/Data Files/Resultdatabase.db'
get_underperforming_students(path)