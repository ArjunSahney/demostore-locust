
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(0.5, 1.5)  # Wait between 0.5 and 1.5 seconds
    host = "http://k8s-ui-uinlb-ec649da61b-675678d6fd305707.elb.us-east-1.amazonaws.com"

    @task
    def browse_website(self):
        self.client.get("/")  # Visit the homepage

    @task
    def view_product(self):
        self.client.get("/catalog/510a0d7e-8e83-4193-b483-e27e09ddc34d")  # View the product

    @task
    def add_to_cart(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = "productId=510a0d7e-8e83-4193-b483-e27e09ddc34d"
        self.client.post("/cart", headers=headers, data=payload)  # Add the product to the cart

    @task
    def checkout(self):
        self.client.get("/checkout")  # Checkout


