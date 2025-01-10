from django.shortcuts import render
from .models import Product, Category, Tag


def StoreListView(request):
    """
    Displays a list of :model:store.Product filtered by query, Category, and Tags.

    **Context**

    - ``products``: A queryset of filtered :model:store.Product entries.
    - ``categories``: A queryset of all :model:store.Category entries.
    - ``tags``: A queryset of all :model:store.Tag entries.
    - ``query``: The search query string entered by the user.
    - ``category_id``: The ID of the selected category filter.
    - ``tag_ids``: A list of IDs for the selected tag filters.

    **Template**

    - :template:`store/index.html`
    """

    query = request.GET.get("query", "")
    category_id = request.GET.get("category", None)
    tag_ids = request.GET.getlist("tags")

    filters = {}
    if query:
        filters["description__icontains"] = query
    if category_id:
        filters["category_id"] = category_id

    products = Product.objects.filter(**filters)

    for tag_id in tag_ids:
        products = products.filter(tags__id=tag_id).distinct()

    products = products.select_related("category").prefetch_related("tags")

    categories = Category.objects.only("id", "name")
    tags = Tag.objects.only("id", "name")

    context = {
        "products": products,
        "categories": categories,
        "tags": tags,
        "query": query,
        "category_id": category_id,
        "tag_ids": tag_ids,
    }

    return render(request, "store/index.html", context)
