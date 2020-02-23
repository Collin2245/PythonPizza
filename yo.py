print("yo")


def cardInfo(cardNum, expDate, cvv, zipCode):
    card = PaymentObject(cardNum, expDate, cvv, zipCode)
    return card