from django.db import models

class student(models.Model):
    name = models.CharField("ФИО", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.CharField("Эл.почта", max_length=100)
    registration_date = models.DateField("Дата регистрации")
    document = models.CharField("Документы", max_length=100)
    level = models.CharField("Уровень", max_length=50)

class teacher(models.Model):
    name = models.CharField("ФИО", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    email = models.CharField("Эл.почта", max_length=100)
    specialization = models.CharField("Специализация", max_length=100)

class course(models.Model):
    enrollment_date = models.DateField("Дата записи")
    name = models.CharField("Название курса", max_length=50)
    teacher_id = models.ForeignKey(teacher, on_delete=models.CASCADE)
    level = models.CharField("Уровень", max_length=100)
    description = models.TextField("Описание", max_length=100)

class lessons(models.Model):
    title = models.CharField("Название", max_length=50)
    content = models.TextField("Содержание", max_length=20)
    date = models.DateField("Дата")
    course_id = models.ForeignKey(course, on_delete=models.CASCADE)

class enrollments(models.Model):
    enrollment_date = models.DateField("Дата записи")
    course_id = models.ForeignKey(course, on_delete=models.CASCADE) 
    student_id = models.ForeignKey(student, on_delete=models.CASCADE)
    progress = models.DecimalField("Процент прохождения курса", max_digits=5, decimal_places=2)

