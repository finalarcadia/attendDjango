from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models
from django.utils import timezone

# Create your models here.

class UniversityDim(models.Model):
    UniversityDimPK = models.AutoField(primary_key=True)
    universityCode = models.IntegerField()
    universityName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.universityName

class Class(models.Model):
    ClassPK = models.AutoField(primary_key=True)
    classId = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    startTime = models.TimeField(default=timezone.now())
    endTime = models.TimeField(default=timezone.now())
    startDate = models.DateField(default=timezone.now())
    endDate = models.DateField(default=timezone.now())
    lateThreshold = models.TimeField(null=True, blank=True)
    absentThreshold = models.TimeField(null=True, blank=True)
    locationFlag = models.BooleanField(blank=True, default=False)
    latitude = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, blank=True,max_digits=9, decimal_places=6)
    codeFlag = models.BooleanField(blank=True, default=False)
    code = models.CharField(null=True, blank=True, max_length=5)
    codeExpirationDate = models.DateTimeField(null=True, blank=True)
    universityKey = models.ForeignKey(UniversityDim, on_delete=models.CASCADE)

    def __str__(self):
        return self.classId

class Attendance(models.Model):
    attendancePK = models.AutoField(primary_key=True)

    # below are the joins
    classkey = models.ForeignKey(Class, on_delete=models.CASCADE)
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    #end of joins

    classId = models.IntegerField() #get from class join
    className = models.CharField(max_length=100) #get from class join
    studentFirstName = models.CharField(max_length=100) #get from user_id
    studentLastName = models.CharField(max_length=100) #get from user_id

    date = models.DateField(default=timezone.now())
    time = models.TimeField(default=timezone.now())

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

class UserDetailDim(models.Model):
    UserDetailDimPK = models.AutoField(primary_key=True)
    schoolId = models.IntegerField()
    #below are the joins
    universityKey = models.ForeignKey(UniversityDim, on_delete=models.CASCADE)
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    #end of joins
    user_id = models.IntegerField()
    universityCode = models.IntegerField()

class ClassRequest(models.Model):
    classRequestPK = models.AutoField(primary_key=True)
    #below are the joins
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    schoolIdKey = models.ForeignKey(UserDetailDim, on_delete=models.CASCADE)
    classIdKey = models.ForeignKey(Class, on_delete=models.CASCADE)
    #end of joins
    className = models.CharField(max_length=100)
    universityName = models.CharField(max_length=100) #get from school_id join
    userType = models.BooleanField(default=False) #get from user_id join 1 for professor, 0 for student


class ClassRoster (models.Model):
    classRosterPK = models.AutoField(primary_key=True)

    #below are the joins
    classIdKey = models.ForeignKey(Class, on_delete=models.CASCADE)
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    #end of joins

    className = models.CharField(max_length=100) #get from class join
    studentName = models.CharField(max_length=100)  #get from user_id join
    professorName = models.CharField(max_length=100)  #get from user_id join
    adminName = models.CharField(max_length=100) #get from user_id join
