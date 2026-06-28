import re
import sys


def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"{filename} file not found")
        print("Please make sure the file exists!")
        sys.exit(1)


def extract_emails(content):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern ,content)
    return emails


def save_emails(emails):
    with open("output.txt", "w") as output_file:
        for email in emails:
            output_file.write(email + "\n")


def print_summary(total_emails,unique_emails):
    print("\n===== Email Extraction Summary =====")
    print(f"Total email addresses found : {total_emails}")
    print(f"Unique email addresses      : {unique_emails}")
    print("Output saved to             : output.txt")
    print("====================================")


def main():
    content = read_file("input.txt")
    emails = extract_emails(content)
    total_emails = len(emails)
    emails = list(dict.fromkeys(emails))
    unique_emails = len(emails)
    save_emails(emails)

    if unique_emails == 0:
        print("No email addresses were found.")
    else:
        print_summary(total_emails, unique_emails)


if __name__ == "__main__":
    main()