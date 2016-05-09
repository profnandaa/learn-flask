import sys
from models import Base, engine


if sys.argv[1] == 'migrate':
	Base.metadata.create_all(engine)
	print "Tables created successfully"