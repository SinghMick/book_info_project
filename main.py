import requests

def get_book_info(isbn):
    url = f"https:/pythog/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
    response = requests.get(url)
    if response.status_code == 200:
        book_data = response.json()
        if f"ISBN:{isbn}" in book_data:
            book_info = book_data[f"ISBN:{isbn}"]
            title = book_info.get("title", "No title available")
            authors = [author['name'] for author in book_info.get("authors", [])]
            publish_date = book_info.get("publish_date", "No publish date available")
            number_of_pages = book_info.get("number_of_pages", "No page count available")

            print(f"Title: {title}")
            print(f"Authors: {', '.join(authors)}")
            print(f"Publish Date: {publish_date}")
            print(f"Number of Pages: {number_of_pages}")
        else:
            print("Book not found!")
    else:
        print("Failed to fetch data from the API")

if __name__ == "__main__":
    isbn = input("Enter the ISBN number of the book: ")
    get_book_info(isbn)
