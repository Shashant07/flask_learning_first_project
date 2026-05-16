from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/something', methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return 'get request'
    elif request.method == 'POST':
        return 'post request'
    else: 
        return "hello this is something page"

# route with parameters
@app.route('/greet/<name>')
def greet(name):
    response = make_response('Hello world\n')
    response.status_code = 202
    response.headers['content-type'] = 'text/plain'
    return response

@app.route('/add/<int:no1>/<int:no2>')
# http://127.0.0.1:5000/add/10/20
def add(no1, no2):
    return f'{no1}+{no2}={no1+no2}'

# Handle url params
@app.route("/handle_url_params")
def handle_params():
    # return str(request.args)
    # http://127.0.0.1:5000/handle_url_params?name=shashant&greeting=hello
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}'
    else: 
        return 'Some parameters are missing'





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)