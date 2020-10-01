def produce_summary(day, filename):
    """Generate report of melon deliveries for a specified day
    
    produce_summary takes in the day and the report txt file, iterates
    through each line of report, processes the data, and prints out 
    delivery report for that day.
    """

    # Print day number as header
    print(f"Day {day}")

    # Open file
    report = open(filename)

    # Iterate through each line of txt file
    for line in filename:

        # Strip last space off and split string input to a list delimited by '|'
        line = line.rstrip()
        words = line.split('|')

        # Store melon name, count sold, and total amount sold in $ into variables
        melon = words[0]
        count = words[1]
        amount = words[2]

        # Print out report of deliveries in a formatted fashion
        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
    
    # Close report
    report.close()

# Calling produce_summary for days 1, 2, 3 to generate their delivery reports
produce_summary(1, "um-deliveries-20140519.txt")
produce_summary(2, "um-deliveries-20140520.txt")
produce_summary(3, "um-deliveries-20140521.txt")
