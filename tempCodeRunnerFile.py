price_without_currency = price.split("$")[1]

# # Convert to floating point number
# price_as_float = float(price_without_currency)
# print(price_as_float)

# if price_as_float < 100:
#     connection = smtplib.SMTP("smtp.gmail.com")
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(from_addr=email, to_addrs= email, msg=f"Subject:Amazon price alert\n\nPot cooker now goes for ${price_as_float}")
#     connection.close()