class CompanyEmployee:
	def __init__(self, position, first_name, last_name, state, phone_number):
		self.position = position
		self.first_name = first_name
		self.last_name = last_name
		self.state = state
		self.phone_number = phone_number

	def __str__(self, type):
		if type.lower() == 'name':#FOR CLEAN OUTPUT
			return "{last}, {first} | {position} | {state} | {phone}".format(last=self.last_name, \
			 first=self.first_name, position=self.position, state=self.state, phone=self.phone_number)
		if type.lower() == 'title':#FOR CLEAN OUTPUT
			return "{position}| {last}, {first} | {state} | {phone}".format(last=self.last_name, \
				first=self.first_name, position=self.position, state=self.state, phone=self.phone_number)
		if type.lower() == 'state':#FOR CLEAN OUTPUT
			return "{state}| {position} | {last}, {first} | {phone}".format(last=self.last_name, \
				first=self.first_name, position=self.position, state=self.state, phone=self.phone_number)

class EmployeeNameIterator:
	def __init__(self, items):
		import operator
		items.sort(key = operator.attrgetter('last_name'))
		self.index_of_items = 0
		self.items = items

	def has_next(self):
		if self.index_of_items >= len(self.items):
			return False
		else:
			return True

	def next(self):
		item = self.items[self.index_of_items]
		self.index_of_items += 1
		return item

class EmployeePositionIterator:
	def __init__(self, items):
		import operator
		items.sort(key = operator.attrgetter('position'))
		self.items = items
		self.index_of_items = 0

	def has_next(self):
		if self.index_of_items >= len(self.items):
			return False
		else:
			return True

	def next(self):
		item = self.items[self.index_of_items]
		self.index_of_items += 1
		return item

class EmployeeStateIterator:
	def __init__(self, items):
		import operator
		items.sort(key = operator.attrgetter('state'))
		self.items = items
		self.index_of_items = 0

	def has_next(self):
		if self.index_of_items >= len(self.items):
			return False
		else:
			return True

	def next(self):
		item = self.items[self.index_of_items]
		self.index_of_items += 1
		return item

class AllEmployees:
	def __init__(self):
		self.items = []

	def add(self, item):
		self.items.append(item)

	def sort_by_last_names(self):
		return EmployeeNameIterator(self.items)

	def sort_by_job_title(self):
		return EmployeePositionIterator(self.items)

	def sort_by_state(self):
		return EmployeeStateIterator(self.items)

if __name__ == '__main__':
	all_employees = AllEmployees()
	emp1 = CompanyEmployee("Compliance","Yvette","Santiago","Georgia", '678-555-4325')
	emp2 = CompanyEmployee("Compliance","Jaime", "Vallgor","Texas", '408-555-5239')

	emp3 = CompanyEmployee("Regional","Becky","Lively","Georgia", '770-435-8891')
	emp4 = CompanyEmployee("Regional","Misty","Godbey","Texas", '281-727-3344')
	emp5 = CompanyEmployee("Regional","Juan","Vegas","Florida", '754-101-5561')

	emp6 = CompanyEmployee("IT","Scott","McCurdy","Georgia", '678-903-1212')
	emp7 = CompanyEmployee("IT","James","Little","Georgia", '678-231-8871')

	emp8 = CompanyEmployee("Owner","Sandra","Harold","Georgia", '770-333-4561')
	emp9 = CompanyEmployee("Owner","Robert","Harold","Georgia", '770-333-5562')

	all_employees.add(emp1)
	all_employees.add(emp2)
	all_employees.add(emp3)
	all_employees.add(emp4)
	all_employees.add(emp5)
	all_employees.add(emp6)
	all_employees.add(emp7)
	all_employees.add(emp8)
	all_employees.add(emp9)

	list_via_last_names = all_employees.sort_by_last_names()
	while list_via_last_names.has_next():
		person = list_via_last_names.next()
		print(person.__str__("name"))
		

	print('-'*20)

	list_via_job_title = all_employees.sort_by_job_title()
	while list_via_job_title.has_next():
		person = list_via_job_title.next()
		print(person.__str__("title"))

	print('-'*20)

	list_via_state = all_employees.sort_by_state()
	while list_via_state.has_next():
		person = list_via_state.next()
		print(person.__str__("state"))