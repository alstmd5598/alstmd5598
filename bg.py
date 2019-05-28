
import Image
import discord
import BgWin
import openpyxl
import random
import Time

client = discord.Client()

up = '👍'
down = '👎'


@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.id)
    print("===========")
    game = discord.Game("패치중")
    await client.change_presence(status=discord.Status.dnd, activity=game) #online


@client.event
async def on_message(message):
    if message.content.startswith("/질문"):
        answer = ["네 맞아요", "절대 아니에요", "잘 모르겠어요", "그런거 같네요", "아닌거 같은데..", "음.. 노코멘트 할게요", "확실해요!"]
        a = random.choice(answer)
        embed = discord.Embed(title=message.author.name + "의 질문에 대한 대답", description=a)
        await message.channel.send(embed=embed)

    if message.content.startswith("안녕"):
        embed = discord.Embed(title=None, description="ㅂㅇㄹ", color=0x00ff56)
        await message.channel.send(embed=embed)

    if message.content.startswith("프렌즈"):
        embed = discord.Embed(title=None, description="네", color=0x00ff56)
        await message.channel.send(embed=embed)


    if message.content.startswith('서버정보'):
        embed = discord.Embed(title="\"%s\" 서버정보!" % (message.guild.name), description=None, color=0x00ff56)
        embed.add_field(name="서버 소유자", value="<@%s>" % message.guild.owner.id, inline=False)
        embed.add_field(name="서버 생성일", value="%s (UTC)" % (message.guild.created_at), inline=False)
        embed.add_field(name="서버 보안등급", value=message.guild.verification_level, inline=False)
        embed.add_field(name="서버 위치", value=message.guild.region, inline=False)
        embed.add_field(name="서버 잠수채널", value="%s (%s분 이상 잠수이면 이동됨)" % (message.guild.afk_channel, message.guild.afk_timeout/60), inline=False)
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.set_footer(text = "Server ID : %s" % (message.guild.id))
        await message.channel.send(embed=embed)

    if message.content.startswith('모든권한'):
         learn = message.content.replace("모든권한 ", "https://discordapp.com/oauth2/authorize?client_id=")
         await message.channel.send(learn+"&scope=bot&permissions=2146958847")

    if message.content.startswith("/123"):
            await message.channel.send(file=discord.File("Superhero.mp3")) #mp3 말고 확장명입력

    if message.content.startswith('/러시안룰렛'):
        def check(msg):
            return msg.channel == message.channel and msg.content == "빵"

        shoot = random.randint(0, 5)
        await message.channel.send('끼릭..끼릭. 총알이 장전되었습니다. 방아쇠를 당겨주세요 -> "빵"')
        for i in range(0, 6):
            try:
                msg = await client.wait_for("message", check=check, timeout=15.0)
            except:
                await message.channel.send('15초내로 방아쇠를 당겨주세요')
                return

            if i == shoot:
                await msg.channel.send("BANG!")
                break
            else:
                await msg.channel.send("SAFE..")

    if message.content.startswith('/사진'):
        a = random.randint(0, 9)
        google = message.content.split(" ")
        if len(google) == 3:
            google[1] = google[1] + "+" + google[2]
        if len(google) == 4:
            google[1] = google[1] + "+" + google[2] + "+" + google[3]
        image = Image.get_image(google[1], a)
        embed = discord.Embed(title=image[1], color=0xffffff)
        embed.set_image(url=image[0])
        await message.channel.send(embed=embed)

    if message.content.startswith('/움짤'):
        a = random.randint(1, 5)
        await message.channel.send(file=discord.File("움짤/" + str(a) + ".gif"))

    if message.content.startswith("/프로필"):
        date = Time.ctime(str(message.author.id))
        embed = discord.Embed(color=0x00fffff)
        embed.add_field(name="이름", value=message.author.name)
        embed.add_field(name="닉네임", value=message.author.display_name)
        embed.add_field(name="아이디", value=str(message.author.id))
        embed.add_field(name="계정생성일", value=date)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("/배그도움말"):
        des1 = ("1. 전적확인 : `/솔로or듀오or스쿼드` `아이디` "
                "\n2.(`솔로or듀오or스쿼드`) 아이디  전적확인)\n\u200b")

        embed = discord.Embed(color=0x26b4df)
        embed.add_field(name="명령어", value=des1)
        await message.channel.send(embed=embed)

    if message.content.startswith("/아이디"):
        id = message.content.split(" ")
        if len(id) == 2:
            file = openpyxl.load_workbook('아이디.xlsx')
            sheet = file.active
            i = 1
            while True:
                if sheet["A" + str(i)].value == str(message.author.id):
                    sheet["A" + str(i)].value = str(message.author.id)
                    sheet["B" + str(i)].value = id[1]
                    await message.channel.send
                    await message.channel.send("아이디를 변경했습니다.")
                    break

                if sheet["A" + str(i)].value == None:
                    sheet["A" + str(i)].value = str(message.author.id)
                    sheet["B" + str(i)].value = id[1]
                    await message.channel.send
                    await message.channel.send("아이디를 등록했습니다.")
                    break
                i += 1

            file.save('아이디.xlsx')

        else:
            await message.channel.send("양식에 맞추어 다시 입력해주세요.")

    if message.content.startswith("/배그") and not message.content.startswith("/배그도움말"):
        name = message.content.split(" ")
        a = ""
        if len(name) == 2:
            file = openpyxl.load_workbook('아이디.xlsx')
            sheet = file.active
            a = 0
            i = 1
            while a == 0:
                if sheet["A" + str(i)].value == str(message.author.id):
                    try:
                        if name[1] == "솔로":
                            a = BgWin.get_solo(sheet["B" + str(i)].value)
                        elif name[1] == "듀오":
                            a = BgWin.get_duo(sheet["B" + str(i)].value)
                        elif name[1] == "스쿼드":
                            a = BgWin.get_squad(sheet["B" + str(i)].value)
                    except:
                        a = "전적 기록 없음"

                    embed = discord.Embed(color=0x00ffff)
                    embed.add_field(name="등급", value=a[0])
                    embed.add_field(name="랭킹", value=a[1])
                    embed.add_field(name="게임시간/승패", value=a[2])
                    embed.add_field(name="K/D", value=a[3])
                    embed.add_field(name="승률", value=a[4])
                    embed.add_field(name="탑10", value=a[5])
                    embed.add_field(name="평균딜량", value=a[6])

                    await message.channel.send(embed=embed)
                    a = 1

                if sheet["A" + str(i)].value == None:
                    a = 1
                    await message.channel.send("등록된 아이디가 없습니다.")
                i += 1

        elif len(name) == 3:
            try:
                if name[2] == "솔로":
                    a = BgWin.get_solo(name[1])
                elif name[2] == "듀오":
                    a = BgWin.get_duo(name[1])
                elif name[2] == "스쿼드":
                    a = BgWin.get_squad(name[1])
            except:
                a = "전적 기록 없음"

            embed = discord.Embed(color=0x00ffff)
            embed.add_field(name="등급", value=a[0])
            embed.add_field(name="랭킹", value=a[1])
            embed.add_field(name="게임시간/승패", value=a[2])
            embed.add_field(name="K/D", value=a[3])
            embed.add_field(name="승률", value=a[4])
            embed.add_field(name="탑10", value=a[5])
            embed.add_field(name="평균딜량", value=a[6])

            await message.channel.send(embed=embed)
        else:
            await message.channel.send("양식에 맞추어 다시 입력해주세요")


client.run('NTgyNTAwNDM3MDA1OTU5MjAw.XOzu7Q.be6pfrWsQbnfSk646rAKMcujkbg')
