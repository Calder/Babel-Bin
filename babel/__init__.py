def main():
    # Check args and import other important functions
    from babel.base import args, fail

    # Expand args.TO if it matches an alias
    import babel.aliases

    # Delegate sending based on recipient type
    import re
    if re.match(r"https?://.*", args.TO):
        import babel.http
    elif re.match(r"(\+\d{1,3})?\d{10}|\d{3}-\d{3}-\d{4}", args.TO):
        import babel.sms
    else:
        fail("Couldn't parse recipient address.")

if __name__ == "__main__": main()