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

    def get(self, request, parent_category_id):
        """
        Handles GET requests, fetches all sub-categories of a parent category from the database and renders the page.
        """
        parent_category = inventory_models.Category.objects.get(id=parent_category_id)
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


class DemoProductsView(View):
    """
    A view that renders a page with all products in a category.
    """

    template_name = "demo/demo_products.html"
    context = {}

    def get(self, request, category_id):
        """
        Handles GET requests, fetches all products in a category from the database and renders the page.
        """
        category = inventory_models.Category.objects.get(id=category_id)
        products_list = inventory_models.Product.objects.filter(
            category=category
        ).order_by("name")

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
