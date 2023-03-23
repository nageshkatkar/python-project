from add_customer_record import *
from display_customer_record import *
from search_customer_record import *
from display_profit_loss import *
from display_customer_records_of_product import *
from time import sleep

class MainClass:

    def main(self):
        while 1:
            sleep(0.5)
            print("\n\n********************************\n  Customer Data Record System\n********************************\n")
            print("1. Add customer record")
            print("2. Display customer records")
            print("3. Search customer record")
            print("4. View profit Loss")
            print("5. Display customer records who buyed THIS product")
            print("6. Exit from system")
            while 1:
                flag = 0
                try:
                    self.user_choice = int(input("\nChoose your choice :- "))
                    flag = 1
                except Exception:
                    print("\n\nEnter valid input")
                if flag == 1:
                    break

            if self.user_choice <= 6 and self.user_choice >= 1:
                if self.user_choice == 1:
                    obj = Add_Customer_Record()
                    obj.main()
                elif self.user_choice == 2:
                    obj = Display_Customer_Record()
                    obj.main()
                elif self.user_choice == 3:
                    obj = Search_Customer_Record()
                    obj.main()
                elif self.user_choice == 4:
                    obj = Display_Profit_Loss()
                    obj.main()
                elif self.user_choice == 5:
                    obj = Display_Customer_Records_of_Product()
                    obj.main()
            else:
                print("\nInvalid choice")

            if self.user_choice == 6:
                break


if __name__=="__main__":
    obj = MainClass()
    obj.main()
