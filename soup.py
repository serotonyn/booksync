import nltk
import re

nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
from bs4 import BeautifulSoup

with open("charlie/ch3/index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

after = open('charlie/ch3/after.html', "w")
EndPunctuation = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!|,|–)\s')
count = 0

pertinents = soup.findAll("p", {"class": re.compile("^(normal|bodytext)$")})

for bodytext in pertinents:
    text = bodytext.get_text()
    tokens = tokenizer.tokenize(text)
    bodytext.clear()
    for token in tokens:
      for bit in EndPunctuation.split(token):
        print(count)
        new_tag = soup.new_tag("span", id=f'span{count}', **{'class':'span_'})
        new_tag.append(f'{bit} ')
        bodytext.append(new_tag)
        count = count + 1

after.write(str(soup))

