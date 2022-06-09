from base64 import decode
from distutils import text_file
import json


if __name__ == '__main__':
   with open('test_123.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        hidden_fields = [d['html_element_attributes'].get('name') if d['html_element_attributes'].get('name') else d['html_element_attributes'].get('id') for d in data if d['html_element_attributes']['type'] == 'hidden']
        text_fields = [d['html_element_attributes'].get('name') if d['html_element_attributes'].get('name') else d['html_element_attributes'].get('id') for d in data if d['html_element_attributes']['type'] == 'text']
        text_fields_label = [d['label'] for d in data if d['html_element_attributes']['type'] == 'text']
        