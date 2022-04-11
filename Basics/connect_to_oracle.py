import cx_Oracle

dsn_tns = cx_Oracle.makedsn('PRDFSS-SCAN.OFFICE.CORP.INDOSAT.COM', '1521', service_name='OPFOSS') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user=r'TNM_MIGRATION', password='Indosat#2020', dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()
c.execute('''SELECT
   COUNT(TO_CHAR(MSISDN_NO)) AS HIGH
INTO 
    num1
FROM
    foss_msisdn_pool
WHERE
    pattern = val1
    AND price_category = 'HIGH'
    AND rownum <100;''') # use triple quotes if you want to spread your query across multiple lines
for row in c:
    print (row[0]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
#conn.close()