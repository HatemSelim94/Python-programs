def mostActive(customers):
    '''
    Input: an array of customer names
    Output: an alphabetically ascending array of customer names 
    '''
    most_active_customers = []
    # set does not store duplicate values
    customers_names = set(dict((key, value) for key, value in enumerate(customers)).values())
    customers_names = list(customers_names)
    customers_trades = [0]*len(customers_names)
    for i in range(len(customers)): # count number of trades for each customer
        for j in range(len(customers_names)):
            if customers[i] == customers_names[j]:
                customers_trades[j] +=1
                break
    total_trades = len(customers)
    for i in range(len(customers_trades)): # calculate the percentage per customer and find the most active ones
        customers_trades[i] /= total_trades
        if customers_trades[i] >= 0.05:
            most_active_customers.append(customers_names[i])
    most_active_customers = sorted(most_active_customers) # sort customers names alphabetically 
    return most_active_customers 