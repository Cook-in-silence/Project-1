from discord import Webhook, RequestsWebhookAdapter, Embed, Color

def avatar_url():
    return ("")

def send_webhook(content):
    url = ("")
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

    embed = Embed(title="You cooked",color=Color.from_rgb(161,90,182))

    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/fhOQCdD2Y0MsocSBk5eEI4nLXmb_pcemyIB838kBGuo/https/images.footlocker.com/pi/55088500/cart/55088500.jpeg")

    embed.add_field(name="Website",value="Footlocker")

    embed.add_field(name="Product", value="Jordan Retro 1 High OG - Men's")

    embed.add_field(name="Size", value="||9.5||")

    embed.add_field(name="Price", value="$170.00")

    embed.add_field(name="Link",value="55088500")

    embed.add_field(name="Profile",value="||Cook in silence||")

    embed.add_field(name="Proxy",value="||bash||")

    embed.add_field(name="Time stamp(utc)",value="2020-04-11 15:08:28PM")

    webhook.send(content,embed=embed, avatar_url=avatar_url(), username="TKS")

send_webhook("Success:Jordan Retro 1 High OG - Men's")