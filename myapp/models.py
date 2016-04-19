from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Class(models.Model):
    classId = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    startTime = models.TimeField()
    endTime = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()
    
    def __str__(self):
        return self.classId

class Attendance(models.Model):
    classId = models.ForeignKey(Class, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=200)
    date = models.DateField()
    ATTEMPT = 'AT'
    PRESENT = 'PR'
    LATE = 'LT'
    ABSENT = 'AB'
    MARK_CHOICES = (
        (ATTEMPT, 'Attempt'),
        (PRESENT, 'Present'),
        (LATE, 'Late'),
        (ABSENT, 'Absent'),
    )
    mark = models.CharField(max_length=2,
                                      choices=MARK_CHOICES,
                                      default=ATTEMPT)
    
    def __str__(self):
        return self.studentName