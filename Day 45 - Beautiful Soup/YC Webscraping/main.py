from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles= soup.find_all(name="span", class_="titleline")

# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.find(name="a").get("href")
#     article_links.append(link)


#using list comprehension
article_texts = [text.getText() for text in articles]
article_links = [link.find(name="a").get("href") for link in articles]
article_upvotes =[int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)


for i in range(len(article_upvotes)):
    if article_upvotes[i] == max(article_upvotes):
        print(article_texts[i])
        print(article_links[i])

#another method
# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)
#
# print(article_texts[largest_index])
# print(article_links[largest_index])





















# with open(file="website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.title.string)
# # print(soup.li)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
#
# # company_url = soup.select_one(selector="#name")
# # print(company_url)
#
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# headings = soup.select(".heading")
# print(headings)