d = {}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16

print(d["George"])
print(d["Tom"])
print(d["Jenny"])

d["Jenny"] = 20

print(d["Jenny"])

d[10] = 100

for key in d:
    print(f'{key}: {d[key]}')