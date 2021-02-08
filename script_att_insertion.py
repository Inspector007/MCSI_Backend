# script for data insertion

#K0253-MLL-2019-07-31-165447


# from celery.schedules import crontab
# from celery.task import periodic_task
# @periodic_task(run_every=crontab(hour=7, minute=30, day_of_week="mon"))
# def every_monday_morning():
#  print("This is run every Monday morning at 7:30")

def capture_att_detail():

	from contract.models import DetailAttCapture,Designation,Contract,ContractDetail,SkillLevel
	import json
	import urllib.request
	import time
	from datetime import datetime
	# siteid = self.kwargs['siteid']
	# vendorid = self.kwargs['vendorid']
	# contractid = self.kwargs['contractid']
	siteid = '12453314582980232158'
	vendorid = '14717317141858447095'
	contractid = 'nocustcode-MLL-2019-09-10-130250'
	date1 = '06-09-2019'
	# date2 = dateime.strptime(date1,'%d-%m-%Y').date()
	date1_l = date1.split('-')
	date2 = '{0}-{1}-{2}'.format(date1_l[2],date1_l[1],date1_l[0])


	apikey = 'Zsj0+CkJJck1e8fwe1L20Zxpu1pbsnWu/7V16dHBdEir63N6tiiU4ozRi3qBGd6ZBeZaS1EL8bkvtOML6tT1xw=='
	headers = {'apikey' : apikey }

	att_url = "https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor={0}&siteId={1}&startDate={2}&endDate={3}".format(vendorid,siteid,date1,date1)
	req1 = urllib.request.Request(att_url)
	req1.add_header('apikey',apikey)

	#https://portal.betterplace.co.in/VishwasAPI/api/Attendance/getRecordSiteVendor?vendor=10178163594610587744&siteId=16252173452509896464&startDate=05-08-2019&endDate=09-09-2019
	print('vendorid - {0} - siteid - {1}'.format(vendorid,siteid))

	recordsitevendor_dict = urllib.request.urlopen(req1).read()
	time.sleep(5)
	recordsitevendor_dict = str(recordsitevendor_dict,'utf-8')

	recordsitevendor_json = json.loads(recordsitevendor_dict)
	recordsitevendor_data = recordsitevendor_json['data']

	if recordsitevendor_data['attendanceDetails'] is not None:
		print('vendorid - {0} * siteid - {1} * attdata - {2}'.format(vendorid\
		 ,siteid,recordsitevendor_data['attendanceDetails']))
		# get conntract detail data
		contractdetail = ContractDetail.objects.filter(contract = contractid)
		skill_list = [i[0] for i in contractdetail.values_list('skilllevel')]
		designation_list = [i[0] for i in contractdetail.values_list('designation')]
		zip_of_skill_designation = [i for i in zip(skill_list,designation_list)]
		for att_dict in recordsitevendor_data['attendanceDetails']:
			# import pdb;pdb.set_trace()
			print('job funct **** {0}'.format(att_dict['jobfunction']))
			try:
				job_function = Designation.objects.get(designation_name = att_dict['jobfunction']) #designation_id , designation_name
				for i in zip_of_skill_designation:
					if i[1] == job_function.designation_id:
						try:
							get_existing_attdetail = DetailAttCapture.objects.get(contractid= contractid,date= date2,skillid= i[0],designation= i[1])
							get_existing_attdetail.skillcount = int(float(att_dict['regManDays']))
							get_existing_attdetail.skillotcount =  int(float(att_dict['totalOTHrs']))
							get_existing_attdetail.extrashift = int(0)
							get_existing_attdetail.save()  
						except:
							print('Not Exist')
							attcapture_obj = DetailAttCapture()
							attcapture_obj.contractid = Contract.objects.get(contractid = contractid)
							attcapture_obj.date = date2
							attcapture_obj.skillid = SkillLevel.objects.get(skillid = i[0])# skillid , skillname
							attcapture_obj.designation = Designation.objects.get(designation_id = i[1]) #designation_id , designation_name
							attcapture_obj.skillcount = int(float(att_dict['regManDays']))
							attcapture_obj.skillotcount =  int(float(att_dict['totalOTHrs']))
							attcapture_obj.extrashift = int(0)
							attcapture_obj.save()
						print('Data Inserted Successfully')
						break
			except:
				print('No job function map')
				pass



 # filter_vendor_list.append(recordsitevendor_data['vendor'])

# return Response(filter_vendor_list)



