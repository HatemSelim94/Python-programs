from mostactive import  mostActive
if __name__ == "__main__":
    # test case 1
    customers1 = ["Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Alpha","Omega","Beta"]
    # test case 2
    customers2 = ["Alpha","Beta","Zeta","Beta","Zeta","Zeta","Epsilon","Beta","Zeta","Beta","Zeta","Beta","Delta","Zeta","Beta","Zeta","Beta","Zeta","Beta","Zeta","Beta"]
    most_active_customers1 = mostActive(customers1)
    print(most_active_customers1)
    most_active_customers2 = mostActive(customers2)
    print(most_active_customers2)
