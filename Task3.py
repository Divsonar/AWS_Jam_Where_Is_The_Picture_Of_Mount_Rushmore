def sentiment_detection(text, language_code):
    '''Extracts sentiment of the text using Amazon Comprehend 
       Arguments:
           text (str): Text to be analyzed 
           language_code (str): 2-letter language code of the text to be analyzed (e.g. "en")
       Output:
           sentiment (str): One the [POSITIVE | NEGATIVE | NEUTRAL | MIXED] returned by Amazon Comprehend    
           sentiment_scores (dict): Confidence that Amazon Comprehend has in the accuracy of its detection 
           of the each of the above sentiments. A dictionary with the following keys [POSITIVE, NEGATIVE, NEUTRAL, MIXED].
           sample:
               sentiment_scores: {
                                    "Mixed": 0.0033542951568961143,
                                    "Positive": 0.9869875907897949,
                                    "Neutral": 0.008563132025301456,
                                    "Negative": 0.0010949420975521207
                                }
    '''
    ### Your code (less than 5 lines of code)
    # Call the API first
    comprehend_session = boto3.Session(profile_name='default')
    comprehend_client = comprehend_session.client('comprehend')
    response = comprehend_client.detect_sentiment(LanguageCode=language_code, Text=text)
    
    sentiment = response['Sentiment'] #Extract from API response
    sentiment_scores = response['SentimentScore'] # Extract from API response (a Python Dictionary)
​
    return sentiment, sentiment_scores

## Later part
task3_answer = '169.jpg'### YOUR ANSWER IN THE FORM of 'xxx.jpg'
plot_image(task3_answer, image_title=results_df.loc[task3_answer, 'text_in_image'])
