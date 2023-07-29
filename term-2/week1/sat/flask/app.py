from flask import Flask

app = Flask(__name__)

# CRUD accounts
# { "accounts": [
# ]
# }
# {
# "account": { name }
# }
# {"message": "Hello World"}

@app.route("/")
def hello_world():
    return {"message": "hello world"}


# list of accounts
@app.route("/accounts")
def list_of_accounts():
    return { "accounts": []}


@app.route('/accounts/<username>')
def show_accounts_with_username(username):
    return {
            "account": {
                "username": username
            }
        }


@app.route('/accounts/<int:id>')
def show_accounts_with_id(id):
    return {
            "account": {
                "id": id
            }
        }
