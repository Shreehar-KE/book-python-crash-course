This folder contains the code without the deployment configurations, for the deployment-ready code visit this [repo](https://github.com/Shreehar-KE/deploy-pcc-learning-log).

Since I got some errors from platorm.sh while creating an account, I used an alternate deployment service called [Render](https://www.render.com).

I followed this [YT playlist](https://www.youtube.com/playlist?list=PL5E1F5cTSTtQMmjFqso__3eSGEvw1mglc) for reference.

**Here is the modified text version of the deployment steps for Render.com:**

1. Set up the Environment Variables
   1. `pip install django-environ`
   2. In `settings.py`,
        ```py
        from environ import Env

        env = Env()
        Env.read_env()
        ```
   3. Create a .env file in the base project folder where `settings.py` exists.
        ```
        ENVIRONMENT=development
        SECRET_KEY=/* insert secret key */
        ```
        use the code `python3 -c "import secrets; print(secrets.token_urlsafe())"` in the terminal to generate a new key if needed.
    4. Modify the `settings.py` to use the environment variables
       1. Ex: `ENVIRONMENT = env('ENVIRONMENT', default='production')`
       2. To set the value for `DEBUG` variable, use an `if-else` block based on the `ENVIRONMENT` variable

2. Setup [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) & collectstatic
   1. `pip install whitenoise`
   2. Add its middleware as mentioned in the [docs](https://whitenoise.readthedocs.io/en/latest/)
   3. In `settings.py`,
      1. Set `STATIC_ROOT = BASE_DIR / 'staticfiles'`
      2. Set `STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"`
   4. Run `python manage.py collectstatic` 

3. Sign-Up/Login to your Render account
   1. Create a new PostgreSQL service from the [Render](https://www.render.com) dashboard
      1. Set name & region for the service
      2. Copy and store the External Database URL as well as the Internal Database URL

4. Connecting to the PostgreSQL DB
   1. Add `DATABASE_URL=/* External DB URL */` in `.env`
   2. `pip install dj-database-url`
   3. In `settings.py`,
        ```py
        import dj_database_url # at top

        # after the DATABASES declaration
        POSTGRES_LOCALLY = True # for connecting to the Postgres DB from the local server
        if ENVIRONMENT == 'production' or POSTGRES_LOCALLY:
            DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))
        ```
   4. `pip install psycopg2-binary`
   5. `python manage.py migrate`
   6. `python manage,py createsuper` to create admin for the Postgres DB
   7. Set `POSTGRES_LOCALLY` to False

5. Setup Git & GitHub
   1. `pip install gunicorn`
   2. `pip freeze > requirements.txt`
   3. In `settings.py`, set `ALLOWED_HOSTS = [*]`
   4. Install git if not installed already and create a `.gitignore` file in the project's root directory
        ```
        venv/  
        __pycache__/ 
        .env 
        db.sqlite3
        /* add any other files/folders if required */
        ```
   5. Add and Commit your code
   6. Sign-Up/Login to your GitHub account and create a new repository
      1. Connect your local repo to the remote repo and upload the code

6. Deployment
   1. Create a new Web service from the [Render](https://www.render.com) dashboard
      1. Choose *build & deploy from git repo*
      2. Connect to your GitHub repo
      3. Set name, region & start command as `gunicorn base.wsgi`
      4. Add the environment variables as in the local`.env` file, except for
        ```
        ENVIRONMENT=production
        DATABASE_URL=/* Internal DB URL */
        PYTHON_VERSION=3.11.3
        ```
      5. Finish
   2. After the Initial Deployment
      1. Modify `ALLOWED_HOSTS` & set `CSRF_TRUSTED_ORIGINS` in the `settings.py` file using the newly generated URL for your web service
      2. Push the updated code to re-deploy the app. 