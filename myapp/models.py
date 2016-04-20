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
    lateThreshold = models.TimeField()
    absentThreshold = models.TimeField()
    locationFlag = models.BooleanField(blank=True, default=False)
    latitude = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, blank=True,max_digits=9, decimal_places=6)
    codeFlag = models.BooleanField(blank=True, default=False)
    code = models.CharField(null=True, blank=True,max_length=5)
    codeExpirationDate = models.DateTimeField(null=True, blank=True)




    def __str__(self):
        return self.classId

class Attendance(models.Model):
    classId = models.ForeignKey(Class, on_delete=models.CASCADE)
    studentName = models.CharField(max_length=200)
    date = models.DateField()
    ATTEMPT = 'Attempt'
    PRESENT = 'Present'
    LATE = 'Late'
    ABSENT = 'Absent'
    MARK_CHOICES = (
        (ATTEMPT, 'Attempt'),
        (PRESENT, 'Present'),
        (LATE, 'Late'),
        (ABSENT, 'Absent'),
    )
    mark = models.CharField(max_length=10,
                                      choices=MARK_CHOICES,
                                      default=ATTEMPT)

    def __str__(self):
        return self.studentName
