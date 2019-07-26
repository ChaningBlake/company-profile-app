from main import db
	
class Company(db.Model):
	__tablename__ = "companies"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	upnew = db.Column(db.Float)
	offerprice = db.Column(db.Integer)
	auditor4 = db.Column(db.Integer)
	internet = db.Column(db.Integer)
	revisionnew = db.Column(db.Float)
	lnage1 = db.Column(db.Float)
	lnproceeds = db.Column(db.Float)
	vc = db.Column(db.Integer)
	lnsales = db.Column(db.Float)
	leverage = db.Column(db.Float)
	hot05 = db.Column(db.Integer)
	lntanew = db.Column(db.Float)


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
		self.lntanew = lntanew
	
	def __repr__(self):
		return "{}: {} {}".format(self.name, self.upnew, self.offerprice)
