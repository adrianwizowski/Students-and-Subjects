# Students-and-Subjects
Program inspired by genetics students from University of Wrocław.
Used to match students with subject they have to sign every term.

## Whats the problem?
Students picks their optional subject from list a semester before subjects start. 
Eg. in winter semester students picks subjects for summer semester.
University automaticly signs them occupational groups for optional subjects.
After that University provides a schedule for summer term. 
Students have to pick obligatory subjects groups to match with their optional subject groups they can't change.

And here comes the trouble, because always something could goes wrong.
Subjects impose on each other and by that students can't attend their classes.

This program may solve this problem showing students which class they should attend to save some nerves for everyone.

## Usage.
### Main_program.py

Core of program. Class containg functions to create Students objects, signing students for classes, checking classes lists.
Program can create Students object from Excel sheet with students names and numbers of groups for subjects they are already in.
Before calling Main class please create subjects and groups for every subject.
Eg.:
Static subject student can't choose or change:
```
abc = Subject('ABC')
Necessary_lists.static_subjects.append(abc)
abc.addgroup(Group('ABC 1', 1, 10, (2018, 2, 19, 8, 0), (2018, 4, 16, 11, 0)))
```

Group('discription', group number, group capacity, date start(year, month, day, hour, min),date end(year, month, day, hour, min))

Subject student have to choose:
```
xyz = Subject('XYZ')
Necessary_lists.choose_subjects.append(xyz)
xyz.addgroup(Group('XYZ 1', 1, 14, (2018, 3, 9, 14, 0), (2018, 3, 23, 17, 0)))
```
After creating all subject and all grops for every subject program will be ready to use.
Subjects discription should be equal to colums names in students Excel sheet.

### Special credits
* [krpisz](https://github.com/krpisz)
Thanks for help and mentoring.
