import discord
from discord.ext import commands
from discord_bot.config import *

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} is loggen in.')


@bot.command()
async def map(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество карт')
        return
    result_ = (map_ * num)
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def map_all(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество карт')
        return
    result_ = map_all_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def bluep(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество чертежей')
        return
    result_ = blueprints_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def bluep_all(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество чертежей')
        return
    result_ = blueprints_all_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def raven(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество: зубов ворона, пыльцы фей, резного рога')
        return
    result_ = raven_task_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def raven_all(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество: зубов ворона, пыльцы фей, резного рога')
        return
    result_ = (raven_task_ + treant_seed_) * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def seed(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество семечек')
        return
    result_ = treant_seed_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def demon(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество когдей демона')
        return
    result_ = demon_claw_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def monolit(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество монолитов')
        return
    result_ = monolit_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def seal(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество печатей')
        return
    result_ = seal_of_doom_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def flat(ctx, num):
    try:
        num = int(num)
    except:
        await ctx.send('Ошибка, введите колличество флатронов')
        return
    result_ = flatron_ * num
    result = '{:,}'.format(result_).replace(',', ' ')
    await ctx.send(str(result))


@bot.command()
async def ps(ctx, boss, num, men):
    try:
        num = int(num)
        men = int(men)
    except:
        await ctx.send('Ошибка, введите нужное значение')
        return
    if boss == 'seed' and men > 1:
        points = treant_seed_ * num
        result1 = int((points * 0.6) / men)
        result2 = int((points * 0.4) + result1)
        result1 = '{:,}'.format(result1).replace(',', ' ')
        result2 = '{:,}'.format(result2).replace(',', ' ')
        await ctx.send(f'{men - 1} игрок(а) получат: {result1}, кто призвал и пробил: {result2}')
    if boss == 'raven' and men > 1:
        points = raven_task_ * num
        result1 = int((points * 0.6) / men)
        result2 = int((points * 0.4) + result1)
        result1 = '{:,}'.format(result1).replace(',', ' ')
        result2 = '{:,}'.format(result2).replace(',', ' ')
        await ctx.send(f'{men - 1} игрок(а) получат: {result1}, кто призвал и пробил: {result2}')
    if boss == 'seal' and men > 1:
        points = seal_of_doom_ * num
        result1 = int((points * 0.6) / men)
        result2 = int((points * 0.4) + result1)
        result1 = '{:,}'.format(result1).replace(',', ' ')
        result2 = '{:,}'.format(result2).replace(',', ' ')
        await ctx.send(f'{men - 1} игрок(а) получат: {result1}, кто призвал и пробил: {result2}')
    if boss == 'monolit' and men > 1:
        points = monolit_ * num
        result1 = int((points * 0.6) / men)
        result2 = int((points * 0.4) + result1)
        result1 = '{:,}'.format(result1).replace(',', ' ')
        result2 = '{:,}'.format(result2).replace(',', ' ')
        await ctx.send(f'{men - 1} игрок(а) получат: {result1}, кто призвал и пробил: {result2}')


@bot.command()
async def helps(ctx):
    for i in commands_bot_:
        await ctx.send(i)


# @bot.command()
# async def help_(ctx):
#     await ctx.send('n - это число выших боссов')
#     await ctx.send('m - это число участников')
#     await ctx.send('Полный список команд:')
#     await ctx.send('!help - вывод всех доступных команд')

bot.run(TOKEN)
