from apiclient.discovery import build



class video:
	def __init__(self,vieww,lc,dlc,comm,idd,uploadd,titlee,tgs,cate,desc,channel,comments_s):
		self.likecount = int(lc)
		self.dislikecount = int(dlc)
		self.comments = int(comm)
		self.vidid = str(idd)
		self.uploaddate = str(uploadd[:-10])
		self.title = str(titlee)
		self.tags =  tgs
		self.categories = str(cate)
		self.viewcount = int(vieww)
		self.desc = str(desc)
		self.channelid  = str(channel)
		self.comments_s = comments_s
	def printt(self):
		print('id  : ' + str(self.vidid))
		print('likecount : ' + str(self.likecount))
		print('dislikecount : ' + str(self.dislikecount))
		print('viewcount : ' + str(self.viewcount))
		print('comment count : ' + str(self.comments))
		print('title : ' + str(self.title))
		print('tags : ' + str(self.tags))
		print('category id : ' + str(self.categories))
		print('upload date : ' + str(self.uploaddate))
		print('description : ' + str(self.desc[:30] + " . . ."))
		print('Channel : ' + str(self.channelid))
		print('duationn   : ' + str(self.comments_s))



class channel:
	def __init__(self,id,name,description,subs,playlist,date1):
		self.channel_id = id
		self.name = name
		self.description = description
		self.subs = subs
		self.playlist = playlist
		self.channelstartdate = date1
	def printt(self):
		print("id : " + str(self.channel_id))
		print("name  : " + str(self.name))
		print("description : " + str(self.description))
		print("subs : " + str(self.subs))
		print("playlist : " + str(self.playlist))
		print("publish date : " + str(self.channelstartdate))

def get_videos_from_playlist(playlist_id,ytube,n):
    k1,k2 = getvideosfromplaylistutility(playlist_id,50,ytube,False)
    run = n
    l = []
    for i in k1 :
        l.append(i)
    for j in range (run):
        m1,m2 = getvideosfromplaylistutility(playlist_id,50,ytube,k2)
        for i in m1 :
            l.append(i)
        k2 = m2
    return(l)

def getvideosfromplaylistutility(id1,number,ytube,token):
    l = []
    if(token):
	    req = ytube.playlistItems().list(playlistId = id1 ,part = 'snippet',maxResults = number, pageToken = token).execute()
    else :
        req = ytube.playlistItems().list(playlistId = id1 ,part = 'snippet',maxResults = number).execute()
    for j in req['items']:
	    l.append(j['snippet']['resourceId']["videoId"])
    if("nextPageToken" in req):
        return(l,req["nextPageToken"])
    else :
        return(l,False)


def getchannelvids(channel_id,ytube):
	res = ytube.channels().list(id=channel_id,part='contentDetails').execute()
	playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
	return(playlist_id)

def videostats(id1,ytube,partt):
	#'snippet', 'statistics', 'contentDetails', 'topicDetails
	res = ytube.videos().list(id=id1,part=partt)
	respo = res.execute()
	return respo

def getvid(id1,ytube):
	try:
		res = ytube.videos().list(id=id1,part='statistics').execute()
		res2 = ytube.videos().list(id=id1,part='snippet').execute()
		#res3 =  ytube.videos().list(id=id,part="contentDetails").execute()
		res3 = getdur("ioNng23DkIM",ytube)
		v1 = video(res['items'][0]['statistics']['viewCount'],res['items'][0]['statistics']['likeCount'],res['items'][0]['statistics']['dislikeCount'],res['items'][0]['statistics']['commentCount'],id1,res2['items'][0]['snippet']['publishedAt'],res2['items'][0]['snippet']['title'],res2['items'][0]['snippet']['tags'],res2['items'][0]['snippet']['categoryId'],res2['items'][0]['snippet']['description'],res2['items'][0]['snippet']['channelId'],res3)
		return(v1)
	except:
		print("error")

def channelinfo(channel_id,ytube):
	res = ytube.channels().list(id=channel_id,part='snippet')
	resp = res.execute()
#	id,name,description,subs,playlist,date1
	c1 = channel(channel_id,resp["items"][0]["snippet"]["title"],resp["items"][0]["snippet"]["description"],0,getchannelvids(channel_id,ytube),resp["items"][0]["snippet"]["publishedAt"])
	return c1


#print(videostats('SB5_UrnQiNE',ytube,'topicDetails'))  https://developers.google.com/youtube/v3/determine_quota_cost


def getdur(id,ytube):
	res = ytube.videos().list(id=id,part="contentDetails")
	respo = res.execute()

	return(respo['items'][0]['contentDetails']['duration'])


keyy = "AIzaSyDQYim9i4xRwRCBjh64OAmTDLyuN7kbqIY"
ytube = build('youtube','v3',developerKey = keyy)
