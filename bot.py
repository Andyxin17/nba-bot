import discord
import os
import random
import asyncio
from datetime import datetime, timedelta
import pytz

BOT_TOKEN = os.environ['BOT_TOKEN']
CHANNEL_ID = 1336640158640111732
VIP_CHANNEL_ID = [1351454113212141588, 1351453716326125629]
CHEF_USER_ID = 323775706800717825
REQUIRED_USERS = random.randint(1,50)
EMOJI_TO_TRACK = "🦞"
unique_users = set()
nba_players = [
    {"name": "LeBron James", "img": "https://img.olympics.com/images/image/private/t_s_pog_staticContent_hero_xl_2x/f_auto/primary/c5r52rbifxn2srhp9no0"},
    {"name": "Luka Doncic", "img": "https://www.proballers.com/media/cache/resize_600_png/https---www.proballers.com/ul/player/luka-doncic-grande-1f086920-1793-6810-8b1b-270f1230ff14.png"},
    {"name": "Austin Reaves", "img": "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/4066457.png&w=350&h=254"},
    {"name": "Jayson Tatum", "img": "https://s3media.247sports.com/Uploads/Assets/601/513/9513601.jpg"},
    {"name": "Derrick White", "img": "https://www.usab.com/imgproxy/D10eTCvrslHTmLzboEspIEZTE-1-8SOE87s0Bw9IjQg/rs:fit:3000:0:0/g:ce/q:90/aHR0cHM6Ly9zdG9yYWdlLmdvb2dsZWFwaXMuY29tL3VzYWItY29tLXByb2QvdXBsb2FkLzIwMjQvMDcvMTUvOTJhOTA5MzYtNTRmMS00MDBiLTgxYjItYWQxOGFmYTYxNzg2LnBuZw.png"},
    {"name": "LaMelo Ball", "img": "https://pbs.twimg.com/media/DX9nEf8UMAEz-TH.jpg"},
    {"name": "Collin Sexton", "img": "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/4277811.png"},
    {"name": "Josh Giddey", "img": "https://images2.minutemediacdn.com/image/upload/c_fill,w_1200,ar_1:1,f_auto,q_auto,g_auto/images/GettyImages/mmsport/307/01k1xaeta5sbc5afq3f1.jpg"},
    {"name": "Kobe Bryant", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOhtKJnT9XWHogugFJTdO1Fs0mj5oPMlGHfg&s"},
    {"name": "Donovan Mitchell", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUoCDTEaARVe7b_fTq76Yw0TaxHMq46VSgyg&s"},
    {"name": "Anthony Davis", "img": "https://i.redd.it/yuh3lqrtu3y71.jpg"},
    {"name": "Nikola Jokic", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMvVwSLaJ9EoeyGZjzvv974ZKN_-JX8LaejQ&s"},
    {"name": "Stephen Curry", "img": "https://a.espncdn.com/i/headshots/nba/players/full/3975.png"},
    {"name": "Kevin Durant", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrGYRt4C49AR6zQIyt9cb0aQyjThXIc5mYUA&s"},
    {"name": "Tyrese Haliburton", "img": "https://www.aljazeera.com/wp-content/uploads/2025/05/AP25142109739878-1747901928.jpg?resize=770%2C513&quality=80"},
    {"name": "James Harden", "img": "https://imageio.forbes.com/specials-images/imageserve/663e7576d6a28bd3726ed1a0/0x0.jpg?format=jpg&crop=1314,1316,x286,y186,safe&height=416&width=416&fit=bounds"},
    {"name": "Giannis Antetokounmpo", "img": "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/3032977.png&w=350&h=254"},
    {"name": "Anthony Edwards", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2CKI6D4sLx_Xawc71gwHa9De5KONgvF78Lg&s"},
    {"name": "Karl Anthony Towns", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-MO3MKdTZLQCBRZGd0ftLD9479sZYpFft9Q&s"},
    {"name": "VJ Edgecum", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJAK6CDnS-ybX86w1ZZ4hA_C9IoLXRy2lJRw&s"},
]

funny_players = [
    {"name": "Quandale Dingle", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh_NTURChQ3igWVOh07Km4_h11EUF79_sQxg&s"},
    {"name": "Chopped Chin", "img": "https://i.ytimg.com/vi/vx0LZ_oQlo4/hq720.jpg"},
    {"name": "Gilbert", "img": "https://i.imgflip.com/3m8m2y.png?a489696"},
    {"name": "Diddy", "img": "https://m.media-amazon.com/images/M/MV5BNTE1ODU3NTM1N15BMl5BanBnXkFtZTcwNTk0NDM4Nw@@._V1_.jpg"}
]

ban_players = [
    {"name": "Epstein", "img": "https://media-cldnry.s-nbcnews.com/image/upload/t_focal-760x428,f_auto,q_auto:best/mpx/2704722219/2025_11/1763165491785_nn_ggu_trump_orders_doj_probe_of_epstein_links_to_democrats_251114_1920x1080-1vly6g.jpg"}
]

goat_players = [
    {"name": "Michael Jordan", "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReBF3BTjh5dejJs2va03vsrUY_7ppMi1_O6Q&s"}
]
daily_nba_users = {}
ny_tz = pytz.timezone("America/New_York")

class Client(discord.Client):

    async def setup_hook(self):
        # Run once async setup is ready
        self.bg_nba_task = asyncio.create_task(self.nba_game())
        self.bg_status_task = asyncio.create_task(self.periodic_status())
        self.bg_chef_task = asyncio.create_task(self.hourly_chef_message())
        self.vip_watching = False
        self.last_reset_day = datetime.now(ny_tz).date()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            current_count = len(unique_users)
            remaining = REQUIRED_USERS - current_count
            await channel.send(
                f"@everyone WE NEED {REQUIRED_USERS} {EMOJI_TO_TRACK} TODAY FROM GENERAL TO UNLOCK THE FREE PICK OF THE DAY!\n"
                f"Currently we are at {current_count}, so we need {remaining} more!! (This resets every new day so BUILD HYPE NOW and check in everyday for new free pick opportunities!)"
            )
    async def send_daily_nba_game(self, message):
        today = datetime.now(ny_tz).date()
        user_id = message.author.id

        if daily_nba_users.get(user_id) == today:
            await message.channel.send(f"{message.author.mention}, come back tomorrow to see what you remind me of again!")
            return

    # Weighted group choice
        group_choice = random.choices(
            ["nba", "funny", "ban", "goat"],
            weights=[54, 34, 10, 2],
            k=1
        )[0]

        if group_choice == "nba":
            player = random.choice(nba_players)
            msg = f"{message.author.mention}, you remind me of {player['name']}!"
        elif group_choice == "funny":
            player = random.choice(funny_players)
            msg = f"{message.author.mention}, you remind me of {player['name']}!"
        elif group_choice == "ban":
            player = random.choice(ban_players)
            msg = f"{message.author.mention}, you remind me of {player['name']}! @everyone Avoid this guy, he gives Epstein vibes"
        elif group_choice == "goat":
            player = random.choice(goat_players)
            msg = f"{message.author.mention}, YOU ARE THE GOAT, DM <@{CHEF_USER_ID}> for FREE VIP 1-DAY PASS ({player['name']})"

    # Send the text message
        await message.channel.send(msg)

    # Send image only
        await message.channel.send(player['img'])

        daily_nba_users[user_id] = today

    # Mark as sent today
        daily_nba_users[user_id] = today
    async def nba_game(self):
        await self.wait_until_ready()
        while not self.is_closed():
            channel = self.get_channel(CHANNEL_ID)
            if channel:
                # Random member
                today = datetime.now(ny_tz).date()
                eligible_members = [m for m in channel.guild.members if not m.bot and daily_nba_users.get(m.id) != today]
                
                if eligible_members:
                    member = random.choice(eligible_members)

                    # Weighted group choice
                    group_choice = random.choices(
                        ["nba", "funny", "ban", "goat"],
                        weights=[54, 34, 10, 2],
                        k=1
                    )[0]


                    if group_choice == "nba":
                        player = random.choice(nba_players)
                        msg = f"{member.mention}, you remind me of {player['name']}!"
                    elif group_choice == "funny":
                        player = random.choice(funny_players)
                        msg = f"{member.mention}, you remind me of {player['name']}!"
                    elif group_choice == "ban":
                        player = random.choice(ban_players)
                        msg = f"{member.mention}, you remind me of {player['name']}! @everyone This guy gives Epstein vibes"
                    elif group_choice == "goat":
                        player = random.choice(goat_players)
                        msg = f"{member.mention}, YOU ARE THE GOAT, DM <@{CHEF_USER_ID}> for FREE VIP 1-DAY PASS ({player['name']})"

                # Send the text message with mention
                    await channel.send(msg)



                    # Send embed with image
                    embed = discord.Embed(color=discord.Color.blue())
                    embed.set_image(url=player['img'])
                    await channel.send(embed=embed)
                    daily_nba_users[member.id] = today
            await asyncio.sleep(300)  # every 1 hour

    async def on_message(self, message):
        global unique_users
        if message.author == self.user:
            return
        if "gay" in message.content.lower() and message.mentions:
            for mentioned in message.mentions:
                number = random.randint(1,10)
                if random.random() < 0.3:
                    penis_str = "(())"
                else:
                    penis_length = random.randint(0,20)
                    penis_str = f"8{'=' * penis_length}>"
                try:
                    await message.channel.send(
                        f"<@{mentioned.id}>'s gayness right now is {number} "
                    )
                    await message.channel.send(f"Also {mentioned.mention}'s current penis size: {penis_str}")
                except Exception as e:
                    print(f"Failed to send message: {e}")
        if 'play' in message.content.lower():
            await self.send_daily_nba_game(message)

        today = datetime.now(ny_tz).date()

        # ---------------- VIP PICK POST ----------------
        if self.vip_watching and message.channel.id in VIP_CHANNEL_ID:
            if message.created_at.astimezone(ny_tz).date() == today:
                main_channel = self.get_channel(CHANNEL_ID)
                if main_channel:
                    await main_channel.send(f"@everyone 🦞🦞🦞 LET'S GOOO EVERYONE, I'VE JUST LEAKED A VIP PICK! :\n{message.content}")
                self.vip_watching = False

        # ---------------- LOBSTER TRACKING ----------------
        if EMOJI_TO_TRACK in message.content:
            unique_users.add(message.author.id)
            await self.send_lobster_status(message.channel)

        # Respond to /freepick command
        if message.content.lower() == "leak":
            await self.send_lobster_status(message.channel)

        # ---------------- BOT MENTION ----------------
        if self.user in message.mentions:
            msg_clean = message.content
            for mention in message.mentions:
                msg_clean = msg_clean.replace(f"<@!{mention.id}>", "").replace(f"<@{mention.id}>", "")
            msg_clean = msg_clean.lower().strip()

            if "hello" in msg_clean or "hi" in msg_clean:
                await message.channel.send(f'Hi there {message.author.mention}!')
            elif "tell me a joke" in msg_clean or "joke" in msg_clean:
                jokes = [
                    "Why did the scarecrow win an award? Because he was outstanding in his field!",
                    "Why don’t scientists trust atoms? Because they make up everything!",
                    "Why did the math book look sad? Because it had too many problems!"
                ]
                await message.channel.send(random.choice(jokes))
            else:
                await message.channel.send("I'm not sure how to respond to that! Try saying 'hello' or 'tell me a joke'.")

    # ---------------- MEMBER LEAVE SHAME ----------------
    async def on_member_remove(self, member):
        img_urls = [
            "https://as1.ftcdn.net/v2/jpg/05/53/56/74/1000_F_553567440_n6tnKQ5khel2X2OiDXWFPDIrHYpW8cVQ.jpg",
            "https://as2.ftcdn.net/v2/jpg/16/24/77/17/1000_F_1624771704_7BjnSZy8k0ueFOVSjOZvABmOQ05PsyUq.jpg",
            "https://www.shutterstock.com/shutterstock/videos/4644425/thumb/1.jpg?ip=x480",
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-JUXhEbwhHR5YVMxS77aG2Tob83wzVG5Obw&s",
            "https://c8.alamy.com/comp/2C4HR5J/traditional-african-hut-in-himba-tribe-village-namibia-2C4HR5J.jpg",
        ]
        img_url = random.choice(img_urls)
        channel = self.get_channel(CHANNEL_ID)
        if channel:
            try:
                await channel.send(f"@everyone {member.name} left. SHAME on this nibberino for leaving. 😤")
                caption = f"Just Doxxed that nibber-dibber for leaving this is what **{member.name}**'s house looks like."
                embed = discord.Embed(title="Shame!", description=caption, color=discord.Color.red())
                embed.set_image(url=img_url)
                await channel.send(embed=embed)
            except Exception as e:
                print(f"Failed to send leave message: {e}")

    # ---------------- LOBSTER STATUS ----------------
    async def send_lobster_status(self, channel):
        global unique_users
        current_count = len(unique_users)
        remaining = max(REQUIRED_USERS - current_count, 0)

        # Reset daily at New York midnight
        today = datetime.now(ny_tz).date()
        if today != getattr(self, "last_reset_day", today):
            unique_users.clear()
            self.last_reset_day = today
            self.vip_watching = False

        if current_count >= REQUIRED_USERS:
            # Check all VIP channels for today's pick
            vip_pick_message = None
            for vip_id in VIP_CHANNEL_ID:
                vip_channel = self.get_channel(vip_id)
                if vip_channel:
                    async for msg in vip_channel.history(limit=50):
                        if msg.created_at.astimezone(ny_tz).date() == today:
                            vip_pick_message = msg
                            break
                if vip_pick_message:
                    break

            if vip_pick_message:
                await channel.send(f"@everyone 🦞🦞🦞 LET'S GOOO EVERYONE, HERE'S THE VIP LEAK! (DON'T TELL CHEF!):\n{vip_pick_message.content}")
                self.vip_watching = False
            else:
                await channel.send("🦞🦞🦞 LET'S GOOO EVERYONE, IMMA LEAK a VIP pick as SOON as it's posted!")
                if not self.vip_watching:
                    self.vip_watching = True  # start watching VIP channels immediately

            unique_users.clear()
        else:
            await channel.send(
                f"WE NEED {REQUIRED_USERS} {EMOJI_TO_TRACK} FROM GENERAL AND I'LL FUCKING LEAK A PICK FROM VIP!(Don't tell chef!)\n"
                f"Currently we are at {current_count}, so we need {remaining} more!! (say 'leak' for update) (This resets every day!)"
            )

    # ---------------- VIP PICK WATCHER ----------------
    async def watch_vip_pick(self):
        """Check every hour for today's VIP pick if not yet posted."""
        await self.wait_until_ready()
        while self.vip_watching and not self.is_closed():
            today = datetime.now(ny_tz).date()
            vip_pick_message = None
            for vip_id in VIP_CHANNEL_ID:
                vip_channel = self.get_channel(vip_id)
                if vip_channel:
                    async for msg in vip_channel.history(limit=50):
                        if msg.created_at.astimezone(ny_tz).date() == today:
                            vip_pick_message = msg
                            break
                if vip_pick_message:
                    break

            if vip_pick_message:
                main_channel = self.get_channel(CHANNEL_ID)
                if main_channel:
                    await main_channel.send(f"@everyone 🦞🦞🦞 LET'S GOOO EVERYONE, I'VE JUST LEAKED A PICK FROM VIP! :\n{vip_pick_message.content}")
                self.vip_watching = False

            await asyncio.sleep(600)  # check every hour

    # ---------------- CHEF HOURLY MESSAGES ----------------
    async def hourly_chef_message(self):
        await self.wait_until_ready()
        while not self.is_closed():
            await asyncio.sleep(86400)
            channel = self.get_channel(CHANNEL_ID)
            if channel:
                number = random.randint(1, 10)
                if random.random() < 0.3:
                    penis_str = "(())"
                else:
                    penis_length = random.randint(0, 20)
                    penis_str = f"8{'=' * penis_length}>"
                try:
                    await channel.send(f"Chef Hourly gayness update: <@{CHEF_USER_ID}>'s gayness right now is {number}")
                    await channel.send(f"Also Chef's current penis size: {penis_str}")
                except Exception as e:
                    print(f"Failed to send message: {e}")

    # ---------------- PERIODIC STATUS REMINDER ----------------
    async def periodic_status(self):
        """Send team effort status every 3 hours if requirement not met."""
        await self.wait_until_ready()
        while not self.is_closed():
            await asyncio.sleep(3 * 3600)  # 3 hours
            channel = self.get_channel(CHANNEL_ID)
            if channel and len(unique_users) < REQUIRED_USERS:
                await self.send_lobster_status(channel)


# ---------------- RUN BOT ----------------
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = Client(intents=intents)
client.run(BOT_TOKEN)





