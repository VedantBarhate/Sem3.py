#  Design a dynamic report generator in Python that uses decorators, class methods, and magic methods to customize and format reports. The system should allow users to dynamically define report templates and apply various formatting options. 

def bold(func):
    def inner(*args, **kwargs):
        return f"b**{func(*args, **kwargs)}**b"
    return inner

def itallic(func):
    def inner(*args, **kwargs):
        return f"i//{func(*args, **kwargs)}//i"
    return inner

def underline(func):
    def inner(*args, **kwargs):
        return f"u__{func(*args, **kwargs)}__u"
    return inner

class Report:
    def __init__(self, heading, writer, body):
        self.__heading = heading
        self.__writer = writer
        self.__body = body

    def get_heading(self):
        return self.__heading

    def get_writer(self):
        return self.__writer

    def get_body(self):
        return self.__body

    def __str__(self):
        st = self.__heading + "\n\n" + f"    - {self.__writer}" + "\n\n"
        for b in self.__body:
            st+=b
        return st
    
    def print_report(self):
        print(self.__str__())

@bold
def make_bold(b):
    return b

@itallic
def make_itallic(b):
    return b

@underline
def make_underline(b):
    return b

class Template:
    def __init__(self, format_func):
        self.format_func = format_func

    def apply_template(self, report):
        formatted_heading = self.format_func(report.get_heading())
        formatted_writer = self.format_func(report.get_writer())
        formatted_body = []
        for b in report.get_body():
            formatted_text = self.format_func(b)
            formatted_body.append(formatted_text)

        return Report(formatted_heading, formatted_writer, formatted_body)

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")

    b1 = make_bold("THIS IS A RANDOM ARTICLE")
    b2 = make_itallic("Design a dynamic report generator in Python that uses decorators, class methods, and magic methods to customize and format reports. The system should allow users to dynamically define report templates and apply various formatting options.\n")
    b3 = make_underline("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n")
    b4 = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English.\n"
    body = [b1, b2, b3, b4]

    r1 = Report("Report 007", "Don_Joe", body)
    r1.print_report()

    print("\n____with template____\n")
    template = Template(make_bold)
    formatted_report = template.apply_template(r1)
    formatted_report.print_report()