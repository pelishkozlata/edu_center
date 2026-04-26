# Planned API Endpoints

## Authentication
POST /api/token/ — login by phone and password, get access and refresh tokens  
POST /api/token/refresh/ — get new access token  
POST /api/token/verify/ — verify token  

## Users
GET /users/ — get list of users
POST /users/ — create user
GET /users/{id}/ — get user details
PUT /users/{id}/ — update user
DELETE /users/{id}/ — deactivate user

## Branches
GET /branches/ — get list of branches
POST /branches/ — create new branch
GET /branches/{id}/ — get branch details
PUT /branches/{id}/ — update branch
DELETE /branches/{id}/ — archive branch

## Subjects
GET /subjects/ — get list of subjects
POST /subjects/ — create new subject
GET /subjects/{id}/ — get subject details
PUT /subjects/{id}/ — update subject
DELETE /subjects/{id}/ — archive subject

## Students
GET /students/ — get list of students
POST /students/ — create new student
GET /students/{id}/ — get student details
PUT /students/{id}/ — update student
DELETE /students/{id}/ — archive student

## Groups
GET /groups/ — get list of groups
POST /groups/ — create new group
GET /groups/{id}/ — get group details
PUT /groups/{id}/ — update group
DELETE /groups/{id}/ — archive group

## Group Students
GET /group-students/ — get list of group memberships
POST /group-students/ — add student to group
GET /group-students/{id}/ — get membership details
PUT /group-students/{id}/ — update membership
DELETE /group-students/{id}/ — remove student from group

## Lessons
GET /lessons/ — get list of lessons
POST /lessons/ — create new lesson
GET /lessons/{id}/ — get lesson details
PUT /lessons/{id}/ — update lesson
DELETE /lessons/{id}/ — cancel lesson

## Attendance
GET /attendance/ — get list of attendance records
POST /attendance/ — mark attendance
GET /attendance/{id}/ — get attendance details
PUT /attendance/{id}/ — update attendance record
DELETE /attendance/{id}/ — delete attendance record