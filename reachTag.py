import csv

if __name__ == '__main__':

    """ tagDistribution contains the 99 filtered tags by moon.
        Directly read them from the csv file as save into the tag variable. """
    
    tags = []
    tagDistFilename = "/home/ywanad/Documents/YanWan/GS/reuters/tagDistribution.csv"
    with open(tagDistFilename, "rb") as fr:
        reader = csv.reader(fr)
        for row in reader:
            tags.append(row[0].split('(')[0].strip())
