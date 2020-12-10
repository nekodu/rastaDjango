from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def anasayfa(request):
	return render(request,'anasayfa.html',{})


def randevu(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		date = request.POST['date']
		time = request.POST['time']
		
		send_mail(
			name + ' tarafından randevu isteği',#konu
			'\n'+phone + '\n'+ date + '\n'+time,#mesaj
			email,#kimden
			['receiver@gg.com'],#kime

			)

		#send mail
		'''
		send_mail(
				message_name, #subject
				message,
				message_email,
				['mail@mail.com'],

			)
'''
		return render(request, 'randevu.html',
			{
			'isim': name,
			'email': email,
			'telefon': phone,
			'tarih': date,
			'saat': time,
			})

	else:
		return render(request,'anasayfa.html',{})