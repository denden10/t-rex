# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
from discord.ext import commands

TOKEN = 'NDY2Nzc4Njg2OTg1ODYzMTY4.Di2Uiw.WgH-UnMhTOejK_3lDmeDw7I7Oz0'

#line below is the sub-library of what the bot can do automatically
disco = discord.Client()
#line below is the sub-library of what user enter to make the bot run
client = commands.Bot(command_prefix = "$")

#when the bot runs, the below will confirm it:
#Setting a "PLaying Status" on the Discord Bot"
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="With Dino Bugs"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot Ready. Prepare for Trouble. Rawr.')

###DISCLAIMER: THIS DISCORD BOT IS NOT READILY UP-TO-DATE. I"m trying my best to keep up with the moves!###

#the following commands are just for fun
@client.command(brief = 'Try it out!', description = 'Try it out!')
async def ping():
	await client.say('Rawr!')

@client.command(brief = 'Jurassic World Alive.', description = 'Gives you informatiom about JWA.')
async def info():
    await client.say('__**Hybrid Information:**__ \nPlease visit <https://metahub.info/jurassic-world-alive/550/jwa-recipes-for-all-hybrids-what-dna-do-you-need/> for more information! \
        \n \n__**JWA Dinosaur Dex:**__ \nPlease visit <https://metahub.info/jwa-dinodex/> for more information. You can also use "$dino [dinosaur]".')

#=================================================================project: setting up an embed code for DINODEX(ongoing)====================================================================#

##DO NOT REMOVE THESE FOLLOWING LINES##
@client.group(brief = 'Gives brief information about dinosaurs in Jurassic World Alive. Use "$dino [dinosaur]', description = 'Usage: $dino [dinosaur] \n Some dinosaurs are shown below:')
async def dino():
    pass

#---------------------------------------------------------------------------------Stand-Alone Dinos------------------------------------------------------
#WUERHOSAURUS#
@dino.command()
async def wuerhosaurus():
        embed = discord.Embed(
                title = 'Wuerhosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Werhosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/weurhosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#SARCOSUCHUS#
@dino.command()
async def sarcosuchus():
        embed = discord.Embed(
                title = 'Sarcosuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Sarcosuchus_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Sarcosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 110 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Sarcosuchus (LV15, 200 DNA) + Einiasuchus (LV15, 50 DNA) = Sarcorixis', inline = 'false')

        await client.say(embed = embed)

#PURRUSAURUS#
@dino.command()
async def purrusaurus():
        embed = discord.Embed(
                title = 'Purrusaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Purussaurus_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/purrusaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 114 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#PURRUSAURUS GEN2#
@dino.command()
async def purrusaurus2():
        embed = discord.Embed(
                title = 'Purrusaurus Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Purussaurus_gen2_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Purrusaurus_gen2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 114 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#DIPLOCAULUS#
@dino.command()
async def diplocaulus():
        embed = discord.Embed(
                title = 'Diplocaulus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Diplocaulus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/diplocaulus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Diplocaulus Gen 1 (LV5, 50 DNA) + Irritator Gen 2 (LV5, 50 DNA) = Diplotator', inline = 'false')

        await client.say(embed = embed)

#DIPLOCAULUS GEN2#
@dino.command()
async def diplocaulus2():
        embed = discord.Embed(
                title = 'Diplocaulus Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Diplocaulus-Gen-2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/diplocaulus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#OPHIACODON#
@dino.command()
async def ophiacodon():
        embed = discord.Embed(
                title = 'Ophiacodon Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Ophiacodon.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Ophiacodon")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 110 \n__Critical:__ 40%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Ankylosaurus Gen 2 (LV5, 50 DNA) +  Ophiacodon (LV5, 50 DNA) = Ankylocodon', inline = 'false')

        await client.say(embed = embed)

#Argentinosaurus
@dino.command()
async def argentinosaurus():
        embed = discord.Embed(
                title = 'Argentinosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Argentinosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Argentinosaurus")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 102 \n__Critical:__ 40%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Carnotaurus
@dino.command()
async def carnotaurus():
        embed = discord.Embed(
                title = 'Carnotaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Carnotaur.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Carnotaurus")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Concavenator
@dino.command()
async def concavenator():
        embed = discord.Embed(
                title = 'Concavenator Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Concavenator.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Concavenator")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 106 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Deinocheirus
@dino.command()
async def deinocheirus():
        embed = discord.Embed(
                title = 'Deinocheirus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Deinocheirus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/deinocheirus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 130 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dilophosaurus (LV20, ?? DNA) + Deinocheirus (LV20, ?? DNA) = Diloracheirus', inline = 'false')

        await client.say(embed = embed)

#Blue
@dino.command()
async def blue():
        embed = discord.Embed(
                title = 'Blue Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/6BC4BE77-037B-4F6E-A0CB-4B2622FDC948.jpeg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/blue/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 131 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Charlie
@dino.command()
async def charlie():
        embed = discord.Embed(
                title = 'Charlie Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Charlie.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/charlie/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Delta
@dino.command()
async def delta():
        embed = discord.Embed(
                title = 'Delta Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Delta_Card.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/delta/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 131 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Echo
@dino.command()
async def echo():
        embed = discord.Embed(
                title = 'Echo Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/20C100B3-BD29-4C47-A7D2-F705A35FFDDA.jpeg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/echo/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Tarbosaurus
@dino.command()
async def tarbosaurus():
        embed = discord.Embed(
                title = 'Tarbosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Tarbosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tarbosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 40%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Tanycolagreus
@dino.command()
async def tanycolagreus():
        embed = discord.Embed(
                title = 'Tanycolagreus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Tanycolagreus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tanycolagreus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 130 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Ouranosaurus
@dino.command()
async def ouranosaurus():
        embed = discord.Embed(
                title = 'Ouranosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Ouranosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/ouranosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 127 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dilophosaurus (LV15, 50 DNA) + Ouranosaurus (LV15, 50 DNA) = Diloranosaurus', inline = 'false')

        await client.say(embed = embed)

#Edmontosaurus
@dino.command()
async def edmontosaurus():
        embed = discord.Embed(
                title = 'Edmontosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Edmontosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/edmontosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Iguanodon
@dino.command()
async def iguanodon():
        embed = discord.Embed(
                title = 'Iguanodon Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Iguanodon.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/igaunodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Lythronax
@dino.command()
async def lythronax():
        embed = discord.Embed(
                title = 'Lythronax Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Lythronax.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/lythronax/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Proceratosaurus
@dino.command()
async def proceratosaurus():
        embed = discord.Embed(
                title = 'Proceratosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Proceratosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/proceratosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Secodontosaurus
@dino.command()
async def secodontosaurus():
        embed = discord.Embed(
                title = 'Secodontosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Secodontosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/secodontosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 114 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Tenontosaurus
@dino.command()
async def tenontosaurus():
        embed = discord.Embed(
                title = 'Tenontosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Tenontosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tenontosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#WORKLOAD FOR NOW

#Ankylosaurus Gen 2
@dino.command()
async def ankylosaurus2():
        embed = discord.Embed(
                title = 'Ankylosaurus Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Ankylosaurus-Gen-2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/ankylosaurus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 111 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Ankylosaurus Gen 2 (LV5, 50 DNA) +  Ophiacodon (LV5, 50 DNA) = Ankylocodon\
            \nAlanqa (LV ??, ?? DNA) + Ankylosaurus Gen 2 (LV15, 500 DNA) = Alankylosaurus', inline = 'false')

        await client.say(embed = embed)

#Dimetrodon Gen 2
@dino.command()
async def dimetrodon2():
        embed = discord.Embed(
                title = 'Dimetrodon Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Dimetrodon-Gen-2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/dimetrodon-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 112 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dimetrodon Gen 2 (L15, 500 DNA) + Monolophosaurus Gen 2 (LV15, 500 DNA) = Monolometrodon', inline = 'false')

        await client.say(embed = embed)

#Baryonyx Gen 2
@dino.command()
async def baryonyx2():
        embed = discord.Embed(
                title = 'Baryonyx Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/8689E7EC-3A11-4407-BF7E-CF4BC5A073B8.jpeg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/baryonyx-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Dracorex Gen 2
@dino.command()
async def dracorex2():
        embed = discord.Embed(
                title = 'Dracorex Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/Dracorex2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/dracorex-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 119 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Koolasuchus
@dino.command()
async def koolasuchus():
        embed = discord.Embed(
                title = 'Koolasuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Koolasuchus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/koolasuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Koolasuchus Gen 2
@dino.command()
async def koolasuchus2():
        embed = discord.Embed(
                title = 'Koolasuchus Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Koolasuchus-Gen-2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/koolasuchus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)


#Monolophosaurus Gen 2
@dino.command()
async def monolophosaurus2():
        embed = discord.Embed(
                title = 'Monolophosaurus Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/monolophosaurus-gen-2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/monolophosaurus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 127 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dimetrodon Gen 2 (L15, 500 DNA) + Monolophosaurus Gen 2 (LV15, 500 DNA) = Monolometrodon', inline = 'false')

        await client.say(embed = embed)

#Stygimoloch Gen 2
@dino.command()
async def stygimoloch2():
        embed = discord.Embed(
                title = 'Stygimoloch Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Stygimoloch_GEN2.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/stygimoloch-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Spinosaurus Gen 2
@dino.command()
async def spinosaurus2():
        embed = discord.Embed(
                title = 'Spinosaurus Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Spinosaurus_GEN2_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/stygimoloch-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Triceratops Gen 2
@dino.command()
async def triceratops2():
        embed = discord.Embed(
                title = 'Triceratops Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Triceratops-Gen-2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/triceratops-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 113 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Tyrannosaurus Rex Gen 2
@dino.command()
async def trex2():
        embed = discord.Embed(
                title = 'Tyrannosaurus Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Tyrannosaurus-Rex-Gen-2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tyrannosaurus-gen2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Irritator Gen 2
@dino.command()
async def irritator2():
        embed = discord.Embed(
                title = 'Irritator Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Irritator_GEN2_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/irritator-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 122 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Suchomimus (LV5, 50 DNA) + Irritator Gen 2 (LV5, 50 DNA) = Suchotator \
            \nDiplocaulus Gen 1 (LV5, 50 DNA) + Irritator Gen 2 (LV5, 50 DNA) = Diplotator', inline = 'false')

        await client.say(embed = embed)

#Suchomimus
@dino.command()
async def suchominus():
        embed = discord.Embed(
                title = 'Suchomimus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Suchomimus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/suchominus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Suchomimus (LV5, 50 DNA) + Irritator Gen 2 (LV5, 50 DNA) = Suchotator', inline = 'false')

        await client.say(embed = embed)

#Suchotator
@dino.command()
async def suchotator():
        embed = discord.Embed(
                title = 'Suchotator Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Suchotator_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/suchotator/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 115 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Suchomimus (LV5, 50 DNA) + Irritator Gen 2 (LV5, 50 DNA) = Suchotator', inline = 'false')

        await client.say(embed = embed)

#Einiosaurus
@dino.command()
async def einiosaurus():
        embed = discord.Embed(
                title = 'Einiosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Eniosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/einiosaurus-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 114 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Einiosaurus (LV5, 50 DNA) + Nundasuchus (LV5, 50 DNA) = Einiasuchus', inline = 'false')

        await client.say(embed = embed)

#Nundasuchus
@dino.command()
async def nundasuchus():
        embed = discord.Embed(
                title = 'Nundasuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Nundasuchus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/nundasuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Einiosaurus (LV5, 50 DNA) + Nundasuchus (LV5, 50 DNA) = Einiasuchus \
            \nMajungasaurus (LV5, 50 DNA) + Nundasuchus (LV5, 50 DNA) = Majundasuchus', inline = 'false')

        await client.say(embed = embed)

#Einiasuchus
@dino.command()
async def einiasaurus():
        embed = discord.Embed(
                title = 'Einiasaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Eniasaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/einiasaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 20% \n__Speed:__ 117 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Einiosaurus (LV5, 50 DNA) + Nundasuchus (LV5, 50 DNA) = Einiasuchus \
            \nSarcosuchus (LV15, 200 DNA) + Einiasuchus (LV15, 50 DNA) = Sarcorixis', inline = 'false')

        await client.say(embed = embed)

#Majungasaurus
@dino.command()
async def majungasaurus():
        embed = discord.Embed(
                title = 'Majungasaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Majungasaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/majungasaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 105 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Majungasaurus (LV5, 50 DNA) + Nundasuchus (LV5, 50 DNA) = Majundasuchus', inline = 'false')

        await client.say(embed = embed)

#Majundasuchus
@dino.command()
async def majundasuchus():
        embed = discord.Embed(
                title = 'Majundasuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Majundasuchus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/majundasuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 108 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Majungasaurus (LV5, 50 DNA) + Nundasuchus (LV5, 50 DNA) = Majundasuchus', inline = 'false')

        await client.say(embed = embed)

#Pyroraptor
@dino.command()
async def pyroraptor():
        embed = discord.Embed(
                title = 'Pyroraptor Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Pyroraptor.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/pyroraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Pyroraptor (LV15, 50 DNA) + Irritator (LV5, 200 DNA) = Pyrritator', inline = 'false')

        await client.say(embed = embed)

#Irritator
@dino.command()
async def irritator():
        embed = discord.Embed(
                title = 'Irritator Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Irritator_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/irritator/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Pyroraptor (LV15, 50 DNA) + Irritator (LV5, 200 DNA) = Pyrritator', inline = 'false')

        await client.say(embed = embed)

#Pyrritator
@dino.command()
async def pyrritator():
        embed = discord.Embed(
                title = 'Pyrritator Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Pyrritator_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/pyrritator/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 127 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Pyroraptor (LV15, 50 DNA) + Irritator (LV5, 200 DNA) = Pyrritator \
            \nDimetrodon (LV20, 500 DNA) + Pyrritator (LV20, 50 DNA) = Magnapyritor', inline = 'false')

        await client.say(embed = embed)

#Dimetrodon
@dino.command()
async def dimetrodon():
        embed = discord.Embed(
                title = 'Dimetrodon Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Dimetrodon.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/dimetrodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 113 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dimetrodon (LV20, 500 DNA) + Pyrritator (LV20, 50 DNA) = Magnapyritor \
            \nPostosuchus (LV10, 50 DNA) + Dimetrodon (LV10, 50 DNA) = Postimetrodon', inline = 'false')

        await client.say(embed = embed)

#Magnapyritor
@dino.command()
async def magnapyritor():
        embed = discord.Embed(
                title = 'Magnapyritor Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Magnapyritor_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/magnapyritor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dimetrodon (LV20, 500 DNA) + Pyrritator (LV20, 50 DNA) = Magnapyritor', inline = 'false')

        await client.say(embed = embed)

#Postosuchus
@dino.command()
async def postosuchus():
        embed = discord.Embed(
                title = 'Postosuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/postosuchus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/postosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Postosuchus (LV10, 50 DNA) + Dimetrodon (LV10, 50 DNA) = Postimetrodon', inline = 'false')

        await client.say(embed = embed)

#Postimetrodon
@dino.command()
async def postimetrodon():
        embed = discord.Embed(
                title = 'Postimetrodon Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Postimetrodon.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/postimetrodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 119 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Postosuchus (LV10, 50 DNA) + Dimetrodon (LV10, 50 DNA) = Postimetrodon \
            \nBaryonyx (Lv15, 50 DNA) + Postimetrodon (LV15, 50 DNA) = Tryostronix', inline = 'false')

        await client.say(embed = embed)

#Baryonyx
@dino.command()
async def baryonyx():
        embed = discord.Embed(
                title = 'Baryonyx Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/012C3A16-3782-437F-A5DE-06A6FE1129C1.jpeg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/baryonyx/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 121 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Baryonyx (Lv15, 50 DNA) + Postimetrodon (LV15, 50 DNA) = Tryostronix', inline = 'false')

        await client.say(embed = embed)

#Tryostronix
@dino.command()
async def tryostronix():
        embed = discord.Embed(
                title = 'Tryostronix Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Tryostronix.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tryostronix/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Baryonyx (Lv15, 50 DNA) + Postimetrodon (LV15, 50 DNA) = Tryostronix', inline = 'false')

        await client.say(embed = embed)

#Nodosaurus
@dino.command()
async def nodosaurus():
        embed = discord.Embed(
                title = 'Nodosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Nodosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/nodosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 113 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Apatosaurus (LV10, 200 DNA) + Nodosaurus (LV10, 50 DNA) = Nodopatosaurus', inline = 'false')

        await client.say(embed = embed)

#Apatosaurus
@dino.command()
async def apatosaurus():
        embed = discord.Embed(
                title = 'Apatosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Apatosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/apatosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 101 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Apatosaurus (LV10, 200 DNA) + Nodosaurus (LV10, 50 DNA) = Nodopatosaurus', inline = 'false')

        await client.say(embed = embed)

#Nodopatosaurus
@dino.command()
async def nodopatosaurus():
        embed = discord.Embed(
                title = 'Nodopatosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Nodopatosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/nodopatosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 106 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Apatosaurus (LV10, 200 DNA) + Nodosaurus (LV10, 50 DNA) = Nodopatosaurus\
            \nStegosaurus (LV15, 500 DNA) + Nodopatosaurus (LV15, 50 DNA) = Stegodeus \
            \nNodopatosaurus (LV15, 50 DNA) + Amargasaurus (LV15, 200 DNA) = Gigaspikasaur\
            \nGiraffatitan (LV15, 50 DNA) + Nodopatosaurus (LV15, 50 DNA)= Nodopatotitan', inline = 'false')

        await client.say(embed = embed)

#Stegodeus
@dino.command()
async def stegodeus():
        embed = discord.Embed(
                title = 'Stegodeus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Stegodeus_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/stegodeus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 30% \n__Speed:__ 107 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Stegosaurus (LV15, 500 DNA) + Nodopatosaurus (LV15, 50 DNA) = Stegodeus', inline = 'false')

        await client.say(embed = embed)

#Gigaspikasaur
@dino.command()
async def gigaspikasaur():
        embed = discord.Embed(
                title = 'Gigaspikasaur Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Gigaspikasaur.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/gigaspikasaur/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 109 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Nodopatosaurus (LV15, 50 DNA) + Amargasaurus (LV15, 200 DNA) = Gigaspikasaur', inline = 'false')

        await client.say(embed = embed)

#Triceratops
@dino.command()
async def triceratops():
        embed = discord.Embed(
                title = 'Triceratops Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/triceratops.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/triceratops/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 20% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Triceratops (LV10, 50 DNA) + Stegosaurus (LV10, 200 DNA) = Stegoceratops', inline = 'false')

        await client.say(embed = embed)

#Stegosaurus
@dino.command()
async def stegosaurus():
        embed = discord.Embed(
                title = 'Stegosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/stegosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/stegosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Triceratops (LV10, 50 DNA) + Stegosaurus (LV10, 200 DNA) = Stegoceratops', inline = 'false')

        await client.say(embed = embed)

#Stegoceratops
@dino.command()
async def stegoceratops():
        embed = discord.Embed(
                title = 'Stegosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/stegoceratops.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/stegoceratops/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 115 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Triceratops (LV10, 50 DNA) + Stegosaurus (LV10, 200 DNA) = Stegoceratops \
            \nStegoceratops (LV15, 50 DNA) + Monolophosaurus (LV15, 50 DNA) = Monostegotops', inline = 'false')

        await client.say(embed = embed)

#Monolophosaurus
@dino.command()
async def monolophosaurus():
        embed = discord.Embed(
                title = 'Monolophosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/monolophosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/monolophosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Stegoceratops (LV15, 50 DNA) + Monolophosaurus (LV15, 50 DNA) = Monostegotops \
            \nMonolophosaurus (LV15, 50 DNA) + Gallimimus (LV15, 50 DNA) = Monomimus', inline = 'false')

        await client.say(embed = embed)

#Monostegotops
@dino.command()
async def monostegotops():
        embed = discord.Embed(
                title = 'Monostegotops Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/monostegotops.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/monostegotops/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 20% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Stegoceratops (LV15, 50 DNA) + Monolophosaurus (LV15, 50 DNA) = Monostegotops', inline = 'false')

        await client.say(embed = embed)

#Amargasaurus
@dino.command()
async def amargasaurus():
        embed = discord.Embed(
                title = 'Amargasaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/amargasaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/amargasaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 103 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Nodopatosaurus (LV15, 50 DNA) + Amargasaurus (LV15, 200 DNA) = Gigaspikasaur \
            \nAmargasaurus (LV10, 50 DNA) + Euoplocephalus (LV15, 200 DNA) = Amargocephalus', inline = 'false')

        await client.say(embed = embed)

#Euoplocephalus
@dino.command()
async def euplocephalus():
        embed = discord.Embed(
                title = 'Euoplocephalus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/euplocephalus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/euplocephalus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 110 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Amargasaurus (LV10, 50 DNA) + Euoplocephalus (LV15, 200 DNA) = Amargocephalus', inline = 'false')

        await client.say(embed = embed)

#Amargocephalus
@dino.command()
async def amargocephalus():
        embed = discord.Embed(
                title = 'Amargocephalus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Amargocephalus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/amargocephalus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 105 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Amargasaurus (LV10, 50 DNA) + Euoplocephalus (LV15, 200 DNA) = Amargocephalus \
            \nAmargocephalus (LV15, 50 DNA) + Parasaurolophus (LV15, 500 DNA) = Tragodistis', inline = 'false')

        await client.say(embed = embed)

#Parasaurolophus
@dino.command()
async def parasaurolophus():
        embed = discord.Embed(
                title = 'Parasaurolophus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/parasaurolophus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/parasaurolophus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Amargocephalus (LV15, 50 DNA) + Parasaurolophus (LV15, 500 DNA) = Tragodistis \
            \nParasaurolophus (LV15, 200 DNA) + Stygimoloch (LV15, 50 DNA) = Paramoloch', inline = 'false')

        await client.say(embed = embed)

#Tragodistis
@dino.command()
async def tragodistis():
        embed = discord.Embed(
                title = 'Tragodistis Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Tragodistis.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tragodistis/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Amargocephalus (LV15, 50 DNA) + Parasaurolophus (LV15, 500 DNA) = Tragodistis', inline = 'false')

        await client.say(embed = embed)

#Stygimoloch
@dino.command()
async def stygimoloch():
        embed = discord.Embed(
                title = 'Stygimoloch Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Stygimoloch.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/stygimoloch/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Parasaurolophus (LV15, 200 DNA) + Stygimoloch (LV15, 50 DNA) = Paramoloch \
            \nTuojiangosaurus (LV20, 500 DNA) +  Paramoloch (LV20, 50 DNA) = Tuoramoloch', inline = 'false')

        await client.say(embed = embed)

#Paramoloch
@dino.command()
async def paramoloch():
        embed = discord.Embed(
                title = 'Paramoloch Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Paramoloch.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/paramoloch/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 127 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Parasaurolophus (LV15, 200 DNA) + Stygimoloch (LV15, 50 DNA) = Paramoloch \
            \nTuojiangosaurus (LV20, 500 DNA) +  Paramoloch (LV20, 50 DNA) = Tuoramoloch', inline = 'false')

        await client.say(embed = embed)

#Allosaurus
@dino.command()
async def allosaurus():
        embed = discord.Embed(
                title = 'Allosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Allosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/allosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Sinoceratops (LV15, 50 DNA) + Allosaurus (LV15, 500 DNA) = Allosinosaurus', inline = 'False')

        await client.say(embed = embed)

#Sinoceratops
@dino.command()
async def sinoceratops():
        embed = discord.Embed(
                title = 'Sinoceratops Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Sinoceratops.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/sinoceratops/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Sinoceratops (LV15, 50 DNA) + Allosaurus (LV15, 500 DNA) = Allosinosaurus \
            \nSinoceratops (LV15, 50 DNA) + Utahraptor (LV15, 200 DNA) = Utasinoraptor', inline = 'False')

        await client.say(embed = embed)

#Allosinosaurus
@dino.command()
async def allosinosaurus():
        embed = discord.Embed(
                title = 'Allosinosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Allosinosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/allosinosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 107 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Sinoceratops (LV15, 50 DNA) + Allosaurus (LV15, 500 DNA) = Allosinosaurus', inline = 'false')

        await client.say(embed = embed)

#Utahraptor
@dino.command()
async def utahraptor():
        embed = discord.Embed(
                title = 'Utahraptor Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Utahraptor.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/utahraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Utahraptor (LV15, 200 DNA) + Sinoceratops (LV15, 50 DNA) = Utahsinoraptor \
            \nSpinosaurus (LV10, 50 DNA) + Utahraptor (LV10, 50 DNA) = Spinotahraptor', inline = 'false')

        await client.say(embed = embed)

#Spinosaurus
@dino.command()
async def spinosaurus():
        embed = discord.Embed(
                title = 'Spinosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Spinosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/spinosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Spinosaurus (LV10, 50 DNA) + Utahraptor (LV10, 50 DNA) = Spinotahraptor', inline = 'false')

        await client.say(embed = embed)

#Spinotahraptor
@dino.command()
async def spinotahraptor():
        embed = discord.Embed(
                title = 'Spinotahraptor Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Spinotahraptor.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/spinotahraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Spinosaurus (LV10, 50 DNA) + Utahraptor (LV10, 50 DNA) = Spinotahraptor \
            \nSpinotahraptor (Lv15, 50 DNA) + Kaprosuchus (LV15, 200 DNA) = Spinotasuchus', inline = 'false')

        await client.say(embed = embed)

#Utasinoraptor
@dino.command()
async def utasinoraptor():
        embed = discord.Embed(
                title = 'Utasinoraptor Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/utasinoraptor.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/utasinoraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Utahraptor (LV15, 200 DNA) + Sinoceratops (LV15, 50 DNA) = Utasinoraptor \
            \nUtasinoraptor (LV20, 50 DNA) + Dracorex (LV20, 500 DNA) = Utarinex', inline = 'false')

        await client.say(embed = embed)

#Dracorex
@dino.command()
async def dracorex():
        embed = discord.Embed(
                title = 'Dracorex Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/JWA_Profile_Dracorex.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/dracorex/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Utasinoraptor (LV20, 50 DNA) + Dracorex (LV20, 500 DNA) = Utarinex', inline = 'false')

        await client.say(embed = embed)

#Utarinex
@dino.command()
async def utarinex():
        embed = discord.Embed(
                title = 'Utarinex Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Utarhinex.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/utarinex/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Utasinoraptor (LV20, 50 DNA) + Dracorex (LV20, 500 DNA) = Utarinex', inline = 'false')

        await client.say(embed = embed)

#Kaprosuchus
@dino.command()
async def kaprosuchus():
        embed = discord.Embed(
                title = 'Kaprosuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Kaprosuchus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/kaprosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Gorgosaurus (LV10, 50 DNA) + Kaprosuchus (LV10, 50 DNA) = Gorgosuchus \
            \nSpinotahraptor (Lv15, 50 DNA) + Kaprosuchus (LV15, 200 DNA) = Spinotasuchus', inline = 'false')

        await client.say(embed = embed)

#Gorgosaurus
@dino.command()
async def gorgosaurus():
        embed = discord.Embed(
                title = 'Gorgosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Gorgosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/gorgosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 102 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Gorgosaurus (LV10, 50 DNA) + Kaprosuchus (LV10, 50 DNA) = Gorgosuchus', inline = 'false')

        await client.say(embed = embed)

#Gorgosuchus
@dino.command()
async def gorgosuchus():
        embed = discord.Embed(
                title = 'Gorgosuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Gorgosuchus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/gorgosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Gorgosaurus (LV10, 50 DNA) + Kaprosuchus (LV10, 50 DNA) = Gorgosuchus \
            \nGorgosuchus (LV15, 50 DNA) + Megalosaurus (LV15, 50 DNA) = Megalosuchus', inline = 'false')

        await client.say(embed = embed)

#Megalosaurus
@dino.command()
async def megalosaurus():
        embed = discord.Embed(
                title = 'Megalosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/megalosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/megalosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 105 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Gorgosuchus (LV15, 50 DNA) + Megalosaurus (LV15, 50 DNA) = Megalosuchus', inline = 'false')

        await client.say(embed = embed)

#Megalosuchus
@dino.command()
async def megalosuchus():
        embed = discord.Embed(
                title = 'Megalosuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/megalosuchus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Megalosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 115 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Gorgosuchus (LV15, 50 DNA) + Megalosaurus (LV15, 50 DNA) = Megalosuchus', inline = 'false')

        await client.say(embed = embed)

#Spinotasuchus
@dino.command()
async def spinotasuchus():
        embed = discord.Embed(
                title = 'Spinotasuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Spinotasuchus_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/spinotasuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Spinotahraptor (Lv15, 50 DNA) + Kaprosuchus (LV15, 200 DNA) = Spinotasuchus', inline = 'false')

        await client.say(embed = embed)

#-----------------------------------------set 5-----------------------------------------------------------

#Rajasaurus
@dino.command()
async def rajasaurus():
        embed = discord.Embed(
                title = 'Rajasaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Rajasaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/rajasaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Rajasaurus (LV15, 50 DNA) + Ankylosaurus (LV15, 50 DNA)', inline = 'false')

        await client.say(embed = embed)

#Ankylosaurus
@dino.command()
async def ankylosaurus():
        embed = discord.Embed(
                title = 'Ankylosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Ankylosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/ankylosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 30% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Rajasaurus (LV15, 50 DNA) + Ankylosaurus (LV15, 50 DNA) = Rajakylosaurus \
            \nAnkylosaurus (LV15, 50 DNA) + Kentrosaurus (LV15, 50 DNA) = Ankyntrosaurus', inline = 'false')

        await client.say(embed = embed)

#Rajakylosaurus
@dino.command()
async def rajakylosaurus():
        embed = discord.Embed(
                title = 'Rajakylosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Rajakylosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/rajakylosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 104 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Rajasaurus (LV15, 50 DNA) + Ankylosaurus (LV15, 50 DNA) = Rajakylosaurus \
            \nRajakylosaurus (LV20, 50 DNA) + Tuojiangosaurus (Lv20, 50 DNA) = Diorajasaur', inline = 'false')

        await client.say(embed = embed)

#Kentrosaurus
@dino.command()
async def kentrosaurus():
        embed = discord.Embed(
                title = 'Kentrosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Kentrosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Kentrosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__0% \n__Speed:__ 115 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Ankylosaurus (LV15, 50 DNA) + Kentrosaurus (LV15, 50 DNA) = Ankyntrosaurus', inline = 'false')

        await client.say(embed = embed)

#Ankyntrosaurus
@dino.command()
async def ankyntrosaurus():
        embed = discord.Embed(
                title = 'Ankyntrosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Ankyntrosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/ankyntrosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__25% \n__Speed:__ 111 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Ankylosaurus (LV15, 50 DNA) + Kentrosaurus (LV15, 50 DNA) = Ankyntrosaurus \
            \nTryannosaurus Rex (LV20, 200 DNA) + Ankyntrosaurus (L20, 50 DNA) = Trykosaurus', inline = 'false')

        await client.say(embed = embed)

#Tuojiangosaurus
@dino.command()
async def tuojiangosaurus():
        embed = discord.Embed(
                title = 'Tuojiangosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/tuojiangosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tuojiangosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 112 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Rajakylosaurus (LV20, 50 DNA) + Tuojiangosaurus (Lv20, 50 DNA) = Diorajasaur \
            \nTuojiangosaurus (LV20, 500 DNA) +  Paramoloch (LV20, 50 DNA) = Tuoramoloch', inline = 'false')

        await client.say(embed = embed)

#Diorajasaur
@dino.command()
async def diorajasaur():
        embed = discord.Embed(
                title = 'Diorajasaur Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Diorajasaur_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/diorajasaur/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 106 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Rajakylosaurus (LV20, 50 DNA) + Tuojiangosaurus (Lv20, 50 DNA) = Diorajasaur', inline = 'false')

        await client.say(embed = embed)

#Velociraptor
@dino.command()
async def velociraptor():
        embed = discord.Embed(
                title = 'Velociraptor Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Velociraptor.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/velociraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 132 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Tryannosaurus Rex (LV15, 50 DNA) + Velociraptor (LV15, 500 DNA) = Indominus Rex \
            \nIndominus Rex (Lv20, 50 DNA) + Velociraptor (LV20, 2000 DNA) = Indoraptor', inline = 'false')

        await client.say(embed = embed)

#Tyrannosaurus Rex
@dino.command()
async def trex():
        embed = discord.Embed(
                title = 'Tyrannosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Tyrannosaurus-Rex.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tyrannosaurus-rex/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 102 \n__Critical:__ 30%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Tryannosaurus Rex (LV15, 50 DNA) + Velociraptor (LV15, 500 DNA) = Indominus Rex', inline = 'false')

        await client.say(embed = embed)

#Indominus Rex
@dino.command()
async def indorex():
        embed = discord.Embed(
                title = 'Indominus Rex Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Indominus-Rex.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Indominus-rex/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 106 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Tryannosaurus Rex (LV15, 50 DNA) + Velociraptor (LV15, 500 DNA) = Indominus Rex \
            \nIndominus Rex (LV20, 50 DNA) + Velociraptor (LV20, 2000 DNA) = Indoraptor', inline = 'false')

        await client.say (embed = embed)

#Indoraptor
@dino.command()
async def indoraptor():
        embed = discord.Embed(
                title = 'Indoraptor Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/F14BA6A0-C0DF-463E-94C6-92D8D5CFB80C.jpeg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Indoraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Indominus Rex (LV20, 50 DNA) + Velociraptor (LV20, 2000 DNA) = Indoraptor', inline = 'false')

        await client.say (embed = embed)

#Erlidominus
@dino.command()
async def erlidominus():
        embed = discord.Embed(
                title = 'Erlidominus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Erlidominus_result.jpg")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/erlidominus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Erlikosaurus (LV20, 200 DNA) + Indominus Rex (LV20, 50 DNA) = Erlidominus', inline = 'false')

        await client.say(embed = embed)

#Erlikosaurus
@dino.command()
async def erlikosaurus():
        embed = discord.Embed(
                title = 'Erlikosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/erlikosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/erlikosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Erlikosaurus (LV20, 200 DNA) + Indominus Rex (LV20, 50 DNA) = Erlidominus', inline = 'false')

        await client.say(embed = embed)

#Trykosaurus
@dino.command()
async def trykosaurus():
        embed = discord.Embed(
                title = 'Trykosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/trykosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Trykosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 102 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Tryannosaurus Rex (LV20, 200 DNA) + Ankyntrosaurus (L20, 50 DNA) = Trykosaurus', inline = 'false')

        await client.say(embed = embed)

#------------------------------------------Extra-Dinosaurs-to-code-after-first-attempt---------------------------------#

#Brachiosaurus
@dino.command()
async def brachiosaurus():
        embed = discord.Embed(
                title = 'Brachiosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Brachiosaurus-1.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/brachiosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 111 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Gallimimus
@dino.command()
async def gallimimus():
        embed = discord.Embed(
                title = 'Gallimimus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Gallimimus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/gallimimus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Monolophosaurus (LV15, 50 DNA) + Gallimimus (LV15, 50 DNA) = Monomimus', inline = 'false')

        await client.say(embed = embed)

#Giraffatitan
@dino.command()
async def giraffatitan():
        embed = discord.Embed(
                title = 'Giraffatitan Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Giraffatitan.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/giraffatitan/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 107 \n__Critical:__ 10%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Giraffatitan (LV15, 50 DNA) + Nodopatosaurus (LV15, 50 DNA)= Nodopatotitan', inline = 'false')

        await client.say(embed = embed)

#Ornithomimus
@dino.command()
async def ornithomimus():
        embed = discord.Embed(
                title = 'Ornithomimus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Ornithomimus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/ornithomimus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 131 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Gryposuchus
@dino.command()
async def gryposuchus():
        embed = discord.Embed(
                title = 'Gryposuchus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Gyprosuchus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/gryposuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 20% \n__Speed:__ 116 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Diplotator
@dino.command()
async def diplotator():
        embed = discord.Embed(
                title = 'Diplotator Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Diplotator.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/diplotator/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Diplocaulus Gen 1 (LV5, 50 DNA) + Irritator Gen 2 (LV5, 50 DNA) = Diplotator', inline = 'false')

        await client.say(embed = embed)

#Ankylocodon
@dino.command()
async def ankylocodon():
        embed = discord.Embed(
                title = 'Ankylocodon Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Ankylocodon-1.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/ankylocodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 107 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Ankylosaurus Gen 2 (LV5, 50 DNA) +  Ophiacodon (LV5, 50 DNA) = Ankylocodon', inline = 'false')

        await client.say(embed = embed)

#Diloranosaurus
@dino.command()
async def diloranosaurus():
        embed = discord.Embed(
                title = 'Diloranosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Diloranosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Diloranosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dilophosaurus (LV15, 50 DNA) + Ouranosaurus (LV15, 50 DNA) = Diloranosaurus\
            \nDilophosaurus (LV20, ?? DNA) + Deinocheirus (LV20, ?? DNA) = Diloracheirus', inline = 'false')

        await client.say(embed = embed)

#Monomimus
@dino.command()
async def monomimus():
        embed = discord.Embed(
                title = 'Monomimus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Monomimus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/monomius/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Monolophosaurus  (LV15, 50 DNA) + Gallimimus (LV15, 50 DNA) = Monomimus', inline = 'false')

        await client.say(embed = embed)

#Tuoramoloch
@dino.command()
async def tuoramoloch():
        embed = discord.Embed(
                title = 'Tuoramoloch Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Tuaromoloch.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Tuoramoloch/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Tuojiangosaurus (LV20, 500 DNA) +  Paramoloch (LV20, 50 DNA) = Tuoramoloch', inline = 'false')

        await client.say(embed = embed)

#Sarcorixis
@dino.command()
async def sarcorixis():
        embed = discord.Embed(
                title = 'Sarcorixis Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Sarcorixi.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/sarcorxis/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 115 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Sarcosuchus (LV15, 200 DNA) + Einiasuchus (LV15, 50 DNA) = Sarcorixis', inline = 'false')

        await client.say(embed = embed)

#Dilophosaurus
@dino.command()
async def dilophosaurus():
        embed = discord.Embed(
                title = 'Dilophosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Dilophosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Dilophosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dilophosaurus (LV15, 50 DNA) + Ouranosaurus (LV15, 50 DNA) = Diloranosaurus', inline = 'false')

        await client.say(embed = embed)

#Dilophosaurus Gen 2
@dino.command()
async def dilophosaurus2():
        embed = discord.Embed(
                title = 'Dilophosaurus Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Dilophosaurus-Gen-2.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/Dilophosaurus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 121 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Bird Update-------------------------------------------
#Nodopatotitan
@dino.command()
async def nodopatotitan():
        embed = discord.Embed(
                title = 'Nodopatitan Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Nodopatitain.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/nodopatotitan/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 105 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Giraffatitan (LV15, 50 DNA) + Nodopatosaurus (LV15, 50 DNA)= Nodopatotitan', inline = 'false')

        await client.say(embed = embed)

#Diloracheirus
@dino.command()
async def diloracheirus():
        embed = discord.Embed(
                title = 'Diloracheirus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Diloracherius.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/diloracheirus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dilophosaurus (LV20, ?? DNA) + Deinocheirus (LV20, ?? DNA) = Diloracheirus', inline = 'false')

        await client.say(embed = embed)

#Monolometrodon
@dino.command()
async def monolometrodon():
        embed = discord.Embed(
                title = 'Monolometrodon Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Monomoletrodon.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/monolometrodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 119 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Dimetrodon Gen 2 (L15, 500 DNA) + Monolophosaurus Gen 2 (LV15, 500 DNA) = Monolometrodon', inline = 'false')

        await client.say(embed = embed)

#Hatzegopteryx
@dino.command()
async def hatzegopteryx():
        embed = discord.Embed(
                title = 'Hatzegopteryx Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Hatzegop.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/hatzegopteryx/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 114 \n__Critical:__ 0%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Swap-In Defense', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Arambourgiania
@dino.command()
async def arambourgiania():
        embed = discord.Embed(
                title = 'Arambourgiania Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Arambourgiania.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/arambourgiania/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 112 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Swap-In Invicibility', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Quetzalcoatlus
@dino.command()
async def quetzalcoatlus():
        embed = discord.Embed(
                title = 'Quetzalcoatlus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Quetzal-.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/quetzalcoatlus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 114 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Swap-In Defense', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Tupandactylus
@dino.command()
async def tupandactylus():
        embed = discord.Embed(
                title = 'Tupandactylus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Tupandactylus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/tupandactylus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 109 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack \
            \nSwap-In Ferocity', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#Alanqa
@dino.command()
async def alanqa():
        embed = discord.Embed(
                title = 'Alanqa Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Alanqa.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/alanqa/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Swap-In Invicibility', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Alanqa (LV ??, ?? DNA) + Ankylosaurus Gen 2 (LV15, 500 DNA) = Alankylosaurus', inline = 'false')

        await client.say(embed = embed)


#Alankylosaurus
@dino.command()
async def alankylosaurus():
        embed = discord.Embed(
                title = 'Alankylosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Alankylosaurus.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/alankylosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 110 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Swap-In Invicibility', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Alanqa (LV ??, ?? DNA) + Ankylosaurus Gen 2 (LV15, 500 DNA) = Alankylosaurus', inline = 'false')

        await client.say(embed = embed)

#Pteranodon
@dino.command()
async def pteranodon():
        embed = discord.Embed(
                title = 'Pteranodon Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/09/Pteranodon-.png")
        embed.set_author(name = "Moveset and More information here", url="https://metahub.info/jwa-dinosaur/pteranodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 112 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack \nSwap-In Ferocity', inline = 'false')
        embed.add_field(name = 'None', inline = 'false')

        await client.say(embed = embed) 
#---------------------------------------------------------------------END PROJECT DINODEX----------------------------------------------------------------------------------------------------------#

client.run(TOKEN)
