from django.shortcuts import render
import os
from django.http import HttpResponse
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from .models import Disease, Pond, UserInfor, FishTypes
# Create your views here. 
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC057bcc46227f5deabe7c5ae30cc3c3d6'
auth_token = 'b8d32079cd758dec6c9c8fddc2613e5f'
client = Client(account_sid, auth_token)
about= ""
@csrf_exempt
def bot(request):
    message = request.POST.get('Body')
    sender_name = request.POST.get('ProfileName')
    sender_number = request.POST.get('From')
    print(f"sender:{sender_name} and the message is {message}")

    if message.lower() in ["hey", "hi", "hie", "hello", "hellow"]:
        client.messages.create(
        from_='whatsapp:+14155238886',
        body=f'Hello, {sender_name}, how is it going. I am your fish farming personal assistant.\n\n'
        'select options here:\n\n'
        '1. Services\n'
        '2. About us\n'
        '3. Contact us\n'
        '4. Registration\n'
        '5. Access information\n',
        to='whatsapp:+263712389290'
        ) 
    
    message = request.POST.get('Body').lower()  # Get the message and convert it to lowercase

    # ...

   
    
    message = request.POST.get('Body').lower()
    
    if message in ['1', 'services']:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="1. We're your assistant, your friendly, 24/7 AI assistant for all things fish farming! Ask us anything, from water quality to feeding schedules, and get personalized advice to keep your fish thriving.\n\n"
            "2. We're passionate about aquaculture and empowering fish farmers. Our chatbot provides tailored support, helping you optimize your farm and achieve success, one fin at a time.\n\n"
            "3. Stop swimming upstream! Get real-time answers, personalized recommendations, and take the stress out of managing your aquatic haven.",
            to='whatsapp:+263712389290'
        )
    
    if message in ['2', 'about us']:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="1. Direct and Informative\n\n"
            "Water Quality Monitoring & Alerts: Receive personalized guidance on maintaining optimal water parameters based on your fish species.\n\n"
            "Feeding Schedule: Get recommendations on the right feed and feeding frequency for your fish.\n\n"
            "Disease Diagnosis: Identify and treat common fish diseases with our AI-powered diagnostic tool.\n\n"
            "Market & Price Updates: Stay informed on relevant market trends and pricing data specific to your fish types.\n\n"
            "2. Benefit-oriented:\n\n"
            "Optimize Your Farm: Get data-driven insights and personalized recommendations to improve efficiency and profitability."
            "Save Time & Money: Reduce the time and resources spent on manual monitoring and problem-solving."
            "Empowerment: Gain access to expert advice and best practices to help you make informed decisions and achieve success.",
            to='whatsapp:+263712389290'
        )
    
    if message in ['3', 'contact us']:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="You can contact us on the following details:\n\n"
            "Email: tanyaradzwatmushonga@gmail.com\n\n"
            "Phone: +263712389290",
            to='whatsapp:+263712389290'
        )
    
    if message in ['4', 'registration']:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="To register, please provide the following details:\n\n"
            "1. Name\n"
            "2. Email\n"
            "3. Phone number\n"
            "4. Location\n"   
            "6. Number of fish\n"
            "7. Type of fish\n"
            "8. Size of pond\n"
            "9. Water source\n"           
            ,
            to='whatsapp:+263712389290'
        )
    user_details = message
    print("the user details are", user_details)
    user_infor = UserInfor(sender_name=sender_name, sender_number=sender_number, details=user_details)
    user_infor.save()
    response_message = "Thank you for registering with us. Your details have been saved."
    
    if message == 'info':
        # Retrieve user information from the database
        user_infor = UserInfor.objects.filter(sender_number=sender_number).first()

        if user_infor:
            # If user information exists, send it back
            response_message = f"Name: {user_infor.sender_name}\n{user_infor.sender_number}\nDetails: {user_infor.details}"
            client.messages.create(
                from_='whatsapp:+14155238886',
                body=response_message,
                to='whatsapp:+263712389290'
            )
        else:
            # If user information does not exist, send a message indicating this
            client.messages.create(
                from_='whatsapp:+14155238886',
                body="No information found for this number.",
                to='whatsapp:+263712389290'
            )
    
    if message == 'delete':
        # Retrieve user information from the database
        user_infor = UserInfor.objects.filter(sender_number=sender_number).first()

        if user_infor:
            # If user information exists, delete it
            user_infor.delete()
            client.messages.create(
                from_='whatsapp:+14155238886',
                body="Your information has been deleted from the database.",
                to='whatsapp:+263712389290'
            )
        else:
            # If user information does not exist, send a message indicating this
            client.messages.create(
                from_='whatsapp:+14155238886',
                body="No information found for this number.",
                to='whatsapp:+263712389290'
            )
        
    if message in ['5', 'access information']:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="Please specify the type of information you want:\n\n"
            "Fish types\n"
            "Pond management\n"
            "Diseases\n"
            "Feeding schedule",
            to='whatsapp:+263712389290'
        )   
    
       
       
     
    def retrieve_fish_information(fish_type):
        # Retrieve fish information from the database
        fishes = FishTypes.objects.filter(fish_type__iexact=fish_type)

        for fish in fishes:
            if fish is not None:
                # Create a response message with the retrieved information
                response_message = "Fish Information:\n\n"
                response_message += f"Fish type: {fish.fish_type}\n\n"
                response_message += f"Description: {fish.description}\n\n"
                response_message += f"Feeding schedule: {fish.feeding_schedule}\n\n"
                response_message += f"Maturity period: {fish.maturity_period}\n\n"
                response_message += f"Size: {fish.fish_size}\n"

                # Send the response message
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=response_message,
                    to='whatsapp:+263712389290'
                )
               
    if message.lower() in ['fish types']:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="Tilapia\n"
            "Catfish\n"
            "Salmon\n"
            "Carp\n"
            "Bass\n"
            "Cod\n",
            to='whatsapp:+263712389290'
        )

    elif message.lower() in ['tilapia', 'catfish', 'trout', 'salmon', 'carp', 'bass', 'cod']:
        retrieve_fish_information(message.lower())

        
    def retrieve_pond_information(action):
        # Retrieve pond information from the database
        ponds = Pond.objects.filter(action__iexact=action)

        for pond in ponds:
            if pond is not None:
                # Create a response message with the retrieved information
                response_message = "Pond Management Information:\n\n"
                response_message += f"Action: {pond.action}\n\n"
                response_message += f"YouTube URL: {pond.youtubeUrl}\n"

                # Send the response message
                client.messages.create(
                    from_='whatsapp:+14155238886',
                    body=response_message,
                    to='whatsapp:+263712389290'
                )
                
    if message in ['pond management']:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="Pond construction\n"
            "Pond maintenance\n"
            "Pond aeration\n"
            "Pond fertilization\n"
            "Pond water quality",
            to='whatsapp:+263712389290'
        )
    elif message.lower() in ['pond construction', 'pond maintanace', 'pond aeration', 'pond aeration', 'pond fertilisation', 'pond water quality']:
         retrieve_pond_information(message.lower())

    def retrieve_disease_information(disease_type):
        # Retrieve disease information from the database
        diseases = Disease.objects.filter(disease_type__iexact=disease_type)

        for disease in diseases:
            if disease is not None:
                # Create a response message with the retrieved information
                response_message = "Disease Information:\n\n"
                response_message += f"Disease: {disease.disease_name}\n\n"
                response_message += f"Symptoms: {disease.symptoms}\n\n"
                response_message += f"Causes: {disease.causes}\n\n"
                response_message += f"Impact: {disease.impact}\n\n"
                response_message += f"Treatement method: {disease.treatment_method}\n\n"
                response_message += f"Medication type: {disease.medication_type}\n\n"
                response_message += f"Dosage: {disease.dosage}\n\n"
                response_message += f"Treatement duration: {disease.treatment_duration}\n\n"
                response_message += f"Prevention startegy: {disease.prevention_strategies}\n\n"
                response_message += f"Types of fish affected mostly: {disease.types_of_fish_affected_mostly}\n\n"
                response_message += f"Further research: {disease.imgUrl}\n"
              
                chunks = [response_message[i:i + 1600] for i in range(0, len(response_message), 1600)]
                # Send the response message
                for chunk in chunks:
                # Send the response message
                    client.messages.create(
                        from_='whatsapp:+14155238886',
                        body=chunk,
                        to='whatsapp:+263712389290'
                )
    
    if message.lower() in ['diseases']:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="Bacterial diseases\n"
            "Fungal diseases\n"
            "Parasitic diseases\n",
            to='whatsapp:+263712389290'
        )
    elif message.lower() in ['bacterial diseases', 'fungal diseases', 'parasitic diseases']:
        retrieve_disease_information(message.lower())
        
    
    return HttpResponse("hello fish farmer!")    
        
   
