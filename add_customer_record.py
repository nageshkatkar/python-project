class Add_Customer_Record:

    def main(self):
        while 1:
            self.customer_name = input("\n\nEnter customer name :- ")
            self.product_name = input("Enter Product name :- ")
            while 1:
                flag = 0
                try:
                    self.buying_price = int(input("Enter buying price :- "))
                    flag = 1
                except:
                    print("\n\nEnter valid input")
                if flag == 1:
                    break
            while 1:
                flag = 0
                try:
                    self.selling_price = int(input("Enter selling price :- "))
                    flag = 1
                except:
                    print("\n\nEnter valid input")
                if flag == 1:
                    break

            self.add_record_in_file()
            while 1:
                extra_rec = input("\n\nDo you want add another record (y/n) :- ")[0]
                self.extra_record = extra_rec.lower()
                if self.extra_record == 'y' or self.extra_record == 'n':
                    break
                else:
                    print("\n\nPlease enter valid input")
            if self.extra_record == 'n':
                break

    def add_record_in_file(self):
        file = open("customer-data-record.txt", "a")
        customer_name = self.customer_name + "\n"
        product_name = self.product_name + "\n"
        buying_price = str(self.buying_price) + "\n"
        selling_price = str(self.selling_price) + "\n"
        file.write(customer_name)
        file.write(product_name)
        file.write(buying_price)
        file.write(selling_price)

