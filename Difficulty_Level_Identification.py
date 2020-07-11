# Import xlrd for performing operations on Excel Sheet
import xlrd 

# Read input from file
workbook = xlrd.open_workbook('entries.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
curr_row = 0

print("Question Id: ","\t\t","Type of Qusetion: ","\t\t","Difficulty Level: ")

# Each row is a seperate question data. So, It will run upto N-th row.
while curr_row < num_rows:
        curr_row += 1

        # Finding Accuracy of Each Question
        type_of_question=worksheet.cell(curr_row,1).value
        total_no_students=int(worksheet.cell(curr_row,8).value)
        difficulty_level_given=worksheet.cell(curr_row,2).value
        max_mark=worksheet.cell(curr_row,3).value
        if total_no_students != 0 :
          total_marks_obtained=max_mark*(worksheet.cell(curr_row,7).value)/2 + max_mark*(worksheet.cell(curr_row,5).value)
          accuracy=(total_marks_obtained/(max_mark*total_no_students))*100
        else:
          print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t\t",difficulty_level_given)
        ''' Finding Average values for Time taken to answer a particular Question, 
        If it is an MCQ, no of times answer was changed, 
        If it is programming Question, no of times compiled, 
        No of hints used to answer the question. '''
        k=9
        average_time_taken=0
        average_no_of_time_answer_changed=0
        average_no_of_time_answer_compiled=0
        average_no_of_hints_used=0
        for i in range(total_no_students):
          average_time_taken+=int(worksheet.cell(curr_row,k).value)
          if type_of_question == "MCQ":
            average_no_of_time_answer_changed+=int(worksheet.cell(curr_row,k+1).value)
          elif type_of_question == "Programming" :
            average_no_of_time_answer_compiled+=int(worksheet.cell(curr_row,k+2).value)
          average_no_of_hints_used+=int(worksheet.cell(curr_row,k+3).value)
          k+=5
        if total_no_students !=0 :
          average_time_taken=average_time_taken/total_no_students
          average_no_of_time_answer_changed=average_no_of_time_answer_changed/total_no_students
          average_no_of_time_answer_compiled=average_no_of_time_answer_compiled/total_no_students
          average_no_of_hints_used=average_no_of_hints_used/total_no_students

        difficulty_value=0
        if total_no_students != 0:
          if difficulty_level_given == "Medium" :
            difficulty_value+=2
          if difficulty_level_given == "Hard" :
            difficulty_value+=3
          if difficulty_level_given == "Easy" :
            difficulty_value+=1
          
          if average_no_of_hints_used <=1 :
            difficulty_value+=1
          elif average_no_of_hints_used <=2:
            difficulty_value+=2
          else :
            difficulty_value+=3

          if accuracy>=0 and accuracy<=33 :
            difficulty_value+=3
          elif accuracy> 33 and accuracy <=60:
            difficulty_value+=2
          elif accuracy > 60:
            difficulty_value+=1
        
        # Finding Difficulty value, If it is an MCQ
        if type_of_question == "MCQ" and total_no_students!=0 :
          
          
          if average_time_taken<=1 :
            difficulty_value+=1
          elif average_time_taken >1 and average_time_taken<=2:
            difficulty_value+=2
          elif average_time_taken>2 :
            difficulty_value+=3
          
          if average_no_of_time_answer_changed <=1 :
            difficulty_value+=1
          elif average_no_of_time_answer_changed >1 and average_no_of_time_answer_changed <=3:
            difficulty_value+=2
          else:
            difficulty_value+=3
          
          q_id = worksheet.cell(curr_row,0).value

          # According to difficulty value, Categorizing the Question whether it is Easy, Medium or hard
          if (difficulty_value <=5):
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t\t","Easy")
          elif (difficulty_value <=10):
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t\t","Medium")
          else :
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t\t","Hard")

        # Finding Difficulty value, If it is a Programmimg Question
        if type_of_question == "Programming" and total_no_students!=0 :
      
          if average_time_taken<=30 :
            difficulty_value+=1
          elif average_time_taken >30 and average_time_taken<= 80:
            difficulty_value+=2
          elif average_time_taken> 80 :
            difficulty_value+=3
          
          if average_no_of_time_answer_compiled <=7 :
            difficulty_value+=1
          elif average_no_of_time_answer_compiled >7 and average_no_of_time_answer_compiled <=14:
            difficulty_value+=2
          else:
            difficulty_value+=3

          q_id = worksheet.cell(curr_row,0).value

          # According to difficulty value, Categorizing the Question whether it is Easy, Medium or hard
          if (difficulty_value <=5):
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t","Easy")
          elif (difficulty_value <=10):
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t","Medium")
          else :
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t","Hard")

        # Finding Difficulty value, If it is a Fill Up
        if type_of_question == "Fill Up" and total_no_students!=0 :
          
          if average_time_taken<=1 :
            difficulty_value+=1
          elif average_time_taken >1 and average_time_taken<=2:
            difficulty_value+=2
          elif average_time_taken>2 :
            difficulty_value+=3
          
          q_id = worksheet.cell(curr_row,0).value
          
          # According to difficulty value, Categorizing the Question whether it is Easy, Medium or hard
          if (difficulty_value <=4):
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t","Easy")
          elif (difficulty_value <=8):
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t","Medium")
          else :
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t","Hard")

        # Finding Difficulty Value, If it is a Match
        if type_of_question == "Match" and total_no_students!=0:
          if average_time_taken<=2 :
            difficulty_value+=1
          elif average_time_taken >2 and average_time_taken<=4:
            difficulty_value+=2
          elif average_time_taken>2 :
            difficulty_value+=3
          
          q_id = worksheet.cell(curr_row,0).value

          # According to difficulty value, Categorizing the Question whether it is Easy, Medium or hard
          if (difficulty_value <=4):
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t\t","Easy")
          elif (difficulty_value <=8):
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t\t","Medium")
          else :
            print("\t",q_id,"\t\t\t",type_of_question,"\t\t\t\t","Hard")
