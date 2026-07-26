
def calc_total(bill, tip_percent):
    tip = bill * tip_percent / 100
    return bill + tip

def main():
    bill = float(input("bill: "))
    pct = float(input("tip %: "))
    print(f"total = {calc_total(bill, pct)}")

if __name__ == "__main__":
    main()
