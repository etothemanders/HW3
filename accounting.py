def get_melon_types(filename):
    """Count up the different types of melons and return a melon dictionary."""
    f = open(filename, "r")
    melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
    for line in f:
        junk, melon_type, melon_count = line.strip().split(",")
        melon_tallies[melon_type] += int(melon_count)
    f.close()
    return melon_tallies
    

def calc_melon_revenue(melon_tallies):
    """Calculate the revenue for each type of melon and print melon revenue report."""
    melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
    total_revenue = 0
    print "******************************************"
    for melon_type in melon_prices:
        price = melon_prices[melon_type]
        revenue = price * melon_tallies[melon_type]
        total_revenue += revenue
        print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
        

def get_sales_types(filename):
    """Count up the sales revenue by type (online vs. phone) and return a sales dictionary."""
    f = open(filename, "r")
    sales_dict = {"online": 0, "phone": 0}
    for line in f:
        junk, sales_type, sales_name, amount = line.split(",")
        if sales_type == "0":
            sales_dict["online"] += float(amount)
        else:
            sales_dict["phone"] += float(amount)
    return sales_dict
    
    
def calc_phone_vs_online_revenue(sales_dict):
    """Print a report of phone vs online sales revenue."""
    print "******************************************"
    print "Salespeople generated %0.2f in revenue." % sales_dict["phone"]
    print "Internet sales generated %0.2f in revenue." % sales_dict["online"]
    if sales_dict["phone"] > sales_dict["online"]:
        print "Guess there's some value to those salespeople after all."
    else:
        print "Time to fire the sales team! Online sales rule all!"
    print "******************************************"
    

def main():
    melon_dict = get_melon_types("orders_by_type.csv")
    calc_melon_revenue(melon_dict)
    sales_dict = get_sales_types("orders_with_sales.csv")
    calc_phone_vs_online_revenue(sales_dict)


if __name__ == "__main__":
    main()
