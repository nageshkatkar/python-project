from time import sleep

class Display_Customer_Record:
    def main(self):
        try:
            file = open("customer-data-record.txt","r")
            count=0
            flag = 0
            for i in file:
                flag = 1
                count+=1
                if count==1:
                    sleep(0.5)
                    print("\n\n**************************")
                    print("Customer name :-",i,end="")
                elif count==2:
                    print("Product name :-",i,end="")
                elif count==3:
                    print("Buying price :-",i,end="")
                elif count == 4:
                    count = 0
                    print("Selling price :-", i,end="")
            if flag==0:
                print("\n\nRecord list is empty")
        except FileNotFoundError:
            print("\n\nNo record list")

