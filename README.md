Master: [![CircleCI](https://circleci.com/gh/anysure/ansible.packages/tree/master.svg?style=svg)](https://circleci.com/gh/anysure/ansible.packages/tree/master) | Dev: [![CircleCI](https://circleci.com/gh/anysure/ansible.packages/tree/dev.svg?style=svg)](https://circleci.com/gh/anysure/ansible.packages/tree/dev)
# Packages

Configures the repository's, settings and runs updates for Debian and RHEL systems.

**Attention:**

- This role handles name differences between package managers but not between distributions using the same package manager.
- Test coverage is rather small so please do report bugs!

## Requirements

- Hosts should be bootstrapped for ansible usage (have python,...)
- Root privileges, eg `become: yes`

## Role Variables

| Variable | Default  | Options | Required | Description |
|---|---|---|---|---|
| `package_list` | `[]` | List of packages **(see details!)** | |
| `package_list_host`| `[]` | List of packages **(see details!)**  | |
| `package_list_group` | `[]` | List of packages **(see details!)** | |
| `package_state` | 'present' | Default package state | |
| `package_update_cache` | `yes` |Update the cache? | |
| `package_cache_valid_time` | 3600 | How long is the package cache valid? (seconds) | |

### `package_list` details

`package_list`, `package_list_host` and `package_list_group` are merged when managing the packages. You can use the host and group lists to specify packages per host or group. 
The package list allows you to define which packages must be managed. Each item in the list can have following attributes:

| Variable | Description | required |
|----------|-------------|----------|
| `name` | Package name | yes |
| `state` | Package state | no |
| `apt` | Package name for apt | no |
| `apt_ignore` | Ignore package for apt | no |
| `apt_install_recommends` | Whether to install recommended dependencies apt    | no |
| `yum` | Package name for yum | no |
| `yum_ignore` | Ignore package for yum | no |
| `dnf` | Package name for dnf | no |
| `dnf_ignore` | Ignore package for dnf | no |

By default `package_state` and `item.name` are used when managing the packages.
If however `item.state` is defined or a more specific package name (eg
`item.apt`) these will be used instead. If you want a package to be ignored for some package managers you can add `***_ignore`: yes.

### `package_list` example

```yaml
package_list:
  - name: package
  - name: package1
    state: absent
  - name: package2
    apt: package2_apt_name
  - name: package3
    apt_ignore: yes
    yum: package3_yum_name
    portage: package3_portage_name
```

## Dependencies

None.

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
---
- hosts: servers
  roles:
  - { role: anysure.packages,
      become: yes,
        package_list: [
          { name: htop,
            brew: htop-osx },
          { name: tree }
        ]
    }
```
## Contributing

All assistance, changes or ideas [welcome][issues]!

## License

Apache License, Version 2.0

## Author Information

[Ronny Roethof][rroethof] (ronny@roethof.net) for AnyLinQ.
