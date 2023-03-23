
flag = 0
while 1:

    try:
        num = int(input("Enter any number :- "))
        flag = 1
        print("Your entered number",num)
    except Exception:
        print("you entered wrong input")
    finally:
        print("bye")
    if flag == 1:
        break


