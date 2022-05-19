import json
import requests
import datetime
import time
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def collect_news():
    current_time = datetime.datetime.now()
    ua = UserAgent()
    # Заголовки для запроса
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": ua.random
    }
    parsed = []
    for number_page in range(1, 10):
        actual = True
        response = requests.get(url=f"https://habr.com/ru/news/page{number_page}/", headers=headers).text
        time.sleep(2)
        print(f"<===================== page {number_page} =====================>")
        soup = BeautifulSoup(response, "lxml")
        article_list = soup.find("div", class_="tm-articles-list").find_all("div", class_="tm-article-snippet")

        for article in article_list:
            print(f'parsed {article_list.index(article)+1} of {len(article_list)} from {number_page} page')
            dict_ = {}
            source = article.find("h2", class_="tm-article-snippet__title tm-article-snippet__title_h2")
            dict_["src_url"] = "https://habr.com" + source.find("a").get("href")
            dict_["title"] = source.text
            date_time = article.find("time").get("title")
            dict_["date_time"] = date_time
            try:
                dict_["img"] = article.find("div", class_="tm-article-body tm-article-snippet__lead").find("img").get("src")
            except:
                print("No image")
            try:
                dict_["description"] = article.find("div", class_="tm-article-body tm-article-snippet__lead").text.strip()
            except:
                print("No description")
            parsed.append(dict_)
            time.sleep(1)
            # Условие проверки новости не старше двух суток.
            date_time = date_time.split(",")
            date_ = date_time[0].strip().split("-")
            time_ = date_time[1].strip().split(":")
            year, month, day, hour, minutes = int(date_[0]), int(date_[1]), int(date_[2]), int(time_[0]), int(time_[1])
            t = datetime.datetime(year, month, day, hour, minutes)
            delta = current_time - t
            if delta.days >= 1:
                actual = False
                break

        if actual == False:
            break

    with open(f"main_new_habr_{current_time.strftime('%Y-%m-%d')}.json", "w") as file:
        json.dump(parsed, file, indent=4, ensure_ascii=False)


def main():
    collect_news()


if __name__ == "__main__":
    main()