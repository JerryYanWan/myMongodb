from database import database

if __name__ == '__main__':


    """ directly reach mongodb with database()
        getTags is a function I wrote in the database.py.
        iterating cursor, your can read each item in the db. 
        please extract all the features you want.
        keys in the db are:
        [date, uid, title, tags, ticker, url]
        uid is the hash number to the file. """

    mongoBase = database()
    cursor = mongoBase.getTags()
    id_tag = {}
    for item in cursor:
        uid = item["uid"]
        tags = item["tags"].split(',')
        tags_filter = []
        for tag in tags:
            tags_filter.append(tag.split('(')[0].strip())
        id_tag[uid] = list(set(tags_filter))
