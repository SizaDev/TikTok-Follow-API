import requests,time,json,base64,hmac,hashlib
from Siza import argus,ladon,gorgon,khronos,params
from urllib.parse import urlencode
url = "https://api31-normal-useast1a.tiktokv.com/aweme/v1/commit/follow/user/"
userid=''
secid=''
cookie={'sid_tt=8ebc3d7ca6aeddca0b68967d88267bd8; sessionid=8ebc3d7ca6aeddca0b68967d88267bd8; sessionid_ss=8ebc3d7ca6aeddca0b68967d88267bd8'} #change sessionid
params = {
    "user_id": userid,
    "sec_user_id": secid,
    "type": "1",
    "channel_id": "0",
    "from": "13",
    "from_pre": "13",
    "item_id": god('itid'),
    "enter_from": "homepage_hot",
    "action_time": "1751630150531",
    "is_network_available": "true",
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": god('rtk'),
    "cdid": god('cdid'),
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "400603",
    "version_name": "40.6.3",
    "manifest_version_code": "2024006030",
    "update_version_code": "2024006030",
    "ab_version": "40.6.3",
    "resolution": "900*1600",
    "dpi": "300",
    "device_type": "MI 9",
    "device_brand": "Xiaomi",
    "language": "en",
    "os_api": "28",
    "os_version": "9",
    "ac": "wifi",
    "is_pad": "0",
    "app_type": "normal",
    "sys_region": "US",
    "last_install_time": "1751629471",
    "mcc_mnc": "60302",
    "timezone_name": "America/Toronto",
    "app_language": "en",
    "carrier_region": "CA",
    "timezone_offset": "3600",
    "host_abi": "arm64-v8a",
    "locale": "en",
    "content_language": "en,fr,",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "CA",
    "build_number": "40.6.3",
    "region": "CA",
    "ts": god('ts'),
    "iid": god("iid"),
    "device_id": god("did"),
    "openudid": god("oid")}
key_b64 = "BAdHRolSnc/fSiVf30YaHrqinxqLKEJw4/0LsC5wXwFv3SJhS7TdoO04IQT2jtRKOwWaG4x2/MBzttoTNmuoj20="
key = base64.b64decode(key_b64)
tts=god('ts')
message =tts.encode()
signature = hmac.new(key, message, hashlib.sha512).hexdigest()
ts_sign = f"ts.1.{signature}"
data = {"req_content":"ticket,path,timestamp","req_sign":"MEQCIG8lr/48WEHfwT9fgITaNX6lgEGUoKpcYJC19f1/0bsDAiA55KFnubhjAi9sfPDnkn4Pan68zVV6lbYuPeyvpIV8cw\u003d\u003d","timestamp":god('ts'),"ts_sign":ts_sign}
json_data = json.dumps(data, separators=(',', ':'))
token = base64.b64encode(json_data.encode()).decode()
headers = {
  'User-Agent': "com.zhiliaoapp.musically/2024006030 (Linux; U; Android 9; en; MI 9; Build/PI;tt-ok/3.12.13.20)",
  'rpc-persist-pyxis-policy-v-tnc': "1",
  'x-bd-kmsv': "0",
  'x-tt-dm-status': "login=1;ct=1;rt=1",
  'x-ss-req-ticket': "1751630150541",
  'x-bd-client-key': "#2PjU3x0oF88WSUWPd/ksEiSwk5A0n449X04wshDCmO19UR+TG34RhwO76fkL+lqLefPEXdi1uICM7pqS",
  'tt-ticket-guard-public-key': "BAdHRolSnc/fSiVf30YaHrqinxqLKEJw4/0LsC5wXwFv3SJhS7TdoO04IQT2jtRKOwWaG4x2/MBzttoTNmuoj20=", #key_b64
  'tt-ticket-guard-client-data':token,
  'sdk-version': "2",
  'tt-ticket-guard-iteration-version': "0",
  'tt-ticket-guard-version': "3",
  'passport-sdk-version': "-1",
  'x-vc-bdturing-sdk-version': "2.3.13.i18n",
  'x-tt-store-region': "ca",
  'x-tt-store-region-src': "uid",
  'x-ladon': ladon(params,cookie),
  'x-khronos':khronos(),
  'x-argus':argus(params,cookie),
  'x-gorgon':gorgon(params,cookie),
  'Cookie':cookie}
response = requests.get(url,params=params,headers=headers)
print(response.text)
