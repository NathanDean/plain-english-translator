from claude_request import make_api_request
from text_extraction import extract_text

text = extract_text("./test_images/test_image_1.jpg")
translation = make_api_request(text)

print(translation)