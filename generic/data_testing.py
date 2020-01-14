import configparser
import json

address = "e65b318b9decf504d1cb6ea5c367ca657a070db1"
key = "1e771da3a1dcae0fd77a942cc816fd6b9b4cca97220f8ea6c6782a848714129d"

print(bytes.fromhex(address))
print(bytes.fromhex(key))
# b'\xe6[1\x8b\x9d\xec\xf5\x04\xd1\xcbn\xa5\xc3g\xcaez\x07\r\xb1'
# b'\x1ew\x1d\xa3\xa1\xdc\xae\x0f\xd7z\x94,\xc8\x16\xfdk\x9bL\xca\x97"\x0f\x8e\xa6\xc6x*\x84\x87\x14\x12\x9d'

address = "0xe65b318b9decf504d1cb6ea5c367ca657a070db1"
print(address.split('0x'))
print(address[2:])


config = configparser.RawConfigParser()
config.read('0xD605dfe98F168324075E2b2fab6D41b071b91c06.properties')

dictonary = config.items("tokens")

print(dictonary)