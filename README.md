# AWS_Jam_Where_Is_The_Picture_Of_Mount_Rushmore  
Repo for AWS Jam Challenge - Where is the picture of Mount Rushmore? Solution  
Category : Machine Learning  

Business Problem  
Welcome to this challenge! You have been recently hired by Anycorp (a major news broadcaster) as a data scientist. Your boss (non-technical) tells you that the company has built a large image archive over the years. Unfortunately, there is no/very little metadata associated with the images which makes it difficult for Anycorp journalists and news anchors to find relevant ones. Your boss points out that most of the images contain text which is important for understanding the context of the image. For your first project, your boss asks you to build a smart cloud solution to automatically extract metadata from the images.  

Learning Objectives  
In this challenge, you are going to extract various type of information from the images to make it easier for the Anycorp journalists to find relevant images. To acomplish this goal, you are going to leverage AWS image (Amazon Rekogntion) and NLP (Amazon Comprehend) AI services which make advanced machine learning accessible without the need to train any model!  

Task 1 : Extract Text from Images using Amazon Rekognition   
Task 2 : Extract Dominant Language from text using Amazon Comprehend  
Task 3 : Sentiment Analysis Using Amazon Comprehend AI Service!  
Task 4 : Count Faces on the Image using Amazon Rekognition!  
Task 5 : Label images using Amazon Rekognition 'detect_labels' API  

# TASK 1  

Background  
You have been recently hired by Anycorp (a major news broadcaster) as a data scientist. Your boss (non-technical) tells you that the company has built a large image archive over the years. Unfortunately, there is no/very little metadata associated with the images which makes it difficult for Anycorp journalists and news anchors to find relevant ones. Your boss points out that most of the images contain text which is important for understanding the context of the image. For your first project, your boss asks you to build a smart cloud solution to automatically extract metadata from the images.

Your Task  
You manager is writing an article on American civil war and is looking for the image of Abraham Lincoln statue. He mentions that although the word 'Lincoln' is not carved on the statue directly, it is engraved on the wall behind him. You have a little time to find the image! In this first task, you are going to extract text from images stored in S3 using Amazon Rekognition 'detect_text' API. Please note that Task #2 and Task #3 depend on correct completion of Task #1. More information on Amazon Rekognition 'detect_text' API: https://docs.aws.amazon.com/rekognition/latest/dg/text-detecting-text-procedure.html To complete this task, you need to:

Step #1:  
Complete the "extract_text_from_image" function: This function returns text in an image stored in S3 by using Amazon Rekognition 'detect_text' API. Remember, you need to extract text tokens from the response returned by Rekognition and then join them by a single space (included in the code). The function should return a string containing all the text lines found in the image joined by single spaces. The portion of the function you write shouldn't be more than a few lines of code.

Please note that the API response from Amazon Rekognition is a Python dictionary. It detects both "LINE" and "WORD" in the image which are linked together using a "ParentID" field for the "WORDS" tokens. So, in order to extract and combine text from the json response, you just need to first extract a list of tokens with "Type: LINE" (text_tokens) and then join them with a space (written for you). Just iterate over response['TextDetections'] and check if the item['Type'] == 'LINE'. If yes, token['DetectedText'] gives you the text in that line. Join all of these line tokens with a space as shown in the code.

Step #2:  
Let's run the "extract_text_from_image" function you just completed on all the images. It is going to extract text from all images stored in S3 and populates the "text_in_image" column of the results_df. You don't need to do anything (no coding) other than running the code block under Task 1 Step 2 subsection. Please makes sure the "extract_text_from_image" function in Step #1 works as expected since this step can take a few minutes to complete and repeating it would take your time it. After it is done, take a look at "results_df" dataframe to make sure the "text_in_image" is populated. Other columns should be empty at this point.

Step #3:  
Find the image file name with the term "Lincoln" (case insensitive) in it. To do that you can iterate over the of the "results_df" dataframe" and check if the term "Lincoln" exist in the "text_in_image" field. You can then either use the dataframe index or the 'image_key' column to extract the image file name. Once you find that image, supply "task1_answer" variable with the image file name. Your response should be a string in the form of 'xxx.jpg'.

Run 'upload_answer_to_s3' line to upload you answer as json to S3. You are done! You'll receive credit in few minutes if your answer is correct. Remember, you have to complete Step #1 and Step #2 before Step #3 or you will not get credit!

Getting Started:  
The entire challenge runs from a SageMaker Notebook already provisioned for you. Once in the AWS Console, type "SageMaker" in the search bar on top or select SageMaker from the "Services" menu (top left). In the SageMaker homepage, select SageMaker Notebook from the left menu. There should be a running SageMaker Notebook instance ready for you. Click on Jupyter and click on "Where_is_the_Picture_of_Mount_Rushmore_.ipynb". You need to complete this notebook which is broken down into five tasks.

For this challenge, you have access to about 100 images. The images are uploaded to S3 and also to the SageMaker Notebook instance at:
'/home/ec2-user/SageMaker/images/'

Inventory:  
SageMaker Notebook Instance
Partially filled Jupyter Notebook
S3 Bucket

Service you use:  
Amazon Rekognition
S3
Task Validation:
The task automatically completes once you extract text for all images, find the image with the term 'Lincoln' and submit your answer using the 'submit_your_answer' (provided in the notebook).
