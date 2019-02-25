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

    # create empty variable
    email = ""

    # read each line and see if email can be found
    for line in lines_lst:
        # remove the leading and trailing spaces and removing the \n
        line_strip = line.strip()

        # Make sure the email string begins with a normal lowercase English character
        # between the ‘@’ and the ending (’.com’ or the ’.edu’)
        # There should be no digits or numbers in the email address.
        if line_strip.find("@") != -1 and line_strip[:1].isalpha() and line_strip[:1].islower() \
                and (line_strip[-4:] == ".com" or line_strip[-4:] == ".edu")\
                and any(i.isdigit() for i in line_strip) is False:
            email = line_strip

    return email



def extract_courses(lines_lst):
    '''Extract the courses from the content list'''

    # create empty variable
    courses = ""

    # read each line and see if courses can be found
    for line in lines_lst:
        # remove the leading and trailing spaces and removing the \n
        line_strip = line.strip()

        # find the line of courses in case "Courses"
        index = line_strip.find("Courses")
        if index != -1:
            # get the substring of the string after "Courses".
            # index+8 because there are 7 characters in "Courses"
            courses = line_strip[index+8:]

            # find the first char after "Courses"
            i = -1
            for char in courses:
                i = i + 1
                if char.isalpha():
                    break

            # get the substring starting from the first char after "Courses"
            courses = courses[i:]

    return courses


def main():
    lines_lst = read_file("resume.txt")
    print(lines_lst)

    name = extract_name(lines_lst)
    print(name)

    email = extract_email(lines_lst)
    print(email)

    courses = extract_courses(lines_lst)
    print(courses)

    # print("123.".isdigit())
    # print("@.".isalpha())
    # print(any(i.isdigit() for i in "1asd@com.tw"))
    # print("Courses :- Programming Languages and Techniques, Biomedical image analysis, ".find("Courses"))

if __name__ == '__main__':
    main()

