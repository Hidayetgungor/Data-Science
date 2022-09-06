import pandas as pd

df = pd.read_csv('GBvideos.csv')

#First 10 records
#result = df.head(10)

#Second 5 records
#result = df[5:20].head(5)

#Columns's names and lengths
#result = df.columns
#result = len(df.columns)

#List of columns without "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed"
#df = df.drop(["thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed"], axis=1)

#The average of the number of likes
#result = df["likes"].mean()

#Likes and dislikes column of first 50 records
#result = df.head(50)[["title", "likes", "dislikes"]]

#The most viewed video
#result = df[df["views"].max() == df["views"]][["title","views"]]

#The least viewed video
#result = df[df["views"].min() == df["views"]]["title"].iloc[0]

#Top 10 most viewed videos
#result = df.sort_values("views", ascending=False)[["title","views"]].head(10)

#Average of likes by category
#result = df.groupby("category_id").mean().sort_values("likes")["likes"]

#Sorting by category from top to bottom
#result = df.groupby("category_id").sum().sort_values("comment_count", ascending=False)["comment_count"]

#videos in the category
#result = df["category_id"].value_counts()

#Number of tags of each videos
#df["tag_count"] = df["tags"].apply(lambda x: len(x.split('|')))
#or
#def tagCount(tag):
#    return len(tag.split('|'))

#df["tag_count"] = df["tags"].apply(tagCount)

#list of the most popular videos by the rate of likes/dislikes
'''
def likedislikeratiocalculator(dataset):
    likeList = list(dataset["likes"])
    dislikeList = list(dataset["dislikes"])

    liste = list(zip(likeList,dislikeList))

    oranlistesi = []

    for like,dislike in liste:
        if (like + dislike) == 0:
            oranlistesi.append(0)
        else:
            oranlistesi.append(like/(like+dislike))
    return oranlistesi

df["like_ratio"] = likedislikeratiocalculator(df)

print(df.sort_values("like_ratio",ascending=False))
'''

#print(df)
#print(result)