import wikipediaapi
import wikipedia
query = 'Islander (Agave) plant'
page_name = wikipedia.search(query,1)

wiki = wikipediaapi.Wikipedia('plant-character-classification 1.0', language='en', extract_format=wikipediaapi.ExtractFormat.HTML)
print(wiki.page(page_name[0]).fullurl)