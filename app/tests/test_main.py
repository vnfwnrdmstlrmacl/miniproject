from app.main import add, app # app 객체와 add 함수를 가져옵니다.
import pytest

# Flask 앱의 테스트 클라이언트를 사용하기 위한 fixture
@pytest.fixture
def client():
    # 테스트 환경 설정 (예외 전파 등)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client # 클라이언트를 테스트 함수에 제공

def test_add_function():
    """일반 add 함수 테스트"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_hello_route(client):
    """'/' 경로의 GET 요청 테스트"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json()['message'] == "Hello from miniproject!"

def test_add_route(client):
    """'/add' 경로의 GET 요청 테스트"""
    # 쿼리 파라미터와 함께 요청
    response = client.get('/add?a=10&b=20')
    assert response.status_code == 200
    assert response.get_json()['result'] == 30
