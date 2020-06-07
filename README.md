# csv2keychain-python-shell

Fork from [https://github.com/nntarasov/csv2keychain]

## Why create this script

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

## How to move account to keychain iCloud

0. Import account from csv(not necessary)

1. Goto `System Preferences` - `Security & Privacy` - `Accessibility `, add `Script Editor.app`
2. Select and drag account to iCloud
3. Open `Script Editor.app` and paste this script, run. 

```applescript
tell application "System Events"
    repeat while exists (processes where name is "SecurityAgent")
        tell process "SecurityAgent"
            set frontmost to true
            try
                keystroke "PUT YOUR KEYCHAIN'S PASSWORD HERE"
                delay 0.1
                keystroke return
                delay 0.1
            on error
                -- do nothing to skip the error
            end try
        end tell
        delay 0.5
    end repeat
end tell
```

