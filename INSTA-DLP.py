import instaloader
import os

def download_media(username, num_posts):
    loader = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        posts = profile.get_posts()

        # Create an "Instagram" folder if it doesn't exist
        os.makedirs("Instagram", exist_ok=True)
        os.chdir("Instagram")

        # Create a folder for the Instagram username
        os.makedirs(username, exist_ok=True)
        os.chdir(username)

        if num_posts.lower() == 'all':
            for post in posts:
                download_post(loader, post)
        else:
            num_posts = int(num_posts)
            for i in range(num_posts):
                post = next(posts)
                download_post(loader, post)
        print("Media downloaded successfully!")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Invalid username!")

def download_post(loader, post):
    loader.download_post(post, target=post.date_utc.date())
    print("Media saved successfully!")

username = input("Enter Instagram username: ")
num_posts = input("Enter the number of posts to download (Enter 'all' for all posts): ")
download_media(username, num_posts)