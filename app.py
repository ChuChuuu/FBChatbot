from bottle import route, run, request, abort, static_file

from fsm import TocMachine
from utils import greeting_message
import os
#VERIFY_TOKEN = "1234567890987654321"
VERIFY_TOKEN=os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']
machine = TocMachine(
    states=[
        'user',
        'state1',
        'about',
        'startmsg',
        'page',
        'eating',
        'eating2',
        'meal',
        'meallist',
        'addmeallist',
        'delmeallist',
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1',
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'about',
            'conditions': 'is_going_to_about'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'about',
                'startmsg',
				'page',
                'eating2',
#				'meallist',
            ],
            'dest': 'user'
        },
        {
            'trigger': 'advance',
            'source' : 'user',
            'dest'   : 'startmsg',
            'conditions': 'is_going_to_startmsg'
        },
        {
            'trigger': 'advance',
            'source' : 'user',
            'dest'   : 'page',
            'conditions': 'is_going_to_page'
        },
        {
            'trigger': 'advance',
            'source' : 'user',
            'dest'   : 'user',
            'unless': ['is_going_to_page','is_going_to_about','is_going_to_state1','is_going_to_eating','is_going_to_meal'],
            'after' : 'user_misunderstand'
        },
        {
            'trigger': 'advance',
            'source' : 'user',
            'dest'   : 'eating',
            'conditions': 'is_going_to_eating'
        },
        {
            'trigger': 'advance',
            'source' : 'eating',
            'dest'   : 'user',
			'conditions':'noeating',
        },
	
        {
            'trigger': 'advance',
            'source' : 'eating',
            'dest'   : 'eating2',
            'conditions': 'is_going_to_eating2'
        },
        {
            'trigger': 'advance',
            'source' : 'user',
            'dest'   : 'meal',
            'conditions': 'is_going_to_meal'
        },
        {
            'trigger': 'advance',
            'source' : 'meal',
            'dest'   : 'user',
            'conditions': 'nowantmeal'
        },
        {
            'trigger': 'advance',
            'source' : 'meal',
            'dest'   : 'meallist',
            'conditions': 'is_going_to_meallist'
        },
        {
            'trigger': 'advance',
            'source' : 'meallist',
            'dest'   : 'user',
            'conditions': 'listthatok'
        },
        {
            'trigger': 'advance',
            'source' : 'meallist',
            'dest'   : 'addmeallist',
            'conditions': 'is_going_to_addmeallist'
        },
        {
            'trigger': 'advance',
            'source' : 'addmeallist',
            'dest'   : 'meallist',
            'conditions': 'addafood'
        },
        {
            'trigger': 'advance',
            'source' : 'meallist',
            'dest'   : 'delmeallist',
            'conditions': 'is_going_to_delmeallist'
        },
        {
            'trigger': 'advance',
            'source' : 'delmeallist',
            'dest'   : 'meallist',
            'conditions': 'delafood'
        },



    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        if 'message' in event:
            if 'attachments' in event['message']:
                return 'OK'        
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')

#greeting_message()

if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)
