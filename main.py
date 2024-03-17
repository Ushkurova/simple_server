import json

from flask import Flask, request, Response

app = Flask(__name__)

status={
    'attempts': 0,
    'success': 0,
}

@app.route('/')
def hello():
    return f'hello user, status = {status}'


@app.route('/auth', methods = ['POST'])
def auth():
    status['attempts'] += 1
    data = request.json
    login = data['login']

    password = data['password']
    print(login, password)

    with open ('users.json') as u_f:
        users = json.load(u_f)

    if login in users and users[login] == password:
        status_code = 200
        status['success'] +=1
    else:
        status_code = 401

    return Response(status=status_code)

if __name__ == '__main__':
    app.run(port=5001)