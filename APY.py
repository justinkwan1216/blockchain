APY=800
cycle_time=1000
token=1

for i in range(cycle_time):
    generated = token*(APY/cycle_time/100)
    token+=generated
    print(token)
