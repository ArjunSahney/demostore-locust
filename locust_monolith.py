from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(0.5, 1.5)  # Wait between 0.5 and 1.5 seconds
    host = "https://d3iilb82cp4l9g.cloudfront.net"

    @task
    def browse_website(self):
        self.client.get("/")  # Visit the homepage

    @task
    def view_screwdriver(self):
        self.client.get("https://rughodbytj.execute-api.us-east-1.amazonaws.com/products/id/8bffb5fb-624f-48a8-a99f-b8e9c64bbe29")  # View the screwdriver

    @task
    def add_to_cart(self):
        headers = {"Content-Type": "application/json"}
        payload = {
            "id": "5",
            "username": "guest",
            "items": [
                {
                    "product_id": "8bffb5fb-624f-48a8-a99f-b8e9c64bbe29",
                    "product_name": "Screwdriver",
                    "quantity": 1,
                    "price": 24.99
                }
            ]
        }
        self.client.put("https://rughodbytj.execute-api.us-east-1.amazonaws.com/carts/5", headers=headers, json=payload)  # Add the screwdriver to the cart

    
    @task
    def checkout(self):
        headers = {"Content-Type": "application/json"}
        payload = {"id": "7", "username": "guest", "items": None}
        self.client.post("https://rughodbytj.execute-api.us-east-1.amazonaws.com/orders", headers=headers, json=payload)  # Checkout with the new URL

        headers = {"Content-Type": "application/json"}
        payload = {"id": "7", "username": "guest", "items": None}
        self.client.post("https://86ww9bscbf.execute-api.us-east-1.amazonaws.com/orders", headers=headers, json=payload)  # Checkout

    @task
    def create_cart(self):
        headers = {"Content-Type": "application/json"}
        payload = {"id": "7", "username": "guest", "items": None}
        self.client.post("https://86ww9bscbf.execute-api.us-east-1.amazonaws.com/carts", headers=headers, json=payload)  # Create a new cart

    @task
    def view_cart(self):
        self.client.get("https://rughodbytj.execute-api.us-east-1.amazonaws.com/products/id/5d37a44b-d121-426e-b528-59e603ba5923")  # View the cart
