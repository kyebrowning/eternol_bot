import settings
from dotenv import load_dotenv
import discord
from discord.ext import commands
import csv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
bot = discord.Bot(intents=intents)


def get_unit_commands():
    with open('csv/Units.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = (
                f"@bot.slash_command(description='{row['Name']} Unit Stats')\n"
                f"async def {row['Name'].replace(' ','_').lower()}(ctx: discord.ApplicationCommand):\n"
                f"\tembed = discord.Embed(color = discord.Color.teal(), title ='{row['Name']}')\n"
                f"\tembed.add_field(name='Cost', value='{row['Points']}', inline=True)\n"
                f"\tembed.add_field(name='Movement', value='{row['Movement']}', inline=True)\n"
                f"\tembed.add_field(name='Combat', value='{row['Combat']}+', inline=True)\n"
                f"\tembed.add_field(name='Defense', value='{row['Defense']}+', inline=True)\n"
                f"\tembed.add_field(name='Defense', value='{row['Defense']}+', inline=True)\n"
                f"\tembed.add_field(name='Morale', value='{row['Morale']}', inline=True)\n"
                f"\tembed.add_field(name='Range', value='{row['Range']}', inline=True)\n"
                f"\tawait ctx.respond(embed=embed)\n"
            )
            exec(code)

def get_keyword_commands():
    with open('csv/Keywords.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            code = (
                f"@bot.slash_command(description='{row['name']} Keyword Definition')\n"
                f"async def {row['name'].replace(' ','_').lower()}(ctx: discord.ApplicationCommand):\n"
                f"\tembed = discord.Embed(color = discord.Color.fuchsia(), title ='{row['name']}')\n"
                f"\tembed.add_field(name='Unit Cost', value='{row['unit_cost']}', inline=True)\n"
                f"\tembed.add_field(name='Army Cost', value='{row['army_cost']}', inline=True)\n"
                f"\tembed.add_field(name='Definition', value='{row['description']}', inline=False)\n"
                f"\tembed.add_field(name='Can Be Taken Twice?', value='{'Yes' if row['can_be_taken_twice'] else 'No' } ', inline=True)\n"
                f"\tembed.add_field(name='Keyword Type', value='{'Keyword' if row['keyword_type'] == 'keyword' else 'Spell or Ability'}', inline=True)\n"
                f"\tawait ctx.respond(embed=embed)\n"
            )
            exec(code)

@bot.listen()
async def on_member_join(member):
    vibe = bot.get_channel(1059274766185406604)
    rules = bot.get_channel(1059274190466854955)
    wip = bot.get_channel(1059275434132504616)
    feedback = bot.get_channel(1059274082010533888)
    # guild = member.guild
    # role_id = 1240118977993379891
    # creators = guild.get_role()
    message = f"""Welcome to the **ETERNØL: 15mm sci-fi warfare across the Void Horizon** server!

We're excited to have you part of the ETERNØL: 15mm community with all our half-scale shenanigans. Make sure to post your best meme or gif to pass the {vibe.mention}.
    
To get yourself started with your ETERNØL army make sure to check out {rules.mention}. Post your WIPs and other projects in {wip.mention} as you are building your army and if you have any feedback about the game please let us know in {feedback.mention}.
    
Again, we're glad you're here, and let any of us know if you have any questions, comments, or concerns. Thanks and happy gaming! 🤘"""
    await member.send(message)


get_unit_commands()
get_keyword_commands()

bot.run(settings.DISCORD_TOKEN)
