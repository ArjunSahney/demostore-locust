from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(5, 9)  # Users wait between 5 and 9 seconds between tasks
    host = "http://k8s-ui-uinlb-2a08af2edf-c8e8764af6a48659.elb.us-east-1.amazonaws.com"

    @task(1)
    def view_home(self):
        self.client.get("/home")

    @task(2)
    def add_to_cart(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "http://k8s-ui-uinlb-2a08af2edf-c8e8764af6a48659.elb.us-east-1.amazonaws.com/home"
        }
        data = {
            "productId": "510a0d7e-8e83-4193-b483-e27e09ddc34d"
        }
        self.client.post("/cart", data=data, headers=headers)

    @task(3)
    def checkout(self):
        self.client.get("/checkout")

