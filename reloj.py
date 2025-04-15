import time as t

hour=-1
min=-1
sec=-1
for hora in range(24):
    min=-1
    hour+=1
    for minuto in range(60):
        sec=-1
        min+=1
        for segundo in range(60):
            sec+=1
            print (f"{hour}:{min}:{sec}")
            t.sleep(1)