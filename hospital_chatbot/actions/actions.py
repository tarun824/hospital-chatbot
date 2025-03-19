# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


all_medicine=[
  {
    "index": 1,
    "medicine_name": "Paracetamol",
    "details": "A common pain reliever and fever reducer.",
    "no_of_quantity": 200,
    "price": 10.50 
  },
  {
    "index": 2,
    "medicine_name": "Ibuprofen",
    "details": "Nonsteroidal anti-inflammatory drug (NSAID) used to reduce fever, pain, and inflammation.",
    "no_of_quantity": 150,
    "price": 15.00
  },
  {
    "index": 3,
    "medicine_name": "Amoxicillin",
    "details": "An antibiotic used to treat a variety of bacterial infections.",
    "no_of_quantity": 75,
    "price": 20.00
  },
  {
    "index": 4,
    "medicine_name": "Metformin",
    "details": "A medication used to treat type 2 diabetes by improving blood sugar control.",
    "no_of_quantity": 100,
    "price": 25.00
  },
  {
    "index": 5,
    "medicine_name": "Lisinopril",
    "details": "An ACE inhibitor used to treat high blood pressure and heart failure.",
    "no_of_quantity": 50,
    "price": 30.00
  },
  {
    "index": 6,
    "medicine_name": "Atorvastatin",
    "details": "A statin medication used to lower cholesterol and reduce the risk of heart disease.",
    "no_of_quantity": 120,
    "price": 35.00
  },
  {
    "index": 7,
    "medicine_name": "Omeprazole",
    "details": "A proton pump inhibitor that decreases stomach acid production, used to treat GERD.",
    "no_of_quantity": 80,
    "price": 18.00
  },
  {
    "index": 8,
    "medicine_name": "Levothyroxine",
    "details": "A synthetic form of the thyroid hormone used to treat hypothyroidism.",
    "no_of_quantity": 60,
    "price": 22.00
  },
  {
    "index": 9,
    "medicine_name": "Sertraline",
    "details": "An antidepressant of the selective serotonin reuptake inhibitor (SSRI) class.",
    "no_of_quantity": 90,
    "price": 28.00
  },
  {
    "index": 10,
    "medicine_name": "Amlodipine",
    "details": "A calcium channel blocker used to treat high blood pressure and angina.",
    "no_of_quantity": 110,
    "price": 27.50
  }
]

all_lab_tests = [
    {
        "id": "test_001",
        "name": "Blood Test",
        "cost": 75
    },
    {
        "id": "test_002",
        "name": "Urine Tests",
        "cost": 50
    },
    {
        "id": "test_003",
        "name": "X-ray",
        "cost": 200
    },
    {
        "id": "test_004",
        "name": "CT Scan",
        "cost": 1200
    }
]

# Medicine
class ActionMedicineEnquiry(Action):
    def name(self) -> Text:
        return "action_medicine_enquiry"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            medicine_name=next(tracker.get_latest_entity_values("medicine_name"),None)
        
            if not medicine_name:
                dispatcher.utter_message(text="Entered Medicine not found")
                return []

            medicine=None
            for medi in all_medicine:
                if medicine_name.lower() in medi["medicine_name"].lower():
                    medicine=medi
                    break
            if medicine:
                msg=""
                if medicine["no_of_quantity"]>1:
                    msg=f"We have in stock {medicine['medicine_name']} : {medicine['details']} "
            # TODO: add buttons to book it
                else:
                    msg=f"We have but not in stock   {medicine['medicine_name']} : {medicine['details']} "

                dispatcher.utter_message(text=msg)
                return []        
        except Exception as e:
            print(e)
            dispatcher.utter_message(text="Sorry, I encountered an error while processing your request.")
        

        
        dispatcher.utter_message(text="Please try again")

        return []

# Lab
  
class ActionLabTestEnquiry(Action):
    def name(self) -> Text:
        return "action_lab_test_enquiry"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            medicine_name=next(tracker.get_latest_entity_values("medicine_name"),None)
        
            if not medicine_name:
                dispatcher.utter_message(text="Entered Medicine not found")
                return []

            medicine=None
            for medi in all_medicine:
                if medicine_name.lower() in medi["medicine_name"].lower():
                    medicine=medi
                    break
            if medicine:
                msg=""
                if medicine["no_of_quantity"]>1:
                    msg=f"We have in stock {medicine['medicine_name']} : {medicine['details']} "
            # TODO: add buttons to book it
                else:
                    msg=f"We have but not in stock   {medicine['medicine_name']} : {medicine['details']} "

                dispatcher.utter_message(text=msg)
                return []

        except Exception as e:
            print(e)
            dispatcher.utter_message(text="Sorry, I encountered an error while processing your request.")

        
        dispatcher.utter_message(text="Please try again")
        return []

class ActionShowAllLabTests(Action):
    def name(self) -> Text:
        return "action_show_all_lab_tests"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:        
            print("Bhai")
            buttons=[]
            for test in all_lab_tests:
                buttons.append({"title":test["name"],"payload":f'/show_details_of_lab_test{{"lab_test_id":"{test["id"]}"}}'})
            print(buttons)
            dispatcher.utter_message(text="Which Test you would like to select",buttons=buttons)
            return []

        except Exception as e:
            print(e)
            dispatcher.utter_message(text="Sorry, I encountered an error while processing your request.")

        
        dispatcher.utter_message(text="Please try again")
        return []

class ActionShowSingleLabTestDetails(Action):
    def name(self) -> Text:
        return "action_show_details_of_lab_test"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:        
            lab_test_id = tracker.get_slot('lab_test_id')
            if not lab_test_id:
                dispatcher.utter_message(text="Please try again later")
                return []
            lab_test_details=None
            for test in all_lab_tests:
                if (test["id"]==lab_test_id):
                    lab_test_details=test
                    break     
            if lab_test_details:
                dispatcher.utter_message(text=f"Test Details\n{lab_test_details['name']}  \n Price: {str(lab_test_details['cost'])}Rs")
                return []
            dispatcher.utter_message(text="Please try later")
            return []

        except Exception as e:
            print(e)
            dispatcher.utter_message(text="Sorry, I encountered an error while processing your request.")

        
        dispatcher.utter_message(text="Please try again")
        return []
