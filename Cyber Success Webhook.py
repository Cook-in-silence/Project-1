from discord import Webhook, RequestsWebhookAdapter, Embed, Color

def avatar_url():
    return ("")

def send_webhook():
    url = ''
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

    embed = Embed(title="Successfully checked out!",description="Motion Logo Hoooded Sweatshirt",color=Color.from_rgb(115,238,139))

    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/MNiC4Jvcq9o5BhxgN_L_JdOnboIqws53gsxuI2R3YVA/https/assets.supremenewyork.com/185653/rs/KgnOaMro5QE.jpg?width=80&height=80")

    embed.add_field(name="Store", value="Supreme EU")

    embed.add_field(name="Size", value="Medium")

    embed.add_field(name="Profile", value="||Cook in silence#8712||")

    embed.add_field(name="Order", value="||13456||")

    embed.add_field(name="Proxy list", value="||bash||")

    embed.add_field(name="Category", value="Sweatshirts")

    embed.add_field(name="blank", value='\u200b')

    embed.add_field(name="Quantity", value="1")

    embed.add_field(name="3D Secure", value="Enable")

    embed.add_field(name="mode", value="Fast").set_footer(text="CyberAIO·14/04/2020 10:50:50.263",icon_url="https://cdn.discordapp.com/avatars/681870741087584267/5d433280a842a4b5efb8b2e2d63b26cd.webp?size=128")

    webhook.send(embed=embed,avatar_url=avatar_url(),username="CyberAIO")

send_webhook()