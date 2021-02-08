#middleware auth and token request
from django.shortcuts import redirect
from iscm.utility import userAuthentication
from django.http import HttpResponse
import requests
import json
class CustomMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
		# One-time configuration and initialization.

	def __call__(self, request):
		# Code to be executed for each request before
		# the view (and later middleware) are called.

		id = '1'
		pwd = 'commercial'
		# dictmsg = authorize_app_api(id,pwd)x
		if request.path == '/api/customermaster/' or request.path == '/api/internalorders/':
			iscm_auth_apikey = request.META['HTTP_X_ISCM_API_KEY']
			api_key = 'oFvyg2g1ffj9DkKw2fTtQZStzZd3hPYt02mF5qvtV9o=QfYSSaBLXdCrFkzqlKM2xGiOx8NF4eug/CtOwyyMBdA='
			if iscm_auth_apikey == api_key:
				response = self.get_response(request)
				return response
			else:
				json_response_data = {
					"Record": {
					"STATUSCODE": "401",
					"MESSAGE": "Unauthorized"
					}
				}
				return HttpResponse(json.dumps(json_response_data))

		if request.path != '/login' and request.path != '/swagger-docs/' and request.path != '/api/ba/' and\
		 '/api/opportunity/' not in request.path and '/script/capture_att_detail_api/' not in request.path and \
		  request.path != '/iscmsapapi/api/sapv1/Login/':
			# import pdb;pdb.set_trace()
			# userId = request.META['HTTP_USERID']
			# authToken = request.META['HTTP_AUTHTOKEN']
			# appid = request.META['HTTP_APPID']
			# apptoken = request.META['HTTP_APPTOKEN']
			
			# print('{0} \n--> {1} \n--> {2} \n--> {3}'.format(userId,authToken,appid,apptoken))
			# dictmsg = authorize_app_api(userId,authToken,appid,apptoken)
			dictmsg['message'] = 'authenticated'
			print(request.path)
			print(dictmsg['message'])
			print(userId,authToken,appid,apptoken)
			print("dict ***** {0}".format(dictmsg))
			if dictmsg['message'] == 'authenticated':
				request.META['QUERY_STRING'] = '25004740'
				print('before {0}'.format(request.META['QUERY_STRING']))
				response = self.get_response(request)
				return response
			else:
				return HttpResponse("Authorization failed")
		else:
			response = self.get_response(request)
			return response

		# Code to be executed for each request/response after
		# the view is called.

from django.utils.deprecation import MiddlewareMixin

# class to import in RemoveHeaders--

class RemoveHeaders(MiddlewareMixin):
    # rest of the code
    def process_response(self, request, response):
        response['Server'] = ''
        return response

def login_api(username,password,devicetype):
	# API_ENDPOINT = "http://10.175.2.29:8080/login"
	# API_ENDPOINT = "http://13.235.45.209:8080/login"
	# API_ENDPOINT = "http://13.234.117.242:8080/login"
	# API_ENDPOINT = "http://13.235.19.252:8080/login"
	# API_ENDPOINT = "http://13.127.241.1:8080/login"
	# API_ENDPOINT = "http://13.126.117.178:8080/login"
	# API_ENDPOINT = "http://13.232.74.130:8080/login"
	from account.models import User
	# import pdb;pdb.set_trace()
	API_ENDPOINT = "http://13.235.195.93:8080/login"
	# import pdb;pdb.set_trace()
	data = {"username":username,
				"password":password,
				"deviceType":devicetype,
					}
	# import pdb;pdb.set_trace()
	headers = {'Content-type': 'application/json'}

	response = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
	user_login_response = json.loads(response.text)
	"""
	{
		'status': 'fail', 
		'message': 'Due to unsucessfull attempts of login your account is temporarily locked. Please contact system administrator.', 
		'data': {}, 
		'error': 
			[
				{'code': 'ERR_006', 'message': 'Due to unsucessfull attempts of login your account is temporarily locked. Please contact system administrator.'}
			]
	}
	"""	
	if user_login_response["status"] == "success":
		userId = user_login_response['data']['token']['userId']
		authToken = user_login_response['data']['token']['authToken']
		userapps_detail_list = user_login_response['data']['userApps']
		tokenId = user_login_response['data']['tokenId']
		user_obj = User.objects.get(userid = tokenId)
		userName = user_obj.firstname + " " + user_obj.lastname
		# print(tokenId,' =====' ,userName)
		devicetype = devicetype

		print("userId - {0}\n\
				authToken - {1}\n\
				userapps_detail_list - {2}\n\
				devicetype - {3}".format(userId,authToken,userapps_detail_list,devicetype))
		

		if userapps_detail_list:
			for appdata in userapps_detail_list:
				if appdata['appId'] == 5:
					appid = 5
					user_role = appdata['roleName']
					break
				else:
					appid = None
					user_role = None

		# authorize_auth_token_api_res = authorize_auth_token_api(userId,authToken,appid,devicetype)
		# import pdb;pdb.set_trace()
		# print("authtoken_response -- > {0}".format(authorize_auth_token_api_res))

		# if  authorize_auth_token_api_res["status"] == "success":
		# 	apptoken = authorize_auth_token_api_res['data']
		# 	authorize_app_response = authorize_app_api(userId,authToken,appid,apptoken)

		# 	if authorize_app_response['status'] == "success":
		# 		return 1
		# 	else:
		# 		return authorize_app_response
		# else:													
		# 	return authorize_auth_token_api_res
		if appid == 5:
			return {"status":"success","tokenId":tokenId,"userName":userName,"userId":userId,"authToken":authToken,"appid":appid,"userrole":user_role,"deviceType":devicetype}
		else:
			return {"status":"unauthorize","tokenId":tokenId,"userName":userName,"userId":userId,"authToken":authToken,"appid":appid,"userrole":user_role,"deviceType":devicetype}

	else:
		if 'locked' in user_login_response["message"]:
			return {"status":"Fail","tokenId":"","userName":"","userid":"","authToken":user_login_response["message"],"appid":"","userrole":"","deviceType":""}
		else: 
			return {"status":"Fail","tokenId":"","userName":"","userid":"","authToken":"","appid":"","userrole":"","deviceType":""}
		
def authorize_auth_token_api(userId,authToken,appid,deviceType):
	# API_ENDPOINT = "http://10.175.2.29:8080/authorize"
	# API_ENDPOINT = "http://13.235.45.209:8080/authorize"
	API_ENDPOINT = "http://13.235.195.93:8080/authorize"

	data = {'userId':userId,
				'authToken':authToken,
				'appid':appid,
				'deviceType':deviceType,
					}
	headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'userId':userId,
			'authToken':authToken,
			'appid':appid,
			'deviceType':deviceType,
        }
	response = requests.post(url = API_ENDPOINT, data = json.dumps(data),headers = headers)

	authtoken_response = json.loads(response.text)
	if authtoken_response["status"] == "success":
		return authtoken_response 
	else:
		return {"status" : authtoken_response }


def authorize_app_api(userId,authToken,appid,apptoken):
	# API_ENDPOINT = "http://13.235.45.209:8080/authorizeApp"
	# import pdb;pdb.set_trace()
	API_ENDPOINT = "http://13.235.195.93:8080/authorizeApp"
	
	data = {'userId':userId,
				'authToken':authToken,
				'appid':appid,
				'apptoken':apptoken,
				'deviceType':'web',
					}
	headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'userId':userId,
			'authToken':authToken,
			'appid':appid,
			'apptoken':apptoken,
			'deviceType':'web',
        }
	response = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers=headers) 
	authorize_app_response = json.loads(response.text)
	if authorize_app_response["status"] == "success":
		return { "message" : "authenticated" }
	else:
		return {"message" : "Failed" }
