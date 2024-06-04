from bs4 import BeautifulSoup
import requests

response = requests.get("https://myanimelist.net/topmanga.php")
top100_manga = response.text
soup = BeautifulSoup(top100_manga, "html.parser")

ranking_rows = soup.find_all('tr', class_='ranking-list')
for row in ranking_rows:
    # Find the rank
    ranked = ''
    rank_td = row.find('td', class_='rank ac')

    if rank_td:
        rank_span = rank_td.find('span', class_=f'lightLink top-anime-rank-text rank{x}')
        if rank_span:
            placement = rank_span.text.strip()
            ranked = placement

    # Find the title
    the_title = ''
    title_td = row.find('td', class_='title al va-t clearfix word-break')
    if title_td:
        title_link = title_td.find('div', class_="detail")
        title_header = title_link.find('h3',class_='manga_h3')
        title = title_header.find('a', class_='hoverinfo_trigger fs14 fw-b')
        if title:
            manga_title = title.text.strip()
            the_title = manga_title
    print(f"Rank: {ranked} Title: {the_title}")
