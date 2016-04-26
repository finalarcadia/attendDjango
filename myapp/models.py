from __future__ import unicode_literals
from django.contrib.auth.models import User, Group
from django.db import models
from django.utils import timezone

# Create your models here.

class University(models.Model):
    universityPK = models.AutoField(primary_key=True)
    
    universityName = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.universityName

class Class(models.Model):
    classPK = models.AutoField(primary_key=True)
    
    classId = models.CharField(max_length=30)
    updated = models.DateTimeField(auto_now=True)
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
    codeExpiration = models.TimeField(null=True, blank=True)
    
    #FKS
    universityKey = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.classId

class Attendance(models.Model):
    attendancePK = models.AutoField(primary_key=True)
    
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    
    ATTEMPT = 'attempt'
    PRESENT = 'present'
    LATE = 'late'
    ABSENT = 'absent'
    MARK_CHOICES = (
        (ATTEMPT, 'attempt'),
        (PRESENT, 'present'),
        (LATE, 'late'),
        (ABSENT, 'absent'),
    )
    mark = models.CharField(max_length=10,
                                      choices=MARK_CHOICES,
                                      default=ATTEMPT)

    #FKS
    classkey = models.ForeignKey(Class, on_delete=models.CASCADE)
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    
    #class Meta:
        #unique_together = ('userIdKey', 'classkey', 'date')

class UserDetail(models.Model):
    userDetailPK = models.AutoField(primary_key=True)
    
    userType = models.CharField(max_length=10)
    schoolId = models.IntegerField()
    
    #FKS
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    universityKey = models.ForeignKey(University, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('universityKey', 'userIdKey',)

class ClassRequest(models.Model):
    classRequestPK = models.AutoField(primary_key=True)
    
    requestType = models.BooleanField(default=False)
    
    #FKS
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    classIdKey = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('classIdKey', 'userIdKey',)


class ClassRoster (models.Model):
    classRosterPK = models.AutoField(primary_key=True)

    #FKS
    classIdKey = models.ForeignKey(Class, on_delete=models.CASCADE)
    userIdKey = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('classIdKey', 'userIdKey',)
