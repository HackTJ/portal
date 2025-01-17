# Portal Secret Files

This directory should contain secret configuration files required by the portal. These files should never be committed to version control.

## Required Files

### Email Whitelists

1. `user_email_whitelist.txt`
   - One email per line
   - Controls who can access the portal
   - Required in production unless explicitly disabled

2. `team_email_whitelist.txt`
   - One email per line 
   - Identifies HackTJ team members
   - Grants elevated permissions

3. `admin_email_whitelist.txt` 
   - One email per line
   - Designates administrative users
   - Highest level of access

### Format

Each whitelist file should contain one email address per line:

```
user1@example.com
user2@example.com
user3@example.com
```

## Other Secret Files

- `secret.py`: Django settings containing sensitive values
  - Copy from `portal/settings/dev.secret.py`
  - Add Google OAuth2 credentials
  - Update `SECRET_KEY`
  - Configure other sensitive settings
