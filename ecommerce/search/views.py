from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
def searchproducts(request):
    p= None
    query = ""
    if (request.method == "POST"):
        query = request.POST['q']
        print(query)
        if query:
            p = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))  # Inorder to add AND or OR logic into Django Queries here we use Q object
            # i->caseinsensive
            # contains-->anywhere inside the field
    context={'pro':p,'query':query}
    return render(request,'search.html',context)
