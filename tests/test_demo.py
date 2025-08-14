import requests
import pytest

# 测试数据
LOGIN_URL = "https://summercamp.venhalo.com/api/auth/login"
VALID_CREDENTIALS = {
    "loginName": "admin",
    "password": "111111"
}

@pytest.mark.login
def test_user_login_success():
    """
    测试管理员用户登录成功
    """
    # 步骤 1: 发送登录请求
    response = requests.request(
        method="POST",
        url=LOGIN_URL,
        json=VALID_CREDENTIALS
    )
    
    # 步骤 2: 检查响应状态码
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # 步骤 3: 解析响应 JSON
    try:
        response_data = response.json()
    except json.JSONDecodeError:
        assert False, "Response is not valid JSON"
    
    # 步骤 4: 验证响应内容包含“登录成功”
    # 假设响应结构是 { "message": "登录成功", ... } 或类似
    assert "登录成功" in response.text, f"Expected '登录成功' in response, but got: {response.text}"
    
    # （可选）更精确的断言，比如检查 token 或用户信息
    # assert "token" in response_data, "Token not found in response"
    # assert response_data.get("message") == "登录成功"
