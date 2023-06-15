import requests
import json
import pandas as pd
from dateutil import parser
####################################################################################################################################
##########################################################-Start Create D365 Token-#################################################
####################################################################################################################################
def token():
    crmorg = 'https://proactive.api.crm8.dynamics.com/'
    clientid = '0189ebfc-8de5-41fe-ba4d-205eca9fe4ca'
    username = 'pro.developer@proactive.co.in'
    userpassword = 'Proact@123'
    secret = 'rYQ8Q~0FEz62y3E.TdvU_KIaJiFmWUOw5EAmvbNX'
    tokenendpoint = 'https://login.microsoftonline.com/a1492249-245b-4a8b-a6e4-ce2d20b36653/oauth2/token' #oauth token endpoint
    #build the authorization token request
    tokenpost = {
        'client_id':clientid,
        'client_secret':secret,
        'resource':crmorg,
        'username':username,
        'password':userpassword,
        'grant_type':'password'
    }
    #make the token request
    tokenresponse = requests.get(tokenendpoint, data=tokenpost)
    tokendatas = tokenresponse.json()
    AccessToken = tokendatas['access_token']
    # print(AccessToken)
    return AccessToken
##################################################################################################################################
##########################################################-End Create D365 Token-#################################################
##################################################################################################################################

##################################################################################################################################
####################################################-Start Create Zoho CRM Token-#################################################
##################################################################################################################################
def zohotoken(test=''):
    url = "https://accounts.zoho.com/oauth/v2/token?refresh_token=1000.fad2a3cd841e1da8ff70aa41a6249038.16dfb0c536cdaa83eb88a0be976246b3&client_id=1000.HN6YI3N0SY7TFO8LOF7O574W701CSE&client_secret=2ebab1f959b7d304455d39d7bc62eb5127d5d75725&grant_type=refresh_token"
    payload = {}
    headers = {}
    # response = requests.request("POST", url, headers=headers, data = payload)
    # token = json.loads(response.text)
    # print(token)
    # return JsonResponse(token)
    tokenresponse = requests.post(url, data=headers)
    tokendatas = tokenresponse.json()
    # print(tokendatas['access_token'])
    # AccessToken = tokendatas['access_token']
    return tokendatas['access_token']
##################################################################################################################################
####################################################-End Create Zoho CRM Token-###################################################
##################################################################################################################################

##################################################################################################################################
###################################################-Start Create Zoho Desk Token-#################################################
##################################################################################################################################
def zohodesktoken(test=''):
    url = "https://accounts.zoho.com/oauth/v2/token?refresh_token=1000.08d3cd6a1018307b6ff7d3743c09ee8c.1b59da2332c836a08e9511a896ff3c9c&client_id=1000.HN6YI3N0SY7TFO8LOF7O574W701CSE&client_secret=2ebab1f959b7d304455d39d7bc62eb5127d5d75725&grant_type=refresh_token"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data = payload)
    token = json.loads(response.text)
    # print(token['access_token'])
    return token['access_token']
    # return JsonResponse(token)
##################################################################################################################################
####################################################-End Create Zoho CRM Token-###################################################
##################################################################################################################################

##################################################################################################################################
###################################################-Start Create Zoho Desk Search Token-#################################################
##################################################################################################################################
def zohodeskSearchtoken(test=''):
    url = "https://accounts.zoho.com/oauth/v2/token?refresh_token=1000.727b6108266a9e4853e7db3cb03da315.9bd693b9ef71336545f567494191ae69&client_id=1000.XLUX2G854HEVITG926DHT8LHH76G4H&client_secret=f743c69558faf7d852d8e99651b170862268287f51&grant_type=refresh_token"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data = payload)
    token = json.loads(response.text)
    # print(token['access_token'])
    return token['access_token']
    # return JsonResponse(token)
##################################################################################################################################
####################################################-End Create Zoho CRM Token-###################################################
##################################################################################################################################

##################################################################################################################################
####################################################-Start Get Tickets from D365-###################################################
##################################################################################################################################

def incidents(id):
    auth_token=token()
    url = "https://proactive.api.crm8.dynamics.com/api/data/v8.1/incidents"
    # url = "https://proactive.api.crm8.dynamics.com/api/data/v8.1/incidents(75e4406c-5505-401f-ac96-ffa0a5983b27)"
    response = requests.get(url, headers={"Authorization": "Bearer %s" %auth_token}, verify=True)
    j = response.json()
    # print(j)
    # return JsonResponse(j)
    return j
##################################################################################################################################
####################################################-End Get Tickets from D365-###################################################
##################################################################################################################################


##################################################################################################################################
###############################################-Start Get Account Data From D365-#################################################
##################################################################################################################################
def accounts(id):
    auth_token=token()
    url = "https://proactive.api.crm8.dynamics.com/api/data/v8.1/accounts"
    response = requests.get(url, headers={"Authorization": "Bearer %s" %auth_token}, verify=True)
    j = response.json()
    return j
##################################################################################################################################
#################################################-End Get Account Data From D365-#################################################
##################################################################################################################################

##################################################################################################################################
###############################################-Start Get Account Data From D365-#################################################
##################################################################################################################################
def TicketOwner(id):
    auth_token=token()
    if(id != ''):
        url = f"https://proactive.api.crm8.dynamics.com/api/data/v8.1/systemusers({id})"
    else:
        url = "https://proactive.api.crm8.dynamics.com/api/data/v8.1/systemusers"
    response = requests.get(url, headers={"Authorization": "Bearer %s" %auth_token}, verify=True)
    j = response.json()
    # print(j)
    return j
##################################################################################################################################
#################################################-End Get Account Data From D365-#################################################
##################################################################################################################################


##################################################################################################################################
###############################################-Start Get Account Data By ID From D365-#################################################
##################################################################################################################################
def accountsByID(id,accessToken):
    payload = json.dumps({})
    headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}
    url = f"https://desk.zoho.com/api/v1/accounts/search?customField1=cf_d365_account_id:{id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.status_code)
    if(response.status_code==200):
        data = json.loads(response.text)
        # print(data['data'][0]['id'] )
        return data['data'][0]['id']
    else:
        # print('434653000001059376' )
        return '434653000001059376'
##################################################################################################################################
#################################################-End Get Account Data By ID From D365-#################################################
##################################################################################################################################

##################################################################################################################################
###############################################-Start Get Contact Data From D365-#################################################
##################################################################################################################################
def contacts(id=False):
    auth_token=token()
    if(id != ''):
        url = f"https://proactive.api.crm8.dynamics.com/api/data/v8.1/contacts({id})"
    else:
        url = "https://proactive.api.crm8.dynamics.com/api/data/v8.1/contacts"
    response = requests.get(url, headers={"Authorization": "Bearer %s" %auth_token}, verify=True)
    j = response.json()
    # print(j)
    return j
##################################################################################################################################
#################################################-End Get Contact Data From D365-#################################################
##################################################################################################################################

##################################################################################################################################
###############################################-Start Get SNo. EntitalMent From D365-#################################################
##################################################################################################################################
def EntitalmentCheck(id=False):
    auth_token=token()
    if(id != ''):
        url = f"https://proactive.api.crm8.dynamics.com/api/data/v8.1/new_entitlementlineses({id})"
    response = requests.get(url, headers={"Authorization": "Bearer %s" %auth_token}, verify=True)
    j = response.json()
    print(j)
    return j
##################################################################################################################################
#################################################-End Get SNo. EntitalMent From D365-#################################################
##################################################################################################################################


##################################################################################################################################
###############################################-Start Get Contact Data By ID From D365-#################################################
##################################################################################################################################
def contactsByID(id,accessTokenSearch):
    payload = json.dumps({})
    headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessTokenSearch}'}
    url = f"https://desk.zoho.com/api/v1/contacts/search?customField1=cf_d365_contact_id:{id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    if(response.status_code==200):
        data = json.loads(response.text)
        # print(data['data'][0]['id'] )
        return data['data'][0]['id']
    else:
        return '434653000001749205'
##################################################################################################################################
#################################################-End Get Contact Data By ID From D365-#################################################
##################################################################################################################################

##################################################################################################################################
#########################################-Start Get D365 Contact Data By D365 Account-############################################
##################################################################################################################################
def ZOHOcontactsbyAccountID(Accountid):
    auth_token=token()
    if(id != ''):
        url = f"https://proactive.api.crm8.dynamics.com/api/data/v8.1/contacts?$filter=parentcustomerid_account/accountid eq {Accountid}"
    response = requests.get(url, headers={"Authorization": "Bearer %s" %auth_token}, verify=True)
    j = response.json()
    return j

##################################################################################################################################
###########################################-End Get D365 Contact Data By D365 Account-############################################
##################################################################################################################################

##################################################################################################################################
#########################################-Start Fetch notes By Incident D365 Account-############################################
##################################################################################################################################
def FetchnotesByIncident(Incidentid):
    auth_token=token()
    if(id != ''):
        url = f"https://proactive.api.crm8.dynamics.com/api/data/v8.1/annotations?$filter=_objectid_value eq {Incidentid}"
    response = requests.get(url, headers={"Authorization": "Bearer %s" %auth_token}, verify=True)
    j = response.json()
    # print(j)
    return j

##################################################################################################################################
###########################################-End Fetch notes By Incident  D365 Account-############################################
##################################################################################################################################

##################################################################################################################################
#########################################-Start Get Accounts Data From Zoho Crm-##################################################
##################################################################################################################################
def getAccountsZohoCrmAll(id):
    payload = json.dumps({})
    headers = {'Authorization': f'Zoho-oauthtoken {zohotoken()}'}

    totalAccounts = []
    for lp in range(50000):
        url = f"https://www.zohoapis.com/crm/v2.1/Accounts?page={lp}"

        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        for i in data['data']:
            totalAccounts.append(i)
        if(len(data['data'])!=200):
            break
        # print(lp)
        # print(len(data['data']))
    return totalAccounts
##################################################################################################################################
###########################################-End Get Accounts Data From Zoho Crm-##################################################
##################################################################################################################################

def getAccountsZohoDeskAll(id):
    accessToken = zohodesktoken()
    payload = json.dumps({})
    headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}

    totalAccounts = []
    for lp in range(50000):
        url = f"https://desk.zoho.com/api/v1/accounts?from={lp*100+1}&limit={100}"
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        for iData in data['data']:
            DetailedAccount = getsinglrAccountZohoDesk(iData['id'],accessToken)
            # print(DetailedAccount)
            totalAccounts.append(DetailedAccount)
        if(len(data['data'])!=100):
            break
        # print(lp)
        # print(len(data['data']))
    # print(totalAccounts)
    return totalAccounts

def getsinglrAccountZohoDesk(id,accessToken):
    payload = json.dumps({})
    headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}
    url = f"https://desk.zoho.com/api/v1/accounts/{id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    print('statuscode',response.status_code)
    if(response.status_code==200):
        return data
    # if data['errorCode'] == 'INVALID_OAUTH':

    # else:
    #     # getsinglrAccountZohoDesk(id,zohodeskSearchtoken())
    #     headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {zohodeskSearchtoken()}'}
    #     url = f"https://desk.zoho.com/api/v1/accounts/{id}"
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     data = json.loads(response.text)
    #     if(response.status_code==200):
    #         return data
    # print("++++++")
    # print(data)
    # return data



def getsinglrAccountZohoDeskbysearch(id,accessToken):
    payload = json.dumps({})
    headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}
    url = f"https://desk.zoho.com/api/v1/accounts/search?customField1=cf_erp_master_customer_id:{id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.status_code)
    if(response.status_code==200):
        data = json.loads(response.text)
        # print("++++++")
        # print(data)
        return data
    else:
        return ''


def getsinglrContactZohoDeskbysearch(id,accessToken):
    payload = json.dumps({})
    headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}
    url = f"https://desk.zoho.com/api/v1/contacts/search?email={id}"
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.status_code)
    if(response.status_code==200):
        data = json.loads(response.text)
        # print("++++++")
        # print(data)
        return data
    else:
        return ''


##############################################################################################################################
#########################################-Start get Contact ZohoDeskAll in Zoho Desk--########################################
##############################################################################################################################
def getContactZohoDeskAll(id):
    payload = json.dumps({})
    headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {zohodesktoken()}'}
    totalcontacts = []
    for lp in range(500):
        url = f"https://desk.zoho.com/api/v1/contacts?from={lp*100+1}&limit={100}"
        print(url)
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        for i in data['data']:
            totalcontacts.append(i)
        if(len(data['data'])!=100):
            break
        # print(lp)
        # # print(url)
        # print(len(data['data']))
    # print(len(totalcontacts))
    return totalcontacts
################################################################################################################################
#############################################-End get Contact ZohoDeskAll in Zoho Desk--########################################
################################################################################################################################


################################################################################################################################
#######################################################-Start Add Account in Zoho Desk--########################################
################################################################################################################################
def AddAccount(Ticketdata,oprtation,accessToken,ZohoTicketId=False):
    if oprtation=="Add":
        payload = json.dumps(
            {
                "accountName": Ticketdata["name"],
                "website": Ticketdata["websiteurl"],
                # "street": Ticketdata["address1_line1"],
                # "city": Ticketdata["address1_line2"],
                "phone": Ticketdata["telephone1"],
                "cf": {
                    "cf_erp_master_customer_id": Ticketdata["new_masternavisionid"],
                    "cf_d365_account_id": Ticketdata["accountid"],
                    "cf_erp_customer_name": Ticketdata["name"],
                    "cf_d365_account_remarks": "D365",
                    "cf_address_from_d365": f'{Ticketdata["address1_line1"]}  {Ticketdata["address1_line2"]}'
                },
            }
        )
        headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}
        url = f"https://desk.zoho.com/api/v1/accounts"
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        # print(f'Ticket inserted {data}')
        return data
    else:
        payload = json.dumps(
            {
                "cf": {
                    "cf_d365_account_id": Ticketdata["accountid"],
                },
            }
        )
        headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}
        url = f"https://desk.zoho.com/api/v1/accounts/{ZohoTicketId}"
        response = requests.request("PATCH", url, headers=headers, data=payload)
        data = json.loads(response.text)
        # print(f'Ticket Updated {data}')
        # print(url)
        # print(payload)
        return data
##############################################################################################################################
#######################################################-End Add Account in Zoho Desk--########################################
##############################################################################################################################


##############################################################################################################################
#######################################################-Start Add Contact in Zoho Desk--######################################
##############################################################################################################################
def AddContact(Contactdata,oprtation,accessToken,RealAccountId,ZohoTicketId=False):
    if oprtation=="Add":
        reallastname = f'{Contactdata["lastname"]}-pro'
        # lastnamedata = lastnamedata.strip()
        # # print()
        # if lastnamedata != '' or lastnamedata != None :
        #     reallastname = Contactdata["lastname"]
        # elif Contactdata["firstname"] != '' or Contactdata["firstname"] != None :
        #     reallastname = Contactdata["firstname"]
        # else:
        #     reallastname = "not found in D365"



        # el:
        #     realfirstname = ''
        #     reallastname = Contactdata["firstname"]
        payload = json.dumps(
            {
                "firstName": Contactdata["firstname"],
                "lastName": reallastname,
                "email": Contactdata["emailaddress1"],
                "mobile": Contactdata["mobilephone"],
                "accountId": RealAccountId,
                "cf": {
                    "cf_d365_contact_id": Contactdata["contactid"]
                }
            }
        )
        headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}
        url = f"https://desk.zoho.com/api/v1/contacts"
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        # print(f'contact inserted {data}')
        # print(url)
        # print(payload)
    else:
        payload = json.dumps(
            {
                "cf": {
                    "cf_d365_contact_id": Contactdata["contactid"],
                    "cf_d365_contact_remarks": "D365"
                },
            }
        )
        headers = {'orgid': '696443772','Authorization': f'Zoho-oauthtoken {accessToken}'}
        url = f"https://desk.zoho.com/api/v1/contacts/{ZohoTicketId}"
        response = requests.request("PATCH", url, headers=headers, data=payload)
        data = json.loads(response.text)
        # print(f'contact Updated {data}')
        # print(url)
        # print(payload)
##############################################################################################################################
#######################################################-End Add Contact in Zoho Desk--########################################
##############################################################################################################################

# AddContact('')

##############################################################################################################################
#################################-Start Migration Of Account and Ticket in Zoho Desk--########################################
##############################################################################################################################
def migratecn(id):
    # d365contact = contacts('')
    # zohodesktoken('')
    accessToken = zohodesktoken()
    d365Accounts = accounts(id)
    # zohoAccountsAll = getAccountsZohoCrmAll(id)
    zohoAccountsDeskAll = getAccountsZohoDeskAll(id)
    zohocontactAll = getContactZohoDeskAll(id)
    # print(d365Accounts)
    print('=====')
    # print(zohoAccountsAll)
    yescount = 0
    nocount = 0
    totalData = 0
    foundData = 0
    # print (zohoAccountsDeskAll)
    totalAccounts = []
    for i in d365Accounts['value']:
        Account_list_Face = list(filter(lambda tag: tag['Master_Customer_Id']==i['new_masternavisionid'], zohoAccountsDeskAll))
        # print(list_Face)
        RealAccountId = i['accountid']
        totalData = totalData + 1
        if RealAccountId:
            matchcontactdata = ZOHOcontactsbyAccountID(RealAccountId)

        if len(Account_list_Face)>0:
            yescount = yescount+1
#####################push cf_d365_account_id and cf_d365_account_remarks in account ####################################
            AddAccount(Account_list_Face,"update",accessToken,ZohoTicketId=False)
            if len(matchcontactdata['value'])>0:
                foundData = foundData + 1
                for s in matchcontactdata['value']:
                    Contact_list_Face = list(filter(lambda tag: tag['Master_Customer_Id']==i['new_masternavisionid'],zohocontactAll))
                    if len(Contact_list_Face)>0:
                        AddContact(s,'Update',accessToken,ZohoTicketId=False)
                    else:
                        AddContact(s,'Add',accessToken,matchcontactdata['id'])
            # else:
            #     matchcontactdata
                # AddContact(Contactdata,oprtation,accessToken,ZohoTicketId=False)




        else:
            nocount = nocount+1
            totalAccounts.append(i)
            # push full data  in account
            AddAccount(Account_list_Face,"Add",accessToken)











        # print("===")
        # print(totalData)
        # print(foundData)
        # print(matchcontactdata)
        # print("**********")

        # for k in matchcontactdata['value']:
        #     # update/create  contacts here
        #     i


    # print(yescount)
    # print(nocount)
    # print(totalAccounts)
##############################################################################################################################
#################################-End Migration Of Account and Ticket in Zoho Desk--##########################################
##############################################################################################################################


##############################################################################################################################
#################################-Start Run Function Here--###################################################################
##############################################################################################################################

# zohodesktoken('')

##############################################################################################################################
#################################-End Run Function Here--#####################################################################
##############################################################################################################################




# {
#     "accountName": "name",
#     "email": '',
#     "website": "websiteurl",


#     "street": "address1_line1",
#     "city": "address1_line2",
#     "phone": "telephone1",
#     "cf": {
#         "cf_erp_master_customer_id": "new_masternavisionid",
#         "cf_d365_account_id": "accountid",
#         "cf_erp_customer_name": "name",
#         "cf_d365_account_remarks": "D365"
#     },
# }



def migrateAccount(id=False):
    d365Accounts = accounts(id)
    accessTokenSearch = zohodeskSearchtoken()
    # print('=====')
    # print('=====')
    # print('=====')
    tokencount = 0
    yescount = 0
    nocount = 0
    totalData = 0
    foundData = 0


    cyescount = 0
    cnocount = 0
    # print (zohoAccountsDeskAll)
    totalAccounts = []
    for i in d365Accounts['value']:
        print(f"##############################-------------{tokencount}")
        tokencount = tokencount+1
        if tokencount>15:
            accessTokenSearch = zohodeskSearchtoken()
            tokencount = 0
        # print(i['new_masternavisionid'])
        if i['new_masternavisionid'] !='' :
            dataa = getsinglrAccountZohoDeskbysearch(i['new_masternavisionid'],accessTokenSearch)
            RealAccountId = i['accountid']
            # print(f"475dataa====={dataa['data'][0]['id']}")
            if(dataa=='' or dataa==None):
                #create account
                nocount = nocount + 1
                # print(f'{nocount} - Account Creating')

                ac=AddAccount(i,"Add",accessTokenSearch)
                # print(ac)
                if RealAccountId:
                    matchcontactdata = ZOHOcontactsbyAccountID(RealAccountId)
                    if len(matchcontactdata)>0:
                        for s in matchcontactdata['value']:
                            # print(f'---------contact - {s} ')
                            condata = getsinglrContactZohoDeskbysearch(s['emailaddress1'],accessTokenSearch)
                            if condata=='' or condata==None:
                                ########################
                                # s
                                # print(f'{cnocount} - Contact Creating')

                                cc = AddContact(s,'Add',accessTokenSearch,ac['id'])
                                # print(cc)
                            else:
                                cu = AddContact(s,'Update',accessTokenSearch,ac['id'],condata['data'][0]['id'])
                                # s
                                # print(f'{cyescount} - updating Account ')

                #create All Account
            else:
                # update account
                # print(f"dataa['id'] {dataa['data'][0]['id']}")
                au = AddAccount(i,"Update",accessTokenSearch,dataa['data'][0]['id'])

                yescount = yescount + 1
                # print(f'{yescount} - updating Account ')
                # print(au)
                totalData = totalData + 1
                if RealAccountId:
                    matchcontactdata = ZOHOcontactsbyAccountID(RealAccountId)
                    if len(matchcontactdata)>0:
                        for s in matchcontactdata['value']:
                            # print(f'---------contact - {s} ')
                            condata = getsinglrContactZohoDeskbysearch(s['emailaddress1'],accessTokenSearch)
                            if condata=='' or condata==None:
                                ########################
                                # s
                                # print(f'{cnocount} - Contact Creating')

                                cc = AddContact(s,'Add',accessTokenSearch,au['id'])
                                # print(cc)
                            else:
                                cu = AddContact(s,'Update',accessTokenSearch,au['id'],condata['data'][0]['id'])
                                # s
                                # print(f'{cyescount} - updating Account ')
                                # print(cu)





# migrateAccount('')

def advancedTechnology(i):
    value=''
    if  i == 100000000:
        value = 'Routing and Switching'
    elif i == 100000001:
        value = 'Wireless'
    elif i == 100000002:
        value = 'Security'
    elif i == 100000003:
        value = 'Storage'
    elif i == 100000004:
        value = 'UCS'
    elif i == 100000005:
        value = 'Collaboration'
    elif i == 100000006:
        value = 'TP and AV'
    elif i == 100000007:
        value = 'Cabling'
    elif i == 100000008:
        value = 'Services'
    elif i == 100000009:
        value = 'Other - 1'
    elif i == 100000010:
        value = 'Other - 2'
    else:
        value = i
    return value

def NBDCheck(i):
    value=''
    if  i == 100000000:
        value = 'NBD'
    elif i == 100000001:
        value = '4 Hours'
    elif i == 'null':
        value = 'null'
    else:
        value = i
    return value

def StatusCodeFilter(i):
    value=''
    # if  i == 100000016:
    #     value = "Open"
    # elif i == 100000000:
    #     value = "Logged"
    # elif i == 100000001:
    #     value = "Entitlement Confirmation"
    # elif i == 100000002:
    #     value = "Ticket Assignment"
    # elif i == 100000003:
    #     value = "Troubleshooting And Identification"
    # elif i == 100000004:
    #     value = "Send for Approval - PSS"
    # elif i == 100000005:
    #     value = "Approved - PSS"
    # elif i == 100000006:
    #     value = "Rejected - PSS"
    # elif i == 100000007:
    #     value = "RMA"
    # elif i == 100000011:
    #     value = "Replacement"
    # elif i == 100000012:
    #     value = "Recovery"
    # elif i == 100000013:
    #     value = "Resolved"
    # elif i == 100000014:
    #     value = "Feedback"
    # elif i == 100000015:
    #     value = "Closed"
    if i == 1000:
        value = "Resolved"
    elif i == 5:
        value = "Closed"
    else:
        value = i
    return value

def createdbyownerFilter(i):
    value=''
    if  i == "Chhitij@proactive.co.in":
        value = 434653000009937001
    elif i == "Rahul.tiwari@proactive.co.in":
        value = 434653000010593157
    elif i == "Dharmendra@proactive.co.in":
        value = 434653000010609426
    elif i == "Mukesh.Kumar@proactive.co.in":
        value = 434653000010740974
    elif i == "Mohit.Saini@proactive.co.in":
        value = 434653000010740002
    elif i == "Jagadisha@proactive.co.in":
        value = 434653000010740506
    elif i == "Vidhata@proactive.co.in":
        value = 434653000009737003
    elif i == "Ankit.Mathuria@proactive.co.in":
        value = 434653000003306001
    elif i == "Nikhil@proactive.co.in":
        value = 434653000010584023
    elif i == "Shrikant@proactive.co.in":
        value = 434653000010584059
    elif i == "ankit.varshney@proactive.co.in":
        value = 434653000010592047
    elif i == "Piyush.n@proactive.co.in":
        value = 434653000010582039
    elif i == "Vinay.r@proactive.co.in":
        value = 434653000010748005
    elif i == "Pankaj.chauhan@proactive.co.in":
        value = 434653000010599011
    elif i == "Manoj_kumar@proactive.co.in":
        value = 434653000010601045
    else:
        value = 434653000007549003
    return value

def Severity(i):
    value=''
    if  i == 100000000:
        value = 1
    elif i == 100000001:
        value = 2
    elif i == 100000002:
        value = 3
    elif i == 100000003:
        value = 4
    elif i == 100000004:
        value = 5
    elif i == 100000005:
        value = 6
    elif i == 100000006:
        value = 7
    elif i == 100000007:
        value = 8
    else:
        value = i
    return value

def SubCatFilter(i):
    value=''
    if  i == 100000000:
        value = "Cisco Hardware Issue"
    elif i == 100000001:
        value = "Cisco Configuration and Software Support Issue"
    elif i == 100000002:
        value = "ProCare Independent Issue (Items not backed-lined with OEM)"
    elif i == 100000003:
        value = "Non-Cisco Service Issue"
    elif i == 100000004:
        value = "LLW Replacement"
    elif i == 100000005:
        value = "Dead on Arrival (DOA) Replacement"
    elif i == 100000006:
        value = "Professional Services"
    else:
        value = i
    return value

def CaseOriginCodeFilter(i):
    value=''
    if  i == 1:
        value = "Phone"
    elif i == 2:
        value = "Email"
    elif i == 3:
        value = "Web"
    elif i == 2483:
        value = "Facebook"
    elif i == 3986:
        value = "Twitter"
    elif i == 700610000:
        value = "IoT"
    else:
        value = i
    return value

def checkkey(i,key):
    value=''
    # key in dic
    if  key in i:
        value = i[key]
    else:
        value = 'null'
    return value


def checkYON(i):
    value=''
    # key in dic
    if i == 100000001:
        value = "No"
    elif i == 100000000:
        value = "yes"
    else:
        value = i
    return value



def ConvDataTime(v):

    # new_date=parser.parse(data)
    print(v)
    if(v):
        data=parser.parse(v)
        return data.date().strftime('%Y-%m-%d')
    else:
        return "1970-01-01"
    # if ty == 'Time':
        # return
    # if ty == 'Date':
    #     return
    # if ty == 'DateTime':
    #     return
    # example:
    # new_date.year
    # new_date.month
    # new_date.day
    # new_date.hour
    # new_dare.minute



def migrateTickets(id):
    accessTokenSearch = zohodeskSearchtoken(id)
    tckt_365=incidents(id)
    # print(tckt_365)
    tokencount = 0
    tokencount1 = 0
    inserteddata = 0
    notinserteddata = 0
    for i in tckt_365['value']:
        D365AccountID = i['_customerid_value']
        D365contactID = i['_primarycontactid_value']
        print("-----")
        tokencount = tokencount+1
        tokencount1 = tokencount1+1
        if tokencount>50:
            accessTokenSearch = zohodeskSearchtoken(id)
            tokencount = 0
        print("total ticket",tokencount)
        print("total ticket count ",tokencount1)
        # if D365AccountID != '' :
        getaccountbyidDesk = accountsByID(D365AccountID,accessTokenSearch)
        # else:
        #     getaccountbyidDesk = "434653000001059376"
        # print("+++++")
        # if D365contactID != '' :
        getcontactsByidDesk = contactsByID(D365contactID,accessTokenSearch)
        getOwnerByidDesk = TicketOwner(checkkey(i,'_owninguser_value'))
        # print(getOwnerByidDesk)
        print('==========----===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-======-=-===-=----=---=-=-==')
        AccountDetailsforem = getsinglrAccountZohoDesk(getaccountbyidDesk,accessTokenSearch)
        print(AccountDetailsforem)
        print('mainid',i['incidentid'])
        print('==========----===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=-======-=-===-=----=---=-=-==')
        # print(getcontactsByidDesk)
        # print(getOwnerByidDesk['domainname'])
        # print(checkkey(i,'_ownerid_value'))
        # else:
        #     getcontactsByidDesk = "434653000001213699"
        # "description": f'{checkkey(i,"description")} <br/><br/>D365 Ticket Number:<b>{checkkey(i,"ticketnumber")}</b><br/><br/><a href="https://proactive.crm8.dynamics.com/main.aspx?app=d365default&forceUCI=1&pagetype=entityrecord&etn=incident&id={checkkey(i,"incidentid")}">D365 Case Link</a><br/><br/><a href="https://proactivedatasys.sharepoint.com/sites/ProactiveServiceDesk-D365Zoho/Shared%20Documents/Forms/AllItems.aspx?ga=1&id=%2Fsites%2FProactiveServiceDesk%2DD365Zoho%2FShared%20Documents%2FD365%20Service%20Desk%20%2D%20Incident%20Attachments%2F{checkkey(i,"ticketnumber")}">There might be more Attachment. For More Click Here</a>',#--s

        print("#######-------------------------")
        # converdata = checkkey(i,"description")+'<br/>'
        if checkkey(i,"description"):
            descdatass = checkkey(i,"description")
        else:
            descdatass =""
        getnotes = FetchnotesByIncident(checkkey(i,'incidentid'))
        list1=[]
        for j in getnotes['value']:
            if j['subject'] !=  None:
                print("kapil subject",j['subject'])
                # converdata=converdata+"Subject: "+j['subject']+"<br/>"
                list1.append(f"<br/><br/><b>Subject:</b>{j['subject']}<br/>")
            if j['notetext'] !=  None:
                print("kapil note",j['notetext'])
                list1.append(f"<b>-></b>{j['notetext']}<br/>")

                # converdata= converdata+"Note: "+j['notetext']+"<br/>"

        print("#######-------------------------")
        converdata='Ticket Real Owner : <b>'+getOwnerByidDesk['domainname']+'</b><br/><br/>'+'Created @ '+ checkkey(i,'createdon')+'<br/><br/>'+descdatass+'<br/>'.join(list1)+'<br/><br/>D365 Ticket Number:<b>'+checkkey(i,"ticketnumber")+'</b><br/><br/><a href="https://proactive.crm8.dynamics.com/main.aspx?app=d365default&forceUCI=1&pagetype=entityrecord&etn=incident&id='+checkkey(i,"incidentid")+'">D365 Case Link</a><br/><br/><a href="https://proactivedatasys.sharepoint.com/sites/ProactiveServiceDesk-D365Zoho/Shared%20Documents/Forms/AllItems.aspx?ga=1&id=%2Fsites%2FProactiveServiceDesk%2DD365Zoho%2FShared%20Documents%2FD365%20Service%20Desk%20%2D%20Incident%20Attachments%2F'+checkkey(i,"ticketnumber")+'">There might be more Attachment. For More Click Here</a>'#--s


        print("All Datas",converdata)
        # if(checkkey(i,'new_eligibleforciscovisit') == 100000001):
        #     EFCV = "No"
        # else:
        #     EFCV ="Yes"

        # print(getaccountbyidDesk)
        # print(getcontactsByidDesk)
        url = "https://desk.zoho.com/api/v1/tickets"
        # print(checkkey(i,''))
        cf_nbd_4_hours = checkkey(i,'new_nbd4hour')
        cfnew_eligibleforciscovisit = checkkey(i,'new_eligibleforciscovisit')
        cf_severity = checkkey(i,'severitycode')
        caseOrg = checkkey(i,"caseorigincode")
        statuscod = checkkey(i,'statuscode')
        cf_advanced_technology = checkkey(i,'new_advancetechnology')
        # print('new_advancetechnology',checkkey(i,'new_advancetechnology'))
        print("nodataaaaa",StatusCodeFilter(statuscod))

        if checkkey(i,'new_majorminor')== 10000001 :
            majorminorfilter = "Major"
        else:
             majorminorfilter =  "Minor"
        if checkkey(i,'_new_serialnoreported_value') != None:
            EntatialmentCheckdata = EntitalmentCheck(checkkey(i,'_new_serialnoreported_value'))

        if checkkey(i,'_new_serialnoreported_value') != None:
            cf_d365_serial_number = EntatialmentCheckdata['new_name']	                                                  #Serial Number
            cf_start_date = ConvDataTime(EntatialmentCheckdata['new_ciscocontractstartdate'])	                                  #Start Date	Parse Dates
            cf_end_date = ConvDataTime(EntatialmentCheckdata['new_ciscocontractenddate'])	                                   #End Date	Parse Dates
            cf_major_minor = EntatialmentCheckdata['new_sntype']	                                                     #Major/ Minor	10000001 – Major else Minor
            cf_parent_chassis_serial_number = EntatialmentCheckdata['new_parentserialno']                                              	#Parent Serial Number
            cf_part_number = EntatialmentCheckdata['new_partnumber']                                                  #	Part Number
            cf_service_part_code = EntatialmentCheckdata['new_servicepartcode']                                      #	New Service Part Code
        else :
            cf_d365_serial_number = "null"	                                                  #Serial Number
            cf_start_date = "1970-01-01"	                                  #Start Date	Parse Dates
            cf_end_date = "1970-01-01"	                                   #End Date	Parse Dates
            cf_major_minor = "null"	                                                     #Major/ Minor	10000001 – Major else Minor
            cf_parent_chassis_serial_number = "null"                                              	#Parent Serial Number
            cf_part_number = "null"                                                  #	Part Number
            cf_service_part_code = "null"
        new_feedback1 = ""
        if checkkey(i,'new_feedback')==100000000 :
            new_feedback1 = "Positive"
        if checkkey(i,'new_feedback')==100000001 :
            new_feedback1 = "Negative"
        if checkkey(i,'new_feedback')==100000002 :
            new_feedback1 = "Neutral"
        new_ordertype1 = ""
        if checkkey(i,'new_ordertype')==100000000 :
            new_ordertype1 = "Attach"
        if checkkey(i,'new_ordertype')==100000001 :
            new_ordertype1 = "Renewal"
        new_orientationprocess1 = ""
        if checkkey(i,'new_orientationprocess')==100000000 :
            new_orientationprocess1 = "Onsite"
        if checkkey(i,'new_orientationprocess')==100000001 :
            new_orientationprocess1 = "Webex"
        if checkkey(i,'new_orientationprocess')==100000002 :
            new_orientationprocess1 = "Telephonic"

        cffpepd = checkkey(i,'new_pickupdate')
        checkciscoco = checkkey(i,'new_ciscormacasecreatedon')
        if checkkey(i,'statuscode') != 1:
            payload = json.dumps({
            "entitySkills": [],
            "accountId": getaccountbyidDesk,     # "accountId": "434653000001059376",
            "departmentId": "434653000000006907",
            "contactId": getcontactsByidDesk,   # "contactId": "434653000001213699",
            "subject":  checkkey(i,'title'), # "subject": "subjectid",--S
            # "statusType": StatusCodeFilter(statuscod),
            # "statusType": "Open",

            "cf": {
                "cf_d365_ticket_status": StatusCodeFilter(statuscod),
                "cf_severity": Severity(cf_severity),
                "cf_entitlement_confirmation": checkkey(i,'new_entitlementconfirmation'),
                "cf_oem_name": checkkey(i,'new_oem'),
                "cf_status_reason": checkkey(i,'statuscode'),
                "cf_cisco_contract_number": checkkey(i,'new_ciscocontractnumber'),
                "cf_service_level": checkkey(i,'servicestage'),
                "cf_applicable_contract": checkkey(i,'new_entitlementtemplid'),
                "cf_nbd_4_hours": NBDCheck(cf_nbd_4_hours),
                "cf_publish_to_we": checkkey(i,'adx_publishtoweb'),
                "cf_failed_part_number": checkkey(i,'new_failedpartno'),
                "cf_eligible_for_cisco_visit": checkYON(cfnew_eligibleforciscovisit),
                "cf_serial_number_covered": checkYON(checkkey(i,'new_serialnocovered')),
                "cf_route_case": checkkey(i,'routecase'),
                "cf_process_id": checkkey(i,'processid'),
                "cf_service_type": checkkey(i,'new_servicetype'),
                "cf_advanced_technology": advancedTechnology(cf_advanced_technology),
                "cf_customer_contacted": checkkey(i,'customercontacted'),
                "cf_major_minor": majorminorfilter,
                "cf_incident_sub_type": checkkey(i,'new_incidentsubtype'),
                "cf_case_created_post_1_30_pm": checkYON(checkkey(i,'new_casecreatedpost130')),
                "cf_date_of_delivery": checkkey(i,'new_dateofdelivery'),
                "cf_expected_ship_date_from_cisco_to_client_location": checkkey(i,'new_eta'),
                "cf_parent_case": checkkey(i,'parentcaseid'),
                "cf_parent_chassis_serial_number": checkkey(i,'new_failedchassisserialno'),
                "cf_expected_date_of_return": checkkey(i,'new_expecteddateofreturn'),
                "cf_approval_pss": checkkey(i,'new_approvalpss'),
                "cf_replaced_part_number": checkkey(i,'new_replacedpartno'),
                "cf_delivery_challan_signed_by": checkkey(i,'new_deliverychallansignedby'),
                "cf_date_of_receipt": checkkey(i,'new_dateofreceipt'),
                "cf_replaced_serial_number": checkkey(i,'new_replacedserialno'),
                "cf_faulty_part_actual_pickup_date": checkkey(i,'new_actualpickupdateandtime'),
                "cf_next_action": checkkey(i,'new_nextaction'),
                "cf_failed_part_classification": checkkey(i,'new_failedpartclassification'),
                "cf_onsite_visit_by": checkkey(i,'new_onsitevisitby'),
                "cf_leave_part_with_security": checkkey(i,'new_leavepartwithsecurity'),
                "cf_pro_care_contract_number": checkkey(i,'new_procarecontractno'),
                "cf_assignment_completed_on": checkkey(i,'new_assignmentdatetime'),
                "cf_entitlement_confirmation_completed_on": checkkey(i,'new_entitlementdatetime'),
                "cf_replacement_completed_on": checkkey(i,'new_replacementdatetime'),
                "cf_recovery_completed_on": checkkey(i,'new_recoverydatetime'),
                "cf_proactive_branch_location": checkkey(i,'new_branchlocation'),
                "cf_client_branch_location": checkkey(i,'new_clientbranchlocation'),
                "cf_cisco_sr_created_on": ConvDataTime(checkciscoco),
                "cf_serial_number_found_on_cisco_website": checkkey(i,'new_snofoundonciscowebsite'),
                "cf_l2_sme": checkkey(i,'new_l2sme'),
                "cf_part_created_flag": checkkey(i,'new_partcreatedflag'),
                "cf_recovery": checkkey(i,'new_recovery'),
                "cf_rma_completed_on": checkkey(i,'new_rmadatetime'),
                "cf_proactive_provided_time_engineer_report_on_site": checkkey(i,'new_engineerreportedonsite'),
                "cf_orientation_process": new_orientationprocess1,
                "cf_review_date": checkkey(i,'new_reviewdate'),
                "cf_delivery_engineer": checkkey(i,'new_deliveryengineer'),
                "cf_collection_date": checkkey(i,'new_collectiondate'),
                "cf_so_number_of_nav": checkkey(i,'new_sonoofnav'),
                "cf_e_way_number": checkkey(i,'new_ewaynumber'),
                "cf_failed_serial_number_found_in_db": checkkey(i,'new_serialnoreported'),
                "cf_professional_service_type": checkkey(i,'new_professionalservicetype'),
                "cf_rma_start_time_troubleshooting_ended_post_2_30": checkkey(i,'new_troubleshootingstarttime'),
                "cf_resolved_on": checkkey(i,'new_resolvedon'),
                "cf_feedback": new_feedback1,
                "cf_raise_case_on_cisco": checkkey(i,'new_raisecaseoncisco'),
                "cf_returnable_part_number": checkkey(i,'new_returnablepartno'),
                "cf_cisco_service_request_number": checkkey(i,'new_ciscoservicerequestno'),
                "cf_cisco_rma_number": checkkey(i,'new_ciscormanumber'),
                "cf_rental_foc": checkkey(i,'new_rentalfoc'),
                "cf_cisco_actual_ship_date": checkkey(i,'new_actualshipdatetime'),
                "cf_ship_to_address_details": checkkey(i,'new_shiptoaddressdetails'),
                "cf_failed_serial_number_not_found_in_db": checkkey(i,'new_snonotfoundindb'),
                "cf_part_working_condition": checkkey(i,'new_partworkingcondition'),
                "cf_order_type": new_ordertype1,
                "cf_child_cases": checkkey(i,'numberofchildincidents'),
                "cf_replacement_from": checkkey(i,'new_replacementfrom'),
                "cf_picked_serial_number": checkkey(i,'new_pickedserialnumber'),
                "cf_replacement": checkkey(i,'new_replacement'),
                "cf_delivery_challan_number": checkkey(i,'new_deliverychallannumber'),
                "cf_steps_to_reproduce": checkkey(i,'adx_stepstoreproduce'),
                "cf_cisco_rma_date_part_arrived_at_client_location": checkkey(i,'new_ciscormadate'),
                "cf_resolution_date": checkkey(i,'adx_resolutiondate'),
                "cf_proactive_spare_as_standby": checkkey(i,'new_proactivespareasstandby'),
                "cf_orientation_date": checkkey(i,'new_orientationdate'),
                "cf_collection_process": checkkey(i,'new_collectionprocess'),
                "cf_reason_for_raising_case_on_cisco": checkkey(i,'new_reasonforraisingcaseoncisco'),
                "cf_faulty_part_expected_pickup_date": ConvDataTime(cffpepd),
                "cf_delivery_contact": checkkey(i,'new_deliverycontact'), #--s
                "cf_publish_to_web": checkkey(i,"adx_publishtoweb"), #--s
                "cf_d365_ticket_id": checkkey(i,"ticketnumber"),
                "cf_proactive_ticket_number": checkkey(i,"ticketnumber"),
                # New Time Fields Added By rajeev Sir
                "cf_entitlement_date_time" : checkkey(i,"new_entitlementdatetime"),
                "cf_assignment_date_time" : checkkey(i,"new_assignmentdatetime"),
                "cf_troubleshooting_date_time" : checkkey(i,"new_troubleshootingdatetime"),
                "cf_troubleshooting_start_time" : checkkey(i,"new_troubleshootingstarttime"),
                "cf_cisco_rma_case_created_on" : checkkey(i,"new_ciscormacasecreatedon"),
                "cf_engineer_reported_onsite" : checkkey(i,"new_engineerreportedonsite"),
                "cf_eta" : checkkey(i,"new_eta"),
                "cf_replacement_date_time" : checkkey(i,"new_replacementdatetime"),
                "cf_actual_pickup_date_and_time" : checkkey(i,"new_actualpickupdateandtime"),
                "cf_cisco_rma_date" : checkkey(i,"new_ciscormadate"),
                "cf_recovery_date_time" : checkkey(i,"new_recoverydatetime"),
                "cf_rma_date_time" : checkkey(i,"new_rmadatetime"),
                "cf_actual_ship_date_time" : checkkey(i,"new_actualshipdatetime"),
                "cf_pick_up_date" : checkkey(i,"new_pickupdate"),
                "cf_resolved_on_1" : checkkey(i,"new_resolvedon"),
                "cf_orientation_date" : checkkey(i,"new_orientationdate"),
                "cf_date_of_delivery_1" : checkkey(i,"new_dateofdelivery"),
                "cf_expected_date_of_return_1" : checkkey(i,"new_expecteddateofreturn"),
                "cf_resolution_date_1" : checkkey(i,"adx_resolutiondate"),
                "cf_date_of_receipt_1" : checkkey(i,"new_dateofreceipt"),
                "cf_review_date" : checkkey(i,"new_reviewdate"),
                "cf_collection_date_1" : checkkey(i,"new_collectiondate"),
                "cf_d365_serial_number" : cf_d365_serial_number,	                                                  #Serial Number
                "cf_start_date" : cf_start_date,
                "cf_end_date" : cf_end_date,
                "cf_major_minor":cf_major_minor,
                "cf_parent_chassis_serial_number":cf_parent_chassis_serial_number,
                "cf_part_number":cf_part_number,
                "cf_service_part_code":cf_service_part_code,
                # "cf_d365_attachment_url": f'https://proactivedatasys.sharepoint.com/sites/ProactiveServiceDesk-D365Zoho/Shared%20Documents/Forms/AllItems.aspx?ga=1&id=%2Fsites%2FProactiveServiceDesk%2DD365Zoho%2FShared%20Documents%2FD365%20Service%20Desk%20%2D%20Incident%20Attachments%2F{checkkey(i,"ticketnumber")}'
            },

            "email": AccountDetailsforem['email'],
            "phone": AccountDetailsforem['phone'],
            "category": "Incident",
            "channel": CaseOriginCodeFilter(caseOrg),
            "modifiedTime": checkkey(i,"modifiedon"), #--s
            "assigneeId": createdbyownerFilter(getOwnerByidDesk['domainname']),
            "priority": checkkey(i,"prioritycode"), #--S
            "status": checkkey(i,"statecode"), #--s
            "description":converdata,
            "subCategory": SubCatFilter(checkkey(i,"new_incidentsubtype"))
            # "email": "gaurav.singh@proactive.co.in",
            # "phone": "9891263618",
            # "slaId":  checkkey(i,"slaid"),#--s
            # "assigneeId": '434653000002217001',
            # "assigneeId": '434653000001213699',#--s   System Generated Field
            # "createdBy": '434653000001213699',#--s   System Generated Field
            # "assigneeId": getOwnerByidDesk['domainname'],#--s   System Generated Field
            # "createdBy": getOwnerByidDesk['domainname'],#--s   System Generated Field
            # "createdTime": checkkey(i,"createdon"), #--s
            # "ticketNumber": checkkey(i,"ticketnumber"),#--s   System Generated Field
            # "description": f'{checkkey(i,"description")} <br/><br/>D365 Ticket Number:<b>{checkkey(i,"ticketnumber")}</b><br/><br/><a href="https://proactive.crm8.dynamics.com/main.aspx?app=d365default&forceUCI=1&pagetype=entityrecord&etn=incident&id={checkkey(i,"incidentid")}">D365 Case Link</a><br/><br/><a href="https://proactivedatasys.sharepoint.com/sites/ProactiveServiceDesk-D365Zoho/Shared%20Documents/Forms/AllItems.aspx?ga=1&id=%2Fsites%2FProactiveServiceDesk%2DD365Zoho%2FShared%20Documents%2FD365%20Service%20Desk%20%2D%20Incident%20Attachments%2F{checkkey(i,"ticketnumber")}">There might be more Attachment. For More Click Here</a>',#--s
            # "modifiedBy": checkkey(i,"modifiedby"),#--s    System Generated Field
            # "dueDate": "2022-12-15T15:10:04.000Z",
            # "onholdTime": null,
            # "language": null,
            # "source": {
            #     "appName": null,
            #     "extId": null,
            #     "permalink": null,
            #     "type": "SYSTEM",
            #     "appPhotoURL": null
            # },
            # "resolution": "Done",
            # "sharedDepartments": [],
            # "closedTime": "2022-12-14T09:13:30.000Z",
            # "approvalCount": "0",
            # "isOverDue": false,
            # "isTrashed": false,
            # "contact": {
            #     "firstName": "Gaurav",
            #     "lastName": "Singh",
            #     "phone": "9891263618",
            #     "mobile": "9891263618",
            #     "id": "434653000001213699",
            #     "isSpam": false,
            #     "type": null,
            #     "email": "gaurav.singh@proactive.co.in",
            #     "account": {
            #     "website": null,
            #     "accountName": "Proactive Data Systems Pvt. Ltd.",
            #     "id": "434653000001059376"
            #     }
            # },
            # "id": "434653000005451282",
            # "isResponseOverdue": true,
            # "customerResponseTime": "2022-12-14T09:10:04.000Z",
            # "productId": null,
            # "threadCount": "0",
            # "secondaryContacts": [],
            # "entitySkills": [],
            # "sentiment": null,
            # "isArchived": false,
            # "isDeleted": false,
            # "timeEntryCount": "10",
            # "channelRelatedInfo": null,
            # "responseDueDate": "2022-12-14T09:15:04.000Z",
            # "classification": "Problem",
            # "commentCount": "0",
            # "taskCount": "0",
            # "webUrl": "https://desk.zoho.com/support/proactivedata/ShowHomePage.do#Cases/dv/434653000005451282",
            # "assignee": {
            #     "photoURL": "https://desk.zoho.com/api/v1/agents/434653000002217001/photo?orgId=696443772",
            #     "firstName": "Gaurav",
            #     "lastName": "Singh",
            #     "id": "434653000002217001",
            #     "email": "gaurav.singh@proactive.co.in"
            # },
            # "isSpam": false,
            # "department": {
            #     "name": "Proactive Data Systems",
            #     "id": "434653000000006907"
            # },
            # "followerCount": "0",
            # "layoutDetails": {
            #     "id": "434653000000074011",
            #     "layoutName": "ProCare Service Desk"
            # },
            # "channelCode": null,
            # "product": null,
            # "isFollowing": false,
            })
            print("payload",payload)
            headers = {
            'orgid': '696443772',
            'Authorization': f'Zoho-oauthtoken {accessTokenSearch}',
            'Content-Type': 'application/json',
            'Cookie': '34f6831605=743533c533455c544b234e9a7cd3c68f; 9a26c99460=0747eb1055f94859f4b4316805fcae9d; JSESSIONID=07A49E4EEBDCCD5D065901CC11528687; _zcsr_tmp=e43c2c91-4ee6-44ec-9716-08cba49a2c7d; crmcsr=e43c2c91-4ee6-44ec-9716-08cba49a2c7d'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            # print(response.text)
            print(response.status_code)
            if response.status_code == 200:
                inserteddata = inserteddata + 1
            else:
                notinserteddata = notinserteddata +1
            print("inserteddata",inserteddata)
            print("notinserteddata",notinserteddata)
            # print(accessTokenSearch)
            # print(payload)

# 9140306107 sahil
# dataframe1 = pd.read_csv('NoteAttachments.csv', error_bad_lines=False, sep='[:,|]',
                 # engine='python')
# print(dataframe1)
# for i in dataframe1:
    # x = i.split(|)
    # print(i)
# migrateTickets('')
# FetchnotesByIncident('FAB936CA-02FD-4D02-BDB9-F4A60DECC3D4')
# token()
# zohodeskSearchtoken()
# TicketOwner('')
# EntitalmentCheck('408bd293-bed4-eb11-bacc-000d3af2349a')




#
dataframe1 = pd.read_csv('NoteAttachments.csv')
dataframe = dataframe1


# csv_length = 0
# for chunk in pd.read_csv('NoteAttachments.csv'):
#     # csv_length += chunk.count()
# print(chunk )
