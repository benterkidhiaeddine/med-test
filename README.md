# Description

This is going to be a platform where medical students cas answer Multiple choice questions about different medical subjects called Modules From Anatomy, Physiology to More Clinical Subjects such as Cardiology and Neurology . The Students can choose which Subjects they are going to be tested on, the corresponding years that those questions were created in and the different Chapters from which the questions were derived . This will make it possible for students to Create their own customized revision session.

# Challenges

The data for the multiple choice questions is not available simply for direct usage for a web application and must first be derived from test Files with different formats such as
(.png , .jpeg , and .pdf) and they they need to be corrected , cleaned and organized in a structured matter to store in a SQL database . (Right now I am going with a SQL database because I am using Django and it works best with SQL type database such as PostGresSQL)

# Roadmap

- Create the basic feature for showing to the users a selection menu from where they can select the Subject they want to get tested on , The chapters from which the questions were derived and the different years.

- Once the User selected all the necessary filters he will be shown a interface with the different questions and the choices , he can select whatever choices he wants and click
  confirm to see how many he got right.

- Include Authentication and different Users


