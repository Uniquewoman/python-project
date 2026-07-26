
def calc_total(bill, tip_percent):
    tip = bill * tip_percent / 100
    return bill + tip

def main():
    bill = float(input("bill: "))
    pct = float(input("tip %: "))
    print(f"total = {calc_total(bill, pct)}")

if __name__ == "__main__":
    main()
from main import calc_total

def test_calc_total():
    assert calc_total(100, 10) == 110
