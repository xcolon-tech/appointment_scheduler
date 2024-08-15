# Social Media Scheduling Tool
Hosts Server Django Application for Social Media Scheduling Tool

# User Registration
curl -X POST http://127.0.0.1:8000/api/account/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "user@example.com", "mobile": "1234567890", "password": "password123", "confirm_password": "password123"}'
# User Login
curl -X POST http://127.0.0.1:8000/api/login/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'

# Create an Appointment
curl -X POST http://127.0.0.1:8000/api/appointment/appointments/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-05-01",
    "time": "10:00:00",
    "category": "Medical",
    "person": "Dr. Smith",
    "reason": "Routine checkup"
}'

# Update an Appointment
curl -X PUT http://127.0.0.1:8000/api/appointments/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-05-03",
    "time": "16:00:00",
    "category": "Doctor",
    "person": "Name 1",
    "reason": "Updated Reason"
}'

# List Active Appointments
curl -X GET http://127.0.0.1:8000/api/appointment/appointments/active/

# List Expired Appointments
curl -X GET http://127.0.0.1:8000/api/appointment/appointments/expired/

# Update an Appointment
curl -X PUT http://127.0.0.1:8000/api/appointments/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-05-03",
    "time": "16:00:00",
    "category": "Doctor",
    "person": "Name 1",
    "reason": "Updated Reason"
}'

# Delete an Appointment
curl -X DELETE http://127.0.0.1:8000/api/appointment/appointments/1/

# List Time Slots
curl -X GET http://127.0.0.1:8000/api/appointment/timeslots/ \
  -H "Authorization: Token YOUR_AUTH_TOKEN"

# Add Time Slots
curl -X POST http://127.0.0.1:8000/api/timeslots/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_AUTH_TOKEN" \
  -d '{"date": "2024-05-09", "time": "10:00:00"}'

# Delete Time Slots
curl -X DELETE http://127.0.0.1:8000/api/timeslots/1/ \
  -H "Authorization: Token YOUR_AUTH_TOKEN"

# Update User Profile
curl -X PUT http://127.0.0.1:8000/api/profile/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_AUTH_TOKEN" \
  -d '{"name": "New Name", "email": "newemail@example.com"}'

# Change Password
curl -X PATCH http://127.0.0.1:8000/api/profile/change-password/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token YOUR_AUTH_TOKEN" \
  -d '{"old_password": "oldpass", "new_password": "newpass", "confirm_password": "newpass"}'

# Logout Request
curl -X POST http://127.0.0.1:8000/api/logout/logout/ \
  -H "Authorization: Token YOUR_AUTH_TOKEN"