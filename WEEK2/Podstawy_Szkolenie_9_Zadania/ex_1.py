class Student:
    def __init__(self, name_, last_name_,  gender_, field_of_study_):
        self.name = name_
        self.last_name = last_name_
        self.gender = gender_
        self.field_of_study = field_of_study_

    def student_information(self):
        print(f'Student: {self.name} {self.last_name}')
        print(f'Gender: {self.gender}')
        print(f'Field of study: {self.field_of_study}')


def main():
    student_1 = Student("John", "Smith", "Male", "IT")
    student_1.student_information()


if __name__ == "__main__":
    main()
