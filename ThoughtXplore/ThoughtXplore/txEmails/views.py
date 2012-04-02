from ThoughtXplore.txMessaging.txEmails.models import sent_messages 
from django.core.mail import send_mass_mail
from ThoughtXplore.txUser.models import User, UserGroup
from django.shortcuts import render_to_response


'''
format of param


  'message'
  'subject'
  'fromUserID' -- User-id of sender
  
 
to send to a custom list:
  'to_id_list'-- list of User-IDs (not emails)
to send to groups:
  'groupIDs' -- List of Goup-ids  
 
'''


def mailing(request):

    users_= User.objects.all()
    return render_to_response('txEmailMessaging/emailing.htm',{'title':'Email','Users':users_ })


def send_mails(param,isgroups):
    
    
    to_id_list=[]
            
    if(isgroups==1):
        for a in param['groupIDs']:
            for b in UserGroup.objects.filter(Group=a):
                to_id_list.append(b.User)
    else:
        to_id_list=param['to_id_list']
    
    print to_id_list

    to_email_list=[]
    for e in to_id_list:
        for f in User.objects.filter(id=e):
            to_email_list.append(f.UserEmail)
    for e in UserGroup.objects.filter(User=param['fromUserID']):
        fromusergroup= e.Group
    for e in User.objects.filter(id=param['fromUserID']):
        from_=e.UserEmail
    datatuple=[param['subject'], param['message'],from_,to_email_list]
    
   # auth_user_="auth_user"
    #auth_password_="auth_password"
    send_mass_mail(datatuple, fail_silently=True)    
    #db entry
    to_id_list_=""
    to_group_list=""
    if(isgroups==1):
        
        for a in param['groupIDs']:
            to_group_list+=","+a
      
    else:
        
        for a in to_id_list_:
            to_id_list_=","+a
    
    
    sent_messages.mailInsertdb(from_, param['fromUserID'], fromusergroup, param['subject'], param['message'], param['attachment'], "",to_group_list, to_id_list_)
        
     
        