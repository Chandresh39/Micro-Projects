import info
import conn


print("-----Car Selling Information Company-----")
print("Show Car Information - Press 1")
print("Show Selling Chart - Press 2")
print("Exit - Press 3")
c = int(input("Enter your Choose : "))

if c == 1:
    info.brand()
    c1 = int(input("Enter Your Choose: "))
    info.model(c1)
if c == 2:
    conn.cho()
    a = int(input("Enter your choose: "))
    conn.opt(a)
if c == 3:
    exit()
