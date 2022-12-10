import hikari
import random
import os

Opperado = hikari.GatewayBot(os.environ["Token_Opperado"])
@Opperado.listen(hikari.MessageCreateEvent)
async def xingamento_de_tutu(evento):
	xingamentos=["Bobo.","Burro.","Seboso.","Chatão, mané.","Boca de sebo."]
	if evento.content.lower()=="o tutu é":
		await evento.message.respond(random.choice(xingamentos))

contador_de_mensagens_do_tutu=0

@Opperado.listen(hikari.MessageCreateEvent)
async def cala_a_boca(evento):
	calabocamentos=["Quem chamou o Tutu?","Ninguem gosta do Tutu, fica quieto!","Cala a boca, Tutu"]
	global contador_de_mensagens_do_tutu
	if evento.message.author.id==os.environ.get("ID_DO_TUTU", 624365838610202624):
		contador_de_mensagens_do_tutu+=1
	if contador_de_mensagens_do_tutu==30:
		contador_de_mensagens_do_tutu=0
		await evento.message.respond(random.choice(calabocamentos))

Opperado.run()