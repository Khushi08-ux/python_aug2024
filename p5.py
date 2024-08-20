 #Accept average score from the student of his exam and print his result as follows:
 
  # 0 to 49 is fail 
  #50 to 74 is second class
  # 76 to 90 is first calss also check for invalid score
   
avg= int(input('Enter your score:'))
if  avg ==0 and avg<=49:
       print('Fail')
elif avg<49 and avg==74:
       print ('Second class')
elif avg>=76 and avg==90:
       print('First class')     
elif avg>90:
    print('Distinction')             
else:
    print('Invalid score')     
      
  