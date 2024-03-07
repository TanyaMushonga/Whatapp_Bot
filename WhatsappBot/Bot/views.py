from django.db import IntegrityError
from django.shortcuts import render
import os
from django.http import HttpResponse
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from .models import User, UserResponse

# Create your views here.
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC057bcc46227f5deabe7c5ae30cc3c3d6'
auth_token = 'd34a61046961debbd7cff870b82fef84'
client = Client(account_sid, auth_token)

questions = [
    "What is your fullname?",
    "What is you gender?",
    "What is your age?",
    "Where are you based?",
    "Do you have an experience in fish farming if yes explain a brief",
    "What is your capital expenditure?",
    "Do you have a fishpond if yes how what is the size?",
    "Which types of fish do you want farm?",
]


@csrf_exempt
def bot(request):
    message = request.POST.get('Body')
    sender_name = request.POST.get('ProfileName')
    sender_number = request.POST.get('From')
    user, created = User.objects.get_or_create(number=sender_number)
    print(f"sender:{sender_name} and the message is {message}")
    existing_response = None
    if created or message.lower() in ['hello', 'hi', 'hey']:
        user.question_index = 0
        user.save()
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'Hello {
                sender_name}, how is it going, I am you fish farming chatbot. I am going to ask you a series of questions',
            to='whatsapp:+263712389290'
        )
    else:
        existing_response = UserResponse.objects.filter(
            user_id=sender_number, question=questions[user.question_index]).first()

        if existing_response is None:
            try:
                UserResponse.objects.create(
                    user_id=sender_number, user_name=sender_name, question=questions[user.question_index], response=message)
                user.question_index += 1
                user.save()
            except IntegrityError:
                options_message = "I have collected your information already. Here are some options you can choose from:\n" \
                                  "1. How to get started with fish farming\n" \
                                  "2. How to construct a fish pond\n" \
                                  "3. How to design a feeding schedule for fish"
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=options_message,
                    to='whatsapp:+263712389290'
                )

            if user.question_index < len(questions):
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=questions[user.question_index],
                    to='whatsapp:+263712389290'
                )
            else:
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body='Congrutulations you are now an official member of our fish farming community.',
                    to='whatsapp:+263712389290'
                )
        else:
            client.messages.create(
                from_='whatsapp:+14155238886',
                body=f'We have already collected information about please select the options below: {
                    questions[user.question_index]}. Please wait for the next question',
                to='whatsapp:+263712389290'
            )
    return HttpResponse("Hello")
