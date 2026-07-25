def apply_discount(price, discount):
    if (isinstance(price, int) or isinstance(price, float)):
        if(isinstance(discount, int) or isinstance(discount, float)):
            if price <= 0:
                return "The price should be greater than 0"
            if discount < 0 or discount > 100:
                return "The discount should be between 0 and 100"
            else:
                return price - (price * (discount / 100))
        else:
            return "The discount should be a number"
    else:
        return "The price should be a number"

