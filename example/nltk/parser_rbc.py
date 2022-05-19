import json
import requests
import datetime
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def collect_news():
    current_time = datetime.datetime.now()
    actual_article_time = datetime.datetime(day=current_time.day - 5, month=current_time.month, year=current_time.year)

    ua = UserAgent()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": ua.random
    }
    parsed = []
    response = requests.get(url=f"https://www.rbc.ru/tags/?tag=IT&dateFrom={actual_article_time.strftime('%d.%m.%Y')}&dateTo={current_time.strftime('%d.%m.%Y')}", headers=headers).text
    time.sleep(2)
    soup = BeautifulSoup(response, "lxml")
    article_list = soup.find("div", class_="l-row g-overflow js-search_form-container").find_all("div", class_="search_form-item__wrap l-col-center")

    if parsed == []:
        parsed.append("За последние два дня новостей не публиковалось!")

    for article in article_list:
        print(f'parsed {article_list.index(article)+1} of {len(article_list)}')
        dict_ = {}
        dict_["src_url"] = article.find("a").get("href")
        dict_["title"] = article.find("span", class_="search_form-item__title").text
        date_time = article.find("span", class_="search_form-item__category").text
        date_time = date_time.split(",")
        dict_["date_time"] = date_time[-2].strip() + " " + date_time[-1].strip()
        try:
            dict_["img"] = article.find("span", class_="search_form-item__image-block").find("img").get("src")
        except:
            print("No image")
        try:
            dict_["description"] = article.find("span", class_="search_form-item__text").text.strip()
        except:
            print("No description")

        print(dict_)
        parsed.append(dict_)
        time.sleep(1)

    with open(f"main_rbc_{current_time.strftime('%Y-%m-%d')}.json", "w") as file:
        json.dump(parsed, file, indent=4, ensure_ascii=False)


def main():
    collect_news()


if __name__ == "__main__":
    main()