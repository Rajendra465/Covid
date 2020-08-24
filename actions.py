# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa.nlu.config import RasaNLUModelConfig
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionRespondCoroanStateCity(Action):
     def name(self):
      return "action_corona_state"

     def run(self, dispatcher, tracker, domain):
      # last_message = tracker.latest_message.get("text", "")


      def api_call(country_name):
          url = "https://covid-19-tracking.p.rapidapi.com/v1/" + country_name
          #print(url)

          headers = {'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com",
                     'x-rapidapi-key': "f2eed9bfd0msh2e7b8e60c2912d1p126f44jsn176f4a33b42d"}

          response = requests.request("GET", url, headers=headers)
          responsee = json.loads(response.text)
          return(responsee)
     

      entities = tracker.latest_message['entities']
      print("Last Message Now ", entities)
      state = None
      for e in entities:
            if e['entity'] == "state":
                state = e['value']
      
     

      print("State ", state.title())   
      message = "Please say correct Country name"
      if(state != None):
          message = "Please say correct Country name"
          data = api_call(state.title())
          print(data)
          message = "Active: "+data["Active Cases_text"] +" Confirmed: " + data["Total Cases_text"] +" Recovered: " + data["Total Recovered_text"] + "Death: " + data["Total Deaths_text"] + " On "+data["Last Update"]

      dispatcher.utter_message(message)

      return []
