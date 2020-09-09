fo = open("credentials.txt", "r")

infura_url = fo.readline()
public_key = fo.readline()
private_key = fo.readline()

print(infura_url)
print(public_key)
print(private_key)
