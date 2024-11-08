#Google BC
import requests

def search(query, pageNum):
    num = 0
    
    URL = "https://rapidapi.p.rapidapi.com/api/Search/WebSearchAPI"
    HEADERS = {
        'x-rapidapi-host': "contextualwebsearch-websearch-v1.p.rapidapi.com",
        'x-rapidapi-key': "1a4a00acfamshaa568dd02d6fc4dp14bd0cjsnfb1b83f87741"
    }

    query = query
    page_number = pageNum
    page_size = 10
    auto_correct = False
    safe_search = True

    querystring = {"q": query,
                   "pageNumber": page_number,
                   "pageSize": page_size,
                   "autoCorrect": auto_correct,
                   "safeSearch": safe_search}
    response = requests.get(URL, headers=HEADERS, params=querystring).json()

    total_count = response["totalCount"]

    for web_page in response["value"]:
        num += 1

        url = web_page["url"]
        title = web_page["title"]
        description = web_page["description"]
        body = web_page["body"]
        date_published = web_page["datePublished"]
        language = web_page["language"]
        is_safe = web_page["isSafe"]
        provider = web_page["provider"]["name"]

        print(str(num)+") Url: {}. Title: {}.".format(url, title))

def main():
    pageNum = 1
    query = input("What do you want to search for? ")
    print()
    thisSearch = search(query, pageNum)
    print()
    nextPage = input("Do you wish to view the next page (Y/N): ")
    print()
    if nextPage == "Y":
        nextPage = True
    else:
        nextPage = False
    while nextPage:
        pageNum += 1
        thisSearch = search(query, pageNum)
        print()
        nextPage = input("Do you wish to view the next page (Y/N): ")
        print()
        if nextPage == "Y":
            nextPage = True
        else:
            nextPage = False

if __name__ == "__main__":
    main()
