

def get_auth():
    from ordermanage.AdminLogin import AdminLogin
    login_api_obj = AdminLogin().send_request()
    return_data = login_api_obj.resp.data
    print(return_data)
    return return_data.tokenHead + ' ' + return_data.token


auth_token = get_auth()
#print(auth_token)