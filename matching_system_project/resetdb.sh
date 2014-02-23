python manage.py sqlclear matching_system_project | python manage.py dbshell
echo "cleared db"
python manage.py syncdb
echo "syncing db"
python populate.py
