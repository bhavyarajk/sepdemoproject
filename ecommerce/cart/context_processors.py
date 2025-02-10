

from cart.models import Cart
def count_items(request):
    u = request.user
    count = 0
    if request.user.is_authenticated: #checks whether the user is authenticated
        c = Cart.objects.filter(user=u)  # to filter cart records for a particular user

        # to calculate Total count

        for i in c:
            count=count+i.quantity

    return {'count':count}
