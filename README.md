## DesignConnect: A Social Network Platform for Designer Community

#### Implemented RESTful APIs for designers’ accounts, posts, comments, friendships, likes, notifications, and newsfeedsbased on Django Rest Framework.
#### Utilized push model to fanout newsfeeds, and utilize Redis as Message Queue Broker to deliver asynchronized tasks.
#### Utilized Redis to cache lists of posts and newsfeeds, and utilize Memcached to cache followers, accounts and posts.
#### Utilized MySQL, HBase, and Amazon S3 to store data.
#### Utilized denormalization to store numbers of comments and likes to reduce database queries.
