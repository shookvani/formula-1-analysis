This program takes data from a spreadsheet that I have used to calculate the average amount of times a driver has landed in a top-10 (current point-scoring position) since 2018 - averaging the results first across that specfifc season, and then across all the seasons the driver has been active in (has raced at least once) since 2018. For example, while Lewis Hamilton has been active for all the seasons since 2018, Oscar Piastri has only been active since 2023, and so Hamilton's averages will be across all years/races since the start of the 2018 season, where as Oscar Piastri will only have his numbers averaged since the start of the season in 2023. 
The python program first reads the csv file of the data with the information pertinent to the program, and then asks the user if they would like to be presented with the database of drivers represented in the program, or if they would like to simply go ahead and search for a driver using their 3-letter driver key as commonly used when displaying various time results by the FIA / Formula 1. Driver numbers are not used due to the fact that some of these drivers have the same driver number (ex. Sebastian Vettel, Gabriel Bortoleto), and some drivers that have multiple driver numbers (not including the WDC number 1) (ex. Oliver Bearman, Jack Doohan). 
The program then presents the user with the average number of points scored by the driver, and then with the precent likelihood of the driver scoring in each of the top 10 positions, and then averaging that value to find a number to learn the likelihood of the driver placing in the top 10. 
The user can then search for another driver as they wish. 