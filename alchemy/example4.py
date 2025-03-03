from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# PostgreSQL Database Connection String
#                                     username password             db-name
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/postgres"

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Base class
# 1.5 BLACK=BOX
Base = declarative_base()

# Define a User model
class User2(Base):
    __tablename__ = "users2"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

# Create table
# 2 BLACK=BOX
Base.metadata.create_all(engine)

# Create a session
# 3 BLACK=BOX
Session = sessionmaker(bind=engine)
session = Session()

# Insert a user
new_user = User2(name="Danny", age=25)
session.add(new_user)
session.commit()

# Select all users
users = session.query(User2).all()
for user in users:
    print(user.id, user.name, user.age)

# users -- fix

# data frame + alchemy
# query = session.query(User)
# df_orm = pd.DataFrame([(u.id, u.name, u.age) for u in query], columns=["id", "name", "age"])
# df_from_db = pd.read_sql("SELECT * FROM users", con=engine)


# Update a user’s age
session.query(User2).filter_by(name="Danny").update({"age": 28})
session.commit()

# Delete a user
# session.query(User2).filter_by(name="Danny").delete()
# session.commit()

session.close()
