def grade_system(user_score):

    """This function checks the grade and points of a user in a university system"""

    grade_score = {
            "A" : 5.0,
            "B" : 4.0,
            "C" : 3.0,
            "D" : 2.0,
            "E" : 1.0,
            "F" : 0.0,
     }
    
    if user_score >= 70.0 and user_score < 100 :
        print(grade_score["A"])
    elif user_score >= 60.0 and user_score < 69.999 : 
        print(grade_score["B"])    
    elif user_score >= 50.0 and user_score < 59.999 : 
        print(grade_score["C"])    
    elif user_score >= 45.0 and user_score < 49.999: 
        print(grade_score["D"])    
    elif user_score >= 40.0 and user_score < 44.999 : 
        print(grade_score["E"])    

    else : 
        print(grade_score["F"])   


def user_input(user_score) : 
    input("Enter your grades to check your results! : ")

