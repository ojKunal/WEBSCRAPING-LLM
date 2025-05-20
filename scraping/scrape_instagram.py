import instaloader

def download_instagram_content(username: str):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)
    
    for post in profile.get_posts():
        print("DATE:", post.date)
        print("CAPTION:", post.caption[:200])
        print("URL:", post.url)
        break

if __name__ == "__main__":
    download_instagram_content("tripbaecommunity")
