from bs4 import BeautifulSoup
import re
html_doc = """
            <a href="http://example.com/elsie" class="sister sisteen" id="link1">Elsie</a>,
            <a href="http://example.com/lacie" class="sister sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister june" id="link3">Tillie</a>;
            <a href="http://example.com/till" class="sister" id="link4">Till</a>;
            <a href="http://example.com/noner" class="sister" >Noner</a>;
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#find matches "sister sis*"
print(soup.find_all(class_=re.compile("sister sis")))
print(soup.find_all(href=re.compile("ie")))
