from collections import OrderedDict
from Subjects_Groups import Necessary_lists

class Student():
    def __init__(self, name):
        self.name = name
        self.groups = []
        self.predictions = {}
        self.priority = 10
        self.picked_groups = []
        self.choosen_subjects = []

    def add_student_group(self, args):
        self.groups = [arg for arg in args]

    def prediction(self):
        """Creates a dictionary of prediction for Student object.
        Compare groups from self.groups with groups that student could choose and checks if they are passible to pick.
        Save self.predictions as dict, sorted by a lenght of values (number of groups that student can choose for a subject.)
        Eg.
        self.pre
        """

        for choose_subject in Necessary_lists.choose_subjects:
            for group_to_pick in choose_subject.groups:
                able = True
                for student_group in self.groups:
                    if group_to_pick.date_start.weekday() == student_group.date_start.weekday():
                        if in_range(student_group.time_start, student_group.time_end, group_to_pick.time_start, group_to_pick.time_end):
                            if in_range(student_group.date_start, student_group.date_end, group_to_pick.date_start, group_to_pick.date_end):
                                able = False
                                break
                if able == True:
                    try:
                        self.predictions[choose_subject].append(group_to_pick)
                    except:
                        self.predictions[choose_subject] = [group_to_pick]
        self.predictions = OrderedDict(sorted(self.predictions.items(), key=lambda x: len(x[1]), reverse=False))

        """self.predictions = {Subjects_Groups.Subject: Subjects_Groups.Group, Subjects_Groups.Group, 
                                Subjects_Groups.Subject: Subjects_Groups.Group, Subjects_Groups.Group, ... }"""

    def get_priority(self):
        """Sets self.priority for students that don't have much groups to choice.
        Lower priority number = Student will be signed to groups before others.
        This will save a place in groups for students who have only one passible group to pick, before others take that place."""
        for key, value in self.predictions.items():
            if self.priority > len(value):
                self.priority = len(value)
            else:
                pass

def in_range(start_a, end_a, start_b, end_b):
    """Checks if groups don't impose on each other in time. Works both for time and date."""
    if end_a < start_a:
        raise Exception()

    if end_a <= start_b:
        return False

    if start_a >= end_b:
        return False

    return True