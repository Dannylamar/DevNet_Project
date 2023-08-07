devices=[]
file=open("/home/devasc/labs/devnet-src/python/devices.txt","a")
while True:
    newItem=input("Enter device name: ")
    if newItem=="exit":
        print("All done!")
        break
    file.write(newItem + "\n")
file.close()
