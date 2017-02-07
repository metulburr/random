from bs4 import BeautifulSoup
import re
html_doc = """
            <a href="http://example.com/elsie" class="sister sisteen" id="link1">Elsie</a>,
            <a href="http://example.com/lacie" class="sister sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister june" id="link3">Tillie</a>;
            <a href="http://example.com/till" class="sister" id="link4">Till</a>;
            <a href="http://example.com/noner" class="sister" data-foo="monks">Noner</a>;
            <b href="http://example.com/nonerb" class="sister" data-foo="monks">Noner</b>;
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#find matches "sister sis*" for class, and ie for href
print(soup.find_all(class_=re.compile("sister sis")))
print(soup.find_all(href=re.compile("ie")))

#only tag a
print(soup.find_all('a', {"data-foo": "monks"}))

#any tags
print(soup.find_all(attrs={"data-foo": "monks"}))

#get a tag with text string of Lacie
print(soup.find_all('a', string="Noner"))

#get sibling(s)
print(soup.find('a', string='Tillie').find_next_sibling())
print(soup.find('a', string='Tillie').find_previous_sibling())
print(soup.find('a', string='Tillie').find_previous_siblings())
