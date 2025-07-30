import os
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './API_credentials.json'

def extract_text(image_path):

    client = vision.ImageAnnotatorClient()
    
    with open(image_path, 'rb') as image_file:

        content = image_file.read()

    image = vision.Image(content = content)

    response = client.annotate_image({

        'image': image,
        'features': [

            {'type_': vision.Feature.Type.TEXT_DETECTION}

        ]

    })

    text = response.text_annotations[0].description if response.text_annotations else ''

    return text