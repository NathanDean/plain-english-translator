import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

api_key = os.getenv('ANTHROPIC_API_KEY')
client = anthropic.Anthropic()

def make_api_request(input_text):

    message = client.messages.create(

        model = 'claude-3-5-sonnet-20241022',
        max_tokens = 1000,
        temperature = 0,
        system = 'Please translate the text supplied into the simplest plain English possible while maintaining its meaning.  Use the guidelines of the Plain English Campaign to guide you.  Please return only the translated text and nothing else.',
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