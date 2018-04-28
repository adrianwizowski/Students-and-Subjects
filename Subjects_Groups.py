import datetime

class Necessary_lists():
    """Containers for subjects that students already picked and can't change (static_subjects),
    subjects that students still have to choose (choose_students) and all created students."""
    static_subjects = []
    students_list = []
    choose_subjects = []

class Subject():
    def __init__(self, desc):
        self.desc = desc
        self.groups = []

    def addgroup(self, group):
        try:
            if group not in self.groups:
                self.groups.append(group)
        except:
            print('Group already in Groups')

class Group():
    def __init__(self, descrip, number, group_capacity, date_start, date_end):
        """Date format: (year, month, day, hour, min)"""
        self.descrip = descrip
        self.capacity = group_capacity
        self.number = number
        self.date_start = datetime.date(year=date_start[0], month=date_start[1], day=date_start[2])
        self.time_start = datetime.time(hour=date_start[3], minute=date_start[4])
        self.date_end = datetime.date(year=date_end[0], month=date_end[1], day=date_end[2])
        self.time_end = datetime.time(hour=date_end[3], minute=date_end[4])
        self.students = []

    def addstudent(self, student):
        self.students.append(student)
        if self not in student.groups:
            student.groups.append(self)