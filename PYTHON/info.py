def brand():
    print("-----Choose you like Brand-----")
    print("BMW - Press 1")
    print("Maruti Suzuki - Press 2")
    print("Hyundai - Press 3")
    print("Honda - Press 4")


def model(n: int):
    print("-----Car Model-----")
    if n == 1:
        print("BMW iX Electric")
        print("     Price - 1.21 Cr*")
        print("BMW M4 Competition")
        print("     Price - 1.48 Cr*")
        print("BMW i7")
        print("   Price - 2.03 Cr*")
    elif n == 2:
        print("Maruti Swift")
        print("   Price - 6.03 Lakh*")
        print("Maruti Baleno")
        print("   Price - 6.61 Lakh*")
        print("Maruti Ertiga")
        print("   Price - 8.64 Lakh*")
    elif n == 3:
        print("Hyundai Creta")
        print("   Price - 10.87 Lakh*")
        print("Hyundai i20")
        print("   Price - 6.99 Lakh*")
        print("Hyundai Verna")
        print("   Price - 10.96 Lakh*")
    elif n == 4:
        print("Honda City")
        print("   Price - 11.63 Lakh*")
        print("Honda Amaze")
        print("   Price - 7.10 Lakh*")
        print("Honda Elevate")
        print("   Price - 11.08 Lakh*")
    else:
        print("Error!")
        print("   Thanks for Visit.")
