# 힙

## 이진 탐색 트리와 다른 점
1. 어느 노드를 루트로 하는 서브트리도 모드 최대/최소 힙이어야 한다는 규칙만 있을 뿐 자식 노드 간의 정렬 순서는 정해져 있지 않다.
2. 특정 키 값을 가지는 원소를 빠르게 검색할 수 없다점
3. 완전 이진 트리여야 한다.

## 최대 힙의 추상적 자료구조

### 연산의 정의
- __init__() : 빈 최대 힙을 생성
- insert(item) : 새로운 원소를 삽입
- remove() : 최대 원소 (root node) 반환

### 데이터 표현의 설계

배열을 이용한 이진 트리의 표현. 완전 이진트리이기 때문에 배열로 표현이 가능하다. 0 번 인덱스를 비워두고 1번 인덱스부터 시작한다고 보자.

1. 노드 번호 m 을 기준으로 
    - 왼쪽 자식의 번호: 2 * m
    - 오른쪽 자식의 번호: 2 * m + 1
    - 부모 노드의 번호: m // 2

2. 완전 이진 트리이므로 노드의 추가/삭제는 마지막 노드에서만 일어난다.

### 최대 힙에 원소 삽입 - 복잡도

일단 배열의 맨 끝에 넣고, 부모 노드보다 작을 때, 혹은 루트 노드가 될 때 까지 위치를 교환하면서 올라간다.

원소의 개수가 n 인 최대 힙에 새로운 원소 삽입  
-> 부모 노드와의 대소 비교 최대 횟수: log2n

즉 최악 복잡도 O(logn) 의 삽입 연산


### 최대 힙의 삽입 구현
```python
class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        now = len(self.data) - 1
        while True:
            next = now // 2
            if next == 0 or self.data[next] >= item:
                break
            self.data[next], self.data[now] = self.data[now], self.data[next]
            now = next
        return True
```

### 최대 힙에서 원소의 삭제

1. 루트 노드의 제거 - 원소들 중 최대값
2. 트리 마지막 자리 노드를 임시로 루트 노드 자리에 배치
3. 삽입 연산과는 반대로 자식 노드들과의 값 비교하며 아래로 아래로 교환해 감. (자식들 중 더 큰 자식과 교환)
4. 복잡도는 삽입연산에 자식들간 크기 비교를 위한 *2 를 추가하지만, 복잡도 계산이기에 생략하여 여전히 log2n

### 최대 힙에서 원소의 삭제 구현

```python
class MaxHeap:

    def __init__(self):
        self.data = [None]


    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data


    def maxHeapify(self, i):
        # 왼쪽 자식 (left child) 의 인덱스를 계산합니다.
        left = i * 2

        # 오른쪽 자식 (right child) 의 인덱스를 계산합니다.
        right = i * 2 + 1

        smallest = i
        # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if left < len(self.data) and self.data[left] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.      
            smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 (무엇보다?) 더 큰지를 판단합니다.
        if right < len(self.data) and self.data[right] > self.data[smallest]:
            # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
            smallest = right

        if smallest != i:
            # 현재 노드 (인덱스 i) 와 최댓값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]

            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
            self.maxHeapify(smallest)
```

## 힙 활용 예

1. 힙 정렬 (heap sort)

```python
def heapsort(unsorted):
    H = MaxHeap()
    for item in unsorted:
        H.insert(item)
    sorted = []
    d = H.remove()
    while d:
        sorted.append(d)
        d = H.remove()
    return sorted
```

2. 우선 순위 큐
삽입, 제거 모두 Ologn 이기 때문에, 양방향 연결 리스트를 이용한 우선순위 큐보다 시간 효율적으로 장점이 있다.