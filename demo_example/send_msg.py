import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("EAAe9dZAtdgPEBAAlutbfLKE4ZCdfuVaeygZAn0TjjjP2u4b1wiS7RYhTdeZCEGniQ0puaQol2b1ZC8aDCt19lL6gvu26Hk1hS17mrXwMymDNxgMtScaC69pz39lQPAOkKFJ5nLYtZAZCJFzsbH5J5A3wBqZBo0vdIkaSWKdosPwCKy8G04WZAldFO")


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text
