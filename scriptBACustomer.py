# dummy script for ba and customer from API
import json
with open('/home/administrator/Documents/ISCM2/iscm/contract/rfpapi.json') as json_file:
	data = json.load(json_file)

from account.models import Customer, BA
from location.models import State, 


customer_dict = data[0]['CustomerList']
ba_dict = data[0]['BAList']
state_dict = data[0]['StateList']

custCount = 0
for customer in customer_dict:
	create_obj = Customer()
	create_obj.custid = customer['CUSTOMERID']
	create_obj.custcode = customer['CUSTOMERCODE']
	create_obj.custname = customer['CUSTOMERNAME']
	create_obj.custcontactname = customer['CONTACTPERSON']
	create_obj.email = customer['EMAIL']
	try:
		create_obj.save()
		custCount += 1
		print(custCount)
	except:
		pass

baCount = 0
for ba in ba_dict:
	create_obj = BA()
	create_obj.baid = ba['BA_ID']
	create_obj.bacode = ba['VENDOR_CODE']
	create_obj.baname = ba['VENDOR_NAME']
	try:
		create_obj.save()
		baCount += 1
		print(baCount)
	except:
		pass


stateCount = 0
for state in state_dict:
	create_obj = State()
	create_obj.stateid = state['STATEID']
	create_obj.statecode = state['STATECODE']
	create_obj.statename = state['STATENAME']
	try:
		create_obj.save()
		stateCount += 1
		print(stateCount)
	except:
		pass


# verticalCount = 0
# for vertical in data

from account.models import UserLocationCustomer
from account.models import User
from location.models import OperationLocation
from account.models import Customer
import time
import random

customer = Customer.objects.all()
oploc = OperationLocation.objects.all()
user = User.objects.all()

for cust in customer[500:]:
	# for ol in oploc: 
	print(cust.custname)
	ulccreate = UserLocationCustomer(ulcpkey=str(random.randrange(10000,50000)),location=oploc[0], customer=cust,user=user[0])
	ulccreate.save()

