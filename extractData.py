from bs4 import BeautifulSoup

def match_class(target):
    target = target.split()
    def do_match(tag):
        try:
            classes = dict(tag.attrs)["class"]
        except KeyError:
            classes = ""
        return all(c in classes for c in target)
    return do_match

soup = BeautifulSoup (open("temp.html"))
links = soup.findAll(match_class("Dark"))

outputfile=file("output.txt", "w+")

for link in links: 
	outputfile.write(link.text.encode('utf-8'))






