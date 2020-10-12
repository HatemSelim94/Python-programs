### Encryption:
Given string s, let s[i] represent the ith character in the string s, using 0-based indexing.

1. Initially i = 0.
2. If s[i] is lowercase and the next character s[i+1] is uppercase, swap them, add a '*' after them, and move to i+2.
3. If s[i] is a number, replace it with 0, place the original number at the start, and move to i+1.
4. Else, move to i+1.
5. Stop if i is more than or equal to the string length. Otherwise, go to step 2.

Note:

    • The original string always contains digits from 1 to 9 and does not contain 0.
    • The original string always contains only alpha-numeric characters.

### Decryption:
1. Find number of zeros(zeros_num) in the list and create a new list (zeros_replacments) contains s[0:zeros_num].
2. Initialize an empty list (decrypted_password).
3. Starting with i=zeros_num loop through s values.
4. If s[i] is 0, append zeros_replacments.pop(-1) to decrypted_password by .append method.
5. If  s[i] is a character, check if i+2 is still in range then if s[i+2] is a '*' append s[i+1] then s[i] to decrypted_password and start next iteration with i = i+2.
6. Else append s[i] to decrypted_password.
7. Convert decrypted_password to string.