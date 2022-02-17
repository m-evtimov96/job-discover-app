# job-discover-app
WebApp about searching for job adverts built with django

## Description

The main idea of the project is to operate as platform for job searching. 
You can register as company to add job adverts or as applicant to search for your next job.
When logged in as a company you will be able to edit your profile, add/edit your job adverts
and review applications for them. When you are in the role of an applicant you are
able to browse all companies, visit their profile pages, filter/search in all job adverts
by category/name/salary, and apply to them.

## Main Objects

### User / Profile
JobDiscoverUser - extended from AbstractBaseUser:
* email - username field
* password
* is_active - flag for active user
* is_staff - can login in admin
* is_company - flag for company type
* is_applicant - flag for applicant type

CompanyProfile - one-to-one relationship with JobDiscoverUser
* user - one-to-one rel. used as PK
* name
* description
* bulstat
* website
* company_icon
* company_banner

ApplicantProfile - one-to-one relationship with JobDiscoverUser
* user - one-to-one rel. used as PK
* first_name
* last_name
* bio
* profile_image

Job - model for job advert
* user - foreign-key JobDiscoverUser
* title
* description
* date_created - used in JobList view
* category - category field with predifined choices
* type - multiselect field with predifined choices
* salary
* image

Application - model for applications
* motivational_letter
* cv - file with cv .docx or .pdf
* job - foreign-key to Job
* applicant - foreign-key to ApplicantProfile
* company - foreign-ket to CompanyProfile

## Getting Started

### Dependencies
Needed packages can be found in requirements.txt
* PostrgreSql

## Help

For bugs and help please contact me at my email

## Authors

Author: Martin Evtimov
Contact me at: m.evtimov196@gmail.com

## Version History

* 1.0
    * Initial Release
* 1.1
    * Added reset password functionality

## Acknowledgments

Inspiration, code snippets, etc.
* https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
