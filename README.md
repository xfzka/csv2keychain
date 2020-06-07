# csv2keychain-python-shell

Fork from [https://github.com/nntarasov/csv2keychain]

## Why create this script ?

I don't want continue to use `1password`, and i named every account record, so i need import `name` column to Apple `keychain.app`.

## Require

- python3.6+

### Account file format

Need 4 columns, they are "name, url, username, password", no column order limit.

## Usage

```bash
chmod +x csv2keychain.py
./csv2keychain.py account_file.csv
```

### Args

```bash
csv2keychain [path.csv] [-u] [-s]
```

- -u - update existing password for every account in keychain, if any

- -s - display credentials on the screen during the process
