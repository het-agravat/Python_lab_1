#Write Program for simple interest. Simple Interest = (P x T x R)/100

def simple_interest(p,r,t):
    simple_interest = (p*r*t) / 100
    return simple_interest

p = float(input("Enter the amount (P): "))
r = float(input("Enter the rate (R): "))
t = float(input("Enter the Period (T): "))

interest = simple_interest(p,r,t)

print(f"Simple Interest = {interest}")
