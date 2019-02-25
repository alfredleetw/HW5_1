import csv


def read_file(file):
    '''Read from a text file and store all the content into a list.'''

    # open file
    stream = open(file)
    # read lines and store as a list
    lines_lst = stream.readlines()

    return lines_lst


def extract_name(lines_lst):
    '''Extract the name from the content list'''

    # Extract the first line, remove the leading and trailing spaces and removing the \n
    name = lines_lst[0].strip()

    # Raise a RuntimeError if the first character in the name string is not an uppercase letter (capital ’A’ through ’Z’).
    if name[:1].islower():
        raise RuntimeError('The first line has to be a name with proper capitalization.')

    return name


def extract_email(lines_lst):
    '''Extract the email from the content list'''

    email = ""

    for line in lines_lst:
        line_strip = line.strip()
        if line_strip.find("@") != -1 and (line_strip[-4:] == ".com" or line_strip[-4:] == ".edu"):
            email = line

    return email


def main():
    lines_lst = read_file("resume.txt")
    print(lines_lst)

    name = extract_name(lines_lst)
    print(name)

    email = extract_email(lines_lst)
    print(email)

if __name__ == '__main__':
    main()

