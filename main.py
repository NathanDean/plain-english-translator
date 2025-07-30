from claude_request import make_api_request
from text_extraction import extract_text

for i in range(1, 5):

    text = extract_text(f'./test_images/test_image_{i}.jpg')
    translation = make_api_request(text)

    print(translation)
    print('\n')