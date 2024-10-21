# ansible-project-template

This project is really only for my use only. Its purpose is to quickly get up-and-running with testing various issues using Ansible.

# Pre-Step

- Fill out the `.env` file appropriately
  - Don't forget to uncomment either CONTROLLER_PASSWORD or CONTROLLER_OAUTH2_TOKEN and fill it out

- Export the environment variables

  ```
  export $(cat .env | grep -v '#' | xargs)
  ```

- Install the appropriate collections

  ```
  ansible-galaxy collection install -r collections/requirements.yml
  ```

# Usage

- Create X number of each resource

  ```
  ansible-playbook -i inventory.yml playbook.yml -e 'count=1'
  ```
  ```
  ansible-playbook -i inventory.yml playbook.yml -e 'count=10'
  ```

- Delete X number of each resources

  ```
  ansible-playbook -i inventory.yml playbook.yml -e 'count=1' -e 'delete=True'
  ```
  ```
  ansible-playbook -i inventory.yml playbook.yml -e 'count=10' -e 'delete=True'
  ```

- Only run on one host at a time

  ```
  ansible-playbook -i inventory.yml playbook.yml -e 'count=1' -e 'thottle=true'
  ```