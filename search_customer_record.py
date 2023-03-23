from time import sleep

class Search_Customer_Record:

    def main(self):
        try:
            file = open("customer-data-record.txt", "r")
            customer_name = input("\nEnter the customer name :- ")
            count, flag, found = 0, 0, 0

            for i in file:
                count += 1
                if count == 1:
                    if i.lower() == customer_name.lower() + "\n":
                        if flag == 0:
                            flag = 1
                            print("\nYes! Customer founded")
                        found = 1
                if found == 1:
                    if count == 1:
                        sleep(0.5)
                        print("\n\n**************************")
                        print("Customer name :-", i, end="")
                    elif count == 2:
                        print("Product name :-", i, end="")
                    elif count == 3:
                        print("Buying price :-", i, end="")
                    elif count == 4:
                        found = 0
                        print("Selling price :-", i, end="")
                if count == 4:
                    count = 0

            if flag==0:
                print("\n\nNo such customer")

        except Exception:
            print("\n\nNo record list")
