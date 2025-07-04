import requests, json, base64, hmac, hashlib
from Siza import god, argus, ladon, gorgon, khronos  # Helper functions from custom TikTok signature module

# TikTok follow API endpoint
url = "https://api31-normal-useast1a.tiktokv.com/aweme/v1/commit/follow/user/"

# Insert valid TikTok user values
userid = ''
secid = ''

# Session cookies (from valid TikTok login)
cookie_str = 'sid_tt=...; sessionid=...; sessionid_ss=...'  # Replace with actual values
cookie = {'Cookie': cookie_str}

# Parameters for the request — define TikTok app & device fingerprint
params = {
    "user_id": userid,
    "sec_user_id": secid,
    "type": "1",  # Follow action type
    "channel_id": "0",
    "from": "13",
    "from_pre": "13",
    "item_id": god('itid'),
    "enter_from": "homepage_hot",
    "action_time": god('ts'),
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
    "last_install_time": god('ts'),
    "mcc_mnc": "60302",
    "timezone_name": "America/Toronto",
    "app_language": "en",
    "carrier_region": "CA",
    "timezone_offset": "3600",
    "host_abi": "arm64-v8a",
    "locale": "en",
    "content_language": "en,fr",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "CA",
    "build_number": "40.6.3",
    "region": "CA",
    "ts": god('ts'),
    "iid": god("iid"),
    "device_id": god("did"),
    "openudid": god("oid")
}

# HMAC SHA-512 signature creation
key_b64 = "BAdHRolSnc/fSiVf30YaHrqinxqLKEJw4/0LsC5wXwFv3SJhS7TdoO04IQT2jtRKOwWaG4x2/MBzttoTNmuoj20="
key = base64.b64decode(key_b64)
timestamp = god('ts').encode()
signature = hmac.new(key, timestamp, hashlib.sha512).hexdigest()
ts_sign = f"ts.1.{signature}"

# Encoded payload used by TikTok security headers
payload = {
    "req_content": "ticket,path,timestamp",
    "req_sign": "MEQCIG8lr/48WEHfwT9fgITaNX6lgEGUoKpcYJC19f1/0bsDAiA55KFnubhjAi9sfPDnkn4Pan68zVV6lbYuPeyvpIV8cw==",
    "timestamp": god('ts'),
    "ts_sign": ts_sign
}
token = base64.b64encode(json.dumps(payload, separators=(',', ':')).encode()).decode()

# Required headers for TikTok API
headers = {
    'User-Agent': "com.zhiliaoapp.musically/2024006030 (Linux; U; Android 9; en; MI 9; Build/PI;tt-ok/3.12.13.20)",
    'rpc-persist-pyxis-policy-v-tnc': "1",
    'x-bd-kmsv': "0",
    'x-tt-dm-status': "login=1;ct=1;rt=1",
    'x-ss-req-ticket': god('rtk'),
    'x-bd-client-key': "#2PjU3x0oF88WSUWPd/ksEiSwk5A0n449X04wshDCmO19UR+TG34RhwO76fkL+lqLefPEXdi1uICM7pqS",
    'tt-ticket-guard-public-key': key_b64,
    'tt-ticket-guard-client-data': token,
    'sdk-version': "2",
    'tt-ticket-guard-iteration-version': "0",
    'tt-ticket-guard-version': "3",
    'passport-sdk-version': "-1",
    'x-vc-bdturing-sdk-version': "2.3.13.i18n",
    'x-tt-store-region': "ca",
    'x-tt-store-region-src': "uid",
    'x-ladon': ladon(params, cookie),
    'x-khronos': khronos(),
    'x-argus': argus(params, cookie),
    'x-gorgon': gorgon(params, cookie),
    **cookie
}
response = requests.get(url, headers=headers)
print(response.text)
