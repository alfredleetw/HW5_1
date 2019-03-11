import csv


def read_file(file):
    '''Read from a text file and store all the content line by line into a list.'''

    # open file
    stream = open(file, "r")
    # read lines and store as a list
    lines_lst = stream.readlines()

    # close stream
    stream.close()

    return lines_lst


def extract_name(resume_lst):
    '''Extract the name from the content list and return as string'''

    # Extract the first line, remove the leading and trailing spaces and removing the \n
    name = resume_lst[0].strip()

    # Raise a RuntimeError if the first character in the name string is not an uppercase letter (capital ’A’ through ’Z’).
    if name[:1].islower():
        raise RuntimeError('The first line has to be a name with proper capitalization.')

    return name


def extract_email(resume_lst):
    '''Extract the email from the content list and return as string'''

    # create empty variable
    email = ""

    # read each line and see if email can be found
    for line in resume_lst:
        # remove the leading and trailing spaces and removing the \n
        line_strip = line.strip()
        # find the location of @
        location_at = line_strip.find("@")

        # Make sure the email string begins with a normal lowercase English character
        # between the ‘@’ and the ending (’.com’ or the ’.edu’)
        # There should be no digits or numbers in the email address.
        if location_at != -1 and line_strip[:1].isalpha() and line_strip[location_at+1:location_at+2].islower() \
                and (line_strip[-4:] == ".com" or line_strip[-4:] == ".edu")\
                and any(i.isdigit() for i in line_strip) is False:
            email = line_strip

    return email


def extract_courses(resume_lst):
    '''Extract the courses from the content list and return as string'''

    # create empty variable
    courses = ""

    # read each line and see if "Courses" can be found
    for line in resume_lst:
        # remove the leading and trailing spaces and removing the \n
        line_strip = line.strip()

        # find the line of courses
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


def extract_projects(resume_lst):
    '''Extract the projects from the content list and return as list'''

    # create empty list
    projects = []

    # read each line and see if "Projects" can be found
    i = -1
    for line in resume_lst:
        i = i+1
        index = line.find("Projects")
        if index != -1:
            # loop through lines_lst starting from the next line of "Projects"
            for project in resume_lst[i+1:]:
                # remove the leading and trailing spaces and removing the \n
                project_strip = project.strip()

                # add project before seeing "----------"
                if project.find("----------") == -1:
                    # excluding empty line
                    if project_strip != "":
                        projects.append(project_strip)
                else:
                    break

    return projects


def surround_block(tag, text):
    '''This function surrounds the given text with the given HTML tag and returns the string'''

    return '<'+tag+'>'+text+'</'+tag+'>'


def create_email_link(email_address):
    '''This function creates an email link with the given email_address
    To cut down on spammers harvesting the email address from your webpage,
    this function should display the email address with an [aT] instead of an @
    '''

    return '<a href=\"mailto:' + email_address + '\">' + email_address.replace('@', '[aT]') + '</a>'


def create_resume_intro(resume_lst):
    '''This function is to create the entire intro section of the resume and return as string.'''

    name = extract_name(resume_lst)
    email_link = create_email_link(extract_email(resume_lst))

    intro = "\n" + surround_block("h1", name) + "\n" + surround_block("p", "Email: " + email_link) + "\n"
    intro = surround_block("div", intro)

    return intro


def create_resume_project(resume_lst):
    '''This function is to create the entire project section of the resume and return as string.'''

    # Extract projects
    projects = extract_projects(resume_lst)

    # Create empty variable
    project = ""

    # Add li tag to each project
    for pj in projects:
        project += "\n" + surround_block("li", pj)

    project += "\n"

    # Add other required components
    project = "\n" + surround_block("h2", "Projects") + "\n" + surround_block("ul", project) + "\n"
    project = surround_block("div", project)

    return project


def create_resume_course(resume_lst):
    '''This function is to create the entire course section of the resume and return as string.'''

    # Extract courses
    courses = extract_courses(resume_lst)

    # Write course section into string as required
    course = "\n" + surround_block("h3", "Courses") + "\n" + surround_block("span", courses) + "\n"
    course = "\n" + surround_block("div", course) + "\n"

    return course


def main():
    # read resume.txt
    resume_lst = read_file("resume.txt")

    # Open and read resume-template.html
    # Read every line of HTML
    html_lst = read_file("resume_template.html")

    # Remove the last 2 lines of HTML
    html_lst.pop()
    html_lst.pop()

    # Write the final HTML to a new file resume.html; will create new file if not exist
    file_out = open('resume.html', 'w')

    # Add template
    file_out.writelines("%s" % line for line in html_lst)

    # Add all HTML-formatted resume content
    # Create a div tag
    file_out.write("<div id=\"page-wrap\">\n")

    # Add basic information
    file_out.write(create_resume_intro(resume_lst))
    file_out.write("\n")

    # Add project
    file_out.write(create_resume_project(resume_lst))

    # Add courses
    file_out.write(create_resume_course(resume_lst))

    # Close the div tag
    file_out.write("</div>\n")

    # Add the last 2 lines of HTML back in
    file_out.write("</body>\n")
    file_out.write("</html>\n")

    # Close the file
    file_out.close()


    '''
    print(resume_lst)

    name = extract_name(resume_lst)
    print(name)

    email = extract_email(resume_lst)
    print(email)

    courses = extract_courses(resume_lst)
    print(courses)

    projects = extract_projects(resume_lst)
    print(projects)

    print(create_email_link("tom@seas.upenn.edu"))
    print(create_email_link("tomseas.upenn.edu"))
    '''

if __name__ == '__main__':
    main()

