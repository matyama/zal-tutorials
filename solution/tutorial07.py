#!/usr/bin/env python3

from utils.text_utils import similar_texts


class Car:
    def __init__(self, rep, brand):
        self.rep = rep
        self.brand = brand

    def __str__(self):
        return 'Car(rep=%d,brand=%s)' % (self.rep, self.brand)

    def set_brand(self, brand):
        self.brand = brand


class Article:
    def __init__(self, url, title, content, hrefs=list()):
        self.url = url
        self.title = title
        self.content = content
        self.hrefs = hrefs

    def __str__(self):
        return '%s:\n%s' % (self.title, self.content)

    def __repr__(self):
        return self.__str__()


class ArticleDB:
    """
    Class representing a database of *Articles*. Represent this database as a dictionary which stores instances of
    *Articles* as values with keys being the respective article URLs.
    """

    def __init__(self):
        self.web = dict()

    def add_article(self, article):
        """
        Add given *article* to this database.

        :param article: instance of an *Article*
        """
        self.web[article.url] = article

    def referenced_articles(self, url):
        """
        Return a *list* with instances of all articles referenced from an article with given *url*.

        :param url: url string of an article
        :return: list of articles referenced from given *url*
        """
        return [self.web[article_url] for article_url in self.web[url].hrefs if article_url in self.web] \
            if url in self.web else []


class Student:
    STATUS = {0: 'clean', 1: 'yellow card', 2: 'red card'}

    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.num_plagiarisms = 0

    def __str__(self):
        return '%s (%s)' % (self.name, self.username)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return other and isinstance(other, Student) and self.username == other.username

    def report_plagiarism(self):
        self.num_plagiarisms += 1

    def get_status(self):
        return Student.STATUS.get(self.num_plagiarisms, Student.STATUS[max(Student.STATUS.keys())])


class Program:
    def __init__(self, course, assignment, author, code):
        self.course = course
        self.assignment = assignment
        self.author = author
        self.code = code

    def __str__(self):
        return '%s -- %s -- %s :\n%s\n' % (self.course, self.assignment, self.author, self.code)

    def __repr__(self):
        return self.__str__()

    def similar_to(self, other):
        return self.course == other.course and self.assignment == other.assignment and self.author != other.author and \
               similar_texts(self.code, other.code)


class PlagiarismDetection:
    def __init__(self):
        self.queue = []

    def add_program(self, program):
        self.queue.append(program)

    def init(self, programs):
        for p in programs:
            self.add_program(p)

    def empty_queue(self):
        self.queue = []

    def get_plagiarisms(self):
        return [(p1, p2) for i, p1 in enumerate(self.queue) for j, p2 in enumerate(self.queue) if
                i < j and p1.similar_to(p2)]

    def run(self):
        for p1, p2 in self.get_plagiarisms():
            p1.author.report_plagiarism()
            p2.author.report_plagiarism()
        self.empty_queue()


if __name__ == '__main__':

    # ---- Example: Car ----
    print('---- Example: Car ----')

    # test car
    car = Car(1, 'BMW')
    print(car)

    # test set brand
    car.set_brand('AUDI')
    print(car)

    # ---- Example: Article Database ----
    print('\n---- Example: Article Database ----')

    # create some articles
    a1 = Article('http://article-web/article/01', 'My first article', 'This is super long text',
                 ['http://article-web/article/02', 'http://article-web/article/03'])

    a2 = Article('http://article-web/article/02', 'Breaking News!', 'Scala is better than Java.',
                 ['http://article-web/article/04'])

    a3 = Article('http://article-web/article/03', "Programmer's Guide", 'C is faster than Java.', [])

    a4 = Article('http://article-web/article/04', "Programmer's Guide: Part 2", 'Do not ever code in PHP!', [])

    articles = [a1, a2, a3, a4]

    # add articles to the database
    db = ArticleDB()
    for article in articles:
        db.add_article(article)

    # retrieve referenced articles from the database
    print(db.referenced_articles('http://article-web/article/01'))
    print(db.referenced_articles('http://article-web/article/02'))
    print(db.referenced_articles('http://article-web/article/03'))

    # ---- Example: Simple Plagiarism Detection ----
    print('\n---- Example: Simple Plagiarism Detection ----')

    # create three students: Alice, Bob and Charlie
    alice = Student('Alice', 'alice1')
    bob = Student('Bob', 'bob5')
    charlie = Student('Charlie', 'charlie')

    students = [alice, bob, charlie]

    # first show all enrolled students
    print('\nstudents:')
    for student in students:
        print('%s : %s' % (student, student.get_status()))

    # instantiate students' programs
    p1 = Program('B6B36ZAL', 'HW01', alice,
                 'import sys\n\n\nif __name__ == "__main__":\n\tsys.stdout.write("Hello World!\\n")\n')
    p2 = Program('B6B36ZAL', 'HW01', bob, 'print("Hello World!")\n')
    p3 = Program('B6B36ZAL', 'HW01', charlie, 'print("Hello World!\\n")\n')

    p4 = Program('B6B36ZAL', 'HW02', alice,
                 'def factorial(n):\n\tif n < 0:\n\t\traise ValueError("n! is undefined for n < 0")\n\tf = 1' +
                 '\tfor i in range(n, 1, -1):\n\t\tf *= i\n\treturn f\n')
    p5 = Program('B6B36ZAL', 'HW02', bob,
                 'def factorial(n):\n\n\tdef rec(n):\n\t\treturn 1 if n <= 1 else n * rec(n - 1)\n\n\treturn rec(n)\n')
    p6 = Program('B6B36ZAL', 'HW02', charlie,
                 'def factorial(n):\n\tif n < 0:\n\t\traise ValueError("n! is undefined for n < 0")\n\n' +
                 '\tdef loop(n, acc):\n\t\treturn acc if n <= 1 else loop(n - 1, n * acc)\n\n\treturn loop(n, 1)\n')

    uploaded_programs = [p1, p2, p3, p4, p5, p6]

    # display the programs
    print('\nuploaded programs:')
    for program in uploaded_programs:
        print(program)

    # run the plagiarism detection
    print('\nrun plagiarism detection:')
    pd = PlagiarismDetection()
    pd.init(uploaded_programs)
    pd.run()

    # show evaluated students
    print('\nstudents after PD:')
    for student in students:
        print('%s : %s' % (student, student.get_status()))
