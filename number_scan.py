"""
Auth: Nate Koike
Proj: number_scan.py
Desc: simplify barcode scans into only the necessary numbers
"""
def main():
    # take the numbers from the front or back?
    direction = input("Numbers in front or back (f/b)?\n>>> ").lower()

    # how many digits are important?
    digits = int(input("How many digits are important?\n>>> "))
    
    # a list of barcode numbers
    num_list = []

    # the number from the barcode scan
    scan = input()

    # while the scan is valid (i.e. the user does not ender a blank line)
    while scan != "":
        # a list of indicies to clean
        clean = []
        
        # check if there are any special characters
        for i in range(len(scan)):
            if ord(scan[i]) > 255:
                clean.append(i)

        # clean the indicies
        clean.reverse()
        for i in clean:
            scan = scan[:i] + scan[i:]

        # reverse the scan if we need the first digits
        if 'f' in direction:
            scan = scan[::-1]

        # append the scanned number to the number list
        num_list.append(scan)

        # get a new scanned number
        scan = input()

    # take the last 12 digits
    for i in range(len(num_list)):
        num_list[i] = num_list[i][-digits:]
        
        # reverse the scan if we need the first digits
        if 'f' in direction: 
            num_list[i] = num_list[i][::-1]

        # add a '#' in the beginning to prevent excel from breaking
        num_list[i] = '#' + num_list[i]

    # make a string of the numbers, separated by newlines
    numbers = "\n".join(num_list)

    # print the numbers (debugging)
    # print(numbers)

    # write to a new file with permission to overwrite any data existing in a
    # file of the same name
    file = open("scanned_numbers.txt", "w")
    file.write(numbers)
    file.close()

if __name__ == "__main__":
    main()
