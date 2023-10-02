from locust import HttpUser, task, between, events
import gevent

class WebsiteUser(HttpUser):
    wait_time = between(0.5, 1.5)  # Wait between 0.5 and 1.5 seconds
    host = "https://d15h8mtx9d5rlw.cloudfront.net"

    @task
    def browse_website(self):
        self.client.get("/")  # Visit the homepage

    @task
    def view_screwdriver(self):
        self.client.get("https://86ww9bscbf.execute-api.us-east-1.amazonaws.com/products/id/8bffb5fb-624f-48a8-a99f-b8e9c64bbe29")  # View the screwdriver

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
        self.client.put("https://86ww9bscbf.execute-api.us-east-1.amazonaws.com/carts/5", headers=headers, json=payload)  # Add the screwdriver to the cart

    @task
    def checkout(self):
        headers = {"Content-Type": "application/json"}
        payload = {"id": "7", "username": "guest", "items": None}
        self.client.post("https://86ww9bscbf.execute-api.us-east-1.amazonaws.com/orders", headers=headers, json=payload)  # Checkout

    @task
    def create_cart(self):
        headers = {"Content-Type": "application/json"}
        payload = {"id": "7", "username": "guest", "items": None}
        self.client.post("https://86ww9bscbf.execute-api.us-east-1.amazonaws.com/carts", headers=headers, json=payload)  # Create a new cart

def ramp_users(target_users, spawn_rate):
    current_users = len(WebsiteUser.environment.runner.locusts)
    if current_users < target_users:
        print(f"Ramping up to {target_users} users at {spawn_rate} users/second.")
        WebsiteUser.environment.runner.start(WebsiteUser, number_of_users=target_users - current_users, spawn_rate=spawn_rate)
    elif current_users > target_users:
        print(f"Ramping down to {target_users} users at {spawn_rate} users/second.")
        WebsiteUser.environment.runner.stop(stop_count=current_users - target_users)

def schedule_ramp():
    # 12 hours ramp up to 10,000 users
    for users in range(0, 10001, 70):  # increment by 70 users every 5 minutes
        gevent.sleep(300)  # 5 minutes
        ramp_users(users, 14)  # spawn rate of 14 users/second to add 70 users in 5 minutes

    # 12 hours ramp down from 10,000 users to 0
    for users in range(10000, -1, -70):  # decrement by 70 users every 5 minutes
        gevent.sleep(300)  # 5 minutes
        ramp_users(users, 14)  # spawn rate of 14 users/second to remove 70 users in 5 minutes

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    max_users = 10000
    environment.runner.start(WebsiteUser, number_of_users=max_users, spawn_rate=max_users)
    gevent.spawn(schedule_ramp)
