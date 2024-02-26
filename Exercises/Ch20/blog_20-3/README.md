Since I got some errors from platorm.sh while deploying, I used an alternate service called [FL0](https://www.fl0.com).

I followed this [YT video](https://youtu.be/dftvQCUauTE) for reference.

Here is the summarized version of the deployment steps for FL0:
1. Sign up for an account in [FL0](https://www.fl0.com) using GitHub(recommended) or Google or Email.
   1. Add your name & create a workspace.
   2. Add a project
2. Create a Postgres database.
   1. Give the database a name 
   2. Set the region nearest to your location
3. Install the following python packages in your virtual environment
   1. `pip install psycopg2-binary`
   2. `pip install dj-database-url`
4. Configure our database settings in the `settings.py` file
   1. Comment out the default SQLite DB object
   2. Import dj_database_url
   3. Create a new DB object using the DB url copied from the 'Connection Info' tab in the Postgres DB's dashboard in the [FL0](https://www.fl0.com)
   4. Run the migrate command to set up the new DB
5. Setup our environment variables
   1. Install the python package: `pip install django-environ`
   2. In `settings.py` file, import environ & initialize the environment variables
   3. Create `.env` file in the same directory as `settings.py`
   4. Create environments variables as `DATABASE_URL` & `SECRET_KEY` and paste the values from the `settings.py` file
   5. Replace the values with these variable name in the `settings.py` file.
6. Testing our admin user
   1. Create a superuser and test the admin login
7. Handling static files with [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/)
   1. Create a `static` folder with subfolders `css` & `js`
   2. Install the python package: `pip install whitenoise`
   3. In the `settings.py` file, add its Middleware, `STATICFILES_STORAGE` & `STATIC_ROOT`
   4. Run the collectstatic command using `manage.py`
8. Important deployment configurations
   1. Install the python package: `pip install gunicorn`
   2. Create `requirements.txt` using `pip freeze` in the base directory
   3. Create a `Procfile` in the base directory
   4. Set `DEBUG` to `False` & `ALLOWED_HOSTS` to `['*']`
9.  Push our application to GitHub
    1.  Create a new repository (if required)
    2.  Create `.gitignore` in your project folder & add the exceptions including `.env` & `db.sqlite3`
    3.  Push your code to the repository
10. Deploying to FL0
    1.  In your FL0 project dashboard, Add a New Web application service
    2.  Connect your GitHub repo & authorize FL0
    3.  Give the web application a name 
    4.  Set the region nearest to your location
    5.  Add the environment variables as same as the ones in .env
    6.  Deploy
11. After Deployment, modify `ALLOWED_HOSTS` & `CSRF_TRUSTED_ORIGINS` in the `settings.py` file using the FL0 URL and finally push the updated code to re-deploy the app.