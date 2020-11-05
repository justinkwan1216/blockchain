import math
eth_in_pool=100
solid_in_pool=100

total_eth_in_wallet=0
total_solid_in_wallet=100

ratio=total_solid_in_wallet/(solid_in_pool+total_solid_in_wallet)
def sigmoid(x):
    return (1/(1+math.exp(-x)))

price=sigmoid(ratio)*eth_in_pool/solid_in_pool

eth_in_pool-=price*total_solid_in_wallet
solid_in_pool+=total_solid_in_wallet

total_eth_in_wallet+=price*total_solid_in_wallet
total_solid_in_wallet=0



print("total eth in wallet: "+str(total_eth_in_wallet))
print("total solid in wallet: "+str(total_solid_in_wallet))

print(eth_in_pool)
print(solid_in_pool)
