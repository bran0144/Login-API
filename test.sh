# register test script
curl -X POST -H "Content-type: application/json" -d '{"name" : "John", "email" : "john@test.com", "password" : "1234"}' http://127.0.0.1:9005/register

# login test script
curl -X POST -H "Content-type: application/json" -d '{"email" : "john@test.com", "password" : "1234"}' http://127.0.0.1:9005/
