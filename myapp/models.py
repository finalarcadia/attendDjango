from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models
from django.utils import timezone

# Create your models here.

class University(models.Model):
    universityPK = models.AutoField(primary_key=True)
    #Dont plan to use for now
    #universityCode = models.IntegerField()
    universityName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.universityName

class Class(models.Model):
    classPK = models.AutoField(primary_key=True)
    classId = models.CharField(max_length=30)
    #Dont plan to use for now
    #name = models.CharField(max_length=100)
    startTime = models.TimeField()
    endTime = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()
    lateThreshold = models.TimeField(null=True, blank=True)
    absentThreshold = models.TimeField(null=True, blank=True)
    locationFlag = models.BooleanField(default=False)
    latitude = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, blank=True,max_digits=9, decimal_places=6)
    codeFlag = models.BooleanField(default=False)
    code = models.CharField(null=True, blank=True, max_length=5)
    codeExpirationDate = models.DateTimeField(null=True, blank=True)
    universityKey = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.classId

class Attendance(models.Model):
    attendancePK = models.AutoField(primary_key=True)

    # below are the joins
    classkey = models.ForeignKey(Class, on_delete=models.CASCADE)
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    #end of joins
    
    """
    Don't plan to use for now - wanna keep the biggest table light on girth
    classId = models.IntegerField() #get from class join
    className = models.CharField(max_length=100) #get from class join
    studentFirstName = models.CharField(max_length=100) #get from user_id
    studentLastName = models.CharField(max_length=100) #get from user_id
    """

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
    date = models.DateField()
    time = models.TimeField()

class UserDetail(models.Model):
    userDetailPK = models.AutoField(primary_key=True)
    userType = models.CharField(max_length=10)
    #below are the joins
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    universityKey = models.ForeignKey(University, on_delete=models.CASCADE)
    #end of joins
    schoolId = models.IntegerField()
    """
    Don't plan to use for now
    not even sure what an user_id is - they already have PK and schoolId
    user_id = models.IntegerField()
    universityCode = models.IntegerField()
    """

class ClassRequest(models.Model):
    classRequestPK = models.AutoField(primary_key=True)
    #below are the joins
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    #Dont think we need this - it would be a FK on university anyway, not userDetail
    #schoolIdKey = models.ForeignKey(UserDetail, on_delete=models.CASCADE)
    classIdKey = models.ForeignKey(Class, on_delete=models.CASCADE)
    #end of joins
    className = models.CharField(max_length=100)
    #dont think we need this
    #universityName = models.CharField(max_length=100) #get from school_id join
    
    #0 student, 1 professor
    #userType = models.BooleanField(default=False) #get from user_id join
    
    #added this to implement "Student x dropped from class y request(notification)"
    #0 normal request, 1 drop request
    requestType = models.BooleanField(default=False)


class ClassRoster (models.Model):
    classRosterPK = models.AutoField(primary_key=True)

    #below are the joins
    classIdKey = models.ForeignKey(Class, on_delete=models.CASCADE)
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    #end of joins

    #className = models.CharField(max_length=100) #get from class join
    #studentName = models.CharField(max_length=100)  #get from user_id join
    #professorName = models.CharField(max_length=100)  #get from user_id join
    #adminName = models.CharField(max_length=100) #get from user_id join
