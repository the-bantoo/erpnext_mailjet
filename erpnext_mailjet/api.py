import frappe
from frappe import _
import requests
import json
from frappe.utils import today
import re
from mailjet_rest import Client
import os
from frappe.utils.password import get_decrypted_password
api_key = '04a946ff54ddaf6a028d07da22286d76'
api_secret = '8a6c25c928da69626ebd0b039d2c1b48'
mailjet = Client(auth=(api_key, api_secret), version='v3')

get_email_group = frappe.db.get_list('Email Group', pluck = 'name')
for data in get_email_group:
     data = {

     "Name": ''
     }
result = mailjet.contactslist.create(data=data)
print (result.status_code)
print (result.json())

# data = {
#   'Email': "test2@thebantoo.com"
# }
# result = mailjet.contact.create(data=data)
# print (result.status_code)
# print (result.json())

# data = {
#      'IsUnsubscribed': "false",
#      'ContactAlt': "test2@thebantoo.com",
#      'ListAlt': "test_list3"
# } 
# result = mailjet.listrecipient.create(data=data)
# print (result.status_code)
# print (result.json())
