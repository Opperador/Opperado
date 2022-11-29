import hikari
import random

Opperado = hikari.GatewayBot("MTA0NjkyNjkzODg0NzA2MDAwOA.GmVtNg.mWLRzUMo6NQmGxBpei4zRFaUOUNTJmI6bnyXDY")
@Opperado.listen(hikari.MessageCreateEvent)
async def xingamento_de_tutu(evento):
	xingamentos=["Bobo.","Burro.","Seboso.","Chato."]
	if evento.content.lower()=="o tutu é":
		await evento.message.respond(random.choice(xingamentos))

Opperado.run()