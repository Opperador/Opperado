import hikari
import random

Opperado = hikari.GatewayBot("MTA0NjkyNjkzODg0NzA2MDAwOA.GmVtNg.mWLRzUMo6NQmGxBpei4zRFaUOUNTJmI6bnyXDY")
@Opperado.listen(hikari.MessageCreateEvent)
async def xingamento_de_tutu(evento):
	xingamentos=["Bobo.","Burro.","Seboso.","Chato."]
	if evento.content.lower()=="o tutu é":
		await evento.message.respond(random.choice(xingamentos))

contador_de_mensagens_do_tutu=0

@Opperado.listen(hikari.MessageCreateEvent)
async def cala_a_boca(evento):
	global contador_de_mensagens_do_tutu
	if evento.message.author.id==624365838610202624:
		contador_de_mensagens_do_tutu+=1
	if contador_de_mensagens_do_tutu==3:
		contador_de_mensagens_do_tutu=0
		await evento.message.respond("Cala a boca, Tutu!")


#async def boas_vindas(evento):



Opperado.run()