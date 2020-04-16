from discord import Webhook, RequestsWebhookAdapter, Embed, Color

def avatar_url():
    return ("")

def send_webhook():
    url = ("")
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

    embed = Embed(title="UNDEFEATED Checkout",url="http://baidu.com",color=Color.from_rgb(115,238,139))

    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/csqhvlOs6r2HxJ70dwPMg9Xn_5ZSn9wWRt9PUDNOwKE/%3Fv%3D1585072279/https/cdn.shopify.com/s/files/1/0094/2252/products/CINDER_YZY_1.jpg?width=80&height=80")

    embed.add_field(name="Product", value="YEEZY BOOST 350 V2 - BLACK --/ 8")

    embed.add_field(name="Size",value="8")

    embed.add_field(name="Billing Profile",value="Cook in silence")

    embed.add_field(name="Checkout Time",value="17.73s")

    embed.add_field(name="Monitor Delay",value="8000ms")

    embed.add_field(name="Retry Delay", value="9000ms")

    embed.add_field(name="Mode", value="Autocheckout")

    embed.add_field(name="Opinion", value="Pre generated checkout").set_footer(text="Sole AIO Shopify Mode",icon_url="https://media.discordapp.net/attachments/698457195729125447/699465230060879973/image0.jpg?width=300&height=300")

    webhook.send(embed=embed, avatar_url=avatar_url(), username="Sole AIO")

send_webhook()