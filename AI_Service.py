from flask import Flask
from Recommendation_System import *;
import json
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get_recommendation')
def getRecommendation():
    movie = request.args.get('movie')
    result = get_recommendations(movie)
    values = list(result.to_dict().values())
    return json.dumps(values)




if __name__ == '__main__':
    app.run()

