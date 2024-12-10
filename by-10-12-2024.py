# task 1

class Teacher:

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience

    @property
    def name(self):
        return self.__name

    @property
    def education(self):
        return self.__education

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, years):
        self.__experience = years

    def get_teacher_data(self):
        string = f'{self.__name}, образование: {self.__education}, опыт: {self.__experience} года.'
        print(string)
        return string

    def add_mark(self, student, mark):
        string = f'Учитель {self.__name} поставил {mark} ученику {student}.'
        print(string)
        return (string)

    def remove_mark(self, student, mark):
        string = f'Учитель {self.__name} удалил оценку {mark} у ученика {student}.'
        print(string)
        return (string)
    
    def give_consultation(self, group):
        string = f'Учитель {self.__name} провёл консультацию в {group}.'
        print(string)
        return string
        
teacher_1 = Teacher('Иван Петров', 'БГПУ', 4)
teacher_1.experience = 5
teacher_1.get_teacher_data()
teacher_1.add_mark('Пётр Сидоров', 4)
teacher_1.remove_mark('Дмитрий Степанов', 4)
teacher_1.give_consultation('9Б')

# task 2

class SubjectTeacher(Teacher):

    def __init__(self, name, education, experience, subject, job_title):
        Teacher.__init__(self, name, education, experience)
        self.__subject = subject # Я не понял, что имелось в виду под "перенести из класса Teacher"
        self.__job_title = job_title

    @property
    def subject(self):
        return self.__subject

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, title):
        self.__job_title = title

    def get_teacher_data(self):
        string = f'{self.name}, образование: {self.education}, опыт: {self.experience} года.\nПредмет: {self.subject}, должность: {self.__job_title}.'
        print(string)
        return string

    def add_mark(self, student, mark):
        string = f'Учитель {self.name} поставил {mark} ученику {student}.\nПредмет: {self.subject}'
        print(string)
        return (string)

    def remove_mark(self, student, mark):
        string = f'Учитель {self.name} удалил оценку {mark} у ученика {student}.\nПредмет: {self.subject}'
        print(string)
        return (string)
    
    def give_consultation(self, group):
        string = f'Учитель {self.name} провёл консультацию в {group}.\nПо предмету: {self.subject}, как {self.job_title}.'
        print(string)
        return string
        
teacher_2 = SubjectTeacher('Иван Петров', 'БГПУ', 4, 'Химия' , 'Директор')
teacher_2.experience = 5
teacher_2.get_teacher_data()
teacher_2.add_mark('Пётр Сидоров', 4)
teacher_2.remove_mark('Дмитрий Степанов', 4)
teacher_2.give_consultation('9Б')










