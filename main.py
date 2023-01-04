import os
from run_forge import *
from MagicT import *
from Contracts import *

# smart_contract = \
# '''
# pragma solidity ^0.5.0;

# contract SmartContract {
#     address public owner;
#     uint public balance;

#     constructor() public {
#         owner = msg.sender;
#         balance = 0;
#     }

#     function deposit() public payable {
#         require(msg.value > 0);
#         balance += msg.value;
#     }

#     function withdraw(uint amount) public {
#         require(amount > 0 && amount <= balance);
#         balance -= amount;
#         msg.sender.transfer(amount);
#     }

#     function transfer(address payable recipient, uint amount) public {
#         require(amount > 0 && amount <= balance);
#         balance -= amount;
#         recipient.transfer(amount);
#     }
# }
# '''

project = 'task-tracker'

if not os.path.exists(project):
    init(project)

# create a contract
smart_contract = make_contracts()
print(smart_contract)
# all contracts will be overwritten in the {project}/src/Counter.sol
write(project, smart_contract)

# build the smart contract via forge
msg = build(project)

if msg!='build successful':
    saved_err = msg
    # errordetails = extract_info(saved_err.output.decode('utf-8'))
    
    # If there's multiple errors, we only want the first one
    errorArray = saved_err.output.decode('utf-8').split("warning[")[0].split("error[")
    error = "error["+errorArray[0].rstrip("\x1b[33m") #take the first error and strip color control code" 
    
    errorPrompt = createPrompt(error, project)
    patch = getPatch(errorPrompt, debug=True, temp=.75)
    runPatch(patch)
    checkPatch(errordetails)
else:
    print(msg)
