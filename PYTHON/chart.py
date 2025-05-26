from matplotlib import pyplot as pt


def brand():
    car = ["BMW", "Maruti Suzuki", "Hyundai", "Honda"]
    sell = [32564, 27556, 26948, 28524]
    pt.plot(car, sell)
    pt.show()


def maruti():
    model = ["Maruti Swift", "Maruti Baleno", "Maruti Ertiga"]
    sell = [5664, 4636, 3534]
    pt.plot(model, sell)
    pt.show()


def honda():
    model = ["Honda City", "Honda Amaze", "Honda Elevate"]
    sell = [5534, 2263, 2153]
    pt.plot(model, sell)
    pt.show()


def bmw():
    model = ["BMW iX Electric", "BMW M4 Competition", "BMW i7"]
    sell = [2563, 5686, 5465]
    pt.plot(model, sell)
    pt.show()


def hyu():
    model = ["Hyundai Creta", "Hyundai i20", "Hyundai Verna"]
    sell = [3651, 4654, 3264]
    pt.plot(model, sell)
    pt.show()
