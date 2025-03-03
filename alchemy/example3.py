from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Define the database (SQLite)
engine = create_engine("sqlite:///example.db", echo=True)

# Base class
Base = declarative_base()

# Define a User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    orders = relationship("Order", back_populates="user", cascade="all, delete")

# Define Order model
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    item = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    user = relationship("User", back_populates="orders")

# **Ensure all tables are created AFTER defining all models**
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
# use this for cascade
# Insert a user with orders
new_user = User(name="Eve", age=28, orders=[
    Order(item="Laptop", price=1200),
    Order(item="Phone", price=800)
])
session.add(new_user)
session.commit()

# Select all orders for a specific user
eve_orders = session.query(Order).join(User).filter(User.name == "Eve").all()
print("Eve's Orders:")
for order in eve_orders:
    print(order.item, order.price)

# Update an order price
session.query(Order).filter(Order.item == "Laptop").update({"price": 1100})
session.commit()

# Delete a specific order
user = session.query(User).filter(User.id == 2).first()
session.delete(user)  # use this for cascade
session.commit()
