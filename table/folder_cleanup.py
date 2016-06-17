
import time
from path import path


def delete_tmp_csv():
    days = 1
    time_in_secs = time.time() - (days * 24 * 60 * 60)
    d = path("/home/scleary/Lab_database/files")
    for i in d.walk():
        if i.isfile():
            if i.mtime <= time_in_secs:
                i.remove()
