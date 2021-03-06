Brandon Balkaransingh
Project Worksheet – Project Four – Final Project - Backend
SEI-pineapple

Project Schedule:
|Day|Deliverable|Status|
|---|-----------|------|
|Day 1|Project Worksheet|Complete|
|Day 1|Models, views, routes for auth and API|Complete|
|Day 2|Test locally on postman; debug|Ongoing|
|Day 2|Test heroku app on postman; debug|Incomplete|

Project Description:
This is the backend repo for a gamesite app. Basically, it would be like one of those free game sites where you can play games on your computer. The difference is that you would have to log in and actually save the links to the games you want to play. One could also make their own games (or their own versions) and save them on here to show to prospective employers, an additional project showcase if you will.



Project link: 
GitHub Repo: https://github.com/bbalkaransingh23888/p4backend.git
Google Sheet link: https://docs.google.com/spreadsheets/d/1MiYUM5Rr0hr_9kbYVNgYzxu88jngsMA9udl1Ox-z7Vw/edit#gid=0


Models: 

User Model:

```
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # *** REQUIRED_FIELDS = ['email', 'first_name', 'last_name'] ***

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.username

```

Category Model:

```
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

Games Model: 

```
class Game(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image_url = models.URLField
    description = models.TextField(blank=True)
    additional info = models.CharField(max_length=5000)
    added = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)
```

Time-Priority Index: 
https://docs.google.com/document/d/1Je7uT1pui2FGCPIXbU3q9nWZWM12zFAUZNWysSR4OQ8/edit

MVP list:
1)	Full CRUD for both models w/ routes
2)	local API, postman-tested
3)	backend API deployed to heroku, post-man tested
4)  Connect frontend and backend
5)  Authentication

Post-MVP list:
None atm (will update this at a later point)

Functional Components: 

MVP:

|Component|Priority|Est. Time|Time Invested|Actual Time|
|---------|--------|---------|-------------|-----------|
|Full CRUD for both models w/ routes|High|4 Hrs.||| 		
|Connect frontend and backend|High|4 Hrs.||| 		
|local API, postman-tested|High|2 Hrs.||| 		
|backend API deployed to heroku, post-man tested|High|3 Hrs.||| 
|Authentication with models, necessary views, routes, etc.|High|4 Hrs.|||			
		

Post-MVP:

|Component|Difficulty|Est. Time|Time Invested|Actual Time|
|---------|--------------------|---------|-------------|-----------|

Additional Libraries:
1) rest_framework
2) Django Rest Framework - JWT