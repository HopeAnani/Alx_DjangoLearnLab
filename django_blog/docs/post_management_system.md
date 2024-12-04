Django Blog Post Management
Introduction
This module allows users to manage blog posts through Create, Read, Update, and Delete (CRUD) operations. Authenticated users can create, edit, and delete posts, while all users can view a list of blog posts and their details.

Features
Create Posts
Authenticated users can create a new blog post with a title and content.

View Posts

A list view displays all blog posts.
A detail view shows the full content of a specific blog post.
Update Posts
Authenticated users can update their own posts.

Delete Posts
Authenticated users can delete their own posts.

Permissions

Only the author of a post can edit or delete it.
Non-authenticated users cannot create, edit, or delete posts but can view posts.


User Guide
Creating a Post
Navigate to /posts/new/.
Fill in the form fields (title, content).
Click Save to create the post.
Viewing Posts
Visit /posts/ to see all blog posts.
Click on a post title to view its full content.
Editing a Post
While logged in, navigate to /posts/<post_id>/edit/.
Update the fields and click Save.
Deleting a Post
Navigate to /posts/<post_id>/delete/.
Confirm the deletion.
Permissions
Authenticated users:
Can create, edit, and delete their own posts.
Non-authenticated users:
Can view posts but cannot create, edit, or delete them.