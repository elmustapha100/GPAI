""" Functions for managing the system 
grade_system(user_score : float) - This function returns the user's grade point (0.0 to 5.0)
grade_scale(user_score: str) - returns the student's grade scale ('A'-'F')
course_point(units, user_score : float) - returns the total score = unit * user_score
"""

def grade_system(user_score):

    if user_score < 0 and user_score > 100 : 
        raise ValueError ("Invalid input. Scores must be between 0-100")
    
    if not isinstance(user_score ,(int , float)) : 
        raise TypeError ("Error!. Enter a number")
    

    if user_score >=  70.00 :
        return 5.0 
    if user_score >= 60.00 : 
        return 4.0 
    if user_score >= 50.00 : 
        return 3.0 
    if user_score >= 45.00 : 
        return 2.0
    if user_score >= 40.00 : 
        return 1.0 
    else : 
        return 0.0
    
def grade_point(user_score) : 

    if user_score < 0 and user_score > 100 : 
        raise ValueError ("Invalid input. Scores must be between 0-100")
    
    if not isinstance(user_score ,(int , float)) : 
        raise TypeError ("Error!. Enter a number")

    if user_score >=  70.00 :
        return "A"
    if user_score >= 60.00 : 
        return "B" 
    if user_score >= 50.00 : 
        return "C" 
    if user_score >= 45.00 : 
        return "D"
    if user_score >= 40.00 : 
        return "E" 
    else : 
        return "F"
    
def total_score(units , user_score) : 
    if units < 0 : 
        raise ValueError ("Invalid") 
    return units * grade_system(user_score)
       

