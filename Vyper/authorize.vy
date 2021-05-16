# @version ^0.2.1

# Simple contract to approve or disapprove a user. 
# Address and name of user stored on the blockchain
    
event Authorized:
    name: String[32]
    status: bool
    location: indexed(address)


statusOf: public(HashMap[address, bool])
addressOf: public(HashMap[String[32], address])
owner: address

@external
def __init__():
    self.owner = msg.sender



@external
def approve(_user : address, _name: String[32]) -> bool:
    assert msg.sender == self.owner, "not authorized"
    self.statusOf[_user] = True
    self.addressOf[_name] = _user
    log Authorized(_name, True, _user)
    return True

@external  
def disapprove(_user : address, _name: String[32]) -> bool:
    assert msg.sender == self.owner, "not authorized"
    assert self.addressOf[_name] == _user, "unknown user"
    self.statusOf[_user] = False
    log Authorized(_name, False, _user)
    return False