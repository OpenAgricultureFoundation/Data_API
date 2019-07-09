# http://flask.pocoo.org/docs/1.0/testing/

from global_vars import global_vars # global vars used in tests
import common


#------------------------------------------------------------------------------
# test submit_recipe_change blueprint
def test_submit_recipe_change_works(client):
    data = {"user_token": global_vars.user_token,
            "device_uuid": global_vars.device_uuid}
    URL = '/api/submit_recipe_change/'
    rv = common.do_post(client, data, URL)
    assert 200 == rv['response_code']

def test_submit_recipe_change_fails(client):
    data = {} # no data so it should fail
    URL = '/api/submit_recipe_change/'
    rv = common.do_post(client, data, URL)
    assert 500 == rv['response_code']
