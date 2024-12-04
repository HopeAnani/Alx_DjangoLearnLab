Comment System Documentation
Objective
The comment system allows users to post, edit, and delete comments on blog posts. It enhances the interactivity of the blog, enabling users to share their thoughts, engage in discussions, and interact with content more effectively. Authenticated users can post, edit, and delete their comments, while unauthenticated users are limited to viewing comments.

Models
Comment Model
The Comment model defines the structure of a comment in the blog application. Each comment is associated with a specific blog post and an authenticated user. It contains the following fields:

post: ForeignKey(Post)
A reference to the Post model, indicating which blog post the comment belongs to. This creates a many-to-one relationship between comments and posts.

author: ForeignKey(User)
A reference to Django’s built-in User model, indicating the user who wrote the comment.

content: TextField
The body of the comment. This is a TextField to accommodate potentially long comment content.

created_at: DateTimeField(auto_now_add=True)
Automatically set to the current date and time when the comment is created. It records when the comment was posted.

updated_at: DateTimeField(auto_now=True)
Automatically set to the current date and time whenever the comment is edited. It tracks when the comment was last updated.