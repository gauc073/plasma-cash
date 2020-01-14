# stop all four clients
kill -9 $(lsof -t -i:5001)

kill -9 $(lsof -t -i:5002)

kill -9 $(lsof -t -i:5003)

kill -9 $(lsof -t -i:5004)

# stop child chain 
kill -9 $(lsof -t -i:8546)

# stop local main blockchain
kill -9 $(lsof -t -i:8545)
