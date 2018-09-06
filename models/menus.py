from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="sid_1590@yahoo.in")
session.add(User1)
session.commit()

# The Dosa street
restaurant1 = Restaurant(name="The Dosa Street", user_id="1")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Sweet Corn Dosa",
                     description="Sweet corn fill crepe made from rice"
                     "batter.",
                     price="$2.99", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Mushroom Paneer Schezwan Dosa",
                     description="Crepe made from rice"
                     "batter, topped with sliced and stir fired mushroom and paneer.",
                     price="$7.50",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="Sada Dosa",
                     description="Crepe made from rice"
                     "batter.",
                     price="$5.50", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()


# Donne's Biryani Pot
restaurant2 = Restaurant(name="Biryani Pot")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Donne Chicken Biryani",
                     description="Rice dish layered with steamed chicken cooked slowly with pepper.",
                     price="$7.99", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Kshtriya kabab Biryani",
                     description="Rice dish"
                     "layered with chicked kabab, vegetables and mango pickle.",
                     price="$25",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Rayala Biryani",
                     description="Rice dish with veggies and chutney"
                     "made with Sorrel leaves.",
                     price="$15", restaurant=restaurant2)

session.add(menuItem3)
session.commit()


print "Added menu items!"
