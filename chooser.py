# Functions for generating rules -- XSLT and TC-XML

import datetime
from pandas import read_excel

TIME_STAMP = str(datetime.datetime.utcnow()) 
FILE_NAME = 'Rules-' + TIME_STAMP.replace(' ','T' ).split('.')[0] + '.xml' 
# FILE_NAME global creates unique file name to avoid appending to a existing file 
# when not intended.

def build_xslt(xpath, to_search, to_assign, otherwise_val):
    '''This function builds XSLT whens.'''
    with open(FILE_NAME, 'a') as data:
        data.write('''<xsl:when test=\"contains({},\'{}\')\"
                    >{}</xsl:when>'''.format(xpath, to_search, to_assign))
        data.write('<xsl:otherwise>{}</xsl:otherwise>'.format(otherwise_val))

def build_tc(to_search, to_assign):
    '''This function builds TC-XML transformations.'''
    with open(FILE_NAME, 'a') as data:
        data.write('''<Transformation type=\"ContainsText\">
                        <TextToSearchFor><![CDATA[{}]]></TextToSearchFor>
                        <TrueValue><![CDATA[{}]]</TrueValue>
                      </Transformation>'''.format(to_search, to_assign))

def clean_data():
    '''This function should replace [&] with [&amp;], and [or] with [|]'''
    pass

class ChooserData:
    
    def __init__(self, column_one, column_two):
        self.column_one = column_one
        self.column_two = column_two
        self.column_one_name = column_one_name
        self.column_two_name = column_two_name
        self.xlsx_file = xlsx_file
        
    def __str__(self):
        columns = str(self.column_one) + str(self.column_two)
        return columns
    
    def alloc_data(self, xlsx_file, column_one_name, column_two_name):
        '''Allocates columns into a zip object.'''
        data = read_excel(self.xlsx_file)
        column_one = data[self.column_one_name]
        column_two = data[self.column_two_name]
        return zip(self.column_one, self.column_two)
    
