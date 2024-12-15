# import requests
# import bs4      # <= beautifulsoup

import requests
import bs4  # BeautifulSoup

url = "https://fr.wikipedia.org/wiki/Romanthony"
response = requests.get(url)
source = response.text

# Parser le contenu HTML avec BeautifulSoup
html = bs4.BeautifulSoup(source, 'html.parser')

# Rechercher toutes les balises de titre (h1, h2, h3, h4, etc.)
titles = html.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

# Afficher les titres avec une tabulation en fonction du niveau
for title in titles:
    level = int(title.name[1])  # Extraire le niveau de la balise (ex. h2 -> 2)
    indentation = "\t" * (level - 1)  # Ajouter une tabulation par niveau
    print(f"{indentation}{title.text}")








