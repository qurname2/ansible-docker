Role for install and configuration docker on ubuntu
=========

- Install docker
- Change default logging driver to json
- Create image from Dockerfile with weather.py
- Run container


Role Variables
--------------
You can set the following variables:
- version and package docker
- name image, tag
- log_driver for docker
- env variables city_name and api_key

Example Playbook
----------------

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
