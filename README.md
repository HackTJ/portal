# HackTJ Portal

[![wakatime](https://wakatime.com/badge/github/HackTJ/portal.svg)](https://wakatime.com/badge/github/HackTJ/portal)

A project submission platform for participants at HackTJ.

## Setup

### Google OAuth2

Full instructions can be found [here](https://developers.google.com/identity/protocols/oauth2).

Make sure to:
- Set up the OAuth consent screen
  - App name = HackTJ Portal
  - User support email = Your Google account email
  - Application home page = https://hacktj.org
  - Authorized domains = hacktj.org
  - Developer contact information = Your Google account email
- Create an OAuth client ID
  - Application type = Web application
  - Name = HackTJ Portal
  - Authorized JavaScript origins = 
    - http://localhost:8000
    - https://portal.hacktj.org
  - Authorized redirect URIs = 
    - https://localhost:8000/auth/complete/google-oauth2/
    - https://portal.hacktj.org/auth/complete/google-oauth2/
- Note down the client ID and client secret

### Application

Dependencies: (see `pyproject.toml`)
- `django` is the web framework used
- `social-auth-app-django` handles Google OAuth2 signup/login
- `django-bootstrap5` helps with UI design
- `rules` is used to manage user permissions
- `django-extensions` adds useful CLI management tools
- `black` is a code formatter

To install dependencies, run:

```bash
poetry install
```

Then, set up your project settings:

```bash
cd portal/settings
cp dev.secret.py secret.py
```

Make sure to edit `secret.py` with your Google OAuth2 client ID and secret.

Finally, create your database and apply migrations with:

```bash
poetry run python manage.py migrate
```

## Run

The app can be run in a terminal with:

```bash
poetry run python manage.py runserver
```

Alternatively, a PyCharm run configuration can be found in `.run/`.
This should automatically be detected when opening the project.

## Apps overview

### Main

This app handles site-wide functionality, such as the homepage and authentication.

It's mainly composed of the user model, found in `portal.apps.main.models.User`.
Some relevant fields are:
- `is_active`: Allows users to be deactivated manually, blocking them from logging in
- `is_staff`: Lets users log in to the built-in admin panel (Note: accessing panel features requires additional permissions)
- `is_superuser`: Users have all permissions, including those for the admin panel
- `is_participant`: The default role given to new accounts
- `is_judge`: A special (currently unused) role for judges
- `is_team`: A role designating HackTJ members with elevated permissions

Additionally, some custom permission properties are defined:
- `is_admin`: is either a superuser (`is_superuser`) or a team member (`is_team`)
- `is_admin_admin`: is both an admin (`is_admin`) and staff (`is_staff`)

Routes:
- `/`: The homepage
- `/about/`: The about page
- `/auth/complete/<str:backend>/`: The OAuth2 callback URL
- `/auth/disconnect/<str:backend>/`: Deletes the user account
- `/auth/disconnect/<str:backend>/<int:association_id>/`: Disconnects the user from the given OAuth2 association
- `/auth/login/<str:backend>/`: Starts the OAuth2 login flow
- `/login/`: The login page
- `/logout/`: Logs the user out

### Categories

This app handles judging categories that projects can submit to.
For example, "Best Web App" and "Best Mobile App."
These categories are created and managed by the HackTJ team.

Fields:
- Name (255 characters)
- Description (4096 characters)

| Action | Route                                   | Permission required |
|--------|-----------------------------------------|---------------------|
| List   | `/categories/`                          | `is_admin`          |
| Add    | `/categories/create/`                   | `is_admin`          |
| View   | `/categories/<int:category_id>/`        | `is_admin`          |
| Change | `/categories/<int:category_id>/update/` | `is_admin`          |
| Delete | `/categories/<int:category_id>/delete/` | `is_admin`          |

### Locations

Locations represent places teams will be at during both competition and judging.
A project specifies a location to let judges know where they are located and where they can be judged.
Locations will be manually created by the HackTJ team.

Fields:
- Name (255 characters, optional)
- Floor (one of 5, 6, 7, 8)
- Room (a valid 5-character string, optional)
- Capacity (positive small integer, optional)

| Action | Route                                   | Permission required |
|--------|-----------------------------------------|---------------------|
| List   | `/locations/`                           | `is_admin`          |
| Add    | `/locations/create/`                    | `is_admin`          |
| View   | `/locations/<int:location_id>/`         | `is_admin`          |
| Change | `/locations/<int:location_id>/update/`  | `is_admin`          |
| Delete | `/locations/<int:location_id>/delete/`  | `is_admin`          |

### Projects

Projects are the main focus of the HackTJ portal, as they represent a team's submission to HackTJ.

Fields:
- Name (255 characters)
- Description (4096 characters)
- Created at (automatically set)
- Modified at (automatically set)
- Members (list of `User`s)
- Created by (a `User`, optional)
- Modified by (a `User`, optional)
- Categories (list of `Category`s)
- Location (a `Location`, optional)
- Location description (1024 characters, optional)

| Action    | Route                                            | Permission required                                    |
|-----------|--------------------------------------------------|--------------------------------------------------------|
| List      | `/projects/`                                     | `is_admin`                                             |
| Add       | `/projects/create/`                              | `is_admin` OR<br/>is not a member of any other project |
| View      | `/projects/<int:project_id>/`                    | `is_admin` OR<br/>is a member of the project           |
| Change    | `/projects/<int:project_id>/update/`             | `is_admin` OR<br/>is a member of the project           |
| Delete    | `/projects/<int:project_id>/delete/`             | `is_admin` OR<br/>is a member of the project           |
| Leave     | `/projects/<int:project_id>/leave/`              | is a member of the project                             |
| Kick from | `/projects/<int:project_id>/kick/<int:user_id>/` | is a member of the project                             |
