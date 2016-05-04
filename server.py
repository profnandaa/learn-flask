import random
from app.views import app


if __name__ == '__main__':
    # you can ignore the following and just have one line
    # app.run(debug=True, port=5050)
    app.debug = True
    try:
        app.run(port=8004)
    except:
        # if port in use, pick random port 
        app.run(port=random.randint(6000, 8000))

