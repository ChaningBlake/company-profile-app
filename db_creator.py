# db_creator.py

from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///profiledata.db', echo=True)
Base = declarative_base()
 
class Company(Base):
	__tablename__ = "companies"

	id = Column(Integer, primary_key=True)
	name = Column(String)
	upnew = Column(Integer)
	offerprice = Column(Integer)

	def __init__(self):
		pass
	
	def __repr__(self):
		return "<Company: {}>".format(self.name)
 
# create tables
Base.metadata.create_all(engine)
