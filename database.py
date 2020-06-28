import psycopg2
from psycopg2 import sql





#python wrapper to make life even simpler 


#insert into database
def insertvideo(video,datab):
    try:
        connection = psycopg2.connect(user = "inkognito",password = "inkognito",host = "127.0.0.1",port = "5432",database = datab)
        cursor = connection.cursor()
        l = ''
        for j in list(video.tags):
	        l = l + "." + j
        sql_query = """ INSERT INTO video (id,likes,dislikes,views,title,description,comments,tags,categoryid , uploaddate ,channelid)   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_insert = (video.vidid ,video.likecount,video.dislikecount,video.viewcount,video.title,video.desc,video.comments,"a.b.c",video.categories,video.uploaddate,video.channelid)
        
        cursor.execute(sql_query,record_insert)
    except (Exception, psycopg2.Error) as error :
        print(record_insert)
        print ("Error  : ", error)
        
    finally:
        if(connection):
            connection.commit()
            cursor.close()
            connection.close()
            print("done")

#retrieve from database
def retrievevideo(idd,datab):
    try:
        connection = psycopg2.connect(user = "inkognito",password = "inkognito",host = "127.0.0.1",port = "5432",database = datab)
        cursor = connection.cursor()

        sql_query = """ SELECT * FROM video WHERE id  = %s """
        cursor.execute(sql_query,(idd,))
        record = cursor.fetchall()

        if (connection):
            connection.commit()
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        return record
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
        cursor.close()
        connection.close()
        return(-1)

#delete from database
def deletevideo(idd,datab):
    try:
        connection = psycopg2.connect(user = "inkognito",password = "inkognito",host = "127.0.0.1",port = "5432",database = datab)
        cursor = connection.cursor()

        sql_query = """ DELETE  FROM video WHERE id  = %s """
        cursor.execute(sql_query,(idd,))
        if (connection):
            connection.commit()
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
        return True
    except (Exception, psycopg2.Error) as error :
        print ("Error  : ", error)
        cursor.close()
        connection.close()
        return(False)
         
# initialize database    
def setupdatabase(db):
    try:
        connection = psycopg2.connect(user = "inkognito",password = "inkognito",host = "127.0.0.1",port = "5432",database =db)
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE video (id CHAR(11) PRIMARY KEY NOT NULL , likes INT ,dislikes  INT ,views INT ,title TEXT,description TEXT,comments INT,tags TEXT,categoryid TEXT , uploaddate DATE ,channelid CHAR(24) );""")
        cursor.execute(""" CREATE TABLE channel (id CHAR(24) PRIMARY KEY NOT NULL , name TEXT , description TEXT , subs INT,playlistid CHAR(34),playlists TEXT,start_date DATE);""")
    #   cursor.execute("""SELECT * from video""")
        connection.commit() 
        rows = cursor.fetchall()
        print(rows)
        cursor.close()
        connection.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


#print databsae
def print_data(db):
    try:
        connection = psycopg2.connect(user = "inkognito",password = "inkognito",host = "127.0.0.1",port = "5432",database =db)
        cursor = connection.cursor()
        cursor.execute("""SELECT * from video""")
        connection.commit() 
        rows = cursor.fetchall()

    except Exception as e :
        print("ERROR : ")
        print(e)
        rows = []
    finally :
        cursor.close()
        connection.close()
        return rows

#second fetch
def get_vid_by_channel(channel_id,db):
    try:
        connection = psycopg2.connect(user = "inkognito",password = "inkognito",host = "127.0.0.1",port = "5432",database =db)
        cursor = connection.cursor()
        cursor.execute("""SELECT * from video WHERE channelid = %s""" ,(channel_id,))
        rows = cursor.fetchall()
    except Exception as e :
        print("ERROR : ")
        print(e)
        rows = []
    finally :
        cursor.close()
        connection.close()
        return rows


#update database
def update_db(idd,db,param , paramval):
    try:
        connection = psycopg2.connect(user = "inkognito",password = "inkognito",host = "127.0.0.1",port = "5432",database =db)
        cursor = connection.cursor()
        cursor.execute(sql.SQL("UPDATE video SET  {} = %s WHERE  id = %s").format(sql.Identifier(param)),[paramval,idd])
        cursor.execute("""SELECT * from video""")
        rows = cursor.fetchall()
    except Exception as e :
        print("ERROR : ")
        print(e)

    finally :
        connection.commit()
        cursor.close()
        connection.close()

