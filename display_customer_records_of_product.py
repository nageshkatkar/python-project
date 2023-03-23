from time import sleep

class Display_Customer_Records_of_Product:
    def main(self):
        try:
            file = open("customer-data-record.txt", "r")
            product_name = input("\n\nEnter product name :- ")
            customer_data = []
            count,flag = 0,0
            found = False
            customer_name = ""

            for data in file:
                count += 1
                if count==1:
                    customer_name = data
                elif count==2:
                    if data.lower() == product_name.lower()+"\n":
                        found = True
                        customer_data.append(customer_name)
                        customer_data.append(data)
                        flag = 1
                elif count==3 and flag==1:
                    customer_data.append(data)
                elif count==4 and flag==1:
                    customer_data.append(data)
                    flag = 0

                if count == 4:
                    count = 0


            if found==True:
                print("\nCustomers record found")
                for i in customer_data:
                    count += 1
                    if count == 1:
                        sleep(0.5)
                        print("\n**************************")
                        print("Customer name :-", i, end="")
                    elif count == 2:
                        print("Product name :-", i, end="")
                    elif count == 3:
                        print("Buying price :-", i, end="")
                    elif count == 4:
                        count = 0
                        print("Selling price :-", i, end="")
            else:
                print("\nNo customers buyed product",product_name)

        except Exception:
            print("\n\nNo record list")
