def extract_image_labels(bucket_name, image_key):
    '''Extracts number of faces in the image using Amazon Rekognition 
       Arguments:
           bucketName (str): Name of the S3 bucket containing images
           image_key (str): object key of the image
       Output:
           label (str): Label with highest score       
           label_conf (float): Label confidence score      
    '''
    ### Your code (less than 5 lines of code)
    # Call the API first
    reko_session = boto3.Session()
    reko_client = reko_session.client('rekognition')
    response = reko_client.detect_labels(Image={'S3Object':{'Bucket':bucket_name,'Name':image_key}})
    var = response['Labels'][0]
    label = var['Name']
    label_conf = var['Confidence']
        
    return(label, label_conf)

## Image 156 is the solution but has a sign as label instead of bird. Find the full parent labelling for the image and replace the sign 99 with bird 55
task5_answer = '156.jpg'### YOUR ANSWER IN THE FORM of 'xxx.jpg'
plot_image(task5_answer, image_title=results_df.loc[task5_answer, 'label'])
