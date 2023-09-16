# Test Case 1 - Order build a custom PC (10/10)

__Test 1 passed.__

## Test 1 Student Output:

Welcome to my PC shop!


Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's start building your PC!  

First, let's pick a CPU.  
1 : Intel Core i7-11700K, $499.99  
2 : AMD Ryzen 7 5800X, $312.99  
Choose the number that corresponds with the part you want:   
Next, let's pick a compatible motherboard.  
1 : MSI B550-A PRO, $197.46  
Choose the number that corresponds with the part you want:   
Next, let's pick your RAM.  
1 : 16 GB, $82.99  
2 : 32 GB, $174.99  
Choose the number that corresponds with the part you want:   
Next, let's pick your PSU.  
1 : Corsair RM750, $164.99  
Choose the number that corresponds with the part you want:   
Next, let's pick your case.  
1 : Full Tower (black), $149.99  
2 : Full Tower (red), $149.99  
Choose the number that corresponds with the part you want: Choose the number that corresponds with the part you want:   
Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).  
1 : 250 GB, $69.99  
2 : 500 GB, $93.99  
3 : 4 TB, $219.99  
Choose the number that corresponds with the part you want (or X to not get an SSD):   
Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).  
1 : 500 GB, $106.33  
2 : 1 TB, $134.33  
Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD):   
Finally, let's pick your graphics card (or X to not get a graphics card).  
1 : MSI GeForce RTX 3060 12GB, $539.99  
Choose the number that corresponds with the part you want:   
You have selected all of the required parts! Your total for this PC is $1134.75  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's pick a pre-built PC!  

Which prebuilt would you like to order?  
1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99  
2 : SkyTech Prism II Gaming PC, $2839.99  
3 : ASUS ROG Strix G10CE Gaming PC, $1099.99  
Choose the number that corresponds with the part you want:   
Your total price for this prebuilt is $3699.99  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? [1134.75, 3699.99]  

## Test 1 Expected Output:

input:   
1, 2, 1, 2, 1, 5, 1, x, 2, x, 2, 1, 3  

output:  

[1134.75, 3699.99]  

# TEST CASE 2 - Purchase a pre-built PC (10/10)

__Test 2 passed.__

## Test 2 Student Output:

Welcome to my PC shop!  


Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's pick a pre-built PC!  

Which prebuilt would you like to order?  
1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99  
2 : SkyTech Prism II Gaming PC, $2839.99  
3 : ASUS ROG Strix G10CE Gaming PC, $1099.99  
Choose the number that corresponds with the part you want:   
Your total price for this prebuilt is $1099.99  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's pick a pre-built PC!  

Which prebuilt would you like to order?  
1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99  
2 : SkyTech Prism II Gaming PC, $2839.99  
3 : ASUS ROG Strix G10CE Gaming PC, $1099.99  
Choose the number that corresponds with the part you want:  
Your total price for this prebuilt is $3699.99  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's pick a pre-built PC!  

Which prebuilt would you like to order?  
1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99  
2 : SkyTech Prism II Gaming PC, $2839.99  
3 : ASUS ROG Strix G10CE Gaming PC, $1099.99  
Choose the number that corresponds with the part you want:   
Your total price for this prebuilt is $3699.99  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? [1099.99, 3699.99, 3699.99]  

## Test 2 Expected Output:

input:     
2, 3, 2, 1, 2, 1, 3

output:  
[1099.99, 3699.99, 3699.99]  

# TEST CASE 3 - Order build a custom PC (10/10)  

__Test 3 passed.__

## Test 3 Student Output:

Welcome to my PC shop!  


Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's start building your PC!  

First, let's pick a CPU.  
1 : Intel Core i7-11700K, $499.99  
2 : AMD Ryzen 7 5800X, $312.99  
Choose the number that corresponds with the part you want:   
Next, let's pick a compatible motherboard.  
2 : MSI Z490-A PRO, $262.3  
Choose the number that corresponds with the part you want:   
Next, let's pick your RAM.  
1 : 16 GB, $82.99  
2 : 32 GB, $174.99  
Choose the number that corresponds with the part you want:   
Next, let's pick your PSU.  
1 : Corsair RM750, $164.99  
Choose the number that corresponds with the part you want:   
Next, let's pick your case.  
1 : Full Tower (black), $149.99  
2 : Full Tower (red), $149.99  
Choose the number that corresponds with the part you want: Choose the number that corresponds with the part you want:   
Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).  
1 : 250 GB, $69.99  
2 : 500 GB, $93.99  
3 : 4 TB, $219.99  
Choose the number that corresponds with the part you want (or X to not get an SSD):   
Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).  
1 : 500 GB, $106.33  
2 : 1 TB, $134.33  
Choose the number that corresponds with the part you want (or X to not get an HDD):   
Finally, let's pick your graphics card (or X to not get a graphics card).  
1 : MSI GeForce RTX 3060 12GB, $539.99  
Choose the number that corresponds with the part you want:   
You have selected all of the required parts! Your total for this PC is $1380.25  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's pick a pre-built PC!  

Which prebuilt would you like to order?  
1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99  
2 : SkyTech Prism II Gaming PC, $2839.99  
3 : ASUS ROG Strix G10CE Gaming PC, $1099.99  
Choose the number that corresponds with the part you want:  
Your total price for this prebuilt is $3699.99  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? [1380.25, 3699.99]  

## Test 3 Expected Output:

input:   
1, 1, 2, 1, 1, x, 2, 3, x, X, 2, 1, 3

output:  
[1380.25, 3699.99]  

# TEST CASE 4 - Order build a custom PC (10/10)  

__Test 4 passed.__

## Test 4 Student Output:

Welcome to my PC shop!

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's start building your PC!  

First, let's pick a CPU.  
1 : Intel Core i7-11700K, $499.99  
2 : AMD Ryzen 7 5800X, $312.99  
Choose the number that corresponds with the part you want:   
Next, let's pick a compatible motherboard.  
1 : MSI B550-A PRO, $197.46  
Choose the number that corresponds with the part you want:   
Next, let's pick your RAM.  
1 : 16 GB, $82.99  
2 : 32 GB, $174.99  
Choose the number that corresponds with the part you want:   
Next, let's pick your PSU.  
1 : Corsair RM750, $164.99  
Choose the number that corresponds with the part you want: Choose the number that corresponds with the part you want:   
Next, let's pick your case.  
1 : Full Tower (black), $149.99  
2 : Full Tower (red), $149.99  
Choose the number that corresponds with the part you want:  
Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).  
1 : 250 GB, $69.99  
2 : 500 GB, $93.99  
3 : 4 TB, $219.99  
Choose the number that corresponds with the part you want (or X to not get an SSD):  
Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).  
1 : 500 GB, $106.33  
2 : 1 TB, $134.33  
Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD):   
Finally, let's pick your graphics card (or X to not get a graphics card).  
1 : MSI GeForce RTX 3060 12GB, $539.99  
Choose the number that corresponds with the part you want:  
You have selected all of the required parts! Your total for this PC is $1014.75  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?  
[1014.7500000000001]

## Test 4 Expected Output:

input:  
1, 2, 1, 1, 2, 1, 1, x, X, 1, x, 3

output:  
[1014.75]  

# TEST CASE 5 - Order build a custom PC (10/10)

__Test 5 passed.__

## Test 5 Student Output:

Welcome to my PC shop!

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?   
Great! Let's start building your PC!  

First, let's pick a CPU.  
1 : Intel Core i7-11700K, $499.99  
2 : AMD Ryzen 7 5800X, $312.99  
Choose the number that corresponds with the part you want:  
Next, let's pick a compatible motherboard.  
2 : MSI Z490-A PRO, $262.3  
Choose the number that corresponds with the part you want:   
Next, let's pick your RAM.  
1 : 16 GB, $82.99  
2 : 32 GB, $174.99  
Choose the number that corresponds with the part you want: Choose the number that corresponds with the part you want:  
Next, let's pick your PSU.  
1 : Corsair RM750, $164.99  
Choose the number that corresponds with the part you want:  
Next, let's pick your case.  
1 : Full Tower (black), $149.99  
2 : Full Tower (red), $149.99  
Choose the number that corresponds with the part you want:   
Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).  
1 : 250 GB, $69.99  
2 : 500 GB, $93.99  
3 : 4 TB, $219.99  
Choose the number that corresponds with the part you want (or X to not get an SSD):   
Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).  
1 : 500 GB, $106.33  
2 : 1 TB, $134.33  
Choose the number that corresponds with the part you want (or X to not get an HDD):   
Finally, let's pick your graphics card (or X to not get a graphics card).  
1 : MSI GeForce RTX 3060 12GB, $539.99  
Choose the number that corresponds with the part you want:   
You have selected all of the required parts! Your total for this PC is $1486.58  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?  
Great! Let's pick a pre-built PC!  

Which prebuilt would you like to order?  
1 : Legion Tower Gen 7 with RTX 3080 Ti, $3699.99  
2 : SkyTech Prism II Gaming PC, $2839.99  
3 : ASUS ROG Strix G10CE Gaming PC, $1099.99  
Choose the number that corresponds with the part you want:  
Your total price for this prebuilt is $3699.99  

Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)?  
[1486.58, 3699.99]

# Test 5 Expected Output:

input:  
1, 1, 2, x, 1, 1, 1, 3, 1, x, 2, 1, 3

output:  
[1486.58, 3699.99]