from flask import Flask, request, session, redirect, make_response


app = Flask(__name__)
app.secret_key = b'rN8e8"_"">*{'


@app.route('/echo', methods=['GET'])
def echo():
    if request.method == 'GET':
        if request.args.get('message'):
            return request.args.get('message'), 200
        else:
            return 'NOT ACCEPTABLE', 406
    else:
        return 'METHOD NOT ALLOWED', 405


@app.route('/set_banner', methods=['POST'])
def admin():
    if request.method == 'POST':
        if request.headers.get('admin-auth') in session:
            return redirect('127.0.0.1:8080/echo')
        else:
            if request.form.get('banner') and request.headers.get('admin-auth') == '1234':
                session['admin-auth'] = request.headers.get('admin-auth')
                response = make_response(redirect('127.0.0.1:8080/echo'), 200)
                response.headers['banner'] = request.form.get('banner')
                return response
            else:
                return 'FORBIDDEN', 403
    else:
        return 'METHOD NOT ALLOWED', 405


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
