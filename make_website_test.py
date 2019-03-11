import unittest

from make_website import *

class Make_Website_Test(unittest.TestCase):

    def setUp(self):
        # create class-wide accessible resume DB
        self.resume_lst = read_file('resume.txt')


    def test_read_file(self):
        self.assertEqual(["Line1\n", "Line2"], read_file("test_read_file.txt"))


    def test_extract_name(self):
        # Normal case with name "Allen Iverson"
        self.assertEqual("Allen Iverson", extract_name(self.resume_lst))

        # Normal case with name "  Allen Iverson  "
        self.assertEqual("Allen Iverson", extract_name(read_file("test_extract_name2.txt")))

        # Error case with name "allen Iverson"
        self.assertRaises(RuntimeError, extract_name, read_file("test_extract_name3.txt"))


    def test_extract_email(self):
        # Normal case with email "Ai.sixers@wharton.upenn.edu"
        self.assertEqual("Ai.sixers@wharton.upenn.edu", extract_email(self.resume_lst))

        # Normal case with email "  Ai.sixers@wharton.upenn.com  "
        self.assertEqual("Ai.sixers@wharton.upenn.com", extract_email(read_file("test_extract_email0.txt")))

        # Error case with email "Ai.sixers@wharton2.upenn.edu"
        self.assertEqual("", extract_email(read_file("test_extract_email1.txt")))

        # Error case with email "Ai.sixers2@wharton.upenn.edu"
        self.assertEqual("", extract_email(read_file("test_extract_email2.txt")))

        # Error case with email "Ai.sixers@Wharton.upenn.edu"
        self.assertEqual("", extract_email(read_file("test_extract_email3.txt")))

        # Error case with email "Ai.sixers@wharton.upenn.abc"
        self.assertEqual("", extract_email(read_file("test_extract_email4.txt")))

        # Error case with no @ present "Ai.sixers[at]wharton.upenn.edu"
        self.assertEqual("", extract_email(read_file("test_extract_email5.txt")))


    def test_extract_courses(self):
        # Normal case with courses "Courses :- Sports Business, Negotiation, Teamwork and Leadership, Sports Analytics, Introduction to R"
        self.assertEqual("Sports Business, Negotiation, Teamwork and Leadership, Sports Analytics, Introduction to R",
                         extract_courses(self.resume_lst))

        # Normal case with courses "  Courses :!-? Sports Business, Negotiation, Teamwork and Leadership, Sports Analytics, Introduction to R  "
        self.assertEqual("Sports Business, Negotiation, Teamwork and Leadership, Sports Analytics, Introduction to R",
                         extract_courses(read_file("test_extract_courses1.txt")))

        # Error case with courses "courses :- Sports Business, Negotiation, Teamwork and Leadership, Sports Analytics, Introduction to R"
        self.assertEqual("", extract_courses(read_file("test_extract_courses2.txt")))


    def test_extract_projects(self):
        # Normal case (with more than 10 minus signs)
        self.assertEqual(["JPMORGAN CHASE & CO. - Summer Analyst, Profiled 5 companies as part of a comprehensive competitor review; compiled data on financial performance, market share, and long-term strategy", "UPENN STUDENT FEDERAL CREDIT UNION - Led an entirely student-run financial institution, managing team of 12 members to develop robust risk management practices and ensure compliance with FRB / NCUA regulations"], extract_projects(self.resume_lst))

        # Normal case with a blank line between project descriptions
        self.assertEqual(["JPMORGAN CHASE & CO. - Summer Analyst, Profiled 5 companies as part of a comprehensive competitor review; compiled data on financial performance, market share, and long-term strategy", "UPENN STUDENT FEDERAL CREDIT UNION - Led an entirely student-run financial institution, managing team of 12 members to develop robust risk management practices and ensure compliance with FRB / NCUA regulations"], extract_projects(read_file("test_extract_projects1.txt")))

        # Normal case with less than 10 minus signs
        self.assertEqual(["JPMORGAN CHASE & CO. - Summer Analyst, Profiled 5 companies as part of a comprehensive competitor review; compiled data on financial performance, market share, and long-term strategy", "UPENN STUDENT FEDERAL CREDIT UNION - Led an entirely student-run financial institution, managing team of 12 members to develop robust risk management practices and ensure compliance with FRB / NCUA regulations", "-------", "Ai.sixers@wharton.upenn.edu"], extract_projects(read_file("test_extract_projects2.txt")))

        # Error case without "Projects"
        self.assertEqual([], extract_projects(read_file("test_extract_projects3.txt")))


    def test_surround_block(self):
        self.assertEqual("<h1>The Beatles</h1>", surround_block('h1', 'The Beatles'))


    def test_create_email_link(self):
        self.assertEqual("<a href=\"mailto:tom@seas.upenn.edu\">tom[aT]seas.upenn.edu</a>",
                         create_email_link('tom@seas.upenn.edu'))


    def test_create_resume_intro(self):
        self.assertEqual("<div>\n<h1>Allen Iverson</h1>\n<p>Email: <a href=\"mailto:Ai.sixers@wharton.upenn.edu\">Ai.sixers[aT]wharton.upenn.edu</a></p>\n</div>",
                         create_resume_intro(self.resume_lst))

    def test_create_resume_project(self):
        self.assertEqual("<div>\n<h2>Projects</h2>\n<ul>\n<li>JPMORGAN CHASE & CO. - Summer Analyst, Profiled 5 companies as part of a comprehensive competitor review; compiled data on financial performance, market share, and long-term strategy</li>\n<li>UPENN STUDENT FEDERAL CREDIT UNION - Led an entirely student-run financial institution, managing team of 12 members to develop robust risk management practices and ensure compliance with FRB / NCUA regulations</li>\n</ul>\n</div>\n",
                         create_resume_project(self.resume_lst))




    def test_create_resume_course(self):
        pass


if __name__ == '__main__':
    unittest.main()