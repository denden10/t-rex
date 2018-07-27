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
    await client.change_presence(game=discord.Game(name="Dino Dex"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Bot Ready. Prepare for Trouble. Rawr.'   )


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
@client.group(brief = 'Gives brief information about dinosaurs in Jurassic World Alive.', description = 'Usage: $dino [dinosaur] \n Some dinosaurs are shown below:')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/weurhosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Instant Cripple (Priority, -90% dmg) \
            \nStrike (1x dmg) \
            \nThagomizer (1.5x dmg, -50% Speed)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Sarcosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 110 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Expose Weak Spot (1x dmg, Vulnerable) \
            \nPinning Strike (1x dmg, Cannot swap)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/purrusaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 114 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Expose Weak Spot (1x dmg, Vulnerable) \
            \nPinning Strike (1x dmg, Cannot swap) \
            \nStrengthening Strike (1x dmg, +50% dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Purrusaurus_gen2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 114 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Expose Weak Spot (1x dmg, Vulnerable) \
            \nPinning Strike (1x dmg, Cannot swap)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/diplocaulus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Impact (2x dmg, -50% dmg \
            \nNullifying Strike (1x dmg, Removes + Effects)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/diplocaulus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Impact (2x dmg, -50% dmg) \
            \nImpairing Strike (1x dmg, No Crit Chance) \
            \nNullifying Strike (1x dmg, Removes + Effects)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Ophiacodon")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 110 \n__Critical:__ 40%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Rampage (2x, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Argentinosaurus")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 102 \n__Critical:__ 40%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Decelerating Impact (1.5x dmg, -90% speed) \
            \nRampage (2x dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Carnotaurus")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Expose Weak Spot (1x dmg, vulnerable) \
            \nPinning Strike (1x dmg, Cannot swap) \
            \nShort Defense (1x dmg, 50% Shield 2 turns)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Concavenator")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 106 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5 dmg, bypass Armor) \
            \nPinning Strike (1x dmg, Cannot swap) \
            \nShort Defense (1x dmg, 50% Shield 2 turns)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/deinocheirus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 130 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Rampage (2x dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/blue/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 131 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Pounce (2x dmg, -50% dmg) \
            \nShort Defense (1x dmg, 50% Shield 2 turns) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/charlie/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Critical Impact (1.5x dmg, +40% Crit Chance) \
            \nPounce (2x dmg, -50% dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/delta/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 131 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Adrenaline Surge (Priority, 1x -> 1.25 dmg, +25% HP) \
            \nPounce (2x dmg, -50% dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/echo/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Nullifying Strike (1x dmg, Remove + Effects) \
            \nSlowing Impact (1.5 dmg, -50% speed) \
            \nStrike (1x dmg)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/tarbosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 40%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nArmor Piercing Strike (1.0x dmg, bypass Armor)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/tanycolagreus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 130 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1.0x dmg, bypass Armor) \
            \nNullifying Impact (1.5x dmg, Remove + Effects)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/ouranosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 127 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Greater Stunning Rampage (2x dmg, 75% Stun) \
            \nImpact and Run (1.5x dmg, Auto Swap) \
            \nStrike (1x dmg)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/edmontosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Greater Stunning Strike (1x dmg, 75% Stun) \
            \nStrike (1x dmg) \
            \nStrike and Run (1x dmg, Auto Swap)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/igaunodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Greater Stunning Strike (1x dmg, 75% Stun) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/lythronax/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Long Protection (1x dmg, 50% Shield 4 turns) \
            \nPinning Strike (1x dmg, Cannot swap)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)' , inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/proceratosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Impact (2x dmg, -50% dmg) \
            \nNullifying Strike (1x dmg, Remove + Effects) \
            \nSlowing Impact (1.5x dmg, -50% speed)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/secodontosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 114 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nCritical Impact (1.5 dmg, +40% Crit Chance) \
            \nDefense Shattering Rampage (2x dmg, Remove Shield, bypass Armor)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)' , inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/tenontosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Strike (1x dmg, -50% dmg) \
            \nGreater Stunning Strike (1x dmg, 75% Stun) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/ankylosaurus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 111 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Long Protection (1x dmg, +50% Shield 4 turns) \
            \nVulnerability Strike (1x dmg, Vulnerable)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/dimetrodon-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 112 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Rampage (2x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/baryonyx-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nDefense Shattering Impact (1.5x dmg, remove Shield, bypass Armor) \
            \nReady to Crush (+50% dmg, +30% Crit Chance)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/dracorex-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 119 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Strike (1x dmg) \
            \nStrike and Run (1x, Auto Swap)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/koolasuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Impact (2x dmg, -50% dmg) \
            \nNullifying Strike (1x dmg, Remove + Effects) \
            \nSlowing Impact (1.5x dmg, -50% speed)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/koolasuchus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Strike (1x dmg, -50% dmg) \
            \nImpairing Strike (1x dmg, No Crit Chance) \
            \nNullifying Strike (1x dmg, Remove + Effects)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/monolophosaurus-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 127 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Impact (2x dmg, -50% dmg) \
            \nNullifying Strike (1x dmg, Remove + Effects)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/stygimoloch-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Impact and Run (1.5 dmg, Auto Swap) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/stygimoloch-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Exploit Wound (DoT 1x dmg 2 turns, Vulnerable) \
            \nStrike (1x dmg) \
            \nWounding Strike (1x dmg, DoT .5x dmg 2 turns)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/triceratops-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 113 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Low Stunning Strike (1x dmg, -20% Stun) \
            \nRampage (2x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/tyrannosaurus-gen2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nArmor Piercing Rampage (2x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None' , inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

        await client.say(embed = embed)

#---------------------------------------------------------------------------------HYBRIDS HERE--------------------------------------------

#Irritator Gen 2
@dino.command()
async def irritator2():
        embed = discord.Embed(
                title = 'Irritator Gen 2 Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/06/JWA_Profile_Irritator_GEN2_result.jpg")
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/irritator-gen-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 122 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1.0x dmg, bypass Armor) \
            \nReady to Crush (+50% dmg, +30% Crit Chance)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Suchomimus (LV5, 50 DNA) + Irritator Gen 2 (LV5, 50 DNA) = Suchotator', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/suchominus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Strike (1x dmg) \
            \nWounding Strike (1x dmg, DoT .5x dmg 2 turns)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/suchotator/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 115 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1.0x dmg, bypass Armor) \
            \nExpose Weak Spot (1x dmg, Vulnerable) \
            \nLockdown Strike (1x dmg, Cannot Swap) \
            \nWounding Strike (1x dmg, DoT .5x dmg 2 turns)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (Remove Negative Effects)', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Suchomimus (LV5, 50 DNA) + Irritator Gen 2 (LV5, 50 DNA) = Suchotator', inline = 'false')

        await client.say(embed = embed)

#----------------------------hybrids and fusion dinos here (still need to code)---------------------------

#-----------------------------------------set 1-----------------------------------------------------------

#Einiosaurus
@dino.command()
async def einiosaurus():
        embed = discord.Embed(
                title = 'Einiosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Eniosaurus.png")
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/einiosaurus-2/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 114 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Minimal Striking Strike (1x dmg, 10% Stun) \
            \nStunning Impact (1.5x dmg, 33% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/nundasuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Ferocious Strike (1x dmg, +50% dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/einiasaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 20% \n__Speed:__ 117 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Adrenaline Pulse (Priority, +25% HP) \
            \nFerocious Strike (1x dmg, +50% dmg) \
            \nMinimal Striking Strike (1x dmg, 10% Stun) \
            \nStunning Impact (1.5x dmg, 33% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/majungasaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 105 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Pinning Strike (1x dmg, cannot swap) \
            \nShort Defense (1x dmg, +50% Shield 2 turns)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/majundasuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 108 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Cleansing Impact (1.5 dmg, cleanse self) \
            \nFerocious Strike (1x dmg, +50% dmg) \
            \nPinning Strike (1x dmg, cannot swap) \
            \nShort Defense (1x dmg, +50% Shield 2 turns)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Majungasaurus (LV5, 50 DNA) + Nundasuchus (LV5, 50 DNA) = Majundasuchus', inline = 'false')

        await client.say(embed = embed)

#-----------------------------------------set 2-----------------------------------------------------------

#Pyroraptor
@dino.command()
async def pyroraptor():
        embed = discord.Embed(
                title = 'Pyroraptor Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Pyroraptor.png")
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/pyroraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Impact (1.5x dmg) \
            \nPounce (2x dmg, -50% dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/irritator/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor) \
            \nReady to Crush (+50% dmg, +30% Crit Chance)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/pyrritator/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 127 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Rampage (2x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor) \
            \nExpose Weak Spot (1x dmg, Vulnerable) \
            \nReady to Crush (+50% dmg, +30% Crit Chance)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/dimetrodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 113 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nCritical Impact (1.5x dmg, +40% Crit Chance) \
            \nDefense Shattering Impact (1.5x dmg, Remove Shield, bypass Armor)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/magnapyritor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor) \
            \nExpose Weak Spot (1x dmg, Vulnerable) \
            \nRampage (2x dmg)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/postosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Adrenaline Pulse (Priority, +25% HP) \
            \nFerocious Strike (1x dmg, +50% dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/postimetrodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 119 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Adrenaline Surge (Priority, 1x -> 1.25x dmg, +25% HP) \
            \nArmor Piercing Impact (1.5x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor) \
            \nFerocious Strike (1x dmg, +50% dmg)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/baryonyx/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 121 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nDefense Shattering Rampage (2x dmg, Remove Shield, bypass Armor) \
            \nReady to Crush (+50% dmg, +30% Crit Chance)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/tryostronix/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nDefense Shattering Impact (1.5x dmg, Remove Shield, bypass Armor) \
            \nExpose Weak Spot (1x dmg, Vulnerable) \
            \nReady to Crush (+50% dmg, +30% Crit Chance)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Baryonyx (Lv15, 50 DNA) + Postimetrodon (LV15, 50 DNA) = Tryostronix', inline = 'false')

        await client.say(embed = embed)

#-----------------------------------------set 3-----------------------------------------------------------

#Nodosaurus
@dino.command()
async def nodosaurus():
        embed = discord.Embed(
                title = 'Nodosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Nodosaurus.png")
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/nodosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 113 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nShort Defense (1x dmg, 50% Shield 2 turns) \
            \nVulnerability Strike (1x dmg, Vulnerable)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/apatosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 101 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Decelerating Impact (1.5x dmg, -90% Speed) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/nodopatosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 106 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nDecelerating Impact (1.5x dmg, -90% Speed) \
            \nShort Defense (1x dmg, 50% Shield 2 turns) \
            \nStrike (1x dmg)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Apatosaurus (LV10, 200 DNA) + Nodosaurus (LV10, 50 DNA) = Nodopatosaurus\
            \n Stegosaurus (LV15, 500 DNA) + Nodopatosaurus (LV15, 50 DNA) = Stegodeus \
            \n Nodopatosaurus (LV15, 50 DNA) + Amargasaurus (LV15, 200 DNA) = Gigaspikasaur', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/stegodeus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 30% \n__Speed:__ 107 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Rampage (2x dmg, bypass Armor) \
            \nShort Defense (1x dmg, 50% Shield 2 turns) \
            \nSuperiority Strike (1x dmg, -33% Speed, Cleanse Self) \
            \nThagomizer (1.5x dmg, -50% Speed)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/gigaspikasaur/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 109 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nDecelerating Impact (1.5x dmg, -90% Speed) \
            \nShort Defense (1x dmg, 50% Shield 2 turns) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/triceratops/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 20% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Greater Stunning Strike (1x dmg, -75% Stun) \
            \nMinor Stunning Strike (1x dmg, -15% Stun) \
            \nStunning Impact (1.5x dmg, -33% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/stegosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Strike (1x dmg) \
            \nThagomizer (1.5x dmg, -50% Speed)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/stegoceratops/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 115 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Greater Stunning Strike (1x dmg, -75% Stun) \
            \nMinimal Stunning Strike (1x dmg, -10% Stun) \
            \nSlowing Impact (1.5x dmg, -50% Speed) \
            \nStunning Impact (1.5x dmg, -33% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/monolophosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Impact (2x dmg, -50% dmg) \
            \nDistracting Strike (1x dmg, -50% dmg) \
            \nNullifying Strike (1x dmg, Remove + Effects)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Stegoceratops (LV15, 50 DNA) + Monolophosaurus (LV15, 50 DNA) = Monostegotops \
            \nMonolophosaurus (LV15, n/a DNA) + Gallimimus (LV15, n/a DNA) = Monomimus', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/monostegotops/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 20% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Strike (1x dmg, -50% dmg) \
            \nNullifying Strike (1x dmg, Remove + Effects) \
            \nSlowing Impact (1.5x dmg, -50% Speed) \
            \nStunning Impact (1.5x dmg, -33% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/amargasaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 103 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Decelerating Impact (1.5x dmg, -90% Speed) \
            \nSlowing Impact (1.5x dmg, -50% Speed) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/euplocephalus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 110 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Impact (1x dmg) \
            \nVulnerability Strike (1x dmg, Vulnerable)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/amargocephalus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 105 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Decelerating Impact (1.5x dmg, -90% Speed) \
            \nImpact (1.5x dmg) \
            \nInstant Invincibility (Priority, 100% Shield) \
            \nVulnerability Strike (1x dmg, Vulnerable)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/parasaurolophus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Greater Stunning Impact (1.5x dmg, -75% Stun) \
            \nStrike (1x dmg)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Amargocephalus (LV15, 50 DNA) + Parasaurolophus (LV15, 500 DNA) = Tragodistis \
            \nParasaurolophus (LV15, 200 DNA) + Stygimoloch (LV15, 50 DNA) = Paramoloch', inline = 'false')

        await client.say(embed = embed)

#Tragodistis
@dino.command()
async def tragodistis():
        embed = discord.Embed(
                title = 'Parasaurolophus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/tragodistis.png")
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/tragodistis/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 40% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Greater Stunning Impact (1.5x dmg, -75% Stun) \
            \nInstant Invincibility (Priority, 100% Shield) \
            \nRampage (2x dmg) \
            \nVulnerability Strike (1x dmg, Vulnerable)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/stygimoloch/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Impact and Run (1.5x dmg, Auto Swap), \
            \nInstant Charge (Priority, 1x dmg, 100% Stun) \
            \nMinor Stunning Strike (1x dmg, 15% Stun)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Parasaurolophus (LV15, 200 DNA) + Stygimoloch (LV15, 50 DNA) = Paramoloch \
            \nTuojiangosaurus (LV20, n/a DNA) +  Paramoloch (LV20, n/a DNA) = Tuoramoloch', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/paramoloch/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 127 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Instant Cripple (Priority, -90% dmg) \
            \nLow Stunning Strike (1x dmg, 20% Stun) \
            \nStrike and Run (1x dmg, Auto Swap) \
            \nStunning Impact (1.5 dmg, 33% Stun)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Parasaurolophus (LV15, 200 DNA) + Stygimoloch (LV15, 50 DNA) = Paramoloch \
            \nTuojiangosaurus (LV20, n/a DNA) +  Paramoloch (LV20, n/a DNA) = Tuoramoloch', inline = 'false')

        await client.say(embed = embed)

#-----------------------------------------set 4-----------------------------------------------------------

#Allosaurus
@dino.command()
async def allosaurus():
        embed = discord.Embed(
                title = 'Allosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/05/Allosaurus.png")
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/allosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nArmor Piercing Strike (1.0x dmg, bypass Armor)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/sinoceratops/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Instant Charge (1x dmg, 100% Stun) \
            \nLow Stunning Strike (1x dmg, 20% Stun) \
            \nStunning Impact (1.5 dmg, 33% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/allosinosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 107 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nArmor Piercing Rampage (2x dmg, bypass Armor) \
            \nArmor Piercing Strike (1.0x dmg, bypass Armor) \
            \nInstant Charge (1x dmg, 100% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/utahraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Critical Impact (1.5x dmg, +40% Crit Chance) \
            \nPounce (2x dmg, -50% dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/spinosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Expose Weak Spot (1x dmg, Vulnerable) \
            \nStrike (1x dmg) \
            \nWounding Strike (1x dmg, DoT .5x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/spinotahraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Critical Impact (1.5x dmg, +40% Crit Chance) \
            \nDistracting Impact (2x dmg, -50% dmg) \
            \nStrike (1x dmg) \
            \nWounding Strike (1x dmg, DoT .5x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/utasinoraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Critical Impact (1.5x dmg, +40% Crit Chance) \
            \nDistracting Impact (2x dmg, -50% dmg) \
            \nInstant Charge (Priority, 1x dmg, 100% Stun) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/dracorex/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Impact and Run (1.5x dmg, Auto Swap) \
            \nInstant Charge (Priority, 1x dmg, 100% Stun) \
            \nMinor Stunning Strike (1x dmg, 15% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/utarinex/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 123 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Critical Impact (1.5x dmg, +40% Crit Chance) \
            \nImpact and Run (1.5x dmg, Auto Swap) \
            \nInstant Charge (Priority, 1x dmg, 100% Stun) \
            \nLow Stunning Strike (1x dmg, 20% Stun)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/kaprosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 125 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Adrenaline Surge (Priority, 1x -> 1.25x dmg, +25% HP) \
            \nFerocious Strike (1x dmg, +50% dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/gorgosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 102 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor)\
            \nDefense Shattering Impact (1.5x dmg, Remove Shield, bypass Armor) \
            \nFerocious Strike (1x dmg, +50% dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/gorgosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Adrenaline Surge (Priority, 1x -> 1.25x dmg, +25% HP) \
            \nFerocious Strike (1x dmg, +50% dmg) \
            \nRampage (2x dmg) \
            \nStrike (1x dmg)Armor Piercing Strike (1x dmg, bypass Armor)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/megalosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 105 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Impact (1.5x dmg) \
            \nPinning Strike (1x dmg, Cannot Swap) \
            \nShort Defense (1x dmg, 50% Shield)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Megalosuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 115 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Critical Impact (1.5x dmg, +40% Crit Chance) \
            \nFerocious Strike (1x dmg, +50% dmg) \
            \nPinning Strike (1x dmg, Cannot Swap) \
            \nShort Defense (1x dmg, 50% Shield)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/spinotasuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Adrenaline Surge (Priority, 1x -> 1.25x dmg, +25% HP) \
            \nCritical Impact (1.5x dmg, +40% Crit Chance) \
            \nStrike (1x dmg) \
            \nWounding Strike (1x dmg, DoT .5x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/rajasaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 104 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Exploit Wound (DoT 1x 2 turns, Vulnerable) \
            \nPinning Strike (1x dmg, Cannot Swap) \
            \nShort Defense (1x dmg, 50% Shield)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/ankylosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 30% \n__Speed:__ 116 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Instant Invincibility (Priority, 100% Shield) \
            \nLong Protection (1x dmg, 50% Defense) \
            \nVulnerability Strike (1x dmg, Vulnerable)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/rajakylosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 104 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Exploit Wound (DoT 1x 2 turns, Vulnerable) \
            \nInstant Invincibility (Priority, 100% Shield) \
            \nPinning Strike (1x dmg, cannot swap) \
            \nShort Defense (1x dmg, 50% Shield)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Kentrosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__0% \n__Speed:__ 115 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Instant Cripple (Priority, -90% dmg) \
            \nStrike (1x dmg) \
            \nThagomizer (1.5 dmg, -50% Speed)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/ankyntrosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__25% \n__Speed:__ 111 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Instant Cripple (Priority, -90% dmg) \
            \nInstant Invincibility (Priority, 100% Shield) \
            \nThagomizer (1.5 dmg, -50% Speed) \
            \nVulnerability Strike (1x dmg, Vulnerable)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/tuojiangosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 112 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Strike (1x dmg, -50% dmg) \
            \nStrike (1x dmg) \
            \nThagomizer (1.5x dmg, -50% Speed)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Rajakylosaurus (LV20, 50 DNA) + Tuojiangosaurus (Lv20, 50 DNA) = Diorajasaur \
            \nTuojiangosaurus (LV20, n/a DNA) +  Paramoloch (LV20, n/a DNA) = Tuoramoloch', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/diorajasaur/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 106 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Strike (1x dmg, -50% dmg) \
            \nInstant Invincibility (Priority, 100% Shield) \
            \nPinning Strike (1x dmg, cannot swap) \
            \nShort Defense (1x dmg, 50% Shield)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Counter Attack (1x dmg after attack)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/velociraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 132 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Pounce (2x dmg, -50% dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/tyrannosaurus-rex/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 102 \n__Critical:__ 30%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nDefense Shattering Impact (1.5x dmg, Remove Shield, bypass Armor) \
            \nDefense Shattering Rampage (2x dmg, Remove Shield, bypass Armor)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Indominus-rex/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 106 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Rampage (2x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor) \
            \nCloak (Priority, 50% Dodge, Next Attack = 2x dmg) \
            \nExpose Weak Spot (1x dmg, Vulnerable', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'Immunity (No Negative Effects)', inline = 'false')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Indoraptor/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 128 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nCleansing Impact (1.5x dmg, cleanse self) \
            \nCloak (Priority, 50% Dodge, Next Attack = 2x dmg) \
            \nDefense Shattering Ramapge (2x dmg, Remove Shield, bypass Armor)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/erlidominus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nCloak (Priority, +50% Dodge, Next attack = 2x dmg) \
            \nRampage (2x dmg) \
            \nStrike (1x dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/erlikosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Minimal Speedup Strike (1x dmg, +10% Speed) \
            \nRampage (2x dmg) \
            \nStrike and Run (1x dmg, Auto Swap)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Trykosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 102 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Rampage (2x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor) \
            \nExpose Weak Spot (1x dmg, Vulnerable) \
            \nInstant Invincibility (Priority, 100% Shield)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/brachiosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 111 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Bellow (Priority, 50% Shield, -50$ Speed \
            \nRampage (2x dmg) \
            \nSuperiority Strike (1x dmg, -33% Speed, Cleanse Self)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/gallimimus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 124 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Evasive Strike (1x dmg, +50% Dodge Chance \
            \nImpact and Run (1.5x dmg, Auto Swap', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Monolophosaurus (LV15, n/a DNA) + Gallimimus (LV15, n/a DNA) = Monomimus', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/giraffatitan/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 10% \n__Speed:__ 107 \n__Critical:__ 10%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Bellow (Priority, 50% Shield, -50$ Speed \
            \nRampage (2x dmg) \
            \nSuperiority Strike (1x dmg, -33% Speed, Cleanse Self)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/ornithomimus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 131 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
           'Evasive Strike (1x dmg, +50% Dodge Chance \
            \nImpact and Run (1.5x dmg, Auto Swap \
            \n Instant Crippple (Priority, -90% dmg)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/gryposuchus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 20% \n__Speed:__ 116 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Ferocious Strike (1x dmg, +50% dmg) \
            \nLockdown Impact (1.5x dmg, Cannot Swap) \
            \nVulnerability Strike (1x dmg, Vulnerable)', \
            inline = 'False')
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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/diplotator/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 120 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nDefense Shattering Impact (1.5 dmg, bypas Armor, Remove Shield) \
            \nDistracting Strike (1x dmg, -50% dmg) \
            \nReady to Crush (+50% dmg, +30% Crit Chance)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Diplocaulus Gen 1 (LV n/a, n/a DNA) + Irritator Gen 2 (LV n/a, n/a DNA) = Diplotator', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/ankylocodon/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 107 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Impact (1.5x dmg, bypass Armor) \
            \nArmor Piercing Strike (1x dmg, bypass Armor) \
            \nDecelerating Impact (1.5x dmg, -50% Speed) \
            \nLong Protection (1x dmg, +50% Defense 4 turns)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Ankylosaurus Gen 2 (LV n/a, n/a DNA) +  Ophiacodon (LV n/a, n/a DNA) = Ankylocodon', inline = 'false')

        await client.say(embed = embed)

#Diloranosaurus
@dino.command()
async def diloranosaurus():
        embed = discord.Embed(
                title = 'Diloranosaurus Stats',
                colour = 0xD3D3D3
        )

        embed.set_footer(text = 'DinoDex')
        embed.set_thumbnail(url = "https://metahub.info/wp-content/uploads/2018/07/Diloranosaurus.png")
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Diloranosaurus/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 25% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Impact (1.5x dmg, -50% dmg) \
            \nGreater Stunning Rampage (2x dmg, -75% Stun) \
            \nImpact and Run (1.5 dmg, Auto Swap) \
            \nSuperiority Strike (1x dmg, Cleanse Self, -33% Speed)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'None', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/monomius/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 129 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Distracting Impact (1.5x dmg, -50% dmg) \
            \nEvasive Stance (Priority, +50% Dodge) \
            \nNullifying Impact (1.5x dmg, Remove + Effects) \
            \nNullifying Strike (1x dmg, Remove + Effects)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Monolophosaurus  (LV15, n/a DNA) + Gallimimus (LV15, n/a DNA) = Monomimus', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/Tuoramoloch/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 0% \n__Speed:__ 126 \n__Critical:__ 5%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Greater Stunning Rampage (2x dmg, 75% Stun) \
            \nImpact and Run (1.5x dmg, Auto Swap) \
            \nLow Stunning Strike (1x dmg, 20% Stun) \
            \nSlowing Impact (1.5 dmg, -50% Speed)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Tuojiangosaurus (LV20, n/a DNA) +  Paramoloch (LV20, n/a DNA) = Tuoramoloch', inline = 'false')

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
        embed.set_author(name = "More information here", url="https://metahub.info/jwa-dinosaur/sarcorxis/")

        embed.add_field(name = 'Stats', value = '__Armor:__ 15% \n__Speed:__ 115 \n__Critical:__ 20%', inline = 'False')
        embed.add_field(name = 'Moveset', value = \
            'Armor Piercing Strike (1x dmg, bypass Armor) \
            \nFerocius Strike (1x dmg, +50% dmg) \
            \nGreater Stunning Impact (1.5x dmg, 75% Stun) \
            \nLockdown Impact (1.5 dmg, Cannot Swap)', \
            inline = 'False')
        embed.add_field(name = 'Passive Effects', value = 'None', inline = 'false')
        embed.add_field(name = 'Hybrid Information', value = 'Sarcosuchus (LV15, 200 DNA) + Einiasuchus (LV15, 50 DNA) = Sarcorixis', inline = 'false')

        await client.say(embed = embed)

#---------------------------------------------------------------------END PROJECT DINODEX----------------------------------------------------------------------------------------------------------#

client.run(TOKEN)
