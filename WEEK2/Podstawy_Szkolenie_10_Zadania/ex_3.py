class Member:
    def __init__(self, name):
        self.full_name = name

    def introduce(self):
        print(f'Hi, I\'m {self.full_name}!')


class Student(Member):
    def __init__(self, name, reason):
        super().__init__(name)
        self.reason = reason


class Instructor(Member):
    def __init__(self, name, bio, skill_set):
        super().__init__(name)
        self.bio = bio
        self.skill_set = skill_set

    def add_skill(self, skill):
        self.skill_set.append(skill)


class Workshop:
    def __init__(self, date, subject, instructors=None, students=None):
        self.date = date
        self.subject = subject
        self.instructors = instructors if instructors is not None else []
        self.students = students if students is not None else []

    def add_participant(self, participant):
        if isinstance(participant, Instructor):
            self.instructors.append(participant)
        elif isinstance(participant, Student):
            self.students.append(participant)

    def print_details(self):
        print(f'Workshop - {self.date} - {self.subject}\n')

        print('Students:')
        for idx, student in enumerate(self.students, 1):
            print(f'{idx}. {student.full_name} - {student.reason}')

        print('\nInstructors:')
        for idx, instructor in enumerate(self.instructors, 1):
            skills = ', '.join(instructor.skillset)
            print(f'{idx}. {instructor.full_name} - {skills}')
            print(instructor.bio)


jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Ruby", "I want to help people learn coding.", [])
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Ruby and want to spread the love", [])
nicole.add_skill("Ruby")

workshop = Workshop("12/03/2014", "Shutl")
workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()

sei = Workshop('12/12/19', 'SEI', [], [])
brandon = Instructor('Brandon', 'I am a genius', ['React', 'Node', 'C'])
payvand = Student('Payvand', 'Money')
sei.add_participant(brandon)
sei.add_participant(payvand)
sei.print_details()
