from tqdm import tqdm
import time

x = [1,2,3,4,5,6,7,8,9,10]
for i in tqdm (range(len(x)),
			desc="Loading…",
			ascii=False, ncols=75):
    print(x[i])
    time.sleep(0.1)
	
print("Complete.")

