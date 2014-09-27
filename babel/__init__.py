from __future__ import absolute_import

def main():
    from babel.base import args, fail
    import re

    if re.match(r"https?://.*", args.TO):
        import babel.http
    elif re.match(r"(\+\d{1,3})?\d{10}|\d{3}-\d{3}-\d{4}", args.TO):
        import babel.sms
    else:
        fail("Couldn't parse recipient address.")

if __name__ == "__main__": main()