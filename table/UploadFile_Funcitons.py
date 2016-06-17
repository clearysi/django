__author__ = 'scleary'


def handle_uploaded_file(f):
    d = {}
    with open("/home/scleary/Lab_database/files/"+str(f), 'r') as infile:
        for line in infile:
            parts = line.strip().split(",")
            d[parts[0]] = [parts[1], parts[2], parts[3]]
        return d
