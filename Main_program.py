import pandas as pd
import math
import copy
from Students import Student, in_range
from Subjects_Groups import *


class Main():
    def __init__(self):
        self.students = {}

    def get_students(self):
        """Creates dataframe from Excel file containing students list and groups for every student.
        Excel file should looks like this:

                |  Subject 1   | Subject 2    | Subject 3    | ...
        -------------------------------------------------------
       Student 1| Group number | Group number | Group number | ...
       Student 2| Group number | Group number | Group number | ...
       ...

       """

        d = pd.read_excel(r"students.xlsx", index_col=[0]).to_dict(orient='index')

        self.tmp = copy.deepcopy(d)

        for student in d:
            for subject, group in d[student].items():
                if math.isnan(group):
                    del self.tmp[student][subject]

        self.students = {k: v for k, v in self.tmp.items() if v}
        """self.students = {'Student Name':{'Subject':group number, 'Subject': group number}, ... }"""

    def create_students(self):
        """Creates Student object for evert student from parsed Excel file and store object in students_list"""
        for student in self.students.keys():
            args = []
            for subject, value in self.students[student].items():
                for static_subject in Necessary_lists.static_subjects:
                    if subject == static_subject.disc:
                        for group in static_subject.groups:
                            if group == str(subject) + ' ' + str(int(value)):
                                args.append(group)

            tmp_student = Student(student)
            tmp_student.add_student_group(args)
            Necessary_lists.students_list.append(tmp_student)

    def setup_students(self):
        """Creates predictions dict for every student and sets priority for students that don't have much choice."""
        for student in Necessary_lists.students_list:
            student.prediction()
            student.get_priority()

    def student_sign(self, student, subject, group):
        #Signing student to choosen group
        student.picked_groups.append(group)
        student.choosen_subjects.append(subject)
        group.addstudent(student)

    def check_if_subject_already_choosen(self, student, subject):
        if subject in student.choosen_subjects:
            return True
        else:
            return False

    def get_groups(self):
        """Match student with a groups for Subjects to Choose these term.
        Function checks if student is able to attend to choosen groups, which means
        checks if groups don't impose on each other."""
        for priority in range(1,11):
            for student in Necessary_lists.students_list:
                if student.priority == priority:
                    for subject in student.predictions.keys():
                        if len(student.predictions[subject]) == 1:
                            self.student_sign(student, subject, student.predictions[subject][0])
                        else:
                            if len(student.picked_groups) !=0:
                                for group in student.predictions[subject]:
                                    if self.check_if_subject_already_choosen(student, subject):
                                        break
                                    else:
                                        if group.capacity > len(group.students):
                                            for student_group in student.picked_groups:
                                                if group.date_start.weekday() == student_group.date_start.weekday():
                                                    if in_range(group.time_start, group.time_end, student_group.time_start, student_group.time_end):
                                                        if in_range(group.date_start, group.date_end, student_group.date_start, student_group.date_end):
                                                            break
                                                        else:
                                                            self.student_sign(student, subject, group)
                                                            break
                                                    else:
                                                        self.student_sign(student, subject, group)
                                                        break
                                                else:
                                                    self.student_sign(student, subject, group)
                                                    break
                            else:
                                for group in student.predictions[subject]:
                                    if self.check_if_subject_already_choosen(student, subject):
                                        break
                                    else:
                                        if group.capacity > len(group.students):
                                            self.student_sign(student, subject, group)

    def print_student_list_for_static_groups(self):
        """Prints lists of students in groups for static subject which students can't change."""
        for subject in Necessary_lists.static_subjects:
            for group in subject.groups:
                print(group.discrip,'|','Group capacity: '+ str(group.capacity),'|','Students in group: '+ str(len(group.students)))
                for student in group.students:
                    print(student.name)

    def print_student_list_for_choose_groups(self):
        """Prints lists of students in groups for subject to choose."""
        for subject in Necessary_lists.choose_subjects:
            for group in subject.groups:
                print(group.discrip,'|','Group capacity: '+ str(group.capacity),'|','Students in group: '+ str(len(group.students)))
                for student in group.students:
                    print(student.name)