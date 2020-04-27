from django.db import models


class Student(models.Model):
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=50
    )

    name = models.CharField(
        verbose_name='Имя',
        max_length=50
    )

    birthday = models.DateField(
        verbose_name='Дата рождения',
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=50
    )

    class Kurs(models.IntegerChoices):
        FIRST = 1
        SECOND = 2
        THIRD = 3
        FOURTH = 4
        FIFTH = 5
        SIXTH = 6
    kurs = models.IntegerField(
        verbose_name='Курс',
        choices=Kurs.choices
    )

    stipend = models.IntegerField(
        verbose_name='Стипендия',
    )

    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE,
        verbose_name='Университет'
    )

    def __str__(self):
        return self.surname + ' ' + self.name

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'


class Lecturer(models.Model):

    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=50
    )

    name = models.CharField(
        verbose_name='Имя',
        max_length=50
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=50
    )

    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE,
        verbose_name='Университет'
    )

    subjects = models.ManyToManyField(
        'Subject',
        verbose_name='Предметы',
    )

    def __str__(self):
        return self.surname + ' ' + self.name

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'


class University(models.Model):

    name = models.CharField(
        verbose_name='Название',
        max_length=50
    )

    rating = models.IntegerField(
        verbose_name='Рейтинг'
    )

    city = models.CharField(
        verbose_name='Город',
        max_length=50
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'университет'
        verbose_name_plural = 'университеты'


class Subject(models.Model):

    name = models.CharField(
        verbose_name='Название',
        max_length=50
    )

    hour = models.IntegerField(
        verbose_name='Часы'
    )

    class Semester(models.IntegerChoices):
        KURS_1_SEM_1 = 1
        KURS_1_SEM_2 = 2
        KURS_2_SEM_1 = 3
        KURS_2_SEM_2 = 4
        KURS_3_SEM_1 = 5
        KURS_3_SEM_2 = 6
        KURS_4_SEM_1 = 7
        KURS_4_SEM_2 = 8
        KURS_5_SEM_1 = 9
        KURS_5_SEM_2 = 10
        KURS_6_SEM_1 = 11
        KURS_6_SEM_2 = 12
    semester = models.IntegerField(
        verbose_name='Семестр',
        choices=Semester.choices
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'предмет обучения'
        verbose_name_plural = 'предметы обучения'


class ExamMark(models.Model):

    class Mark(models.IntegerChoices):
        MARK_1 = 1
        MARK_2 = 2
        MARK_3 = 3
        MARK_4 = 4
        MARK_5 = 5
    mark = models.IntegerField(
        verbose_name='Оценка',
        choices=Mark.choices
    )

    subject = models.ForeignKey(
        'Subject',
        verbose_name='Предмет',
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        'Student',
        verbose_name='Студент',
        on_delete=models.CASCADE
    )

    date = models.DateField(
        verbose_name='Дата',
    )

    def __str__(self):
        return f'Оценка: {self.mark}'

    class Meta:
        verbose_name = 'оценка по экзамену'
        verbose_name_plural = 'оценки по экзамену'
