import requests
import json
import time

def fetch_reddit_posts(subreddit, post_count=200):
    base_url = f"https://www.reddit.com/r/{subreddit}/new.json"
    headers = {'User-Agent': 'Python script for subreddit scraping'}
    posts = []
    after = None  
    
    while len(posts) < post_count:
        params = {'limit': 100}
        if after:
            params['after'] = after
        response = requests.get(base_url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error fetching {subreddit}: {response.status_code}")
            break
        
        data = response.json()
        posts.extend(data['data']['children'])
        after = data['data']['after']
        
        if not after:  
            break
        time.sleep(1)  
    
    return posts[:post_count]

def save_posts_to_file(subreddit, posts):
    filename = f"{subreddit}.json"
    with open(filename, 'w') as file:
        json.dump(posts, file, indent=2)
    print(f"Saved {len(posts)} posts to {filename}")

def main():
    subreddits = ["mcgill", "montreal", "programming", "marvel", "mylittlepony", "3Dprinting"]
    post_count = 200
    
    for subreddit in subreddits:
        print(f"Fetching posts for r/{subreddit}...")
        posts = fetch_reddit_posts(subreddit, post_count=post_count)
        save_posts_to_file(subreddit, posts)

if __name__ == "__main__":
    main()
