from flask import Flask, request, json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def sum_num(num1, num2):
    return num1 + num2


def subtract_num(num1, num2):
    return num1 - num2


@app.route('/chatbot', methods=['POST'])
def chatbot():


    req = request.get_json(silent=True, force=True)

    print(json.dumps(req, indent=4))

    # dissect the incoming message
    try:
        # if action is 'add_numbers' do addition
        if (req['result']['action'] == 'add_numbers'):
            # grab two numbers from dialogflow parameters
            num1 = int(req['result']['parameters']['num1'])
            num2 = int(req['result']['parameters']['num2'])
            # use sum_num() function to find sum of  numbers
            return "The sum of {} and  {} is {}".format(num1, num2, sum_num(num1, num2))
        else:
            return req['result']['fulfillment']['speech']
    except:
        return "Oops had an error, try again"



if __name__ == '__main__':
    app.run()
