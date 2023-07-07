from instagrapi import Client

with open("credentials.txt",'r') as f:
    username,password = f.read().splitlines()

client = Client()
client.login(username,password) #login to insta ac

#commenting on a post based on hashtag
hashtag = "bookstagram"

#it is going to post recent bookstagram accounts
medias = client.hashtag_medias_recent(hashtag,9)

#iterating over the collection of posts that we got from the hashtap_medias_recent
for i, media in enumerate(medias):
    client.media_like(media.id) #liking the post
    print(f"liked post number {i+1} of hashtap {hashtag}")
    