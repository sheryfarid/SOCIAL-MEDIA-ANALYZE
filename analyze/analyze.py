'''--------------------------------------------SOCIAL MEDIA ANALYZE------------------------------------------------'''
class User:
    def __init__(self):
        self.username = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.followers = int(input("Enter followers: "))

    def display_user_info(self):
        print(f"Username: {self.username}, Age: {self.age}, Followers: {self.followers}")


class Post:
    def __init__(self, author, content, likes=0, comments=None):
        self.author = author
        self.content = content
        self.likes = likes
        self.comments = comments or []

    def display_post_info(self):
        print(f"Author: {self.author}\nContent: {self.content}\nLikes: {self.likes}\nComments: {len(self.comments)}")

    def get_user_input(self):
        self.likes = int(input("Enter likes for the post: "))
        num_comments = int(input("Enter the number of comments: "))
        for _ in range(num_comments):
            comment = input("Enter a comment: ")
            self.comments.append(comment)


class SocialMediaAnalysisTool:
    def __init__(self):
        self.users = []
        self.posts = []

    def add_user(self, user):
        self.users.append(user)

    def add_post(self, post):
        self.posts.append(post)

    def display_user_stats(self):
        print("User Statistics:")
        for user in self.users:
            user.display_user_info()

    def display_post_stats(self):
        print("Post Statistics:")
        for post in self.posts:
            post.display_post_info()

    def analyze_engagement(self):
        print("Analyze Report:")
        total_likes = sum(post.likes for post in self.posts)
        total_comments = sum(len(post.comments) for post in self.posts)
        average_likes_per_post = total_likes / len(self.posts) if len(self.posts) > 0 else 0
        average_comments_per_post = total_comments / len(self.posts) if len(self.posts) > 0 else 0

        print(f"Total Likes: {total_likes}")
        print(f"Total Comments: {total_comments}")
        print(f"Average Likes per Post: {average_likes_per_post}")
        print(f"Average Comments per Post: {average_comments_per_post}")


if __name__ == "__main__":
    
    user1 = User()

    analysis_tool = SocialMediaAnalysisTool()

    analysis_tool.add_user(user1)

    num_posts = int(input("Enter the number of posts: "))
    for _ in range(num_posts):
        post_content = input("Enter post content: ")
        post = Post(user1.username, post_content)
        post.get_user_input()
        analysis_tool.add_post(post)

    analysis_tool.display_user_stats()
    print("\n")

    analysis_tool.analyze_engagement()
cle