# Microservice coding question:
Google allows users with different roles (Admin, Modifier, Watcher) to access it's platform.

We need to create users CRUD apis.

1. Write an API to create user with user details (Id, Name, Role, Email).
Should return - Status code and message on user creation.
Name, Role, Email are required fields.
Success scenario: Be able to create a new user.
If a user already exists, then this API should return failure with an error message.


2. A user can have multiple roles:
a. Admin can be Modifier, Watcher.
b. Modifier can also be a Watcher.
c. Watcher cannot assume any other role.
Write an API that allows updating/adding roles as per the rules given above.
If rules are followed, return success else failure with an error message.


3. We should be able to see details about users in our system.
Write an API to list details about any given user.
If user details are not sent, list details for all the users in the system.
If no users are present on the system, return an empty list.


4. We should be able to delete any user from our system.
If user does not exist, return failure with an error message.

