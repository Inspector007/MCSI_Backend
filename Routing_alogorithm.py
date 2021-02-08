
# dummy script for ba and customer from API
import json
import math
import numpy as np
with open('/usr/local/src/projects/SaralApplication/Saral/project4/projects/routing.json') as json_file:
	data = json.load(json_file)


class Site:
	def __init__(self,data):
		# self.lat = data['lat'][0]
		self.customerID = data['customerID']
		self.siteId = data['siteId']
		self.shiftId = data['shiftId']
		self.shiftType = data['shiftType']
		self.siteLat = float(data['siteLat'])
		self.siteLong = float(data['siteLong'])

	def get_available_vehicle(self,data):
		return data['availableVehicles']

	def get_employees(self,data):
		return data['employees']

	def get_guards(self,data):
		return data['guards']

	def get_constraints(self,data):
		return data['constraints']		


class Employee:
	def __init__(self):
		self.empId = None
		self.empName = None
		self.lat = None
		self.long = None
		self.gender = None
		self.special = None
		self.index=0
		self.site_distance = 0.0


	def emp_obj_json(self,emp):
		self.empId = emp['empId']
		self.empName = emp['empName']
		self.lat = emp['lat']
		self.long = emp['long']
		self.gender = emp['gender']
		self.special = emp['special']
		self.index =0
		self.site_distance = 0.0


	def emp_obj_json_withindex(self,emp,index,site_distance):
		self.empId = emp['empId']
		self.empName = emp['empName']
		self.lat = emp['lat']
		self.long = emp['long']
		self.gender = emp['gender']
		self.special = emp['special']
		self.index = index
		self.site_distance = site_distance

class Vehicle:
	def __init__(self):
		self.type = type
		self.totalCount = totalCount
		self.seatingCapacity = seatingCapacity
		self.avgSpeed = avgSpeed

	def __init__(self,data):
		self.type = type
		self.totalCount = totalCount
		self.seatingCapacity = seatingCapacity
		self.avgSpeed = avgSpeed


class Employee_Distance:
	def __init__(self):
		pass
		

class current_trip:
	def __init__(self):	
		pass


def the_optimizer(data):
	site_obj = Site(data)
	print("Request Json ***************************** \n {0}".format(data))
	emp_dist_from_source_array = []
	dist_array = []
	k_no = 0
	#CREATE Site to Employee Distance Array
	for emp_obj in site_obj.get_employees(data):
		radius = 6371
		emp_lat = float(emp_obj['lat'])
		emp_lon = float(emp_obj['long'])

		dlat = math.radians(emp_lat - site_obj.siteLat)
		dlon = math.radians(emp_lon - site_obj.siteLong)
		sitea = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(site_obj.siteLat)) \
														  * math.cos(math.radians(emp_lat)) * math.sin(
				dlon / 2) * math.sin(dlon / 2)
		sitec = 2 * math.atan2(math.sqrt(sitea), math.sqrt(1 - sitea))
		sited = radius * sitec
		tmp_emp = Employee()
		tmp_emp.emp_obj_json_withindex(emp_obj,k_no,float(sited)*1.6)
		k_no += 1
		emp_dist_from_source_array.append(tmp_emp)

	#Available vehicles with seatign capacity, speed, % capacity utilizatino constraint etc..
	available_vehicle_types = []
	for pos,vehicle_obj in enumerate(site_obj.get_available_vehicle(data)):
		available_vehicle_types.append(vehicle_obj)
	
	available_vehicle_sorted = sorted(available_vehicle_types, key=lambda k: k['seatingCapacity'],reverse=True)
	
	print("Sorted vehicle Array *********************************\n {0}".format(available_vehicle_sorted))

	# print("1-D-Array- Distannce of all emp from Site \n {0}".format(sorted_site_emp_dist_list))
	print("1-D-Array- Distannce of all emp from Site ******************************** \n ")
	print([(emp.site_distance, emp.index) for emp in emp_dist_from_source_array])

	emp_distance_matrix = []
	
	# Create Matrix for all distance using all the node
	column_array = []
	for emp_i in emp_dist_from_source_array:
		row_array = []
		for emp_j in emp_dist_from_source_array:
			lat1 = float(emp_i.lat)
			lat2 = float(emp_j.lat)
			lon1 = float(emp_i.long)
			lon2 = float(emp_j.long)
			radius = 6371
			dlat = math.radians(lat2 - lat1)
			dlon = math.radians(lon2 - lon1)
			a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
														  * math.cos(math.radians(lat2)) * math.sin(
				dlon / 2) * math.sin(dlon / 2)
			c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
			d = radius * c
			row_array.append(float(d)*1.6)
		column_array.append(row_array)

	final_emp_distance_matrix = np.array(column_array)
	print("2-D-Array- Distannce of all emp from others emp ******************************************** \n\n {0}".format(final_emp_distance_matrix))
	
	#Algo Starts
	#Get Farthest Employee
	#sorted_site_emp_dist_list = sorted(emp_dist_from_source_array, key=lambda x:x.site_distance,reverse=True)
	current_farthest_employee = max(emp_dist_from_source_array, key=lambda x:x.site_distance)
	farthest_emp_dist = current_farthest_employee.site_distance

	#numpy array for index based fetching of employee objects
	np_emp_dis_arr = np.array([emp_dist_from_source_array])

	print("Farthest Emp object :*******************\n {0}".format(farthest_emp_dist))
	
	#Define all constraints in an object

	# Check max_emp_node_distance is less than allowed maximum trip distance

	constraints_max_distance_value = 0
	for constraints in site_obj.get_constraints(data):
		if constraints['type'] == 'distance':
			for clause in constraints['conditions']:
				if clause['clause'] == 'total_distance':
					constraints_max_distance_value = clause['value']

	# Check max_time is less than or greater than constraints total_dist

	constraints_max_time_value = 0
	for constraints in site_obj.get_constraints(data):
		if constraints['type'] == 'time':
			for clause in constraints['conditions']:
				if clause['clause'] == 'total_time':
					constraints_max_time_value = clause['value']

	# Check in_between_time is less than or greater than constraints total_dist

	constraints_inbetween_time_value = 0
	for constraints in site_obj.get_constraints(data):
		if constraints['type'] == 'time':
			for clause in constraints['conditions']:
				if clause['clause'] == 'inbetween_time':
					constraints_inbetween_time_value = clause['value']

	# check for Max allowed distance vs farthest node
	valid = 1
	if farthest_emp_dist > constraints_max_distance_value:
		valid = 1001
		throw

	# Check for time taken by fastst vehicle in reaching  farthest node vs allowed trip time
	max_speed_vehicle = max([i['avgSpeed']for i in site_obj.get_available_vehicle(data)])
	farthest_emp_trip_duration = farthest_emp_dist / max_speed_vehicle
	if farthest_emp_trip_duration > constraints_max_time_value:
		valid = 1002
		throw 


	# Check if aailable no of vehicles are sufficient for servince all empployees
	total_available_capacity = sum([i['seatingCapacity']for i in site_obj.get_available_vehicle(data)])
	if total_available_capacity < len(emp_dist_from_source_array)*1.2:
		valid = 1003
		throw

	import pdb;pdb.set_trace()
	is_validate_fail = 0
	finalized_trips =[]
	while(True):
		farthest_emp_obj = max_emp_obj
		current_trip = []
		current_trip.append(farthest_emp_obj)
		current_trip_distance = farthest_emp_obj['site_distance']
		current_allocated_vehicle = max_capacity_vehicle_obj
		while(True):
			next_nearest_emp = get_nearest_emp_from_trip(current_trip,final_emp_distance_matrix,emp_dist_from_source_array)
			tmp_current_trip_detail = current_trip.append(next_nearest_emp)
			tmp_trip_distance = get_trip_distance(tmp_current_trip_detail)

			#available vehicle with highest capacity cannot accomodate current no of people in trip
			#Break Both loops
			remaining_seat_count = 0
			if current_allocated_vehicle['seatingCapacity'] < len(current_trip):
				is_validate_fail = 1
				break 
			elif tmp_trip_distance > constraints_max_distance_value: #Failling due to DIstance: Check if vehicel is fully utilized 
				remaining_seat_count = current_allocated_vehicle['seatingCapacity'] - len(current_trip)
				if remaining_seat_count < 2:# convert it into percentage above 75%
					break
				else:
					next_highest_capacity_obj = get_find_next_possible_vehicle(current_allocated_vehicle,\
						current_trip_len,site_obj,data)
			elif tmp_trip_distance > constraints_max_distance_value:
				best_fit_vehicle = get_best_fit_vehicle(current_allocated_vehicle,\
					current_trip,site_obj)

			
			#if not use lowest  capacitiy vehicle which can  serve the trip & break both loops

			#Failing due to time: use next highest capacitiy vehicle which can  serve the trip capacitywise 
				#check capacity  see if loop should be broken   
			
			#

		if is_validate_fail == 1:
			break

def get_best_fit_vehicle(current_allocated_vehicle,current_trip,site_obj,*create_trip):
	vehicle_list = site_obj.get_available_vehicle(data)

	current_trip_len = len(current_trip)

	# vehicle capacity c
	vehicle_capacity_list = set([i['seatingCapacity']for i in vehicle_list])
	vehicle_capacity_list.sort()

	vehicle_capacity_list = vehicle_capacity_list[::-1]


	remaining_trip = []
	# check vehicle utilization

	vehicle_utilization_percentage = ((current_trip_len / current_allocated_vehicle['seatingCapacity'])*100)

	if vehicle_utilization_percentage > 75: # take percentage value from json as per vehicle communicate with vaayu team
		create_trip = current_trip
	else:
		for veh_capacity_divide in vehicle_capacity_list[1:]: # check for second highest capacity vehicle 
			if int(current_trip_len / veh_capacity_divide) > 0:
				pass
			else:
				pass 



def get_find_next_possible_vehicle(current_allocated_vehicle,current_trip_len,site_obj,data):
	vehicle_list = site_obj.get_available_vehicle(data)

	for i,val in enumerate(vehicle_list):
		if val['seatingCapacity'] == current_allocated_vehicle['seatingCapacity']:
			del vehicle_list[i]

	vehicle_capacity_list = set([i['seatingCapacity']for i in vehicle_list])
	vehicle_capacity_list.sort()
	next_highest_capacity_val = vehicle_capacity_list[::-1][0]

	for veh_obj in vehicle_list:
		if veh_obj['seatingCapacity'] == next_highest_capacity_val:
			next_highest_capacity_obj = veh_obj


	return next_highest_capacity_obj




def get_trip_distance(tmp_current_trip_detail):
	trip_distance = 0
	previous_emp = None
	for emp in tmp_current_trip_detail:
		if trip_distance == 0:
			trip_distance = emp['site_distance'] 
			previous_emp = emp
		else:
			trip_distance = trip_distance + get_distance_between_2_emp(previous_emp,emp)
			previous_emp = emp

	return trip_distance

def get_nearest_emp_from_trip(current_trip,final_emp_distance_matrix,emp_dist_from_source_array):
	nearest_emp = None
	for employee in current_trip:
		tmp_nearest_emp_distance = np.amin(final_emp_distance_matrix[employee['j'],...])
		tmp_nearest_emp_pos = np.where(final_emp_distance_matrix[employee['j'],...] == tmp_nearest_emp_distance)[0]
		if nearest_emp == None:
			for new_emp in emp_dist_from_source_array:
				if new_emp['j'] == tmp_nearest_emp_pos[0]:
					nearest_emp = new_emp
		else:
			if tmp_nearest_emp_distance < final_emp_distance_matrix[nearest_emp['j']:tmp_nearest_emp_pos]:
				nearest_emp = employee

	return nearest_emp


def get_distance_between_2_emp(emp1,emp2):
	return final_emp_distance_matrix[emp1['j'],emp2['j']]

"""
def is_valid_trip(current_trip_list,current_trip_distance,sortedby_capacity_available_veh_array[0]):
	# can the max sized avialable vehicle capacity > current trip emp
	if len(current_trip_list) < sortedby_capacity_available_veh_array[0]:
		print('trip is possible')
	else:
		print('trip is not possible') # error Code 1201
		break
	# distance < max allowed trip sdistance
	if current_trip_distance < sortedby_capacity_available_veh_array[0]:
		print('trip is possible')
	else:
		print('trip is not possible') # error Code 1201
	# time with max capacity < max allowed time
"""

the_optimizer(data)