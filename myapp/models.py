from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Class(models.Model):
    ClassPK = models.IntegerField(primary_key=True)
    classId = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    startTime = models.TimeField()
    endTime = models.TimeField()
    startDate = models.DateField()
    endDate = models.DateField()
    lateThreshold = models.TimeField(null=True, blank=True)
    absentThreshold = models.TimeField(null=True, blank=True)
    locationFlag = models.BooleanField(blank=True, default=False)
    latitude = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=6)
    longitude = models.DecimalField(null=True, blank=True,max_digits=9, decimal_places=6)
    codeFlag = models.BooleanField(blank=True, default=False)
    code = models.CharField(null=True, blank=True,max_length=5)
    codeExpirationDate = models.DateTimeField(null=True, blank=True)
    universityKey = models.ForeignKey(UniversityDim, on_delete=models.CASCADE)

    def __str__(self):
        return self.classId

class Attendance(models.Model):
    attendancePK = models.IntegerField(primary_key=True)

    # below are the joins
    classkey = models.ForeignKey(Class, on_delete=CASCADE)
    userIdKey = models.ForeignKey(auth_user, on_delete=CASCADE)
    #end of joins

    classId = models.IntegerField() #get from class join
    className = models.CharField() #get from class join
    studentFirstName = models.CharField() #get from user_id
    studentLastName = models.Charfield() #get from user_id

    date = models.DateField()
    time = models.TimeField()

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

class UniversityDim(models.Model):
    UniversityDimPK = models.IntegerField(primary_key=True)
    universityCode = models.IntegerField()
    universityName = models.Charfield()

class UserDetailDim(models.Model):
    UserDetailDimPK = models.IntegerField(primary_key=True)
    schoolId = models.IntegerField()
    #below are the joins
    universityKey = models.ForeignKey(UniversityDim, on_delete=models.CASCADE)
    userIdKey = models.ForeignKey(auth_user, on_delete=CASCADE)
    #end of joins
    user_id = models.IntegerField()
    universityCode = models.IntegerField()

class ClassRequest(models.Model):
    classRequestPK = models.IntegerField(primary_key=True)
    #below are the joins
    userIdKey = models.ForeignKey(auth_user, on_delete=CASCADE)
    schoolIdKey = ForeignKey(UserDetailDim, on_delete=CASCADE)
    classIdKey = models.ForeignKey(Class, on_delete=models.CASCADE)
    #end of joins
    className = models.CharField()
    universityName = models.Charfield() #get from school_id join
    userType = models.BooleanField(default=False) #get from user_id join 1 for professor, 0 for student


class ClassRoster (models.Model):
    classRosterPK = models.IntegerField(primary_key=True)

    #below are the joins
    classIdKey = ForeignKey(Class, on_delete=True)
    userIdKey = models.ForeignKey(auth_user, on_delete=CASCADE)
    #end of joins

    className = models.Charfield() #get from class join
    studentName = models.Charfield()  #get from user_id join
    professorName = models.Charfield()  #get from user_id join
    adminName = models.Charfield() #get from user_id join
