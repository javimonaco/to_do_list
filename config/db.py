from email.policy import default
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from pathlib import Path
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import relationship # Genera una relacion entre tablas

BASE_DIR=str(Path(__file__).parent.absolute())

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR + '/todolist.sqlite'

# Clase base de la cual heredan los modelos
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, future=True) #Crea la Base de Datos

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    firstname = Column(String(255))
    lastname = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    deleted = Column(Boolean, default=False)
    thisUser = relationship("Task", back_populates="myuserid", cascade="all, delete-orphan")

    def __init__(self, name, firstname, lastname, email, password, deleted):
        self.name = name
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.deleted = deleted

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String(255), primary_key=True)
    id_user = Column(String(255), ForeignKey("users.id"))
    title = Column(String(255))
    summary = Column(String(255))
    dateIni = Column(DateTime)
    dateEnd = Column(DateTime)
    completed = Column(Boolean)
    deleted = Column(Boolean)
    myuserid = relationship("User", back_populates="thisUser", cascade="all, delete-orphan")

    def __init__(self, id_user, title, summary, dateIni, dateEnd, completed, deleted):
        self.id_user = id_user
        self.title = title
        self.summary = summary
        self.dateIni = dateIni
        self.dateEnd = dateEnd
        self.completed = completed
        self.deleted = deleted

# Crea las tablas Definidas
Base.metadata.create_all(engine)