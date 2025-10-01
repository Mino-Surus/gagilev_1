from django.db import models

class student(models.Model):
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    patronymic = models.CharField("Отчество", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Эл.почта", max_length=100)
    registration_date = models.DateField("Дата регистрации")
    document = models.CharField("Документы", max_length=100)
    level = models.CharField("Уровень", max_length=50)
    
    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"

    def __str__(self): 
        return f"{self.name} {self.surname}"

class teacher(models.Model):
    name = models.CharField("Имя", max_length=100)
    surname = models.CharField("Фамилия", max_length=100)
    patronymic = models.CharField("Отчество", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Эл.почта", max_length=100)
    specialization = models.CharField("Специализация", max_length=100)
    
    class Meta:
        verbose_name_plural = "Преподаватели"
        verbose_name_plural = "Преподаватель"

    def __str__(self): 
        return f"{self.name} {self.surname}"

class course(models.Model):
    enrollment_date = models.DateField("Дата записи")
    name = models.CharField("Название курса", max_length=50)
    teacher_id = models.ForeignKey(teacher, on_delete=models.CASCADE)
    level = models.CharField("Уровень", max_length=100)
    description = models.TextField("Описание", max_length=100)

    class Meta:
        verbose_name_plural = "Курсы"
        verbose_name = "Курс"

    def __str__(self): 
        return f"{self.name}" 

class lessons(models.Model):
    title = models.CharField("Название", max_length=50)
    content = models.TextField("Содержание", max_length=20)
    date = models.DateField("Дата")
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Занятия"
        verbose_name = "Занятие"


    def __str__(self): 
        return f"{self.title}"

class lessons_list(models.Model):
    enrollment_date = models.DateField("Список пройденных занятий")
    lessons_id = models.ForeignKey(lessons, on_delete=models.CASCADE) 
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Списки пройденных занятий"
        verbose_name = "Список пройденных занятий"

    def __str__(self): 
        return f"{self.id}"

class enrollments(models.Model):
    enrollment_date = models.DateField("Дата записи")
    course_id = models.ForeignKey(course, on_delete=models.CASCADE) 
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Записи на занятия"
        verbose_name = "Запись на занятие"


    def __str__(self): 
        return f"{self.id}"
    

