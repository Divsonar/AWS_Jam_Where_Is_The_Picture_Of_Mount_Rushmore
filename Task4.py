def extract_num_faces(bucket_name, image_key):
    '''Extracts number of faces in the image using Amazon Rekognition 
       Arguments:
           bucketName (str): Name of the S3 bucket containing images
           image_key (str): object key of the image
       Output:
           n_faces (int): number of faces detected in the image       
    '''
    ### Your code (less than 5 lines of code)
    # Call the API first
    reko_session = boto3.Session()
    reko_client = reko_session.client('rekognition')
    response = reko_client.detect_faces(Image={'S3Object':{'Bucket':bucket_name,'Name':image_key}})
    y=0
    for faces in response['FaceDetails']:
        y = y + 1
​
    n_faces = y
​
    return(n_faces)

## Later part
task4_answer = '143.jpg'### YOUR ANSWER IN THE FORM of 'xxx.jpg'
plot_image(task4_answer, image_title='')
