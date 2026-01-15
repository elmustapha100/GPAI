from scripts import grade_system , grade_point , total_score 

class Courses :
    def __init__(self , course_code  : str, course_units : float , grade_score : float) : 
        self.course_code = course_code 
        self.course_units = float(course_units)
        self.grade_score = float(grade_score)


def grade_scale(self) : 
    """return the total score for the weighted score point"""
    return total_score(self.course_units , self.grade_score) 

def grade(self) : 
    """returns the equivalent letter scale based on score"""   
    return grade_point(self.grade_score) 

def gpa(courses : list ) : 
    """returns the student's gpa for the semester 
    Args : collect input of courses from user in form of a list 
    
    Return : semester grade point average 

    Raises ; valueError if the total units == 0
    """
    total_units = 0 
    for i in courses : 
        total_units += i 
    
    if total_units == 0 : 
        raise ValueError ("Your total units must be greater than 0")
    
    total_grade_point = 
    