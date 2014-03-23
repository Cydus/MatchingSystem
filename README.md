Overview
--------

This is a systemt to help applicants and managers both apply to projects and approve
applications respectively. PMs also get a to create projects and positions. We have some
a list of functionality including ajax features and email notifications outlined in the
achivements section of this readme.

Usage
-----

A demo of the Project Matching System can be access on http://davidball.me

1. You will want to register as a new applicant user and apply for some positions.
2. Log out.
3. Log in as the project manager credentails, username: SarahJ, password: password
4. Approve some of the applications you created and explore the interface.
5. You may want to login as the applicant to see the changes.

Note that an email will be sent to the applicant users email
you when you approve the application, so proivde a working email address if possible.

Local Installation
------------------

To install this project perform a git clone:

$ git clone https://github.com/Cydus/MatchingSystem.git

inside matching_system_project run our script for resetting the db,
(this performs database erase and loads our population script)

$ sh resetdb.sh

A pip requirements.txt has been provided to ensure any depndancies can be met.

Achievements
------------

* Users can browse through positions within projects even if they are not registered yet, but they can't apply unless they are logged in
* Register and Login functionality
* PM can accept applications
* PM can create projects and positions within projects
* Once an applicant sends an application the status is pending until the manager will accept the application
* If the application status has changed, the applicant can see on his account the updated status
* Search functionality
* When a PM creates a new project they must add positions as well to make the project visible  for applicants
* Responsive design for mobile devices
* AJAX functionality, applying does not cause page to refresh or user to lose their position
* Date picker with the appropriate constraints (start date must come before the end date)
* E-mail notification when application is approved
