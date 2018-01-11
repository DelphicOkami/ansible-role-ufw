# Ansible Role: UFW

[![Build Status](https://travis-ci.org/markahesketh/ansible-role-ufw.svg?branch=master)](https://travis-ci.org/markahesketh/ansible-role-ufw)

Ansible role to manage UFW (Uncomplicated Firewall), a firewall configuration tool for Ubuntu/Debian systems.

## Installation

```
ansible-galaxy install markahesketh.ufw
```

## Role Variables

Default values are listed below (see [`defaults/main.yml`](defaults/main.yml)):

```yml
ufw_default_policy: deny

ufw_rules:
  - to_port: 22
    rule: limit
  - to_port: 80
    rule: allow
  - to_port: 443
    rule: allow
```

The `ufw_rules` variable is an list of dictionaries, with the following options from the [UFW module](http://docs.ansible.com/ansible/latest/ufw_module.html):

```yml
ufw_rules:
  - to_port:
    rule:
    proto:
    to_ip:
    from_port:
    from_ip:
    interface:
    direction:
    log:
```

You can specify the firewall's default policy with the `ufw_default_policy` variable, which accepts `allow`, `deny` and `reject ` as options.

```yml
ufw_default_policy: "allow|deny|reject"
```

## Dependencies

None.

## Example Playbook

```yml
- hosts: web
  roles:
    - markahesketh.ufw
```

## Testing

    molecule test

Requires [Molecule](https://molecule.readthedocs.io/en/latest/) and [Docker](https://docs.docker.com/engine/installation/).

## License

This role is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).

## Author

By [Mark Hesketh](https://www.markhesketh.co.uk/), a web developer from Manchester, UK.

* Blog: [markhesketh.co.uk](https://www.markhesketh.co.uk/)
* Twitter: [twitter.com/markahesketh](https://www.twitter.com/markahesketh/)
* GitHub: [github.com/markahesketh](http://www.github.com/heskethm/)
* Email: [contact@markhesketh.co.uk](mailto:contact@markhesketh.co.uk)
