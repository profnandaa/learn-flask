import sys
from app.views import app


if __name__ == '__main__':
    # you can ignore the following and just have one line
    # app.run(debug=True, port=5050)
    app.debug = True
    if len(sys.argv) > 1 and int(sys.argv[1]) >= 5000:
    	port = int(sys.argv[1])
    	app.run(port=port)
    app.run(port=5000)

