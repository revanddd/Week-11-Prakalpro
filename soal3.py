email_counts = {}

with open("mbox-short.txt", "r") as file:
    for line in file:
        if line.startswith("From "):
            sender_email = line.split()[1]
            email_counts[sender_email] = email_counts.get(sender_email, 0) + 1

print(email_counts)