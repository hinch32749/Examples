import json
import requests
import datetime
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


current_time = datetime.datetime.now().strftime("%Y-%m-%d")


def collect_news():

    ua = UserAgent()
    # Заголовки для запроса
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": ua.random
    }

    response = requests.get(url="https://3dnews.ru/software", headers=headers).text

    soup = BeautifulSoup(response, "lxml")

    article_list = soup.find("div", class_="content-block-data white sub-section-list").find_all("li")

    parsed = []
    for article in article_list:
        print(f"parsed {article_list.index(article)+1} of {len(article_list)}")

        dict_ = {}
        src_url = article.find("a").get("href")
        dict_["source_url"] = "https://3dnews.ru" + src_url
        dict_["title"] = article.find("a").text.strip()
        dict_["date_time"] = article.find("span", class_="strong").text. strip()

        parsed.append(dict_)

    with open(f"main_3dnews_{current_time}.json", "w") as file:
        json.dump(parsed, file, indent=4, ensure_ascii=False)


def important_news():

    ua = UserAgent()
    # Заголовки для запроса
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": ua.random
    }

    response = requests.get(url="https://3dnews.ru/software", headers=headers).text
    time.sleep(2)
    soup = BeautifulSoup(response, "lxml")

    article_list = soup.find("div", class_="content-block margin-top margin-bottom").\
        find_all("div", class_="content-block-data white")

    parsed = []
    for article in article_list:
        print(f"parsed {article_list.index(article)+1} of {len(article_list)}")
        dict_ = {}
        src_url = article.find("a", class_="icon").get("href")
        dict_["source_url"] = 'https://3dnews.ru' + src_url
        dict_["title"] = article.find("a", class_="icon").get("title").strip()
        dict_["description"] = article.find("div", class_="teaser _ga1_on_").text.replace('\n', '').replace('\t', '')
        img = article.find("a", class_="icon").get("style").split(" ")
        dict_["image"] = "https://3dnews.ru" + img[1][4:-2]
        parsed.append(dict_)
        print(dict_)

    with open(f"main_important_3dnews_{current_time}.json", "w") as file:
        json.dump(parsed, file, indent=4, ensure_ascii=False)


def main():
    collect_news()
    # important_news()


if __name__ == "__main__":
    main()