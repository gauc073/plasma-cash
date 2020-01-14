# run local blockchain
ganache-cli i -d -m "nose phone clip fee agent crop decorate spell album february oppose anxiety" --db ganache_db/ &
sleep 2

# run plasma child chain
python -m plasma_cash.child_chain &
sleep 1
# run plasma client on diff ports with diff identity
PYTHONPATH=. python plasma_cash/user/user_flask_application.py -p 5001 &
sleep 1

PYTHONPATH=. python plasma_cash/user/user_flask_application.py -p 5002 -r 1 &
sleep 1

PYTHONPATH=. python plasma_cash/user/user_flask_application.py -p 5003 -r 2 &
sleep 1

PYTHONPATH=. python plasma_cash/user/user_flask_application.py -p 5004 -r 3 &
sleep 1

# run plasma child chain cron job
python -m plasma_cash.operator_cron_job &
