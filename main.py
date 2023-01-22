import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import Publisher, Book, Shop, Stock, Sale

Base = declarative_base()

DSN = "postgresql://postgres:794722001@localhost:5432/bd-homework-6"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()


def searching_publisher_id():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите идентификатор (id) издателя: ')
    query_result = query_join.filter(Publisher.id_publisher == query_publisher_name)
    for result in query_result.all():
         for book_title, shop_name, sale_price, sale_date in session.query(Book.book_title, Shop.shop_name, Sale.sale_price, Sale.sale_date).select_from(Sale).join(Stock).join(Book).join(Shop).filter(Book.id_publisher == query_publisher_name): print(f'{book_title} | {shop_name} | {sale_price} | {sale_date}')


if __name__ == '__main__':
    searching_publisher_id()

session.close()
