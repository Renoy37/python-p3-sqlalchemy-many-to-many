#!/usr/bin/env python3

from sqlalchemy import create_engine, delete
from sqlalchemy.orm import sessionmaker

from models import Game, Review, User, game_user

if __name__ == '__main__':

    engine = create_engine('sqlite:///many_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # delete(game_user).where(game_user.c.id > 1)
    # newgame = Game(title='Doomer', genre="Good genre", platform="PC", price=3000)
    # session.add(newgame)
    # newuser = User(name='John Doe')
    # session.add(newuser)
    # newgame.users.append(newuser)
    # session.query(MyClass).filter_by(name = 'some name')
    # session.commit()

    gamerecord = session.query(Game).filter_by(title='Doomer').first()
    gameuser = session.get(User, 4)
    gamerecord.users.append(gameuser)
    session.commit()
    # firstgame = session.get(Game,1)
    # print(gamerecord)

    print()

    import ipdb
    ipdb.set_trace()
