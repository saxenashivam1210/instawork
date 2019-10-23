Build image with docker-compose locally:
	docker-compose build

Test the image locally(docker includes postgresql 10 server for which credentials are mentioned in .env file):
	docker-compose up

To deploy remotely on aws:
	build the image "docker-compose build"
	find the image with "docker images" command
	tag and push the image to docker hub/private repo "docker tag <image_id> instawork/teams:<version> && docker push instawork/teams:<version>"
	setup credentials in aws bucket "instawork-docker" using "dockercreds/.dockercfg" as mentioned in Dockerrun.aws.json and update the image version in the same file
	setup elasticbeanstalk application and environment to work with branch (same can be updated in .elasticbeanstalk/config.yml) or use "eb init"
	deploy to aws using "eb deploy"

To deploy remotely on azure:
	follow the same steps to build image and deploy on docker hub/private repo
	create app service with app service plan.
	configure docker registry credentials in app service configuration along with the image details


Testing locally:

To get all users:
Request : curl -X GET 'http://127.0.0.1/team'
Response :
[
    {
        "uuid": "b33cfcda-073f-49f4-afd0-cd68295b7321",
        "first_name": "qwe",
        "last_name": "zxczxc",
        "phone_number": 23323,
        "email": "xx@sds.com",
        "role": "regular"
    },
    {
        "uuid": "02746cff-59e4-4c95-9b21-330cca987aab",
        "first_name": "q121we",
        "last_name": "zx21czxc",
        "phone_number": 23323,
        "email": "xx@sds.com",
        "role": "regular"
    },
    {
        "uuid": "a22778d0-9574-4135-b865-81758190a040",
        "first_name": "q121we",
        "last_name": "zx21czxc",
        "phone_number": 23323,
        "email": "xx@sds.com",
        "role": "admin"
    }
]

To search specific user with uuid:
Request : curl -X GET 'http://127.0.0.1/team?uuid=3a5b4824-0b0e-4bfc-837a-3028c6765eaa'

Response : 404 Not Found
{
    "message": "Record with uuid 3a5b4824-0b0e-4bfc-837a-3028c6765eaa does not exist"
}

Response : 200 Ok
{
    "uuid": "02746cff-59e4-4c95-9b21-330cca987aab",
    "first_name": "q121we",
    "last_name": "zx21czxc",
    "phone_number": 23323,
    "email": "xx@sds.com",
    "role": "regular"
}


To create new user:
curl -X POST \
  http://127.0.0.1/team \
  -H 'content-type: application/json' \
  -d '    {
        
        "first_name": "q121we",
        "last_name": "zx21czxc",
        "phone_number": 23323,
        "email": "xx@sds.com",
        "role": "regular"
    }'

Note: Role type can only be admin or regular
Response:
{
    "uuid": "1d03fda4-5c97-4a31-98c7-7943ebd7228c",
    "first_name": "q121we",
    "last_name": "zx21czxc",
    "phone_number": 23323,
    "email": "xx@sds.com",
    "role": "regular"
}

To update user:
Request : curl -X PUT \
  http://127.0.0.1/team/ \
  -H 'content-type: application/json' \
  -d '{
    "uuid": "1d03fda4-5c97-4a31-98c7-7943ebd7228c",
    "first_name": "q121we",
    "last_name": "zx21czxc",
    "phone_number": 23323,
    "email": "asa@sds.com",
    "role": "admin"
}'

Response : 
{
    "uuid": "1d03fda4-5c97-4a31-98c7-7943ebd7228c",
    "first_name": "q121we",
    "last_name": "zx21czxc",
    "phone_number": 23323,
    "email": "asa@sds.com",
    "role": "admin"
}

Delete user:
Request : curl -X DELETE 'http://127.0.0.1/team?uuid=b33cfcda-073f-43f4-afd0-cd68295b7321'

Response: 404 Not Found
{
    "message": "Record with uuid b33cfcda-073f-43f4-afd0-cd68295b7321 does not exist"
}

Response: 200 Ok
{
    "message": "Record deleted"
}

