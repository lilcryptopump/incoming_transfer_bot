from time import sleep
import time
import pprint

from bitshares.account import Account
from bitshares.block import Block
from bitshares.blockchain import Blockchain
from bitshares.asset import Asset
from bitshares import BitShares

from twilio.rest import Client

# User Inputs
ACCOUNT_WATCHING = 'iamredbar1'
BOT_PHONE_NUMBER = '+17637031688'
YOUR PHONE NUMBER = '+19522128926'


for op in blockchain.stream(['transfer']):
    payee = Account(op['to']).name
    pprint(op)
#    if payee == ACCOUNT_WATCHING:
        


#account_sid = 'AC0d3a91069b2604617ad1e765414f6631'
#auth_token = '7b9050c62d44c7daf4cb5c8e28ab86fa'
#client = Client(account_sid, auth_token)

#message = client.messages.create(
#                                body=''.format(),
#                                from_=BOT_PHONE_NUMBER,
#                                to=YOUR_PHONE_NUMBER
#                                )
#print(message.sid)
