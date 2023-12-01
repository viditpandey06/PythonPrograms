class Student:
    print('VIDIT')
    def __init__(self, stu_name, stu_roll_no, ob_marks, max_marks):
        self.stu_name = stu_name
        self.stu_roll_no = stu_roll_no
        self.ob_marks = ob_marks
        self.max_marks = max_marks
        self.percentage = 0 
        #VIDIT
    def cal_percentage(self):
        if self.max_marks != 0:
            self.percentage = (self.ob_marks / self.max_marks) * 100
        else:
            print("Error: Max marks cannot be zero!")

    def cal_grade(self):
        if self.percentage >= 60:
            return 'A'
        elif 40 <= self.percentage < 60:
            return 'B'
        elif 39 < self.percentage < 40:
            return 'C'
        else :
            return 'No grade is awarded'

    def display(self):
        print(f"{self.stu_name}'s percentage is {self.percentage}% and grade is {self.cal_grade()}")

student1 = Student("Vidit", 101, 455, 500)
student1.cal_percentage()
print("Grade Calculated")
student1.display()

