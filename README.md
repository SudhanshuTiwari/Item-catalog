## Item-catalog

```
A web application that provides a list of items within a variety of categories.
Integrates third party user registration and authentication(Google/Facebook Auth). 
Authenticated users have the ability to post, edit, and delete their own items.
```
## Set Up

Create a restaurant menu app where users can add, edit, and delete restaurants and menu items in the restaurants.
## Setup and run the project
### Prerequisites
* Python 2.7
* Vagrant
* VirtualBox

### 
1. Install VirtualBox and Vagrant
2. Clone this repo
3. Unzip and place the Item Catalog folder in your Vagrant directory
4. Launch Vagrant
```
$ Vagrant up 
```
5. Login to Vagrant
```
$ Vagrant ssh
```
6. Change directory to `/vagrant`
```
$ Cd /vagrant
```
7. Initialize the database
```
$ Python database_setup.py
```
8. Populate the database with some initial data
```
$ Python menus.py