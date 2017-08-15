from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):

	assert status in resp.status, "expected respinse %r not in %r " %( status, resp.status)
	
	if status == '200':
		assert resp.data, "response data is empty"
		
	if contains:
		assert contains in resp.data, "Response does not contain %r" % contains
	
	if matches:
		reg = re.compile(matches)
		assert reg.matches(resp.data), "response does not match %r" % match 
		
	if headers:
		assert_equal(resp.headers,headers)
	