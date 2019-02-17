Role for install and configuration docker on ubuntu
=========

Install docker
Change default logging driver to json
Create image from Dockerfile with weather.py
Run container

Requirements
------------


Role Variables
--------------
You can set the following variables:
version and package docker
name image, tag
log_driver for docker
env variables city_name and api_key

Dependencies
------------


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    ---
    
    - hosts: all
      become: yes
      gather_facts: true

      roles:
       - docker_install

License
-------

BSD

Author Information
------------------
bakyrskiy@gmail.com
