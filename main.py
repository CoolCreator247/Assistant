import time
print("Hello I am Echo I can help you with your daliy tasks")
time.sleep(3)
print("what is your name")
time.sleep(1)
name = input("name:")   
print(f"Hi",name)
while True:
    user_input = input().lower()
    if user_input == "hi":
        print("hello")

