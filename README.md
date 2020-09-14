Brandon Balkaransingh
Project Worksheet – Project Four – Final Project - Backend
SEI-pineapple

Project Description:
This is the backend portion for an app that allows a user to input a movie quote and attach it to the movie that it came from. A fellow cohort mate helped me to come up with this idea, so I am very thankful to that person (not a member of this project group)



Project link: 
GitHub Repo: https://github.com/bbalkaransingh23888/p4backend.git
Google Sheet link: https://docs.google.com/spreadsheets/d/1MiYUM5Rr0hr_9kbYVNgYzxu88jngsMA9udl1Ox-z7Vw/edit#gid=0


Models: 

Category Model:

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


Games Model: 

class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='recipes', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    additional info = models.CharField(max_length=5000)
    added = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)


Time-Priority Index: !['Time/Priority Index'](image4.jpeg)

MVP list:
1)	Full CRUD for both models
2)	local API, postman-tested
3)	backend API deployed to heroku, post-man tested
4)  Connect frontend and backend

Post-MVP list:
None atm (will update this at a later point)

Functional Components: 

MVP:

|Component|Priority|Est. Time|Time Invested|Actual Time|
|---------|--------|---------|-------------|-----------|
|Full CRUD for both models|High|4 Hrs.||| 		
|Connect frontend and backend|High|4 Hrs.||| 		
|local API, postman-tested|High|2 Hrs.||| 		
|backend API deployed to heroku, post-man tested|High|3 Hrs.||| 			
		

Post-MVP:

|Component|Difficulty|Est. Time|Time Invested|Actual Time|
|---------|--------------------|---------|-------------|-----------|
