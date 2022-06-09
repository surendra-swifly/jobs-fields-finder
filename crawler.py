import requests
from lxml import html
from requests_html import HTMLSession


class GeneralFinder:
    def __init__(self, url):
        self.url = url

    def get_response(self):
        session = HTMLSession()
        response = session.get(
            self.url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
            },
        )
        if response.status_code == 200:
            return response
        else:
            return None

    def find_label(self, element):
        # parent and preceding-sibling
        if element.xpath("./preceding-sibling::label"):
            return element.xpath(
                "./preceding-sibling::label//text()"
            ), element.xpath("./preceding-sibling::label//@for")
        elif element.xpath("./parent::label"):
            return element.xpath("./parent::label//text()"), element.xpath(
                "./parent::label//@for"
            )
        else:
            return "", ""

    def html_element(self, page, element):
        total_fields = []
        html_elements = page.xpath(f"//{element}")
        if not html_elements:
            return None
        else:
            for html_fields in html_elements:
                label, label_for = self.find_label(html_fields)
                if label:
                    label = " ".join(label)
                    total_fields.append(
                        {
                            "label": label,
                            "label_for": label_for,
                            "html_element_tag": html_fields.tag,
                            "id": html_fields.attrib.get("id", ""),
                            "name": html_fields.attrib.get("name", ""),
                            "type": html_fields.attrib.get("type", ""),
                            "class": html_fields.attrib.get("class", ""),
                            "placeholder": html_fields.attrib.get(
                                "placeholder", ""
                            ),
                        }
                    )
                else:
                    total_fields.append(
                        {
                            "label": label,
                            "label_for": label_for,
                            "html_element_tag": html_fields.tag,
                            "id": html_fields.attrib.get("id", ""),
                            "name": html_fields.attrib.get("name", ""),
                            "type": html_fields.attrib.get("type", ""),
                            "class": html_fields.attrib.get("class", ""),
                            "placeholder": html_fields.attrib.get(
                                "placeholder", ""
                            ),
                        }
                    )
            return total_fields


def main(url):
    finder = GeneralFinder(url)
    fields_total_list = []
    response = finder.get_response()
    if response:
        page = html.fromstring(response.content)
        for element in ["input", "select", "textarea", "button", "label"]:
            fields_list = finder.html_element(page, element)
            if fields_list:
                fields_total_list.extend(fields_list)
    return fields_total_list


if __name__ == "__main__":
    url = "https://www.famplus.de/gast/kinderbetreuerin/stellenangebote/node/1105699"
    field_list_all = main(url)
    with open(
        f'{url.split("//")[1].split("/")[0]}.json', "w", encoding="utf-8"
    ) as f:
        f.write(
            str(field_list_all)
            .replace("'", '"')
            .replace("\xa0", "")
            .replace("\n", "")
        )
