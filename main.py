from bs4 import BeautifulSoup
import requests

response = requests.get("https://myanimelist.net/topmanga.php")
top100_manga = response.text
soup = BeautifulSoup(top100_manga, "html.parser")

ranking_rows = soup.find_all('tr', class_='ranking-list')
hardcoded_rank = 0
mangas = []
users_favorite_manga = input("Here are the top 50 manga titles on mal. Type in your favorite manga to check if it in there.")


for row in ranking_rows:
    # Find the rank
    ranked = ''
    rank_td = row.find('td', class_='rank ac')
    hardcoded_rank += 1
    if rank_td:
        rank_span = rank_td.find('span', class_=f'lightLink top-anime-rank-text rank')
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
            mangas.append(the_title)
    print(f"Rank: {hardcoded_rank} Title: {the_title}")

if users_favorite_manga in mangas:
    user_rank = mangas.index(users_favorite_manga) + 1
    print(f"Your favorite manga {users_favorite_manga} is in the current top 50 at {user_rank}!")
