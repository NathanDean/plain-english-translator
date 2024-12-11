import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.getenv('ANTHROPIC_API_KEY')
client = anthropic.Anthropic()

input_text = "All the works in this section have one core formal concern in common: the idea of ‘time’ (and space). The artist’s creative act of dissolution combines stillness and the intimation of motion, leading us to the very edge of identifiable form and playfully subverting minimalist concerns."

def make_api_request(input_text):

    message = client.messages.create(

        model = 'claude-3-5-sonnet-20241022',
        max_tokens = 1000,
        temperature = 0,
        system = 'Please translate the text supplied into the simplest plain English possible while maintaining their meaning.  Use the guidelines of the Plain English Campaign to guide you.  Please return only the translated text and nothing else.',
        messages = [

            {

                'role': 'user',
                'content': [

                    {

                        'type': 'text',
                        'text': input_text

                    }

                ]

            }

        ]

    )

    text = message.content[0].text

    return text

text = make_api_request(input_text)