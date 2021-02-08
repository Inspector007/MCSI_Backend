from contract.models import ContractType, RateType
contracttype = [
    {
        "contracttypeid": 1,
        "cnttypename": "Manpower",
        "cnttypecode": "MNP"
    },
    {
        "contracttypeid": 2,
        "cnttypename": "Fixed price",
        "cnttypecode": "FXP"
    },
    {
        "contracttypeid": 3,
        "cnttypename": "Output based pricing",
        "cnttypecode": "OBPR"
    }
]

ratetype = [
    {
        "ratetypeid": 1,
        "ratetypename": "FLatrate",
        "ratetypecode": "FRCO",
        "contracttypeid": 1
    },
    {
        "ratetypeid": 2,
        "ratetypename": "Costplusrate",
        "ratetypecode": "CTRT",
        "contracttypeid": 1
    },
    {
        "ratetypeid": 3,
        "ratetypename": "Lumsum",
        "ratetypecode": "LUMS",
        "contracttypeid": 2
    },
    {
        "ratetypeid": 4,
        "ratetypename": "Slabbasedoverlap",
        "ratetypecode": "SBOV",
        "contracttypeid": 3
    },
    {
        "ratetypeid": 5,
        "ratetypename": "Slabbasedflat",
        "ratetypecode": "SBFL",
        "contracttypeid": 3
    }
]


def contracttypeFun():
	if ContractType.objects.all().count() == 0:
		contractCount = 0
		for contracttype_obj in contracttype:
			contracttype_create = ContractType(contracttypeid = contracttype_obj["contracttypeid"],\
				cnttypename = contracttype_obj["cnttypename"],\
				cnttypecode = contracttype_obj["cnttypecode"]
				)
			contracttype_create.save()
			contractCount += 1
		print("ContrcactType Load Count {0}".format(contractCount))
	else:
		print("No Need To initialize")


def ratetypeFun():
	if RateType.objects.all().count() == 0:
		rateCount = 0
		for ratetype_obj in ratetype:
			contracttype_obj = ContractType.objects.get(contracttypeid = ratetype_obj["contracttypeid"])
			ratetype_create = RateType(ratetypeid = ratetype_obj["ratetypeid"],\
				ratetypename = ratetype_obj["ratetypename"],\
				ratetypecode = ratetype_obj["ratetypecode"],\
				contracttypeid = contracttype_obj
				)
			print(rateCount)
			ratetype_create.save()
			rateCount += 1
		print("Rate Load Count {0}".format(rateCount))
	else:
		print("No Need To initialize")



# dummy script for ba and customer from API
import json
with open('/home/administrator/Documents/ISCM2/iscm/contract/rfpapi.json') as json_file:
	data = json.load(json_file)

from account.models import Customer, BA
from location.models import State


customer_dict = data[0]['CustomerList']
ba_dict = data[0]['BAList']
state_dict = data[0]['StateList']


def loadcustomerFun():
	custCount = 0
	if Customer.objects.all().count() == 0:
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
		print("Customer Load Count {0}".format(custCount))
	else:
		print("No Need To initialize")


def loadbaFun():
	baCount = 0
	if BA.objects.all().count() == 0:
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
		print("BA Load Count {0}".format(baCount))
	else:
		print("No Need To initialize")


def loadstateFun():
	stateCount = 0
	if State.objects.all().count() == 0:
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
		print("State Load Count {0}".format(stateCount))
	else:
		print("No Need To initialize")



def initial_load_data():
	contracttypeFun()
	ratetypeFun()
	loadcustomerFun()
	# loadbaFun()
	loadstateFun()
