#author: bugzzy

from django.db import models
from ThoughtXplore import txMisc, txUser


class Subjects(models.Model):
    """
    This class defines all the subjects
    
    """
    Subject_id= models.IntegerField()
    Subject_name= models.CharField(max_length=50)
    Description= models.TextField()
    Subject_id.primary_key=True
    
class Topics(models.Model):
    """
    
    
    
    """
    Topic_id= models.IntegerField()
    Subject_id= models.ForeignKey(Subjects)
    Topic_name= models.CharField(max_length=50)
    Topic_id.primary_key=True
    
    
class Question_levels(models.Model):
    """
    here questions in different levels will have different scoring criteria  
    """
    
    Level_id= models.IntegerField()
    Level_name= models.CharField(max_length=50)
    Level_Desc= models.TextField()
    Level_marks_correct= models.FloatField()
    Level_marks_wrong= models.FloatField()
    Level_id.primary_key=True
    
class Qtype(models.Model):
    """
    This class defines the type of the quiz
    
    """
    Qtype_id= models.IntegerField();
    Quiz_type= models.CharField(max_length=50)
    Qtype_desc=models.TextField()
    Qtype_id.primary_key= True;
    
class Quiz_Main(models.Model):
    """
    This class describes the main model for quiz having all i
    descriptions like title, expiry and activation dates, total q
    questions, score and all.
       
    """
    Quiz_id= models.IntegerField()
    Ref_ID= models.IntegerField()
    Quiz_title= models.CharField(max_length=100)
    Quiz_Desc= models.TextField()
    Quiz_Expiry= models.DateTimeField()
    Quiz_Activation= models.DateTimeField()
    Qtype_id= models.ForeignKey(Qtype)
    Total_Questions= models.IntegerField()
    Total_score= models.FloatField()  #to be updated after selecting all the questions for the quiz 
    Cut_Off= models.FloatField()    #to be calculated on the basis of no_of questions selected from each level
    Attempt_credits= models.IntegerField()
    Quiz_id.primary_key=True

class Questions(models.Model):

    """
    will serve as a quesion_bank for any quiz  
    """
    # Quiz_id= models.ForeignKey(Quiz_Main)
    Ques_id= models.IntegerField()
    Question_detail= models.TextField()
    Level_id= models.ForeignKey(Question_levels)
    Topic_id= models.ForeignKey(Topics)
    Pic_id= models.IntegerField()
    Ques_id.primary_key=True
    
    
class Solutions(models.Model):
    
    """
    """
    Sol_id= models.IntegerField()
    Ques_id= models.ForeignKey(Questions)
    Options_desc=models.TextField()
    Is_correct=models.BooleanField()
    Pic_id= models.IntegerField()
    Sol_id.primary_key=True
    
class Quiz_level_mapping(models.Model):
    Quiz_id= models.ForeignKey(Quiz_Main)
    Level_id= models.ForeignKey(Question_levels)
    Level_question_count= models.IntegerField() #to be used for setting no of question per level in a quiz for auto selecting questions mapped with that quiz
    Level_cutoff= models.IntegerField()
    

    

class QQmapping(models.Model):
    """
    this is for mapping questions from question_bank to
    quizes
    
    """
    Quiz_id= models.ForeignKey(Quiz_Main)
    Ques_id=models.ForeignKey(Questions)


class QUsers(models.Model):
    """
    """
    
    Quiz_id= models.ForeignKey(Quiz_Main)
    Perm_id= models.ForeignKey(txMisc.models.PermissionContentType)
    User_id= models.ForeignKey(txUser.models.User)
    Attempts_Credits_left= models.IntegerField()
    
class Complete_Quiz_Attempts(models.Model):
    """
    """
    Attempt_id=models.IntegerField()
    Attempt_id.primary_key=True
    Quiz_id=models.ForeignKey(Quiz_Main)
    User_id=models.ForeignKey(txUser.models.User)
    Attempt_date_time=models.DateTimeField()
    Score= models.FloatField()   
    Q_attempted=models.IntegerField()
    Correct_attempts=models.IntegerField()
    
    
class User_Attempt_Details(models.Model):
    """
    
    """
    Attempt_id= models.ForeignKey(Complete_Quiz_Attempts)
    Ques_id=models.ForeignKey(Quiz_Main)
    Ques_index= models.IntegerField()
    User_solution= models.CharField(max_length=50)
    Correct_solution= models.CharField(max_length=50)
    Is_attempted= models.BooleanField()
    Level_id= models.ForeignKey(Question_levels)
    Ques_score=models.FloatField()  #to be calculated on the basis of scoring_scheme in table Question_levels

    