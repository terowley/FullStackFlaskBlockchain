# Template for Flask frontend to Ether/BSC Contracts

# Completely Python or Python-like (Vyper)
# 
# Uses Flask and waitress to provide framework for
# HTML and waitress to connect to the internet
# 
# Assumes the related contract is in Ganach or a test net, 
# Contract  written in Vyper
# #
import json

from flask import Flask, Response, request, jsonify, render_template
from waitress import serve # for connection to internet when on Windows
from web3 import Web3  # uses the web3.py version

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(f' Ganache is online: {web3.isConnected()}')

'''
# TO DEPLOY A CONTRACT TO THE BLOCKCHAIN(TESTNET)
# first compile to get ABI and bytecode
# Code below results in address of contract deployed to blockchain
#

abi = json.loads('INSERT FROM COMPILE')
bytecode = 'INSERT FROM COMPILE'
# # set pre-funded account as sender
web3.eth.defaultAccount = web3.eth.accounts[0]

# # Instantiate and deploy contract
NewContract = web3.eth.contract(abi=abi, bytecode=bytecode)

# # Submit the transaction that deploys the contract
tx_hash = NewContract.constructor().transact()

# # Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

# # Create the contract instance with the newly-deployed address
contract = web3.eth.contract(
    address=tx_receipt.contractAddress,
    abi=abi,
)

print(f' Contract address: {tx_receipt.contractAddress}')
'''

# CHECK: contract  deployed to Ganache with remix.ethereum.org

# Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[0]


app = Flask(__name__)

# test contract - authorize.vy - sets approve/disapprove status for user at address

# api to set approval for user
# request must be sent from contract originating account
abi =json.loads('  [{"name":"Authorized","inputs":[{"type":"string","name":"name","indexed":false},{"type":"bool","name":"status","indexed":false},{"type":"address","name":"location","indexed":true}],"anonymous":false,"type":"event"},{"outputs":[],"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"name":"approve","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_user"},{"type":"string","name":"_name"}],"stateMutability":"nonpayable","type":"function","gas":78379},{"name":"disapprove","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"_user"},{"type":"string","name":"_name"}],"stateMutability":"nonpayable","type":"function","gas":29311},{"name":"statusOf","outputs":[{"type":"bool","name":""}],"inputs":[{"type":"address","name":"arg0"}],"stateMutability":"view","type":"function","gas":1336},{"name":"addressOf","outputs":[{"type":"address","name":""}],"inputs":[{"type":"string","name":"arg0"}],"stateMutability":"view","type":"function","gas":1448}]')
byte_code = 0x336002556103f656341561000a57600080fd5b6004361015610018576103e8565b600035601c526329cd00f760005114156101985760043560a01c1561003c57600080fd5b604060243560040161014037602060243560040135111561005c57600080fd5b600254331415156100ac576308c379a06101a05260206101c052600e6101e0527f6e6f7420617574686f72697a6564000000000000000000000000000000000000610200526101e05060646101bcfd5b6001600060043560e05260c052604060c020556004356001610140516101602060e05260c052604060c0205560016102005260406101a0526101a0516101e0526101408051602001806101a0516101e0018284600060045af161010e57600080fd5b50506101a0516101e001518060206101a0516101e0010101818260206001820306601f820103905003368237505060206101a0516101e0015160206001820306601f82010390506101a05101016101a0526004357fa3555e7d2ff7bc749eac150d23efe83fef7922ac05fee4a2cecb2123f2f0f1106101a0516101e0a2600160005260206000f350005b63b552296e600051141561035e5760043560a01c156101b657600080fd5b60406024356004016101403760206024356004013511156101d657600080fd5b60025433141515610226576308c379a06101a05260206101c052600e6101e0527f6e6f7420617574686f72697a6564000000000000000000000000000000000000610200526101e05060646101bcfd5b6004356001610140516101602060e05260c052604060c0205414151561028b576308c379a06101a05260206101c052600c6101e0527f756e6b6e6f776e20757365720000000000000000000000000000000000000000610200526101e05060646101bcfd5b6000600060043560e05260c052604060c0205560006102005260406101a0526101a0516101e0526101408051602001806101a0516101e0018284600060045af16102d457600080fd5b50506101a0516101e001518060206101a0516101e0010101818260206001820306601f820103905003368237505060206101a0516101e0015160206001820306601f82010390506101a05101016101a0526004357fa3555e7d2ff7bc749eac150d23efe83fef7922ac05fee4a2cecb2123f2f0f1106101a0516101e0a2600060005260206000f350005b6397a5d5b560005114156103985760043560a01c1561037c57600080fd5b600060043560e05260c052604060c0205460005260206000f350005b63ccf1454a60005114156103e75760406004356004016101403760206004356004013511156103c657600080fd5b6001610140516101602060e05260c052604060c0205460005260206000f350005b5b60006000fd5b6100086103f6036100086000396100086103f6036000f3
# address in Ganache
contract_address =Web3.toChecksumAddress('0xa2AeF9cA3254E1456bC86C4e17D45238cF1BE90c')
    
# Create the contract instance with the newly-deployed address
authorize_contract = web3.eth.contract(
        address=contract_address, abi=abi,
    )

@app.route("/approve", methods=['GET', 'POST']) # sample ?0x5d695c3540cE6D1101ee1a7498994819A27E23E4,John Q
def transaction():
    
    #web3.eth.defaultAccount = web3.eth.accounts[1]


    return render_template("index.html")


@app.route("/form", methods=['GET', 'POST']) 
def form():
    
    name = request.form.get('Name')
    address_string = request.form.get('Address')
    address = Web3.toHex(hexstr=address_string)   #Convert string of hex digit  characters to address   
    address = Web3.toChecksumAddress(address) #force upper case - required by web3
    #print(f'address: {address}, name: {name}')
    tx_hash = authorize_contract.functions.approve(address, name)
    #print(f'hash: {tx_hash}')
    tx_hash = tx_hash.transact()
    # Wait for transaction to be mined...
    web3.eth.waitForTransactionReceipt(tx_hash)
    #print(f'transaction complete')
    user_data = authorize_contract.functions.statusOf(address).call()
    
    # report transaction success
    return render_template("status.html",name=name,address=address, status=user_data)
    


if __name__ == "__main__":
    app.run(host='0.0.0.0')
    #We now use this syntax to server our app. 
    #serve(app, host='0.0.0.0', port=5000)

