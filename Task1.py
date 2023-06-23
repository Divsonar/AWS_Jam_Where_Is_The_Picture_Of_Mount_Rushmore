def extract_text_from_image(bucket_name, image_key):
    '''Extracts text from an image by calling Amazon Rekognition detect_text API
       Arguments:
           bucketName (str): Name of the S3 bucket containing images
           image_key (str): object key of the image
       Output:
           text (str): Space joined text lines found on the image       
    '''
    rekog_session = boto3.Session(profile_name='default')
    rekog_client = rekog_session.client('rekognition')
    response = rekog_client.detect_text(Image={'S3Object': {'Bucket': bucket_name, 'Name': image_key}})
    textDetections = response['TextDetections']
    text_tokens=[]
    for text in textDetections:
        if text['Type'] == 'LINE':
            text_tokens.append(text['DetectedText'])
    text = ' '.join(text_tokens) # Asuming text_tokens is a list of tokens of type 'LINE' from the API response
    return(text.lower())

## Later part
task1_answer = '117.jpg'### YOUR ANSWER IN THE FORM of 'xxx.jpg'
plot_image(task1_answer, image_title='')
