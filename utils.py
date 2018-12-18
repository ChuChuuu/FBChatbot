import requests
import os

GRAPH_URL = "https://graph.facebook.com/v2.6"
#ACCESS_TOKEN = "EAAe9dZAtdgPEBAMDyQjWQBjZCKnCb9ezn6365TW1yb22ZAR1UnZBxQj36FxdRV0Mye2eTGpSlVHQceSVlCZAz0ve1w6BiTr7wGc9VjtZBNuz9G4cTO2QvbZAIqZA9N0Bs8BjNwWS2uEEWk4ndXbbRjz05ZBojs3uG7ElRQoK3ZCm4E03UqKWwxZABhJ"
ACCESS_TOKEN=os.environ['ACCESS_TOKEN']

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_page_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
		"message":{
			 "attachment":{
				 "type":"template",
				 "payload":{
			     "template_type":"button",
			     "text": text,
				 "buttons":[
					{
						"type":"web_url",
					    "url":"https://www.facebook.com/鴨肉飯-566835160428523/?modal=admin_todo_tour",
						"title":"點我去粉專"
					},
				 ]
				}
			 }
		 },
#        "sender_action":"typing_on"
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def send_two_template(id, text,button1,button2):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
		"message":{
			 "attachment":{
				 "type":"template",
				 "payload":{
			     "template_type":"button",
			     "text": text,
				 "buttons":[
					{
						"type":"postback",
						"title": button1,
						"payload":"<DEVELOPER_DEFINED_PAYLOAD>"
					},
					{
						"type":"postback",
						"title": button2,
						"payload":"<DEVELOPER_DEFINED_PAYLOAD>"
					},

				 ]
				}
			 }
		 }		
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


def send_three_template(id, text,button1,button2,button3):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
		"message":{
			 "attachment":{
				 "type":"template",
				 "payload":{
			     "template_type":"button",
			     "text": text,
				 "buttons":[
					{
						"type":"postback",
						"title": button1,
						"payload":"<DEVELOPER_DEFINED_PAYLOAD>"
					},
					{
						"type":"postback",
						"title": button2,
						"payload":"<DEVELOPER_DEFINED_PAYLOAD>"
					},
                    {                                                           
                        "type":"postback",
                        "title": button3,
                        "payload":"<DEVELOPER_DEFINED_PAYLOAD>"
                    }

				 ]
				}
			 }
		 }		
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response

def greeting_message():
    url = "{0}/me/messenger_profile?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
		"greeting": [
			{
			  "locale":"default",
			  "text":"我是一碗鴨肉飯，擺在你桌上那一碗" 
			}
#, {
#			  "locale":"en_US",
#"text":"我是一碗鴨肉飯，擺在你桌上那碗"
#			  "text":"asdasd"
#			}
		  ],
		"get_started":{
			 "payload":"<GET_STARTED_PAYLOAD>"
		 }
	}
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
