#author: bugzzy

from django.db import models
from ThoughtXplore import txMisc, txUser
from ThoughtXplore.txMisc.models import StateContentType, PermissionContentType
from ThoughtXplore.txUser.models import User

class test_cities(models.Model):
    name=models.TextField()
    country= models.TextField()
    

class test_centres(models.Model):
    name=models.TextField()
    address=models.TextField()
    city= models.ForeignKey(test_cities)
    capacity=models.IntegerField()

class Subjects(models.Model):
    """
    This class defines all the subjects
    """
    name= models.CharField(max_length=50)
    Description= models.TextField()
    SCI= models.ForeignKey(StateContentType)
     
    
class Question_levels(models.Model):
    """
    here questions in different levels will have different scoring criteria  
    """
    
    Level_name= models.CharField(max_length=50)
    Level_Desc= models.TextField()
    Level_marks_correct= models.FloatField()
    Level_marks_wrong= models.FloatField()
    SCI= models.ForeignKey(StateContentType)

class Qtype(models.Model):
    """
    This class defines the type of the quiz
    
    """
    Quiz_type= models.TextField()
    Qtype_desc=models.TextField()
    SCI= models.ForeignKey(StateContentType)
    
    
class Quiz_Main(models.Model):
    """
    This class describes the main model for quiz having all i
    descriptions like title, expiry and activation dates, total q
    questions, score and all.
       
    """
    test_centres=models.TextField()   #comma seperated centre ids
    Ref_ID= models.IntegerField()
    Quiz_title= models.CharField(max_length=100)
    Quiz_Desc= models.TextField()
    Quiz_Expiry= models.DateTimeField()
    Quiz_Activation= models.DateTimeField()
    Qtype= models.ForeignKey(Qtype)
    Total_Questions= models.IntegerField()
    Total_score= models.FloatField()  #to be updated after selecting all the questions for the quiz 
    Cut_Off= models.FloatField()    #to be calculated on the basis of no_of questions selected from each level
    Attempt_credits= models.IntegerField()
    Subjects=models.TextField()   #it will contain comma seperated ids of Subjects included in this quiz
    SCI= models.ForeignKey(StateContentType)
    
    
class Questions(models.Model):

    """
    will serve as a quesion_bank for any quiz  
    """
    # Quiz_id= models.ForeignKey(Quiz_Main)
    Subject= models.ForeignKey(Subjects)
    Question_detail= models.TextField()
    Level= models.ForeignKey(Question_levels)
    Pics= models.TextField()       #it will have comma seperated ids of pictures  as a question may use more than one pic....
    SCI= models.ForeignKey(StateContentType)
    
    
class Solutions(models.Model):       #each row will be an option for some questions
    
    """
    """
    Ques= models.ForeignKey(Questions)
    Options_desc=models.TextField()
    Is_correct=models.BooleanField()
    Pics= models.TextField()       #it will have comma seperated ids of pictures  as it may use more than one pic....
    SCI= models.ForeignKey(StateContentType)
    
class Quiz_sub_level_mapping(models.Model):
    
    Quiz= models.ForeignKey(Quiz_Main)
    Subject=models.ForeignKey(Subjects)
    Level= models.ForeignKey(Question_levels)
    Level_question_count= models.IntegerField() #to be used for setting no of question per level in a quiz for auto selecting questions mapped with that quiz
    Level_cutoff= models.IntegerField()
    

    

class QQmapping(models.Model):
    """
    this is for mapping questions from question_bank to
    quizes
    
    """
    Quiz= models.ForeignKey(Quiz_Main)
    Ques=models.ForeignKey(Questions)

class QAdmins(models.Model):
    
    Quiz= models.ForeignKey(Quiz_Main)
    User= models.ForeignKey(txUser.models.User)
    Permission=models.ForeignKey(PermissionContentType)
    
class QUsers(models.Model):
    """
    """
    test_centre=models.ForeignKey(test_centres)
    Registration_No= models.TextField()
    Registration_No.unique= True
    Quiz= models.ForeignKey(Quiz_Main)
    User= models.ForeignKey(txUser.models.User)
    Attempts_Credits_left= models.IntegerField()
    
class subject_wise_attempts(models.Model):
    
    Quiz=models.ForeignKey(Quiz_Main)
    User=models.ForeignKey(txUser.models.User)
    subject= models.ForeignKey(Subjects)
    Score= models.FloatField()   
    Q_attempted=models.IntegerField()
    Correct_attempts=models.IntegerField()
    
    
class Complete_Quiz_Attempts(models.Model):
    """
    """
    Quiz=models.ForeignKey(Quiz_Main)
    User=models.ForeignKey(txUser.models.User)
    Attempt_date_time=models.DateTimeField()
    Score= models.FloatField()   
    Q_attempted=models.IntegerField()
    Correct_attempts=models.IntegerField()
    
    
class User_Attempt_Details(models.Model):
    """  
    """
    Attempt= models.ForeignKey(Complete_Quiz_Attempts)
    Ques=models.ForeignKey(Quiz_Main)
    Ques_index= models.IntegerField()
    User_solution= models.CharField(max_length=50)
    Correct_solution= models.CharField(max_length=50)
    Is_attempted= models.BooleanField()
    Level= models.ForeignKey(Question_levels)
    Ques_score=models.FloatField()  #to be calculated on the basis of scoring_scheme in table Question_levels


class QuizLogs(models.Model):
    
    # user making changes
    LogsUser = models.ForeignKey(User)
    # row id being changed
    LogsObject = models.IntegerField()
    LogsPCI = models.ForeignKey(PermissionContentType)
    LogsIP = models.CharField(max_length=20)
    LogsTimeStamp = models.DateTimeField()
    LogsDescription = models.CharField(max_length=200)
    LogsPreviousState = models.CharField(max_length=5000)
    