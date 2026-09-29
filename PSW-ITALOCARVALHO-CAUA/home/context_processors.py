def cart_count(request):
    cart = request.session.get("carrinho", {})
    return {"quantidade_carrinho": sum(cart.values())}
