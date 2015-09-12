import flask
from pyspark  import SparkContext
from operator import itemgetter

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return 'Example: /dt/140'

@app.route('/dt/<int:delaythreshold>')
def dt(delaythreshold):
    global flights_rdd

    flights_dict =                                              \
        flights_rdd                                             \
        .filter( lambda (day, delay): delay >= delaythreshold ) \
        .keys()                                                 \
        .countByValue()
    sorted_flight_tuples = \
        sorted( flights_dict.items(), key=itemgetter(1), reverse=True )

    return flask.render_template('delays.html', tuples=sorted_flight_tuples[:5])

if __name__ == '__main__':
    global flights_rdd

    sc = SparkContext()
    flights_rdd =                                   \
        sc.textFile('/tmp/flights.csv', 4)          \
          .map( lambda s: s.split(',') )            \
          .map( lambda l: ( l[0][:4], int(l[1]) ) ) \
          .cache()

    app.config['DEBUG'] = True
    app.run(host='0.0.0.0')

