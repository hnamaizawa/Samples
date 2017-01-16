print 'Purge Instance and Payload.\n'

username   = 'weblogic'
password   = 'welcome1'
url        = 't3://demo.jp.oracle.com:8001'
start_date = '01-01-2017 00:00:00:00'
end_date   = '31-12-2020 00:00:00:00'

connect(username,password,url)
purgeInstanceData(start_date, end_date, testMode='false', status='*', runPayloadPurge='TRUE')

exit ()

# test

# test
