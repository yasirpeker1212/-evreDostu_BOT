import discord,random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='.', intents=intents)

tavsiyeler = [
    "Tasaruflu olmaya çalış, yani ayağını yorganına göre uzat.",
    "Buzdolabına koyulacakları buzdolabına koy, dışarıya koyulacakları dışarıya koy.",
    "Geri dönüşümü unutma. ",
    "Dengeli beslen ve yiyebileceğin kadar al önüne.",
    "Aileniz, arkadaşlarınız ve çevrenizdekilerde geri dönüşüm konusunda farkındalık yaratın",
    "onları bilinçlendirin.",
    "Sürdürülebilir ve geri dönüşüme uygun ürünler tercih edin. Ambalajsız ürünler ya da geri dönüşüm sembollü ürünleri seçmeye özen gösterin."
    ,"Yaşam alanınızdaki atıkları kağıt, plastik, cam ve metal olarak ayrı ayrı kaplarda toplayın."
    ,"Plastik atıklarını azaltmak için alışveriş yaparken plastik torbalar yerine bez çantalar, kese kağıdı ya da kanvas çantalar kullanın.",
    "Organik atıklarınızı yeniden doğaya dönüştürmek için bahçenizde ya da bitki yetiştirdiğiniz alanda kullanın.",
    "Kullanılmış pilleri normal çöplere değil, özel olarak belirlenmiş atık kutularına atın. Böylece içerisinde bulunan zararlı maddelerin doğaya daha az zarar vermesini sağlayabilirsiniz.","Sıkça kullandığınız karton kutular"
    , "plastik şişeler tekrar kullanabilir malzemeler olduğu için bunları geri dönüşüm kutularına atın."
]
atiklar = {
    "şişe" : "plastik",
    "peçete" : "kağıt",
    "gazete":"kağıt",
    "metal" : "metal",
    "karton" : "kağıt"
}
@bot.event

async def on_ready():

    print(f'{bot.user} olarak giriş yaptık')

 

@bot.command()

async def hello(ctx):

    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')


@bot.command()

async def tavsiye_ver(ctx):
    await ctx.send("Sana Bir tavsiye : " + random.choice(tavsiyeler))

@bot.command()

async def atik_at(ctx,atik):
    await ctx.send("Bunu " + atiklar[atik] + " kısmına at.")

@bot.command()

async def yardim(ctx):
    await ctx.send("Kullanabileceğin Komutlar : tavsiye_ver , atik_at")
 
bot.run("BOT_TOKEN HERE")
