from hashlib import md5

# note the 22th character
t1 = "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak".encode('ascii')
t2 = "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak".encode('ascii')
for i in range(len(t1)):
    if t1[i] != t2[i]:
        print(f"Position {i+1}: '{chr(t1[i])}' in text 1, '{chr(t2[i])}' in text 2")

h1 = md5( t1 ).hexdigest()
h2 = md5( t2 ).hexdigest()
print(f"the hash is the same: '{h1,h2,h1 == h2}'") 