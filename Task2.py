def extract_dominant_language(text):
    '''Extracts dominant language by calling Amazon Comprehend 'detect_dominant_language' API
       Arguments:
           text (str): Text to be analyzed 
       Output:
           dominant_language_code (str): Deteceted dominant language code       
           dominant_language_score (float): Score that indicates the confidence level on detected dominant language
    '''
    ### Your code (less than 5 lines of code)
    # Call the API first
    comprehend_session = boto3.Session(profile_name='default')
    comprehend_client = comprehend_session.client('comprehend')
    response = comprehend_client.detect_dominant_language(Text=text)
    
    info = response['Languages'][0]
    dominant_language_code = info['LanguageCode']
    dominant_language_score = info['Score']
    return dominant_language_code, dominant_language_score

## Later Part
task2_answer = '110.jpg'### YOUR ANSWER IN THE FORM of 'xxx.jpg'
print('Text: {}'.format(results_df.loc[task2_answer, 'text_in_image']))
print('Dominant Language: {}'.format(results_df.loc[task2_answer, 'dominant_language_code']))
print('Dominant Language Confidence: {}'.format(results_df.loc[task2_answer, 'dominant_language_score']))
plot_image(task2_answer, image_title='')
