# VeriTure Tips
By Zeng Hao (Oscar)
	This file is written for the following developers of VeriTure, all the suggestions are based on my development experience and my personal understanding. 

### What is VeriTure
	VeriTure is a platform that provides users with certificates related services. Registered users are able to upload certificates, view existing certificates, verify existing certificates and issue new certificates(issue new certificates is not available now). All the certificates are based on blockchain.
### Current Version
	This is the very first version of VeriTure. This version only contains viewing certificates, uploading certificates and verifying certificates. The site is based on the Django framework and the basic language is python. This version only support those very basic features of VeriTure and may have 
## Develop Tips

### Development system: 
Windows is not recommended for development since lots of commands are not supported by windows system. Developers using Windows may encounter errors related to wrong commands formats, which is hard to solve. Ubuntu system is recommended since it may have better performance. 

### Required main site-packages: 
account(Pinax project), cert-core(which includes two packages), cert-viewer.

### Python version: 
Suggested 3.6.x and before, Django may not work well with python 3.7.x and later. 

### Django Version: 
Suggested 2.0.x and before, Pinax projects may not support Django versions later than 2.1.x. Python 3.7.x and later may not be supported by Pinax projects. 

### Pinax Projects: 
Pinax is a platform that This website is based on the pinax-user-account project. If you want to change the user account information, please refer to the Pinax official website with more detailed information. 
	Website for user-account: https://django-user-accounts.readthedocs.io/en/latest/
	Website for pinax: https://pinaxproject.com/
Besides the user-account project, other pinax projects which are not developed by the first generation are not recommended to deploy. Because according to my personal experience, there is not sufficient information about Pinax projects installation and implementation. Hence, it may take longer time to learn. In addition, some of the projects may not able to implement properly. 

### More information about the site-packages
1.  Cert-core: cert-core includes all the basic elements of the certificates. 
a.	Cert-model: includes how the certificate model is defined and how the json file can be converted into certificates’ module.
b.	Cert-store: includes the function how the certificates can be stored into the mongo Database and read locally stored files. 
c.	The coupling between cert-model and cert-store is very high, try not to use these two packages seperately.

2.	account: This site-package based on basic code inside the project (The app’s name: Django_Veriture), this part is also the homepage of the whole website. The site package itself contains all the logic code of user-account system, including login, sign up, email verification, password modification and so on. Try not to modification the site package if it is possible. You are able to modify the user account information, for example, adding company name to the user account information. Please read through all the information mentioned above about the project before you make any modification.

3.	Cert-viewer: This is the original version of the cert-viewer, which means it may contain the lots of reused code for the current version. It may not be a necessary site-package for the future development. You may need to refer to the original code from this website. This package is based on Flask, hence, some of the functions may not able to perform properly under the Django framework. You may need to break down the code into small parts to operate. 


