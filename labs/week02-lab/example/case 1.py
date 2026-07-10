print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

# input
radius = float(input("Enter Your radius :"))
π = 3.14159

# process
area = π * radius ** 2
Circumference = 2 * π * radius

# output
print("Area of Your circle = ",area)
print("The Circumference of Circle =" + str(Circumference))
print(f"Area {area},Circumference {Circumference}")
