import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token'5677942783:AAHY1KH8LA6V9iYTmeUC1UipJd47d-vZDKg')
API_ID =  os.environ.get('api_id','24253609')
API_HASH = os.environ.get('api_hash','20c1618672d0d23844bf79d8a25de44f')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','darielxd').split(';')
#ACCES_USERS = ('tl_admin_user','darielxd','Pjsr55')
#ACCES_USERS = os.environ.get(ACCES_USERS)
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc',''))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
