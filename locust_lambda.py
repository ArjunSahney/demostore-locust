from locust import HttpUser, task, between

class RetailDemoUser(HttpUser):
    host = "https://c1cy8x1o2d.execute-api.us-east-1.amazonaws.com"
    wait_time = between(1, 2)  # wait time between tasks

    # This task simulates fetching the product details
    @task
    def fetch_gig_details(self):
        # May need to change depending on pathname
        self.client.get("/Prod/prod1/hammer")

    # This task simulates making a payment
    @task
    def make_payment(self):
        payload = {
            "gigId": "hammer",
            "name": "Alex Smith",
            "email": "alexsmith@gmail.com",
            "cardCVC": "123",
            "cardExpiryMonth": "5",
            "cardExpiryYear": "2026",
            "cardNumber": "5454545454545454",
            "disclaimerAccepted": True,
            "nameOnCard": "Alex Smith"
        }
        self.client.post("/Prod/purchase", json=payload)

# If you want the test to be run in sequence, you can organize the tasks accordingly
class SequentialRetailDemoUser(RetailDemoUser):
    @task(1)
    def fetch_product_details(self):
        super().fetch_product_details()

    @task(2)
    def make_payment(self):
        super().make_payment()
