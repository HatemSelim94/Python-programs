### Most active customers:
* Given a list of trades by customer name, determine which customers account for at least 5% of the total number of trades. 
* Order the list alphabetically ascending by name.
#### mostActive function:
* Input: an array of customer names.
* Output: an alphabetically ascending array of customer names.
* Example:
    
    Input = ["Alpha","Beta","Zeta","Beta","Zeta","Zeta","Epsilon","Beta","Zeta","Beta","Zeta","Beta","Delta","Zeta","Beta","Zeta","Beta","Zeta","Beta","Zeta","Beta"]

    Output = ['Beta', 'Zeta']
* Explanation: Both Beta and Zeta made 9 trades out of 21 (42.86% of the total). Alpha, Delta and Epsilon made 1 trade each, which is only 4.76% of the total number of trades. Only Beta and Zeta meet the threshold.

