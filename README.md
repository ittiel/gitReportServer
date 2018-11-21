
# # gitReportServer
Git commits can be done against local repository. 
We want to track each change any developer makes to their repositories, even when they do not wish to push these changes to the “origin” repository (remote repository). 
The task is to create a service that will enable us to see that information, and aggregate the commit data from all users into a central, real time, live log, and show top 3 committers.

## Installation
Build Docker: 
`docker build -t server .`

Run Docker: 
`docker run -p 5000:5000 server`

Connect to UI: 
`http://localhost:5000/`

Update record example: 
> curl --header "Content-Type: application/json"   --request POST  
> --data '{"user":"user1","branch":"branch1", "repository":"repo1", "files":"list of files", "diff":"differences", "commitMsg":"commit
> message"}'  http://localhost:5000/backend

**Notes**
 1. Uses Python 3
 2. Data is saved on local db
	init db: 
> 		python 	  
>       >>> from database import init_db
> 	    >>> init_db()

3. Basic logs are saved also on the docker machine (app.log)
