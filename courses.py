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
    """returns the equivaelent letter scale based on score"""
    return grade_point(self.grade_score) 

