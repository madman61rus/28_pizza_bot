from models_json import catalog
from sqlalchemy import create_engine
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy.orm import scoped_session, sessionmaker
from models import Pizza, Choice, db

engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

if __name__ == '__main__':
    for pizza in catalog:
        new_pizza = Pizza()
        new_pizza.title = pizza.get('title')
        new_pizza.description = pizza.get('description')

        for choice in pizza.get('choices'):
            new_choice = Choice()
            new_choice.title = choice.get('title')
            new_choice.price = choice.get('price')
            new_pizza.choices.append(new_choice)

        db_session.add(new_pizza)
        db_session.commit()



