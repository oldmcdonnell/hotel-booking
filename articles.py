import pandas as pd
import pyarrow

df = pd.read_csv("articles.csv", dtype={"id":str})

class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.id, 'price'].squeeze()


class Receipt:
    def __init__(self, article):
        self.article = article
        print(article)

    def generate(self):
        pass

#main look
print(df)
article_ID = input("Enter the id of the item to purchase : ")
article = Article(article_ID)