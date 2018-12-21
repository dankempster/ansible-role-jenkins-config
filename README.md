# Ansible Role: Jenkins Configuration

Provides the ability to deploy a configure Jenkins.

This rols is based on [geerkingguy.jenkins](https://github/geerlingguy.jenkins)
infact, it shares a lot of the same variables. You see, this role doesn't
actually install Jenkins, it only configures an existing installation.


## Role Variables

### Jenkins Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    jenkins_hostname: localhost

The system hostname; usually `localhost` works fine. This will be used during setup to communicate with the running Jenkins instance via HTTP requests.

    jenkins_home: /var/lib/jenkins

The Jenkins home directory which, amongst others, is being used for storing artifacts, workspaces and plugins. This variable allows you to override the default `/var/lib/jenkins` location.

    jenkins_http_port: 8080

The HTTP port for Jenkins' web interface.

    jenkins_admin_username: admin
    jenkins_admin_password: admin

Default admin account credentials which will be created the first time Jenkins is installed.

    jenkins_admin_email: ""

Additional admin details used by some plugins.

    jenkins_admin_password_file: ""

Default admin password file which will be created the first time Jenkins is installed as /var/lib/jenkins/secrets/initialAdminPassword

    jenkins_config_plugins: []

Jenkins plugins to be installed automatically during provisioning.

    jenkins_plugins_install_dependencies: true

Whether Jenkins plugins to be installed should also install any plugin dependencies.

    jenkins_plugins_state: present

Use `latest` to ensure all plugins are running the most up-to-date version.

    jenkins_plugin_updates_expiration: 86400

Number of seconds after which a new copy of the update-center.json file is downloaded. Set it to 0 if no cache file should be used.

    jenkins_plugin_timeout: 30

The server connection timeout, in seconds, when installing Jenkins plugins.

    jenkins_url_prefix: ""

Used for setting a URL prefix for your Jenkins installation. The option is added as `--prefix={{ jenkins_url_prefix }}` to the Jenkins initialization `java` invocation, so you can access the installation at a path like `http://www.example.com{{ jenkins_url_prefix }}`. Make sure you start the prefix with a `/` (e.g. `/jenkins`).

    jenkins_connection_delay: 5
    jenkins_connection_retries: 60

Amount of time and number of times to wait when connecting to Jenkins after initial startup, to verify that Jenkins is running. Total time to wait = `delay` * `retries`, so by default this role will wait up to 300 seconds before timing out.

```
jenkins_owner: jenkins
jenkins_group: jenkins
```

```
jenkins_config_executors: 2
```

```
jenkins_security_enabled: true
jenkins_security_deny_read_access: false
jenkins_security_disable_signup: true
jenkins_security_captcha: false
jenkins_security_disable_remember_me: false
```


### Jenkins Credentials

```
# jenkins_credentials_user_pass: []
# jenkins_credentials_ssh_key: []
# jenkins_credentials_secret_file: []
jenkins_credentials_secret_text: []
# jenkins_credentials_certificates: []
```


### Git Variables

```
jenkins_git_installations:
  - name: default
    home: git
jenkins_git_config_name: John Smith
jenkins_git_config_email: john@example.com
```


### Github Variables

```
jenkins_github_enabled: false
jenkins_github_token: ""
jenkins_github_credentials_id: "github-admin-token"
jenkins_github_servers:
  - name: Github
    api_url: https://api.github.com
    credentials_id: "{{ jenkins_github_credentials_id }}"
    client_cache_size: 20
```


### NodeJS Variables

```
jenkins_nodejs_installations: []
```


### Ant Variables

```
jenkins_ant_installations: []
```


### Job DSL Variables

```
jenkins_dsl_enabled: false
jenkins_dsl_security: true
```


## Dependencies

  - Jenkins installation (try
    [geerkingguy.jenkins](https://github/geerlingguy.jenkins))

## Example Playbook

```yaml
- hosts: jenkins
  vars:
    jenkins_hostname: jenkins.example.com
  roles:
    - role: geerlingguy.java
      become: yes
    - role: geerlingguy.jenkins
      become: yes
    - role: dankempster.jenkins-config
```

## License

MIT (Expat) / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
