# Functions for generating rules -- XSLT and TC-XML

import datetime
from pandas import read_excel

TIME_STAMP = str(datetime.datetime.utcnow())
FILE_NAME = 'Rules-' + TIME_STAMP.replace(' ','T' ).split('.')[0] + '.xml' 

def build_xslt(xpath, to_search, to_assign, otherwise_val):
   with open(FILE_NAME, 'a') as data:
        data.write('''<xsl:when test=\"contains({},\'{}\')\"
                    >{}</xsl:when>'''.format(xpath, to_search, to_assign))
        data.write('<xsl:otherwise>{}</xsl:otherwise>'.format(otherwise_val))

def build_tc(to_search, to_assign):
    with open(FILE_NAME, 'a') as data:
        data.write('''<Transformation type=\"ContainsText\">
                        <TextToSearchFor><![CDATA[{}]]></TextToSearchFor>
                        <TrueValue><![CDATA[{}]]</TrueValue>
                      </Transformation>'''.format(to_search, to_assign))

def alloc_data(xlsx_file, column_one_name, column_two_name):
   data = read_excel(xlsx_file)
   column_one = data[column_one_name]
   column_two = data[column_two_name]
   return zip(column_one, column_two)
