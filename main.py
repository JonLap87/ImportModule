from datetime import datetime, date, time
from apllication.salary import calculate_salary
from apllication.db.people import get_employees

if __name__ == '__main__':
	
	print (calculate_salary())
	print (get_employees())
	print (datetime.now())
