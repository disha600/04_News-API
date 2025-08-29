import requests

query=input("What are you interested in today?")
api="38bb50244fd44f05b7e2f3ade7bf5c22"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-07-29&sortBy=publishedAt&apiKey={api}"


r=requests.get(url)
data=r.json()

articles=data["articles"]

for ind,art in enumerate(articles):
    print(ind+1,art["title"])
    print(art["author"])
    print(art["url"])
    print("\n*********************************\n")





print(url)