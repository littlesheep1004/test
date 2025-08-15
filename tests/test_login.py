import requests
import pytest
import allure
import json

LOGIN_URL = "https://summercamp.venhalo.com/api/auth/login"
VALID_CREDENTIALS = {
    "loginName": "admin",
    "password": "111111"
}

@allure.feature("用户认证")
@allure.story("管理员登录")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login
def test_user_login_success():
    """
    测试管理员用户登录成功
    """
    with allure.step("发送登录请求"):
        response = requests.post(
            url=LOGIN_URL,
            json=VALID_CREDENTIALS
        )
        allure.attach(
            str(response.status_code), 
            name="响应状态码", 
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            response.text, 
            name="响应内容", 
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("验证响应状态码为 200"):
        assert response.status_code == 200, \
            f"Expected 200, got {response.status_code}"

    with allure.step("解析响应 JSON"):
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            pytest.fail("响应不是合法的 JSON")

    with allure.step("验证响应包含 '登录成功'"):
        assert "登录成功" in response.text, \
            f"Expected '登录成功', got: {response.text}"
