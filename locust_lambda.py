from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    host = "https://f2y33bxst7.execute-api.us-east-1.amazonaws.com"
    wait_time = between(1, 2.5)

    @task(1)
    def get_gig(self):
        self.client.get(
            "/Prod/gigs/the-beatles-new-york-1965",  # Corrected URL path
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                "Origin": "http://timelessmusic-frontend.s3-website-us-east-1.amazonaws.com",
                "Referer": "http://timelessmusic-frontend.s3-website-us-east-1.amazonaws.com/",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            }
        )

    @task(1)
    def post_purchase(self):
        self.client.post(
            "/Prod/purchase",  # Corrected URL path
            json={
                "gigId": "the-beatles-new-york-1965",
                "name": "Alex Smith",
                "email": "alexsmith@gmail.com",
                "nameOnCard": "Alex Smith",
                "cardNumber": "5454545454545454",
                "cardExpiryMonth": "5",
                "cardExpiryYear": "2026",
                "cardCVC": "123",
                "disclaimerAccepted": True
            },
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                "Content-Type": "application/json",
                "Origin": "http://timelessmusic-frontend.s3-website-us-east-1.amazonaws.com",
                "Referer": "http://timelessmusic-frontend.s3-website-us-east-1.amazonaws.com/",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
            }
        )

