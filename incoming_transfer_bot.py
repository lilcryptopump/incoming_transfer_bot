from pprint import pprint
from bitshares.account import Account
from bitshares.blockchain import Blockchain
from bitshares.asset import Asset
from bitshares import BitShares
from twilio.rest import Client

# User Inputs
ACCOUNT_WATCHING = 'iamredbar1'
BOT_PHONE_NUMBER = '+17637031688'
YOUR_PHONE_NUMBER = '+19522128926'

account_sid = 'AC0d3a91069b2604617ad1e765414f6631'
auth_token = ''
client = Client(account_sid, auth_token)


bitshares = BitShares(
                        node=[
                            "wss://na.openledger.info/ws",
                            "wss://kc-us-dex.xeldal.com/ws"
                        ]
            )

blockchain = Blockchain(
                        blockchain_instance=bitshares,
                        mode='head'
)

for op in blockchain.stream(['transfer']):
    payee = Account(op['to']).name
    from_account = Account(op['from']).name
    asset_symbol = Asset(op['amount']['asset_id']).symbol
    asset_precision = int(Asset(op['amount']['asset_id']).precision)
    amount = int(op['amount']['amount'])
    if asset_precision != 0:
        amount = amount / (10 ^ asset_precision)
    pprint('{} sent {} {} {} in block {}.'.format(
                                    from_account,
                                    payee,
                                    amount,
                                    asset_symbol,
                                    op['block_num']))
    if payee == ACCOUNT_WATCHING:
        message = client.messages.create(
                                body='{} sent {} {} {} in block {}.'.format(
                                    from_account,
                                    payee,
                                    amount,
                                    asset_symbol,
                                    op['block_num']
                               ),
                                from_=BOT_PHONE_NUMBER,
                               to=YOUR_PHONE_NUMBER
                                )
        print(message.sid)
