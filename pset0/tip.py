def main():
    meal_cost = float(input("Cost of meal: "))
    tip_percent = int(input("Tip percentage: "))
    
    tip = meal_cost * tip_percent / 100
    total = meal_cost + tip
    
    print(f"Total amount: {total:.2f}")

if __name__ == "__main__":
    main()
