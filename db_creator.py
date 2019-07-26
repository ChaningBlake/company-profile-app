# db_creator.py

from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///profiledata.db', echo=True)
Base = declarative_base()
 
class Company(Base):
	__tablename__ = "companies"

	id = Column(Integer, primary_key=True)
	name = Column(String)
	upnew = Column(Float)
	offerprice = Column(Integer)
	auditor4 = Column(Integer)
	internet = Column(Integer)
	revisionnew = Column(Float)
	lnage1 = Column(Float)
	lnproceeds = Column(Float)
	vc = Column(Integer)
	lnsales = Column(Float)
	leverage = Column(Float)
	hot05 = Column(Integer)
	lntanew = Column(Float)


	def __init__(self, name, upnew, offerprice, auditor4,
	internet, revisionnew, lnage1, lnproceeds, vc, lnsales, leverage, hot05, lntanew):
		self.name = name
		self.upnew = upnew
		self.offerprice = offerprice
		self.auditor4 = auditor4
		self.internet = internet
		self.revisionnew = revisionnew
		self.lnage1 = lnage1
		self.lnproceeds = lnproceeds
		self.vc = vc
		self.lnsales = lnsales
		self.leverage = leverage
		self.hot05 = hot05
		self.lntanew = lnta
	
	def __repr__(self):
		return "<Company: {}>".format(self.name)
 
# create tables
Base.metadata.create_all(engine)
