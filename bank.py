#user input
answer = input("Greeting: ").lower().strip()

#check if the answer 'hello', print $0
if 'hello' in answer:
    print("$0")

#check if the answer start with 'h', print $20
elif 'h' in answer[0]:
    print("$20")

#otherwise, print $100
else:
    print("$100")
    
