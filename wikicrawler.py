import wikipedia
import sys


page = wikipedia.page(wikipedia.search(argv[-1])[0])
links = []

for link in page.links:
	links.append({"page":link, "summary": wikipedia.summary(link)})
	
for link in links:
	print("[{}] ({})").format(link["page"], link["summary"])