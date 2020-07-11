CONTENTS
========
Introduction
General Info
Inputs
Development
Additional Information
Note

INTRODUCTION
============
Algorithm to find difficulty of a question by using the Details which are given under the topic Inputs. 
The Question which may be An MCQ, Programming Question, Fill Up or Math the Following. This Algorithm derives a solution according to the type of the Question.

GENERAL INFO
============
Algorithm to find difficulty of the question.

INPUTS
======
1) Question type - MCQ, Fill-up, Programming, Match the following
2) Manually assigned difficulty - Easy, Medium, Hard
3) Total number of students who have attended this question
	a) Time taken by each student to answer this question
	b) Number of times the answer was changed if it is MCQ type question
	c) Number of times the program was compiled if it is programming question
	d) Number of hints used
	e) Programming language used if it is programming question (c, c++, java etc)
4) Feedback given for this question by other students
5) Total number of students who have answered it right
6) Total number of students who have answered it wrong
7) Total number of students who have answered it partially correct
8) Maximum marks allocated for this question

DEVELOPMENT
===========
Read input spreadsheet file.
Each row is a Separate Question data. So the algorithm will for N-1 times. Each time, It will print the difficulty level of the Question.
Accuracy of Question is derived from the values total number of students attempted the question, 
number of students who have answered it right, number of students who have answered it wrong, number of students who have answered it partially correct.
According to the Accuracy of a Question, Difficulty Level point is assigned.
Average time taken to answer a particular question is calculated.
Average number of times the answer was changed if it is MCQ type question is calculated.
Average number of times the program was compiled if it is programming question is calculated.
Average number of of hints used is calculated.
According to the above 4 average values, Difficulty Level point gets increased.
Finally result will be produced using Difficulty level point.

ADDITIONAL INFORMATION
======================
Herewith, I have attached the google drive link of project. Project will run through the Google Colab. Drive contains sample data set also.

Link : https://drive.google.com/drive/folders/1t4LF3qQ44vggxoFMZahxRZ5svnfWBLHn?usp=sharing

Add shared drive folder to your folder. 
Mount drive to Google Colab. Then only input file will be read by project.

NOTE
====
Input file attributes order should not be changed. 
But any number of students data about a particular Question can there. But it should be in same order which is given in sample data set. 
