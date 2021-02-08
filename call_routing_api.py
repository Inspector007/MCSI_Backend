#fake Json for routing algorithm

import json
import math
import numpy as np
with open('/home/administrator/Documents/ISCM2/iscm/routing_multi_emp.json') as json_file:
	data = json.load(json_file)
	

def routing_response(data):
	all_vehicles_detail_dict = data['availableVehicles']

	sort_all_vehicles_detail_dict = sorted(all_vehicles_detail_dict, key=lambda k: k['seatingCapacity'],reverse=True)

	all_emp_detail_dict = data['employees']

	final_json = {}

	all_emp_count = len(all_emp_detail_dict)

	valid = 1
	available_seating_capacity = sum([(v['totalCount'] * v['seatingCapacity']) for v in all_vehicles_detail_dict])
	available_current_type_seat = []

	if available_seating_capacity >= all_emp_count:
		print('available_seating_capacity {0} ********** all_emp_count {1}'.format(\
			available_seating_capacity,all_emp_count))
		for veh_detail in sort_all_vehicles_detail_dict:
			veh_count = veh_detail['totalCount']
			print(len(all_emp_detail_dict) % (veh_detail['seatingCapacity'] * veh_detail['totalCount']))
			if len(all_emp_detail_dict) % (veh_detail['seatingCapacity'] * veh_detail['totalCount']) >= 0 and len(all_emp_detail_dict) > 0:
				for count in range(veh_count):
					count = 1
					all_emp_detail_dict = all_emp_detail_dict[veh_detail['seatingCapacity']:]
					veh_detail['totalCount'] -= 1
					available_current_type_seat.append(veh_detail)
					if len(all_emp_detail_dict) == 0:
						valid = 1
						break
			if valid == 1001:
				break
	else:
		print('emp count is greater than vehicle capacity')
		valid = 1001

	print('available_current_type_seat ************ \n {0}'.format(available_current_type_seat))

	final_json_dict = {}
	final_json_dict['statusCode'] = 200
	final_json_dict['responseBody'] = call_response_body(data,available_current_type_seat,\
		available_seating_capacity,all_emp_count)
	final_json_dict['msg'] = 'Success'
	final_json_dict['errors'] = ''

	if valid == 1001:
		final_json_dict['statusCode'] = 1001
		final_json_dict['responseBody'] = None
		final_json_dict['msg'] = 'Employee count is greater than vehicle capacity'
		final_json_dict['errors'] = 'Employee count is greater than vehicle capacity'

	return json.dumps(final_json_dict)

def call_response_body(data,filled_emp_vehicle_seat,available_seating_capacity,all_emp_count):
	response_body_dict = {}
	response_body_dict["customerID"] = data["customerID"]
	response_body_dict["siteId"] = data["siteId"]
	response_body_dict["shiftId"] = data["shiftId"]
	response_body_dict["shiftType"] = data["shiftType"]
	response_body_dict["tripStart"] = "tripStart"
	response_body_dict["siteLat"] = data["siteLat"]
	response_body_dict["siteLong"] = data["siteLong"]
	response_body_dict["tripEnd"] = "tripEnd"
	response_body_dict["routes"] = call_routes(data,filled_emp_vehicle_seat,available_seating_capacity,all_emp_count)

	return response_body_dict

def call_routes(data,filled_emp_vehicle_seat,available_seating_capacity,all_emp_count):
	routes = []
	routes_dict = {}
	routes_dict["routeId"] = '23423232342344'
	routes_dict["total_time"] = ''
	routes_dict["total_distabce"] = ''
	routes_dict["tripStartTime"] = ''
	routes_dict["tripEndTime"] = ''
	routes_dict["vehicle_type"] = ''
	routes_dict["total_seats"] = available_seating_capacity
	routes_dict["empty_seats"] = all_emp_count
	routes_dict["guard_required"] = ''
	routes_dict["vehicle_allocated"] = ''
	routes_dict["trip_cost"] = ''
	routes_dict["route_final_path"] = call_routing_path(data,filled_emp_vehicle_seat)
	routes_dict["employees_nodes_addresses"] = call_employee_node_adresses(data,filled_emp_vehicle_seat)

	routes.append(routes_dict)

	return routes

def call_routing_path(data,filled_emp_vehicle_seat):
	route_final_path = {}
	for index,emp in enumerate(data['employees']):
		route_final_path[str(index)] = {
			"lat": emp["lat"],
			"long": emp["long"],
			"time": "DateTime" 
			}	

	return route_final_path


def call_employee_node_adresses(data,filled_emp_vehicle_seat):
	employees_nodes_addresses = []
	for index,emp in enumerate(data['employees']):
		employee_address = {
		"rank" : index,
		"empId" : emp["empId"],
		"empName" : emp["empName"],
		"lat" : emp["lat"],
		"long" : emp["long"],
		"gender" : emp["gender"],
		"special" : emp["special"]
		}

		employees_nodes_addresses.append(employee_address)	

	return employees_nodes_addresses


print(routing_response(data))
