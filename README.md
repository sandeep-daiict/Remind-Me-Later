RML is a webapp that reminds user over their preferred channel of notification with the message.

Used TWILIO for sending SMS create account and use TWILIO SID, Auth Keys and Phone number for sending SMS
Use Email with SMTP server and port

fill the above details in config.sh

Run following command in shell where you start celery queue and django server
source config.sh

Model one table RemindME:
    remind_message
    remind_date
    remind_email
    remind_phone

Future scope
    API to update reminder, lists based on emailID,phonnumber etc
    adding celery task_id in model to reschedule the task.
    mongoDB or NoSQL for better scaling and flexibily with different notification
    more notification options like (pushnotifications, tweet, post etc). adding it as a simple celery task
    API for status of tasks
    web interface

API endpoints
1)/remindmelists/

    method : Get
    use : lists all reminders scheduled till now
    response : [
               {
                "remind_message": "message to remind",
                "remind_date": "2016-07-25 01:53:50",
                "remind_email": "email@example.com",
                "remind_phone": "+xxxxxxxxxxx"                     

            }]


2)/remindmeadd/
    method : Post
    use : add a reminder to be sceduled at given time. assumption either phone number or emailid is not empty. reminder will be send to non empty field.

    request : {
                "remind_message": "message to remind",
                "remind_date": "2016-07-25 01:53:50", //remind_date format yyyy-mm-dd hh:mm:ss  and this field cant be empty
                "remind_email": "email@example.com",
                "remind_phone": "+xxxxxxxxxxx"
                }



    sample response


    response : {
            "status": "ok"
            }


    response : {
                "error":{
                           "remind_date":[
                                "Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
                                ]
                                },
                "status": "error"
                }




