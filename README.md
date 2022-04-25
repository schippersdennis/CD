# Assignment: CD
## Python Flask Calculator

I want to name three components of my solution and explain what they are and how they relate to each other.

## **GitHub Actions**
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, 
and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production. 
To make this all happen i had to create a workflow in my repository by setting up a *.YML file. For this project i made two jobs: Test and Deploy.

**Test**

Before my files are pushed to github they go through the tests I wrote. These tests are important. 
I made a calculator and these calculations need to be very precise. So I want to make sure that these are correct.
To test my code I use the library PYTEST. The project is made in Python and uses the Flask framework.
In order for the test phase to run smoothly, we depend on these libraries and indicate in the *.yml that we need them.
In the pipeline, github actions will run PYTEST and look for test_files.py. The tests written there must pass. If not, it will be rejected and the code will not end up in the repository.

**Deploy**

When the tests have been completed successfully, the project will proceed to the deploy part in the pipeline. 
This piece is connected to my VPS(Digital Ocean) via my self-hosted-runner. The moment a request comes here, 
my runner will take over and go through the last steps in the *.yml. These steps ensure that the right files are placed in the right place on the server.

##  **Action Runners**
***A GitHub-hosted runner is a virtual machine hosted by GitHub with the GitHub Actions runner application installed. 
GitHub offers runners with Linux, Windows, and macOS operating systems. GitHub-hosted runners offer a quicker, simpler way to run your workflows, 
while self-hosted runners are a highly configurable way to run workflows in your own custom environment.*** 


I accidentally opted for a self-hosting runner. On closer examination, setting up a runner that you host yourself on a VPS is basically quite easy, 
but can become very complicated because you can set it up completely to your own taste. So real customization. Not necessary for this assignment and 
the basic settings were sufficient for me. It is quite easy to configure it via a *.sh file. Actually, github tells you exactly which steps you need to go through to get the runner working properly.


##  **VPS (Digital Ocean)**

I had to prepare this server first to be able to host a python project. We set up an HTTP server on the VPS with Gunicorn. 
To make this all connected to outbound connections have to configure Nginx aswell.
When my action-runner is deploying it will put or overwrite the right files in the right places at the last step. After every deploy you want to restart Gunicorn. 
Only then are the updates visible.


## **Problems** 

**Discuss three problems that you encountered along the way and how you solved them.**

**PYTEST**

Testing in the workflow (actions) did not work properly. All tests passed even if they were wrong. It turned out that I had not configured my *.YML correctly.


**Action-runner keeps going offline**

My action runner kept going offline. This was because I had chosen a self hosted action runner. This one worked fine but went offline when I closed the bash. 
I now have this run as a service running on the VPS .

**After deploy on VPS my project didnt update the content**


After deploying on the vps, my new updates were not visible. Apparently I had to restart my Gunicorn server. I have now set this in the settings so that when there is new content, it automatically restarts
