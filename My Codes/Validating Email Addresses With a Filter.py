
def fun(s):
    # return True if s is a valid email, else return False
    if "@" and "." in str(s):
        x = s.split("@")
        y = x[1].split(".")
        username = x[0]
        webname = y[0]
        doname = y[1]
        print(username,webname,doname, type(webname), str(webname), str(webname).isalnum())
        if len(doname) >0 and len(doname)<=3:
            print("if")
            if str(webname).isalnum():
                print("web")
                if str(username).isalnum() or "-" in str(username) or "_" in str(username):
                    print("user")
                    return True
    return False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
