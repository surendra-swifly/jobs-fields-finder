from gettext import find
import requests
from lxml import html
from requests_html import HTMLSession
import json



class GeneralFinder:
    def __init__(self, url):
        self.url = url

    def get_response(self):
        session = HTMLSession()
        response = session.get(self.url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        if response.status_code == 200:
            return response
        else:
            return None

    def find_label(self, element):
        # parent and preceding-sibling
        if element.xpath('./preceding-sibling::label'):
            return element.xpath('./preceding-sibling::label//text()'), element.xpath('./preceding-sibling::label//@for')
        elif element.xpath('./parent::label'):
            return element.xpath('./parent::label//text()'), element.xpath('./parent::label//@for')
        else:
            return None, None
def main(url):
    url = 'https://jobs.dashmote.com/o/technical-product-owner-shanghai/c/new'
    finder = GeneralFinder(url)
    fields_list = []
    response = finder.get_response()
    label_for_list = []
    if response:
        page = html.fromstring(response.content)
        input_fields = page.xpath('//input')
        if not input_fields:
            print('No input fields found')
            
        for field in input_fields:
            field_details = {}
            label,label_for = finder.find_label(field)
            if label:
                try:
                    field_details['label_text'], field_details['label_for'] = ''.join(label), label_for
                except:
                    breakpoint()
            else:
                field_details['label_text'], field_details['label_for'] = '', ''
            attributes = field.attrib
            # if attributes.get('id') == 'Candidate_CurrentTitle':
            #     breakpoint()
            field_details.update(attributes)
            fields_list.append(field_details)
        select_fields = page.xpath('//select')
        for field in select_fields:
            field_details = {}
            label = field.xpath('./parent::label/@for')
            if label:
                field_details['label'],  = ''.join(label)
            else:
                field_details['label'] = ''
            attributes = field.attrib
            field_details.update(attributes)
            fields_list.append(field_details)
        textarea_fields = page.xpath('//textarea')
        for field in textarea_fields:
            field_details = {}
            label = finder.find_label(field)
            if label:
                field_details['label'] = ''.join(label)
            else:
                field_details['label'] = ''
            attributes = field.attrib
            field_details.update(attributes)
            fields_list.append(field_details)
        return fields_list
if __name__ == '__main__':
    url = 'https://www.adadigital.se/lediga-jobb/net-backendutvecklare-till-ica-i-stockholm/?src=cb'
    field_list = main(url)
    # with open('hitachi_input_fields.txt', 'w') as f:
    #     for field in fields_list:
    #         f.write(str(field) + '\n')

    with open(f'{url.split("//")[1].split("/")[0]}.json', 'w') as f:
        json.dump(field_list, f, indent=4)

            
   



    