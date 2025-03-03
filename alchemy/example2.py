from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

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

# Create table
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert multiple users
session.add_all([
    User(name="Bob", age=30),
    User(name="Charlie", age=35),
    User(name="David", age=40)
])
session.commit()

# Select users older than 30
older_users = session.query(User).filter(User.age > 30).all()
print("Users older than 30:")
for user in older_users:
    print(user.name, user.age)

# Select a specific user by name
charlie = session.query(User).filter(User.name == "Charlie").first()
print("Found user:", charlie.name, charlie.age)

# Update user's name
session.query(User).filter(User.name == "Bob").update({"name": "Robert"})
session.commit()

# Delete users older than 35
session.query(User).filter(User.age > 35).delete()
session.commit()
