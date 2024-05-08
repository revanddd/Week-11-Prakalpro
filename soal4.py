domain_counts = {}

with open("mbox-short.txt", "r") as file:
    for line in file:
        if line.startswith("From "):

            sender_email = line.split()[1]

            domain = sender_email.split("@")[1]

            domain_counts[domain] = domain_counts.get(domain, 0) + 1

print(domain_counts)