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

# TASK 2

Background:  
Your manager is happy with your progress but tells you that some of the images contain languages other than English. It is important to know which ones, as it impacts image selection. So, she wonders if it is possible to detect the dominant language automatically.

Your Task:  
Your task is first to find dominant language in the text of all images. Out of all images containing German text (not all images), which one has the highest dominant language confidence score. To do this, you are going to leverage detect_dominant_language API of Amazon Comprehend AI service. More about the 'detect_dominant_language' API:

https://docs.aws.amazon.com/comprehend/latest/dg/get-started-api-dominant-language.html

Boto3 Amazon Comprehend API 'detect_dominant_language' reference:

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_dominant_language

Step #1 (YOUR INPUT NEEDED):  
Complete "extract_dominant_language" function: This function uses Amazon Comprehend detect_dominant_language API to detect the dominant language in the text. Once you receive raw response from Amazon Comprehend, analyze it to see where you can find dominant language code and dominant language score. Return both the dominant language code and the dominant language score (detection confidence). The portion of the function you write shouldn't be more than a few lines of code.

Step #2:  
Let's run the "extract_dominant_language" function you just completed on the text of all the images. It is going to extract dominant language and confidence score from 'text_in_image' column of 'results_df' and fill the 'dominant_language_code' and 'dominant_language_score' columns. You don't need to do anything (no coding) other than running the code block under Task 2 Step 2 subsection. Please makes sure the "extract_dominant_language" function in Step #1 works as expected before running this step. After it is done, take a look at "results_df" dataframe to make sure the 'dominant_language_code' and 'dominant_language_score' are populated. Other columns should be empty at this point.

Step #3 (YOUR INPUT NEEDED):  
Out of all images with German text (language code: 'de'), which one has the higest 'dominant_language_score'? Code is provded to filter "results_df" to rows with German text. You can then either use the 'index' or the 'image_key' column to extract the image file name. Once you find that image, populate "task2_answer" with the image file name. Your response should be a string in the form of 'xxx.jpg'.

Run 'upload_answer_to_s3' line to upload you answer as json to S3. You are done! You'll receive credit in few minutes if your answer is correct.

Inventory:  
SageMaker Notebook Instance
Partially filled Jupyter Notebook
S3 Bucket

Service you use:  
Amazon Comprehend
S3

Task Validation:  
The task automatically completes once you find dominant language and confidence scores for text in all images, find the image with highest language confidence score (out of of images with German text), and submit your answer using the 'submit_your_answer' (provided in the notebook).

# TASK 3

Background:  
You wonder if you can do automated sentiment analysis and further enrich the image metadata. To do this, you are going to leverage 'detect_sentiment' API of Amazon Comprehend AI service. More about the 'detect_sentiment' API:

https://docs.aws.amazon.com/comprehend/latest/dg/how-sentiment.htmlBoto3

Amazon Comprehend API 'detect_sentiment' reference:

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html#Comprehend.Client.detect_sentiment

Your Task:
Your task is extract sentiment and associated scores from text found on each of the images, and find the image with most negative sentiment among those with English text.

Step #1:
Complete 'sentiment_detection' function: This function uses Amazon Comprehend 'detect_sentiment' API to extract text sentiment. Extract both the sentiment and sentiment_scores for each of the [POSITIVE | NEGATIVE | NEUTRAL | MIXED] sentiment possibilities. The portion of the function you write shouldn't be more than a few lines of code. First call Amazon Comprehend 'detect_sentiment' and get a raw response. Analyze the response and make see how you can extract both sentiment and sentiment score. sentiment_score is going to be a Python dictionary. You can complete this is less than 5 lines of code!

Step #2:
Let's run the 'sentiment_detection' function on the text of all images. It is going to extract sentiment and see sentiment scores from 'text_in_image' column of 'results_df' and fill the 'sentiment' and four 'sentiment_score' columns. You don't need to do anything (no coding) other than running the code block under Task 3 Step 2 subsection. Please makes sure the "sentiment_detection" function in Step #1 works as expected before running this step. After it is done, take a look at "results_df" dataframe to make sure the 'sentiment' and four 'sentiment_score' are populated. Other columns should be empty at this point. Note that in some cases it is not possible to extract the sentiment (maybe not enough text). Don't worry if you see those cases!

Step #3:
Based on the 'sentiment_negative_score' and 'dominant_language_code' column of the results_df, which image has the most negative English text sentiment in it? Code is provided to sort the dataframe by 'sentiment_negative_score' in descending order. You can then either use the 'index' or the 'image_key' column to extract the image file name. Once you find that image, populate "task3_answer" with the image file name. Your response should be a string in the form of 'xxx.jpg'.

Run 'upload_answer_to_s3' line to upload you answer as json to S3. You are done! You'll receive credit in few minutes if your answer is correct.

Inventory:  
SageMaker Notebook Instance
Partially filled Jupyter Notebook
S3 Bucket

Service you use:  
Amazon Comprehend
S3

Task Validation:  
The task automatically completes once you extract text sentiment and associate scores for all the images, find the image with most negative English text sentiment and submit your answer using the 'submit_your_answer' (provided in the notebook).

