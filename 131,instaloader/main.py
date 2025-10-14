import instaloader

l=instaloader.Instaloader()
# l.login('samoraii_tanha','125852')
profile=instaloader.Profile.from_username(l.context,'samoraii_tanha')
# print(profile.followers)
# print(profile.followees)
# print(profile.get_profile_pic_url())
# print(profile.is_private)
# print(profile.is_verified)
# print(profile.biography)
# print(profile.get_posts())
for post in profile.get_posts():
    print(post.likes)

# for i in profile.get_similar_accounts():
#     print(i.username)