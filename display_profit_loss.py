class Display_Profit_Loss:

    def main(self):
        try:
            file = open("customer-data-record.txt", "r")
            count, buying_amount, selling_amount = 0, 0, 0

            for data in file:
                count += 1
                if count == 3:
                    buying_amount += int(data)
                if count == 4:
                    selling_amount += int(data)
                    count = 0

            print("\n\nTotal buying amount :-", buying_amount)
            print("Total selling amount :-", selling_amount)

            if buying_amount > selling_amount:
                print("Loss :-", (buying_amount-selling_amount))
            elif selling_amount > buying_amount:
                print("Profit :-", (selling_amount-buying_amount))
            else:
                print("Profit :- 0")

        except Exception:
            print("\n\nNo record list")
