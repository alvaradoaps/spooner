# This script generates XML feed from Clayton Homes csv files

from pandas import read_csv
import datetime
import sys
import time
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
import termcolor
import pyfiglet

def ascii_lolz():
	termcolor.cprint(pyfiglet.figlet_format('APS NICA', font='starwars'),
       'blue', attrs=['bold'])

TIME_STAMP = str(datetime.datetime.utcnow()) 
FILE_NAME = 'Rules_' + TIME_STAMP.replace(' ','T').replace(':','_').replace('.','_') + '.xml'
# FILE_NAME global creates unique file name to avoid appending to an existing file 
# when not intended.

def alloc_data(raw_data):
	data = read_csv(raw_data, keep_default_na=False)

	# Allocating columns in lists. 
	reqDivision = data['Requisition Division']
	reqId = data['Requisition ID']
	reqLocation = data['Requisition Location']
	category = data['Job Category']
	reqPosition = data['Requisition Position']
	jobTitle = data['Requisition Display Job Title']
	reqAddress1 = data['Requisition Address 1']
	reqAddress2 = data['Requisition Address 2']
	locationCity = data['Requisition City']
	locationState = data['Requisition State/Province']
	locationZipCode = data['Requisition Postal Code']
	reqPrimOwnerName = data['Requisition Primary Owner - Name']
	reqEmployeeType = data['Requisition Full/Part Time']

	# Zipping all lists into iterable.
	return zip(reqDivision, reqId, reqLocation, category,
			   reqPosition, jobTitle, reqAddress1, reqAddress2,
			   locationCity, locationState, locationZipCode,
			   reqPrimOwnerName, reqEmployeeType)

def build_file(file_name):
	# pass
	mappedData = alloc_data(file_name)
	with open(FILE_NAME, 'a') as feed:
		feed.write('<Jobs>')
	for a, b, c, d, e, f, g, h, i, j, k, l, m in mappedData:
		with open(FILE_NAME, 'a') as feed:
			feed.write('''<Job>
				<RequisitionDivision>{}</RequisitionDivision>
				<RequisitionID>{}</RequisitionID>
				<RequisitionLocation>{}</RequisitionLocation>
				<JobCategory>{}</JobCategory>
				<RequisitionPosition>{}</RequisitionPosition>
				<RequisitionDisplayJobTitle>{}</RequisitionDisplayJobTitle>
				<RequisitionAddress1>{}</RequisitionAddress1>
				<RequisitionAddress2>{}</RequisitionAddress2>
				<RequisitionCity>{}</RequisitionCity>
				<RequisitionState>{}</RequisitionState>
				<RequisitionPostalCode>{}</RequisitionPostalCode>
				<RequisitionPrimaryOwnerFullName>{}</RequisitionPrimaryOwnerFullName>
				<RequisitionFullPartTime>{}</RequisitionFullPartTime>
				<JobURL>https://claytonhomes.csod.com/ats/careersite/JobDetails.aspx?id={}</JobURL>
				</Job>\n'''.format(a, b, c, d, e, f, g, h, i, j, k, l, m, b.split('req')[1]))
	with open(FILE_NAME, 'a') as feed:
		feed.write('</Jobs>')

def main():
	ascii_lolz()
	print('''\nThis script needs to execute from the folder where the\nfile to process is in.''')
	print('''\nIf you try to do it your way I\'m not going to help... At all.''')
	file_name = input('\nEnter file name: ')
	try:
		build_file(file_name)
		print('\nClayton XML has been created at your current directory/folder!')
		time.sleep(10)
	except FileNotFoundError:
		print('\nPlease check the file name. Bye Bye!')
		time.sleep(10)

if __name__ == '__main__':
	main()
