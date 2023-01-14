import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('compiler.xml')
root = tree.getroot()

data = []

for book in root.findall('book'):
    book_id = book.get('id')
    author_name = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    price = float(book.find('price').text)
    publish_date = book.find('publish_date').text
    description = book.find('description').text
    data.append([book_id, author_name, title, genre, price, publish_date, description])
    print("\n")
    print(book_id)
    print(author_name)
    print(title)
    print(genre)
    print(price)
    print(publish_date)
    print(description)
df = pd.DataFrame(data, columns=['Book_id', 'Author_Name', 'Title', 'Genre', 'Price', 'Publish_date', 'Description'])
df.to_excel('books_data.xlsx', index=False)


