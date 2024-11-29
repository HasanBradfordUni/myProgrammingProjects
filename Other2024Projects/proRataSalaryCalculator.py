def calculate_pro_rata_salary(annual_salary, hours_per_week, full_time_hours):
    pro_rata_annual_salary = (annual_salary / full_time_hours) * hours_per_week
    pro_rata_monthly_salary = pro_rata_annual_salary / 12
    pro_rata_hourly_rate = pro_rata_annual_salary / (52 * hours_per_week)
    
    return pro_rata_annual_salary, pro_rata_monthly_salary, pro_rata_hourly_rate

def main():
    try:
        annual_salary = float(input("Enter the annual salary: "))
        hours_per_week = float(input("Enter the hours per week: "))
        full_time_hours = float(input("Enter the full time hours per week: "))
        
        pro_rata_annual_salary, pro_rata_monthly_salary, pro_rata_hourly_rate = calculate_pro_rata_salary(annual_salary, hours_per_week, full_time_hours)
        
        print(f"Pro Rata Annual Salary: £{pro_rata_annual_salary:.2f}")
        print(f"Pro Rata Monthly Salary: £{pro_rata_monthly_salary:.2f}")
        print(f"Pro Rata Hourly Rate: £{pro_rata_hourly_rate:.2f}")
    except ValueError:
        print("Please enter valid numerical values.")

if __name__ == "__main__":
    main()