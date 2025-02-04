import re
class Student:
    def __init__(self, id, name, email, password, phone):
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        if not self.is_valid_phone(phone):
            raise ValueError("Invalid phone number.")
        
        if not self.is_valid_id(id):
            raise ValueError("Invalid ID. Student ID must be exactly 9 digits.")
        
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.enrolled_courses = {}
        
    def is_valid_email(self, email):
        """Validate email using regex."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))
    
    def is_valid_phone(self, phone):
        """Validate phone number using regex (starts with +98 or 09)."""
        phone_regex = r'^\+98\d{10}$|^09\d{9}$'
        return bool(re.match(phone_regex, phone))

    @staticmethod
    def is_valid_id(student_id):
        return isinstance(student_id, int) and len(str(student_id)) == 9
    
    def enroll(self, course_id):
        self.enrolled_courses[course_id] = {}
        #print(f"Enrolled in course {course_id}")
    
    def view_grades(self, course_id):
        if course_id in self.enrolled_courses:
            return self.enrolled_courses[course_id]
        else:
            print("You are not enrolled in this course.")
            return None
    
   
