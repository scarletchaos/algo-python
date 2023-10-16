from algo_py.q import Queue 
import pytest

@pytest.fixture
def que():
    que = Queue()
    que.push(1)
    que.push(2)
    que.push(3)
    return que

def test_q(que):

    assert que.pop() == 1
    assert que.pop() == 2
    assert que.pop() == 3
    
