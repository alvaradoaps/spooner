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

def alloc_data(xlsx_file, column_one_name, column_two_name):
    '''Allocates columns into a zip object.'''
    data = read_excel(xlsx_file)
    column_one = data[column_one_name]
    column_two = data[column_two_name]
    return zip(column_one, column_two)

def clean_data():
    '''This function should replace [&] with [&amp;], and [or] with [|]'''
    pass

class ChooserData:
    
    def __init__(self):
        self.printed_form = printed_form
        
    def __str__(self):
        return str(self.__str__)
