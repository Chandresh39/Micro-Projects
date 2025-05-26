import chart


def cho():
    print("Press 1 - View Brand Sell")
    print("Press 2 - View BMW Sell")
    print("Press 3 - View Maruti Suzuki Sell")
    print("Press 4 - View Hyundai Sell")
    print("Press 5 - View Honda Sell")


def opt(n: int):
    if n == 1:
        chart.brand()
    if n == 1:
        chart.bmw()
    if n == 2:
        chart.maruti()
    if n == 3:
        chart.hyu()
    if n == 4:
        chart.honda()
