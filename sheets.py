import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

def get_init_worksheet(cred_file_name, sheet_file_name, ws_title):
	scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

	creds = ServiceAccountCredentials.from_json_keyfile_name(cred_file_name, scope)
	client = gspread.authorize(creds)
	sheet = client.open(sheet_file_name)
	worksheet = sheet.worksheet(ws_title)
	return worksheet

def update_cell(sheet, row_index, col_index, val):
	sheet.update_cell(row_index,col_index,val)

def get_id_from(email):
	id = email.partition("@")[0]
	return id

def get_col_count_of(sheet_list):
	row_header = sheet_list[0]
	col_count = len(row_header)
	return col_count

def add_new_class_col_header(worksheet,list,non_class_col_count):
	# non_class_col_count = number of column headers that are not not related to classes
	info_col_count = get_col_count_of(list)
	# Get new column header name
	header_name = "C"+str(info_col_count-non_class_col_count+1)
	# Insert new column header
	col_index = info_col_count+1
	update_cell(worksheet, 1, col_index, header_name)
	# Make column header bold and centered
	#worksheet.format("C1", {'textFormat': {'bold': True}, "horizontalAlignment": "CENTER",})

def update_entire_col(ws,list,non_class_col_count,col_index,val):
	# val is a list of list containing attendance. Example: [[1], [0], [1]]
	mapping = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', 'I':'9', 'J':'10', 'K':'11', 'L':'12', 'M':'13', 'N':'14', 'O':'15', 'P':'16', 'Q':'17', 'R':'18', 'S':'19', 'T':'20', 'U':'21', 'V':'22', 'W':'23', 'X':'24', 'Y':'25', 'Z':'26'}
	row_count = len(list)
	col_index_letter = mapping[str(col_index)]
	add_new_class_col_header(ws,list,non_class_col_count)
	header_notation = col_index_letter+"1"
	ws.format(header_notation, {'textFormat': {'bold': True}, "horizontalAlignment": "CENTER",})

	req_notation = col_index_letter+"2:"+col_index_letter+str(row_count+1)
	ws.update(req_notation, val)
	ws.format(req_notation, {'textFormat': {'bold': False}, "horizontalAlignment": "CENTER",})

def get_class_att_list(info_list, form_list):
	att_list = []
	for dict in info_list:
		id = dict["ID"]
		email = str(id)+"@seu.edu.bd"
		response = list(filter(lambda response: response['Email Address'] == email, form_list))
		# If no match is found (0=absent)
		if not response:
			att_list.append([0])
		# If match found (1=present)
		else:
			att_list.append([1])
	return att_list

def print_id_by_course(list,separator):
	print("\n---------- A T T E N D A N C E ----------")
	# If course code has been used as an option in the form
	if "Course Code" in list[0]:
		att_dict = {}
		for dict in list:
			id = int(get_id_from(dict['Email Address']))
			course = dict['Course Code']
			#print("id: ",id, "| cc: ",course)
			if course in att_dict:
				att_dict[course].append(id)
			else:
				att_dict[course] = [id]
		
		for course, id_list in att_dict.items():
			print("\nCOURSE CODE: ",course)
			print(*id_list, sep=separator)
	# If course code has NOT been used as an option in the form
	else:
		id_list = []
		for dict in list:
			id = int(get_id_from(dict['Email Address']))
			id_list.append(id)
		print(*id_list, sep=separator)

	print("\n-----------------------------------------\n")

"""---------------------------------------"""
# USER DEFINED PARAMETERS
cred_file_name = "credentials.json"
form_file_name = "C1"
form_ws_title = "Form Responses 1"

info_file_name = "CSE101"
info_ws_title = "Attendance"
non_class_col_count = 2

id_separator = " "
update_worksheet = True
"""---------------------------------------"""

start = time.time()
form_ws = get_init_worksheet(cred_file_name, form_file_name, form_ws_title)
if update_worksheet:
	info_ws = get_init_worksheet(cred_file_name, info_file_name, info_ws_title)
end1 = time.time()
#print("Time taken to fetch worksheet: %0.2fs" % (end1-start))

# Create a list of dict from the worksheet
form_list = form_ws.get_all_records()
if update_worksheet:
	info_list = info_ws.get_all_records()
end2 = time.time()
#print("Time taken to get list of dicts from worksheet: %0.2fs" % (end2-end1))

# Print attendance by course
print_id_by_course(form_list, id_separator)

# Update worksheet
if update_worksheet:
	att_list = get_class_att_list(info_list, form_list)
	col_count = get_col_count_of(info_list)
	update_entire_col(info_ws,info_list,non_class_col_count,(col_count+1),att_list)
	end3 = time.time()
	#print("Time taken to update worksheet: %0.2fs" % (end3-end2))
	#print("Total time taken: %0.2fs" % (end3-start))












