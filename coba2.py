import os, json as js
from time import sleep


if not os.path.exists('nomor.json'):
    print("file nomor.json not found")
    data = [input("MASUKKAN NOMER (Ex: 62852) > ")]
    open('nomor.json', "w").write(js.dumps(data, indent=1))
else:
    data = js.loads(open('nomor.json', 'r').read())
    data2 = input("MASUKKAN NOMER (Ex: 62852) > ")
    data.append(data2)
    open('nomor.json', "w").write(js.dumps(data, indent=1))