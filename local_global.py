user="Ram"

def sayhello():
    global user
    user = "Sham"
    print(f"Hello {user}")

sayhello()
print(f"Hi {user}")
