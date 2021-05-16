# Full STack Template
This folder contains a complete app written in Python for interacting with the blockchain

The frontend is written in Python using the
Flask framework with w3.css for display and blockchain connection thru Web3.py

The backend is a contract on the Ganache testnet written in Vyper
(python derived blockchain programming language)

Application is a simple key:value store of authorizations on the blockchain

Contract Functions:
    Approve(address,name)- stores a True value and name at blockchain address 
    DisApprove(address,name) - changes authorization value to False
    StatusOf(address) - getter for authorization value
    nameOf(address) - returns name associated with address

Web Frontend displays a webpage at localhost:5000/approve when using Ganache local blockchain
    webpage requests name and address in a form 
    data passed to blockchain via web3.py calls
a confirmation webpage is displayed when the blockchain transaction is completed

Can also use python library 'waitress' (windows) or 'gunicorn' (unix) for external internet connection. 

