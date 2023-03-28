from brownie import accounts, config, SimpleStorage


# putting all the logic for our deployent in a function
def deploy_simple_storage():
    account =accounts[0]# for adding accounts from brownie, inst
    simple_storage = SimpleStorage.deploy({"from": account})# anytime a contract is deployed, there is a point there is also a destination (from and to)
    #transact
    #call
    stored_value = simple_storage.retrieve()# since this is a view function, we dont hae to add "{"from": account}", we dont have to make a tansaction with  view function
    print(simple_storage)
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})  #updateing stored_value.  since this is a transction, we will need to add "{"from": account}"
    transaction.wait(1)#this similar to web3.py
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()