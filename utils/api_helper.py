import requests
from utils.logger import logger

class APIclient:
    @staticmethod
    def delete_user_api(email: str, password: str) -> requests.Response:
        url = "https://automationexercise.com/api/deleteAccount"
        data = {"email": email, "password": password}
        response = requests.delete(url, data=data)
        # raise on error so failures are visible
        response.raise_for_status()
        logger.info(f"successfully deleted user: {email}")
        return response