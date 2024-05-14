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

get_unit_commands()
get_keyword_commands()

bot.run(settings.DISCORD_TOKEN)
