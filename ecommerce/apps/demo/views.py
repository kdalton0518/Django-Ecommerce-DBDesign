from django.views.generic import View
from django.shortcuts import render
from ecommerce.apps.inventory import models as inventory_models

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class DemoHomeView(View):
    """
    A view that renders the demo home page.
    """

    template_name = "demo/demo_home.html"
    context = {}

    def get(self, request):
        """
        Handles GET requests, renders the demo home page.
        """
        return render(request, self.template_name, self.context)


class DemoParentCategoriesView(View):
    """
    A view that renders a page with all parent categories.
    Parent category can be clicked to view all sub-categories in that category.
    """

    template_name = "demo/demo_parent_categories.html"
    context = {}

    def get(self, request):
        """
        Handles GET requests, fetches all parent categories from the database and renders the page.
        """
        categories_list = inventory_models.Category.objects.filter(
            parent=None
        ).order_by("name")

        items_per_page = 20
        paginator = Paginator(categories_list, items_per_page)

        page = request.GET.get("page")
        try:
            categories = paginator.page(page)
        except PageNotAnInteger:
            categories = paginator.page(1)
        except EmptyPage:
            categories = paginator.page(paginator.num_pages)

        self.context["categories"] = categories
        return render(request, self.template_name, self.context)


class DemoSubCategoriesView(View):
    """
    A view that renders a page with all sub-categories of a parent category.
    Sub category can be clicked to view all products in that category.
    """

    template_name = "demo/demo_sub_categories.html"
    context = {}

    def get(self, request, parent_category_slug):
        """
        Handles GET requests, fetches all sub-categories of a parent category from the database and renders the page.
        """
        parent_category = inventory_models.Category.objects.get(
            slug=parent_category_slug
        )
        sub_categories_list = inventory_models.Category.objects.filter(
            parent=parent_category
        ).order_by("name")

        items_per_page = 20
        paginator = Paginator(sub_categories_list, items_per_page)

        page = request.GET.get("page")
        try:
            sub_categories = paginator.page(page)
        except PageNotAnInteger:
            sub_categories = paginator.page(1)
        except EmptyPage:
            sub_categories = paginator.page(paginator.num_pages)

        self.context["parent_category"] = parent_category
        self.context["sub_categories"] = sub_categories
        return render(request, self.template_name, self.context)


class DemoSubCategoriesProductsView(View):
    """
    A view that renders a page with all products in a category.
    """

    template_name = "demo/demo_sub_categories_products.html"
    context = {}

    def get(self, request, category_slug):
        """
        Handles GET requests, fetches all products in a category from the database and renders the page.
        """
        category = inventory_models.Category.objects.get(slug=category_slug)
        products_list = (
            inventory_models.Product.objects.filter(category=category)
            .values(
                "id",
                "name",
                "slug",
                "product__product_type__name",
                "product__brand__name",
            )
            .order_by("name")
            .distinct()
        )

        items_per_page = 20
        paginator = Paginator(products_list, items_per_page)

        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        self.context["category"] = category
        self.context["products"] = products
        return render(request, self.template_name, self.context)


class DemoProductDetailView(View):
    """
    A view that renders a page with details of a product.
    """

    template_name = "demo/demo_product_detail.html"
    context = {}

    def get(self, request, product_slug):
        """
        Handles GET requests, fetches details of a product from the database and renders the page.
        """
        product = inventory_models.Product.objects.get(slug=product_slug)
        product_inventory = inventory_models.ProductInventory.objects.filter(
            product=product
        )

        product_inventory_stock_media_map = []
        for pi in product_inventory:
            stock = inventory_models.Stock.objects.get(product_inventory=pi)
            media = inventory_models.Media.objects.filter(product_inventory=pi)

            product_inventory_stock_media_map.append(
                {
                    "product_inventory": pi,
                    "stock": stock,
                    "media": media,
                    "attribute_values": pi.attribute_values.all(),
                }
            )

        self.context["brand"] = product_inventory.first().brand
        self.context["product"] = product
        self.context["product_inventory_stock_media_map"] = (
            product_inventory_stock_media_map
        )
        self.context["categories"] = product.category.all()

        return render(request, self.template_name, self.context)


class DemoProductTypesView(View):
    """
    A view that renders a page with all product types.
    """

    template_name = "demo/demo_product_types.html"
    context = {}

    def get(self, request):
        """
        Handles GET requests, fetches all product types from the database and renders the page.
        """
        product_types_list = inventory_models.ProductType.objects.all().order_by("name")

        items_per_page = 20
        paginator = Paginator(product_types_list, items_per_page)

        page = request.GET.get("page")
        try:
            product_types = paginator.page(page)
        except PageNotAnInteger:
            product_types = paginator.page(1)
        except EmptyPage:
            product_types = paginator.page(paginator.num_pages)

        self.context["product_types"] = product_types
        return render(request, self.template_name, self.context)


class DemoProductTypeProductsView(View):
    """
    A view that renders a page with all products of a product type.
    """

    template_name = "demo/demo_product_type_products.html"
    context = {}

    def get(self, request, product_type_id):
        """
        Handles GET requests, fetches all products of a product type from the database and renders the page.
        """
        product_type = inventory_models.ProductType.objects.get(id=product_type_id)
        products_list = (
            inventory_models.ProductInventory.objects.filter(product_type=product_type)
            .values(
                "product__id",
                "product__name",
                "product__slug",
                "brand__name",
            )
            .order_by("product__name")
            .distinct()
        )

        items_per_page = 20
        paginator = Paginator(products_list, items_per_page)

        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        print(products[0])

        self.context["product_type"] = product_type
        self.context["products"] = products
        return render(request, self.template_name, self.context)


class DemoBrandsView(View):
    """
    A view that renders a page with all brands.
    """

    template_name = "demo/demo_brands.html"
    context = {}

    def get(self, request):
        """
        Handles GET requests, fetches all brands from the database and renders the page.
        """
        brands_list = inventory_models.Brand.objects.all().order_by("name")

        items_per_page = 20
        paginator = Paginator(brands_list, items_per_page)

        page = request.GET.get("page")
        try:
            brands = paginator.page(page)
        except PageNotAnInteger:
            brands = paginator.page(1)
        except EmptyPage:
            brands = paginator.page(paginator.num_pages)

        self.context["brands"] = brands
        return render(request, self.template_name, self.context)


class DemoBrandProductsView(View):
    """
    A view that renders a page with all products of a brand.
    """

    template_name = "demo/demo_brand_products.html"
    context = {}

    def get(self, request, brand_id):
        """
        Handles GET requests, fetches all products of a brand from the database and renders the page.
        """
        brand = inventory_models.Brand.objects.get(id=brand_id)
        products_list = (
            inventory_models.ProductInventory.objects.filter(brand=brand)
            .values(
                "product__id",
                "product__name",
                "product__slug",
                "product_type__name",
            )
            .order_by("product__name")
            .distinct()
        )

        items_per_page = 20
        paginator = Paginator(products_list, items_per_page)

        page = request.GET.get("page")
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        self.context["brand"] = brand
        self.context["products"] = products
        return render(request, self.template_name, self.context)
