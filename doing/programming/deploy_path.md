## Needed Terms
CLI -> Command Line Interface

**STEP1**
Install oc binary in the Jenkins server, you can download it from: https://access.redhat.com/downloads/content/290 (RedHat account is required). Multiple CLI operations need git to be locally installed. 
```{bash, 1steps}
oc login # A Username and password will be needed
oc new-project <projectname>
```

Use `oc config view` to see the actual oc configuration, you can combine many. When you get into a project with `oc project <projectname>` you can use oc status to have a highlevel overview of the components and relationships. 

